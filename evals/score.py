#!/usr/bin/env python3
"""Scores execute.py answers against each task's checklist, blind to arm.

The grader gets the task, the checklist and one answer, never the arm, in
shuffled order. An answer can still reveal its arm by what it says (a toli
refusal line, a mention of agents). The grader returns, per
checklist item, whether the answer recovered it, and lists any claim the
answer makes that the checklist and fixture do not support.

  python3 evals/score.py evals/execution/runs/pilot-1

Writes scores.json (unblinded) and prints a per-task table.
"""
import json, random, subprocess, sys, uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
TASKS = HERE / "execution" / "tasks"
GRADER = "claude-opus-5"

SCHEMA = {
    "type": "object",
    "properties": {
        "findings": {"type": "array", "items": {"type": "object", "properties": {
            "id": {"type": "string"}, "recovered": {"type": "boolean"},
            "why": {"type": "string"}}, "required": ["id", "recovered", "why"]}},
        "exclusions": {"type": "array", "items": {"type": "object", "properties": {
            "id": {"type": "string"}, "wrongly_reported": {"type": "boolean"},
            "why": {"type": "string"}}, "required": ["id", "wrongly_reported", "why"]}},
        "answer_correct": {"type": ["boolean", "null"]},
        "unsupported_claims": {"type": "array", "items": {"type": "string"}},
        "harmful_mistakes": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["findings", "exclusions", "answer_correct",
                 "unsupported_claims", "harmful_mistakes"],
}

PROMPT = """You are grading one answer to a work task against its answer key.
Be strict and literal. Grade only what the answer says, not what it might mean.

For every checklist finding, set recovered=true only if the answer meets that
finding's counts_if. For every exclusion, set wrongly_reported=true only if the
answer presents that decoy as a real finding (mentioning it as not an issue is
fine). grading_notes list extras that are acceptable. If the checklist has an
"answer", set answer_correct against its counts_if, otherwise null.

unsupported_claims: findings the answer reports that are neither in the
checklist nor acceptable extras, and that you judge wrong or unsupported. You
may read the task files in fixture/ to check. harmful_mistakes: any item from
mistakes_that_matter the answer commits.

--- TASK ---
{task}
--- CHECKLIST ---
{checklist}
--- ANSWER ---
{answer}
--- END ---"""


def grade(task, answer):
    ck = (TASKS / task / "checklist.json").read_text()
    prompt = PROMPT.format(task=(TASKS / task / "task.md").read_text(),
                           checklist=ck, answer=answer)
    cmd = ["claude", "-p", "--model", GRADER, "--output-format", "json",
           "--json-schema", json.dumps(SCHEMA), "--restricted",
           "--strict-mcp-config", "--disable-slash-commands", "--tools", "Read,Grep,Glob"]
    for attempt in range(3):
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                           cwd=TASKS / task / "fixture", timeout=1800)
        try:
            d = json.loads(r.stdout)
            out = d.get("structured_output") or json.loads(d["result"])
            out["grader_cost_usd"] = d.get("total_cost_usd")
            return out
        except Exception:
            err = r.stderr[-300:] or r.stdout[-300:]
    return {"error": err}


def main():
    run = Path(sys.argv[1])
    items = []
    for s in sorted(run.glob("*/*/summary.json")):
        summ = json.loads(s.read_text())
        items.append({"blind_id": uuid.uuid4().hex[:8], **summ})
    random.shuffle(items)                          # grading order says nothing about arm
    print(f"grading {len(items)} answers", file=sys.stderr)

    def job(it):
        g = grade(it["task"], it["answer"])
        print(f"graded {it['blind_id']}", file=sys.stderr)
        return it, g

    with ThreadPoolExecutor(max_workers=4) as ex:
        graded = list(ex.map(job, items))

    rows = []
    for it, g in graded:
        ck = json.loads((TASKS / it["task"] / "checklist.json").read_text())
        row = {k: it[k] for k in ("task", "arm", "blind_id", "cost_usd", "elapsed_s",
                                  "agents", "peak_agent_overlap", "card_shown",
                                  "skill_invoked")}
        if "error" in g:
            row["error"] = g["error"]
        else:
            row["found"] = sum(f["recovered"] for f in g["findings"])
            row["of"] = len(ck["findings"])
            row["traps_hit"] = sum(x["wrongly_reported"] for x in g["exclusions"])
            row["answer_correct"] = g["answer_correct"]
            row["unsupported"] = len(g["unsupported_claims"])
            row["harmful"] = len(g["harmful_mistakes"])
            row["grade"] = g
        rows.append(row)
    rows.sort(key=lambda r: (r["task"], r["arm"]))
    (run / "scores.json").write_text(json.dumps(rows, indent=2))

    print(f"{'task':26} {'arm':7} {'found':>7} {'traps':>5} {'unsup':>5} {'answer':>6} {'$':>6} {'agents':>6}")
    for r in rows:
        if "error" in r:
            print(f"{r['task']:26} {r['arm']:7} ERROR")
            continue
        print(f"{r['task']:26} {r['arm']:7} {r['found']:>3}/{r['of']:<3} {r['traps_hit']:>5} "
              f"{r['unsupported']:>5} {str(r['answer_correct']):>6} {r['cost_usd']:>6.2f} {r['agents']:>6}")


if __name__ == "__main__":
    main()
