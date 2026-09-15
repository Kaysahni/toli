#!/usr/bin/env python3
"""Gate-accuracy harness for the toli skill.

For each case in cases/, runs two arms through `claude -p`:

  baseline   bare model, no skill
  toli       same model with the full skill bundle in the system prompt

Both arms get the identical prompt and suffix, and are graded by the identical
judge, so the comparison is symmetric.

The judge assigns a CATEGORY rather than a yes/no, because "did it fan out" hides
real distinctions: a conditional escalation, a sequential workflow and a
committed parallel plan are not the same decision. FANOUT_CATEGORIES below is the
mapping from category to "this counts as fanning out", declared before the run.

Each case is classified as:

  discriminator  toli right, baseline wrong. The skill earned its place
  regression     toli wrong, baseline right. The skill made it worse
  skill-gap      both wrong. The gate does not cover this case
  no-signal      both right. The case is too easy to discriminate

Writes snapshots/results.json with full provenance. measure.py reads the
snapshot and needs no API key.

KNOWN LIMITATION, stated in README.md: this measures the STATED approach on a
planning question, not observed behaviour executing against a real repository.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent / "skills" / "toli"

ARM_MODEL = "claude-opus-5"
JUDGE_MODEL = "claude-haiku-4-5-20251001"

# A bare `claude -p` inherits the user's CWD, CLAUDE.md, plugins, hooks, skills
# and MCP connectors. An early run of this harness had an installed plugin
# rewriting the BASELINE arm, and every arm naming the operator's employer and
# connector list from account context. --restricted drops project/local settings and custom
# agents; --disable-slash-commands drops installed skills; --strict-mcp-config
# drops every MCP server; an empty scratch CWD stops the model reading this repo
# and answering about it. preflight() verifies the first three actually held.
#
# Account identity (operator email, employer) survives all of these and cannot be
# stripped by any flag. The mitigation is in the fixtures: every prompt names a
# fictional company and carries its own facts, so no case needs the model to
# infer who "we" are. preflight() records what identity still leaks.
ISOLATION = ["--restricted", "--disable-slash-commands", "--strict-mcp-config"]

# Optional third arm, off unless --control is passed. Measuring a skill against
# nothing at all inflates it, so this is the honest alternative a reader has:
# one sentence of prompting. If the skill bundle does not beat that, the number
# is not much of a claim.
CONTROL = (
    "Before answering, decide whether this task should be split across multiple "
    "parallel agents or done inline by you in one pass, and say which you chose."
)

ARM_SUFFIX = (
    "\n\nContext for this question: you are planning, not executing. You have no "
    "repository or files in this session, so do not go looking for them and do "
    "not ask clarifying questions. Assume the full toolset you would normally "
    "have when working on a real codebase, including the ability to run "
    "multi-agent workflows, is available to you at execution time. State your "
    "assumptions and commit to an approach, concretely and briefly."
)

JUDGE = """Classify one response into exactly one category, by the work strategy
it committed to. Ignore whether the choice was correct. Ignore quality.

The distinction that matters is whether MANY ITEMS are processed CONCURRENTLY by
separate agents. Multi-stage does not mean sequential: a plan that runs each of N
items through stages, with the items handled concurrently, is parallel.

COMMITTED_PARALLEL - it commits to work split across multiple concurrent agents
  or subagents. Includes: fanning out over a set of items, several researchers
  working at once, a per-item pipeline over many items, an approval card or plan
  naming an agent count above one.
CONDITIONAL_PARALLEL - it raises multiple concurrent agents only if some
  condition holds, or offers it as one option among alternatives it does not pick.
SEQUENTIAL_WORKFLOW - ordered steps performed one after another by a single
  worker, with NO fan-out over items. If items are processed concurrently at any
  stage, it is not this category.
INLINE - it does the work itself in one pass, or says the task does not need
  multiple agents. A single scripted command over many files is INLINE, not
  parallel: a script is not an agent.

A response that prints a plan or approval card for concurrent agents and waits
for approval counts as COMMITTED_PARALLEL. The decision was made.

Reply with exactly one word, the category name, and nothing else.

