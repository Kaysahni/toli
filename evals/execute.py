#!/usr/bin/env python3
"""Execution harness: runs one task through each arm with real tools.

  normal   the task only
  coord    the task plus a one-paragraph coordination prompt
  toli     the task, with the toli plugin installed. If it prints a card, the
           harness replies `go` on the same session and counts both turns

Every arm runs in its own copy of the task fixture, under the same isolation
as run.py, with the same tools, model and budget cap. Per arm it writes:

  events.jsonl   every stream-json event, all turns
  transcripts/   the session transcript plus every subagent and workflow agent
  summary.json   cost, tokens, elapsed, agent count, peak agent overlap, answer

Scoring against the answer checklist is a separate step.
"""
import argparse, glob, json, os, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
TASKS = HERE / "execution" / "tasks"
MODEL = "claude-opus-5"

# run.py isolation, minus the slash-command switch (it also disables plugin
# skills, which is the arm under test). --restricted strips Workflow unless
# --tools names it, and Workflow still asks for review headless unless allowed.
TOOLS = "Read,Grep,Glob,Write,Agent,Workflow,Skill,ToolSearch,TaskOutput,TaskStop"
ISOLATION = ["--restricted", "--strict-mcp-config", "--tools", TOOLS,
             "--allowedTools", "Workflow"]

COORD = ("Plan and execute this task. Parallelize independent work, give workers "
         "distinct responsibilities, define their outputs and dependencies, and "
         "verify findings before synthesis. Use one agent when sufficient.")

CARD = re.compile(r"^\s*INTENT\b.*^\s*COST\b", re.M | re.S)

# Inherited from a parent Claude Code session, these would tie the arm to it.
SCRUB = ("CLAUDE_CODE_SESSION_ID", "CLAUDE_CODE_CHILD_SESSION",
         "CLAUDE_CODE_SESSION_ATTENDED", "CLAUDE_CODE_MESSAGING_SOCKET",
         "CLAUDE_CODE_MESSAGING_TOKEN")


def invoke(prompt, cwd, extra, events, budget):
    cmd = ["claude", "-p", "--model", MODEL, "--output-format", "stream-json",
           "--verbose", "--max-budget-usd", str(budget)] + ISOLATION + extra
    env = {k: v for k, v in os.environ.items() if k not in SCRUB}
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                       cwd=cwd, env=env, timeout=3600)
    evs = [json.loads(l) for l in r.stdout.splitlines() if l.strip().startswith("{")]
    with open(events, "a") as f:
        f.writelines(json.dumps(e) + "\n" for e in evs)
    results = [e for e in evs if e.get("type") == "result"]
    if not results:
        raise RuntimeError(f"no result event, rc={r.returncode}: {r.stderr[-400:]}")
    # One invocation can emit several result events (a background workflow
    # finishing adds a turn). Usage on each is cumulative for the invocation,
    # so the last one is the invocation total.
    return results[-1], evs


def agent_spans(session_dir):
    spans = []
    for f in glob.glob(str(session_dir / "subagents" / "**" / "agent-*.jsonl"), recursive=True):
        ts = [json.loads(l)["timestamp"] for l in open(f) if '"timestamp"' in l]
        if ts:
            spans.append((min(ts), max(ts)))
    return spans


def peak_overlap(spans):
    marks = sorted([(s, 1) for s, _ in spans] + [(e, -1) for _, e in spans],
                   key=lambda m: (m[0], m[1]))
    cur = peak = 0
    for _, d in marks:
        cur += d
        peak = max(peak, cur)
    return peak


