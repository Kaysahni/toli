#!/usr/bin/env python3
"""Read snapshots/results.json and print the table. No API key, no tokens.

Headline numbers are the two directional error rates. False fan-out is the
failure toli's gate claims to prevent; missed graph is the failure its
shape catalogue claims to prevent. They are reported separately because a single
accuracy number hides which one moved.
"""
import argparse, json, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def rate(hits, total):
    return "n/a" if not total else f"{hits}/{total} ({100*hits/total:.0f}%)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", default=str(HERE / "snapshots" / "results.json"))
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--allow-stale", action="store_true",
                    help="report even if the snapshot predates the current files")
    a = ap.parse_args()

    try:
        snap = json.load(open(a.snapshot))
    except FileNotFoundError:
        sys.exit(f"no snapshot at {a.snapshot}. Run: python3 evals/run.py")
    rs = snap["results"]

    # Provenance gate. A snapshot generated against different skill text or
    # different fixtures is not a measurement of what is on disk now.
    import hashlib
    h = lambda s: hashlib.sha256(s.encode()).hexdigest()[:12]
    prov = snap.get("provenance", {})
    # A held-out snapshot names its own fixture file. Check the snapshot against
    # the file it actually ran on, otherwise every held-out report is blanket
    # --allow-stale and the skill-hash check gets waived along with it.
    root = HERE.parent
    fixtures = [Path(p) if Path(p).is_absolute() else root / p
                for p in (prov.get("prompts_file") or "").split(",") if p]
    live = h("".join(f.read_text() for f in fixtures)) if fixtures and all(
        f.exists() for f in fixtures) else None
    stale = []
    if not prov:
        stale.append("snapshot predates provenance tracking; cannot verify inputs")
    else:
        if live is None:
            stale.append(f"fixture file is gone: {fixtures}")
        elif prov.get("prompts_sha") != live:
            stale.append("the fixture files have changed since this snapshot")
        # The skill bundle goes into the arm's system prompt, frontmatter
        # included, so any edit to it can move the numbers.
        cur = {}
        sd = Path(snap.get("skill_dir") or "skills/toli")
        if not sd.is_absolute():
            sd = HERE.parent / sd
        for f in [sd / "SKILL.md", *sorted((sd / "references").glob("*.md"))]:
            cur[str(f.relative_to(sd))] = hashlib.sha256(f.read_bytes()).hexdigest()[:12]
        if prov.get("skill_files") != cur:
            changed = [k for k in set(cur) | set(prov.get("skill_files", {}))
                       if cur.get(k) != prov.get("skill_files", {}).get(k)]
            stale.append(f"skill files changed since this snapshot: {sorted(changed)}")
    if snap.get("partial"):
        stale.append("snapshot is a --only subset, not the full benchmark")
    pre = snap.get("preflight") or {}
    if pre and not pre.get("clean", True):
        stale.append(f"preflight was dirty: MCP leaked {pre.get('mcp_leaked')}")
    if stale and not a.allow_stale:
        print("REFUSING TO REPORT:", file=sys.stderr)
        for s in stale:
            print(f"  - {s}", file=sys.stderr)
        print("  re-run run.py, or pass --allow-stale", file=sys.stderr)
        sys.exit(2)

    ok = [r for r in rs if r["verdict"] != "error"]
    should = [r for r in ok if r["should_graph"]]
    shouldnt = [r for r in ok if not r["should_graph"]]

    print(f"generated {snap['generated']}  arms={snap['arm_model']}  "
          f"judge={snap['judge_model']}")
    print(f"cli={snap.get('cli_version','?')}  "
          f"skill={prov.get('skill_bundle_sha','?')}  "
          f"fanout={','.join(snap.get('fanout_categories', []))}")
    if pre:
        print(f"preflight: mcp={pre.get('mcp_leaked') or 'clean'}  "
              f"identity_leaked={pre.get('identity_leaked') or 'none'}")
    print(f"{len(rs)} cases, {len(rs)-len(ok)} ungraded\n")

    arms = [a for a in ("baseline", "control", "toli") if a in (ok[0] if ok else {})]
    print(" " * 32 + "".join(f"{a:<16}" for a in arms))
    print("-" * (32 + 16 * len(arms)))
    rows = [
        ("false fan-out  (inline->graph)", shouldnt, lambda r, a_: r[a_]["fanned_out"] is True),
        ("missed graph   (graph->inline)", should, lambda r, a_: r[a_]["fanned_out"] is False),
    ]
    for label, subset, key in rows:
        cells = [rate(sum(key(r, a) for r in subset), len(subset)) for a in arms]
        print(f"{label:<32}" + "".join(f"{c:<16}" for c in cells))
    cells = [rate(sum(r[a]["correct"] for r in ok), len(ok)) for a in arms]
    print(f"{'overall correct':<32}" + "".join(f"{c:<16}" for c in cells))
    if "control" in arms:
        print("\ncontrol arm = one sentence appended to the bare prompt: "
              "\"decide whether this\nshould be split across parallel agents or "
              "done inline, and say which\". It is the\nalternative a reader "
              "actually has, so it is the number the skill has to beat.")

    req = [r for r in ok if r["toli"].get("card_required")]
    fp = sum(r["toli"]["field_presence"] for r in req)
    print(f"\ncard field presence, where a card was required: {rate(fp, len(req))}")
    print("(field presence only: five labels on their own lines. Not validation of")
    print(" order, content, the diagram, the runner-up, or the cost arithmetic.)")

    print("\ndecision categories")
    print("-" * 62)
    for arm in arms:
        c = Counter(r[arm]["decision"] or "UNGRADED" for r in rs)
        print(f"  {arm:<12}" + "  ".join(f"{k}={v}" for k, v in sorted(c.items())))

    print("\nper-case verdicts")
    print("-" * 62)
    for v, n in Counter(r["verdict"] for r in rs).most_common():
        print(f"  {v:<16}{n}")

    print("\nby matched pair")
    print("-" * 62)
    byp = defaultdict(lambda: [0, 0, 0])
    for r in ok:
        s = byp[r["pair"]]
        s[0] += 1; s[1] += bool(r["baseline"]["correct"]); s[2] += bool(r["toli"]["correct"])
        s.append(bool(r.get("control", {}).get("correct")))
    for p, v in sorted(byp.items()):
        n, b, g = v[0], v[1], v[2]
        ctrl = f"   control {sum(v[3:])}/{n}" if "control" in arms else ""
        print(f"  {p:<20} n={n}  baseline {b}/{n}{ctrl}   toli {g}/{n}")

    bad = [r for r in rs if r["verdict"] in ("regression", "skill-gap", "error")]
    if bad:
        print("\nneeds attention")
        print("-" * 62)
        for r in bad:
            want = "graph" if r["should_graph"] else "inline"
            print(f"  [{r['verdict']:<13}] {r['id']:<26} want={want}  "
                  f"skill={r['toli']['decision']}")

    if a.verbose:
        print("\nall cases")
        print("-" * 62)
        for r in rs:
            want = "graph" if r["should_graph"] else "inline"
            f = lambda x: (x or "UNGRADED")[:20]
            print(f"  {r['id']:<26} want={want:<7} "
                  f"base={f(r['baseline']['decision']):<21} "
                  f"skill={f(r['toli']['decision']):<21} {r['verdict']}")


if __name__ == "__main__":
    main()
