# The five dials

Shape is the easy part. These are the decision surface.

## 1. Barrier

**Default: none. Use `pipeline()`.**

A barrier (`parallel()` between stages) is correct only when stage N needs cross-item context from all of stage N-1:

- dedupe or merge across the full result set before expensive downstream work
- early-exit when the total is zero
- stage N's prompt literally references "the other findings"

Not a reason: "I need to flatten or filter first" (do it inside a pipeline stage), "the stages feel separate", "cleaner code".

Cost of a wrong barrier: on uneven work the fast items idle while the slowest sibling finishes, every stage. Real-world inputs are almost always uneven.

## 2. Verify depth

| setting | when |
|---|---|
| none | extraction only, no judgment involved |
| 1 judge | low stakes, internal, you'll eyeball the output anyway |
| 3 refuters | the finding is a claim that could be plausible-but-wrong |
| diverse lens | the finding can fail in more than one way |

A single evaluator agrees with confident-sounding wrong output. Refuters are
prompted to kill the finding, and they return one of three verdicts, never two:

- `refuted` requires counter-evidence, quoted. Not a hunch, not silence
- `confirmed` requires the finding to survive an actual attempt to kill it
- `unresolved` is the honest answer when neither holds, and it is common

Majority of confirmed survives. Unresolved findings are carried into the output
separately and never silently dropped. "Default to refuted when uncertain" is the
wrong rule for an exhaustive sweep: it converts missing evidence into a clearance
claim, which is exactly how a sweep misses the one that mattered.

Diverse lens beats redundancy when failure modes differ: is it accurate / does it reproduce / is it defensible / would the decision-maker care. Same count, more coverage.

## 3. Termination

- **fixed** when the input set is knowable up front (20 documents, 8 competitors)
- **until-dry** when it is not. Keep spawning finders until K consecutive rounds surface nothing new. Dedupe against everything *seen*, not everything *confirmed*, or rejected findings reappear forever and it never converges
- **until-budget** when the user set a token target. Guard on `budget.total` or an unset target loops to the agent cap

Fixed fan-out on an unknown-cardinality problem silently truncates, and truncation reads as coverage.

Dry rounds are evidence of convergence, not proof of completeness. If every finder
searched the same way, the rounds go dry while a whole modality is still unlooked-at.
Say so in WATCH.

## 4. Casting

Who runs each node: agent type, effort, model, tool reach. Set per stage, never per run.

Full roster and rules in `casting.md`. The three that decide most cases:

- ask first whether the node needs an agent at all. Filtering, deduping and grouping belong in script code
- fan-out stages run `effort: 'low'`, verify and synthesis run default or higher
- read-only stages get a read-only agent type so a looking stage cannot write

Nodes that touch interactively-authenticated MCP servers cannot run headless or on a cron. See `casting.md`.

## 5. Isolation

- read-only: nothing
- agents write to the same working tree in parallel: `isolation: 'worktree'`

Worktree costs setup time and disk per agent. Only when writes would actually collide.