def run_arm(task_dir, arm, out, budget):
    arm_dir = out / arm
    arm_dir.mkdir(parents=True)
    work = Path(tempfile.mkdtemp(prefix=f"toli-exec-{arm}-")).resolve()
    shutil.copytree(task_dir / "fixture", work / "fixture")
    cwd = work / "fixture"
    task = (task_dir / "task.md").read_text().strip()
    extra = []
    if arm == "toli":
        # A copy beside the fixture, readable through --add-dir: under
        # --restricted the skill cannot otherwise open its own references.
        plug = work / "plugin"
        shutil.copytree(REPO / ".claude-plugin", plug / ".claude-plugin")
        shutil.copytree(REPO / "skills", plug / "skills")
        extra = ["--plugin-dir", str(plug), "--add-dir", str(plug)]
    prompt = f"{task}\n\n{COORD}" if arm == "coord" else task

    events = arm_dir / "events.jsonl"
    t0 = time.monotonic()
    first, evs = invoke(prompt, cwd, extra, events, budget)
    turns = [first]
    skill_used = any(c.get("type") == "tool_use" and c.get("name") == "Skill"
                     and "toli" in json.dumps(c.get("input"))
                     for e in evs if e.get("type") == "assistant"
                     for c in e["message"]["content"])
    card = bool(CARD.search(first.get("result", "")))
    if arm == "toli" and card:
        turns.append(invoke("go", cwd, extra + ["--resume", first["session_id"]],
                            events, budget)[0])
    elapsed = time.monotonic() - t0

    sid = first["session_id"]
    main = next(iter(glob.glob(str(Path.home() / ".claude/projects/*" / f"{sid}.jsonl"))), None)
    spans = []
    if main:
        shutil.copy(main, arm_dir / "transcript.jsonl")
        sdir = Path(main[:-len(".jsonl")])
        if sdir.is_dir():
            shutil.copytree(sdir, arm_dir / "transcripts")
            spans = agent_spans(sdir)
    shutil.rmtree(work, ignore_errors=True)

    summary = {
        "arm": arm, "task": task_dir.name, "model": MODEL, "budget_usd": budget,
        "session_id": sid,
        "cost_usd": round(sum(t["total_cost_usd"] for t in turns), 4),
        "output_tokens": sum(u["outputTokens"] for t in turns for u in t["modelUsage"].values()),
        "elapsed_s": round(elapsed, 1),
        "invocations": len(turns), "card_shown": card, "skill_invoked": skill_used,
        "agents": len(spans), "peak_agent_overlap": peak_overlap(spans),
        "errors": [t.get("subtype") for t in turns if t.get("is_error")],
        "answer": turns[-1].get("result", ""),
    }
    (arm_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    print(f"[{datetime.now():%H:%M:%S}] {task_dir.name}/{arm} done: "
          f"${summary['cost_usd']} agents={summary['agents']} "
          f"overlap={summary['peak_agent_overlap']} card={card}", file=sys.stderr)
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tasks", nargs="+", help="task ids under execution/tasks")
    ap.add_argument("--arms", default="normal,coord,toli")
    ap.add_argument("--budget", type=float, default=10.0, help="USD cap per invocation")
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--out", default=str(HERE / "execution" / "runs" / time.strftime("%Y%m%d-%H%M%S")))
    a = ap.parse_args()
    out = Path(a.out)
    jobs = [(TASKS / t, arm) for t in a.tasks for arm in a.arms.split(",")]
    for t, _ in jobs:
        if not (t / "task.md").exists():
            sys.exit(f"no task.md in {t}")
    print(f"{len(jobs)} runs, {a.workers} at a time, -> {out}", file=sys.stderr)

    def job(j):
        try:
            return run_arm(j[0], j[1], out / j[0].name, a.budget)
        except Exception as e:                    # one bad arm must not sink the batch
            print(f"{j[0].name}/{j[1]} FAILED: {e}", file=sys.stderr)
            return {"task": j[0].name, "arm": j[1], "error": str(e)}

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        results = list(ex.map(job, jobs))
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.json").write_text(json.dumps(
        [{k: v for k, v in r.items() if k != "answer"} for r in results], indent=2))


if __name__ == "__main__":
    main()