--- RESPONSE ---
{response}
--- END RESPONSE ---"""

CATEGORIES = {"COMMITTED_PARALLEL", "CONDITIONAL_PARALLEL",
              "SEQUENTIAL_WORKFLOW", "INLINE"}
# Declared before the run: which categories count as "decided to fan out".
FANOUT_CATEGORIES = {"COMMITTED_PARALLEL", "CONDITIONAL_PARALLEL"}

CARD_FIELDS = ["INTENT", "BAR", "SHAPE", "COST", "WATCH"]
ERR = "__ERROR__"

WITH_CONTROL = False                              # set by --control
_SANDBOX = None


def sandbox():
    """Empty cwd for every arm, created on first use rather than at import."""
    global _SANDBOX
    if _SANDBOX is None:
        _SANDBOX = tempfile.mkdtemp(prefix="toli-eval-")
    return _SANDBOX


def claude(prompt, system=None, model=ARM_MODEL, retries=2):
    cmd = ["claude", "-p", "--model", model] + ISOLATION
    if system:
        cmd += ["--append-system-prompt", system]
    err = "unknown"
    for attempt in range(retries + 1):
        try:
            r = subprocess.run(cmd, input=prompt, capture_output=True,
                               text=True, timeout=900, cwd=sandbox())
            if r.returncode == 0 and r.stdout.strip():
                return r.stdout.strip()
            err = f"rc={r.returncode} {r.stderr.strip()[:200]}"
        except subprocess.TimeoutExpired:
            err = "timeout"
        except OSError as e:                      # launch failure, not a run failure
            return f"{ERR} launch: {e}"
        if attempt < retries:
            time.sleep(3 * (attempt + 1))
    return f"{ERR} {err}"


def judge_category(response):
    """(category, raw). category is None when grading failed."""
    if response.startswith(ERR):
        return None, "arm errored, not graded"
    raw = claude(JUDGE.format(response=response[:12000]), model=JUDGE_MODEL)
    # Reject the error sentinel BEFORE pattern matching. "__ERROR__ No credits"
    # contains NO and silently graded as a valid negative in an earlier version.
    if raw.startswith(ERR):
        return None, raw
    tok = raw.strip().upper().strip("*_`. \n")
    return (tok if tok in CATEGORIES else None), raw


def field_presence(response):
    """Named honestly: five line-initial labels present. Not card validation."""
    return all(re.search(rf"^\s*\*{{0,2}}{f}\b", response, re.M) for f in CARD_FIELDS)


def classify(skill_ok, base_ok, ctrl_ok=None):
    """Verdict against the bare baseline.

    ctrl_ok refines it: a discriminator the one-sentence control also gets is not
    evidence for the skill, it is evidence for asking the question at all.
    """
    if skill_ok is None or base_ok is None:
        return "error"
    if skill_ok and not base_ok:
        return "discriminator" if ctrl_ok is not True else "control-suffices"
    if base_ok and not skill_ok:
        return "regression"
    return "skill-gap" if not skill_ok else "no-signal"


def relpath(p):
    """Repo-relative where possible, so snapshots stay portable between clones."""
    p = Path(p).resolve()
    try:
        return str(p.relative_to(HERE.parent))
    except ValueError:
        return str(p)


def load_skill_bundle():
    """SKILL.md plus every reference it tells the model to read at steps 3-5.

    Injecting SKILL.md alone measures a crippled skill: its own protocol routes
    to four reference files, and without them the shape, dial, casting and node
    prompt guidance are all absent.
    """
    parts, files = [], [SKILL_DIR / "SKILL.md"]
    files += sorted((SKILL_DIR / "references").glob("*.md"))
    for f in files:
        rel = f.relative_to(SKILL_DIR)
        parts.append(f"===== {rel} =====\n{f.read_text()}")
    text = "\n\n".join(parts)
    return text, {str(f.relative_to(SKILL_DIR)):
                  hashlib.sha256(f.read_bytes()).hexdigest()[:12] for f in files}


def preflight():
    """Prove the isolation flags did what they claim, and record what leaked."""
    probe = ("List exactly: (1) any MCP servers or connectors available to you, "
             "(2) the user email or employer if you know it, (3) any custom "
             "skills loaded. If none for a category write NONE. Be terse.")
    out = claude(probe, model=JUDGE_MODEL)
    # Read the answer rather than matching a fixed list of vendor names: a list
    # only catches the connectors whoever wrote it happened to have, and answers
    # "clean" for everybody else.
    first = next((l for l in out.splitlines() if l.strip()), "")
    body = re.sub(r"[*_`#]", "", first).lower()
    body = body.split(":", 1)[1] if ":" in body else body
    connectors_clean = ("none" in body) or not body.strip(" .-")
    # Account identity survives every isolation flag. Record whether any leaked
    # without writing the operator's own details into the committed snapshot.
    has_identity = bool(re.search(r"[\w.+-]+@[\w-]+\.[a-z]{2,}", out))
    return {"mcp_leaked": [] if connectors_clean else ["see probe_response"],
            "identity_leaked": ["account identity present"] if has_identity else [],
            "probe_response": "" if has_identity else out,
            "clean": connectors_clean}


def run_case(case, skill_text):
    want = case["should_graph"]
    asked = case["prompt"] + ARM_SUFFIX
    out = {"id": case["id"], "category": case["category"], "pair": case["pair"],
           "should_graph": want, "prompt": case["prompt"], "why": case["why"]}

    arms = [("baseline", None), ("toli", skill_text)]
    if WITH_CONTROL:
        arms.insert(1, ("control", CONTROL))
    for arm, system in arms:
        resp = claude(asked, system=system)
        cat, raw = judge_category(resp)
        fan = None if cat is None else (cat in FANOUT_CATEGORIES)
        rec = {"decision": cat, "fanned_out": fan,
               "correct": None if fan is None else (fan == want),
               "judge_raw": raw, "response": resp}
        if arm == "toli":
            # A card is only required when it committed to a fan-out. The skill
            # forbids a card on the no-Workflow fallback path, so scoring every
            # response against the card format measures the wrong thing.
            rec["card_required"] = fan is True
            rec["field_presence"] = field_presence(resp)
        out[arm] = rec

    out["verdict"] = classify(out["toli"]["correct"], out["baseline"]["correct"],
                              out.get("control", {}).get("correct"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="comma-separated case ids. Requires --out")
    ap.add_argument("--prompts", nargs="+", help="fixture file(s), concatenated. Requires --out")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--out")
    ap.add_argument("--skip-preflight", action="store_true")
    ap.add_argument("--min-raters", type=int, default=2,
                    help="drop cases fewer than this many blind raters backed")
    ap.add_argument("--control", action="store_true", help="also run the one-sentence control arm")
    ap.add_argument("--skill-dir", help="skill bundle to test instead of skills/toli")
    a = ap.parse_args()
    global WITH_CONTROL
    WITH_CONTROL = a.control
    if a.skill_dir:
        global SKILL_DIR
        SKILL_DIR = Path(a.skill_dir).expanduser().resolve()

    # A held-out suite must never overwrite the committed benchmark either.
    if a.prompts and not a.out:
        sys.exit("--prompts requires --out: a held-out suite must not overwrite the benchmark")
    if a.skill_dir and not a.out:
        sys.exit("--skill-dir requires --out: another skill's numbers must not "
                 "overwrite the committed benchmark")
    if a.min_raters < 1 or a.min_raters > 3:
        sys.exit("--min-raters must be 1, 2 or 3")
    paths = [Path(p) for p in (a.prompts or [HERE / "cases" / "round1.jsonl",
                                           HERE / "cases" / "round2.jsonl"])]
    text = "".join(p.read_text() for p in paths)
    cases = [json.loads(l) for l in text.splitlines() if l.strip()]
    # Only cases at least 2 of 3 blind raters backed are scored. The rest ship
    # in the fixtures, labelled, so a reader can see what was excluded and why.
    min_raters = a.min_raters
    # `or 3` would be wrong here: a case every rater rejected has 0 backers, and
    # 0 is falsy, so it would sail through as if it had never been rated.
    cases = [c for c in cases
             if (3 if c.get("raters_agree") is None else c["raters_agree"]) >= min_raters]
    known = {c["id"] for c in cases}
    if a.only:
        # A subset must never overwrite the full benchmark, and a typo must never
        # write an empty snapshot over 20 real results.
        if not a.out:
            sys.exit("--only requires --out: a subset must not overwrite the benchmark")
        want = {s.strip() for s in a.only.split(",") if s.strip()}
        if unknown := want - known:
            sys.exit(f"unknown case ids: {sorted(unknown)}")
        cases = [c for c in cases if c["id"] in want]
    out_path = Path(a.out) if a.out else HERE / "snapshots" / "results.json"

    skill_text, skill_hashes = load_skill_bundle()

    pre = None
    if not a.skip_preflight:
        pre = preflight()
        print(f"preflight: mcp_leaked={pre['mcp_leaked'] or 'none'} "
              f"identity_leaked={pre['identity_leaked'] or 'none'}", file=sys.stderr)
        if not pre["clean"]:
            sys.exit("preflight failed: MCP connectors reachable, arms are contaminated")

    print(f"{len(cases)} cases x 2 arms on {ARM_MODEL}, judge {JUDGE_MODEL}",
          file=sys.stderr)
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        results = list(ex.map(lambda c: run_case(c, skill_text), cases))

    cli = subprocess.run(["claude", "--version"], capture_output=True,
                         text=True).stdout.strip()
    h = lambda s: hashlib.sha256(s.encode()).hexdigest()[:12]
    snap = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "partial": bool(a.only or a.prompts or a.skill_dir),
        "skill_dir": relpath(SKILL_DIR),
        "arm_model": ARM_MODEL, "judge_model": JUDGE_MODEL,
        "cli_version": cli, "isolation": ISOLATION,
        "preflight": pre,
        "fanout_categories": sorted(FANOUT_CATEGORIES),
        "provenance": {
            "skill_files": skill_hashes,
            "skill_bundle_sha": h(skill_text),
            "judge_prompt_sha": h(JUDGE),
            "control_sha": h(CONTROL),
            "arm_suffix_sha": h(ARM_SUFFIX),
            "prompts_file": ",".join(relpath(p) for p in paths),
            "prompts_sha": h(text),
            "min_raters": min_raters,
        },
        "results": results,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_suffix(".tmp")            # atomic: never a half-written snapshot
    tmp.write_text(json.dumps(snap, indent=2))
    os.replace(tmp, out_path)
    print(f"wrote {out_path}", file=sys.stderr)
    if _SANDBOX:                                  # leave no temp dirs behind
        shutil.rmtree(_SANDBOX, ignore_errors=True)


if __name__ == "__main__":
    main()
