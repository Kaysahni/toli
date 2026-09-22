---
name: toli
description: Use when work spans many independent items or an unknown number of them, and getting it wrong means missing some. Sweeps, audits, coverage claims, migration and pre-retirement surveys, research passes, competitive scans, synthesis across sources. Fires on asks shaped like "find every place X", "which of our N things do Y", "what still depends on X before we retire it", "nobody has a list", "prove we checked everything", or a reviewer or exec wanting evidence. Also when the user says "/toli", "fan out", "parallelize", "spawn agents", "use a workflow", "use a graph", "graph this", or "be comprehensive"; when a multi-agent run returned wrong or incomplete output; or when asked which topology, pattern or shape fits a task. Use it to decide NOT to fan out too: it refuses work that only looks big.
license: MIT
---

# Toli

Turns a vague ask into a shaped multi-agent run. The user approves a short card, says `go`, and it executes.

**This skill is explicit user opt-in for the Workflow tool.** When the user says `go`, call Workflow without asking again.

## Gate

Fan out when **two or more** hold:

- more than 5 independent items to process. Items are the ones the **ask** names,
  not a decomposition you invent. Three vendors scored on six axes is three items,
  not eighteen. Any task can be sliced until it clears five, so if you had to
  slice it to get there, you did not have five. A single artifact whose own ask
  names the items ("30 requirements, tell me about each") does clear it, as long
  as each item is judged on its own. It does **not** fire when the deliverable is
  one thing whose parts must agree with each other: a ranking, a single filing, a
  questionnaire response, one flow reviewed end to end. Twelve agents scoring in
  isolation produce twelve incompatible scales. This exception covers the
  deciding, not the evidence. When each part's evidence is its own dig, held by a
  different team, system or authority (one policy line that binds five owning
  teams, a permit path with five separate inspectors, a card rebuilt from a year
  of a competitor's moves), the items still count: gather in parallel, then write
  the single artifact in one pass
- each item needs its own **multi-step exploration**, not a lookup: many tool
  calls, its own dead ends, no state shared with the other items. This holds even
  at three or four items ("sign up for each of these 5 competitors and walk the
  flow"). Count it only when the ask requires that depth, not when you could
  choose to go deep. Reading one document or checking one fact is a lookup.
  A few factual claims in one outbound artifact (a customer email, a contract
  about to be signed, a filing) do count when each claim needs its own evidence
  from a different system or team. The must-agree exception covers the wording,
  not the checking
- unknown cardinality of the **input set**: nobody has the list, and building it
  means searching more than one place or more than one lookup. Not the number of
  findings, and not "unknown until I read it". Findings are always unknown and
  everything is unknown until read, so either of those readings makes this
  criterion always true and the gate stops working. A set you can enumerate in one
  tool call, one file or one stated number, is a known set
- the output feeds a decision someone makes **on the coverage claim itself**: a
  retirement, a sign-off, an audit response. Not merely that the artifact has
  readers. Every doc and every piece of copy is read by someone, so counting
  that makes this criterion always true on writing work
- the verdict is a judgment call a single agent would be too agreeable about
- more than one separate source has to be searched for real coverage. Count
  places, not kinds: four answer engines are four sources even though they are the
  same kind of tool. Two queries against the same index are one

If the verdict hinges only on a count nobody knows ("how many surfaces mention
the old tier name?") and one lookup would settle it, do that lookup inline first,
then apply the gate. That is not a fan-out, and it turns a guess into a decision.

Otherwise inline. One known change, one lookup, or one rewrite never splits,
and neither does one source unless it holds more than 5 genuinely independent items
that each need their own judgment. Iterating one artifact to a standard is the
review loop shape, which does split, so do not let this line veto it.

Two things that look like fan-outs are not:

- **One causal chain is one item.** An incident traced through four systems has
  four sources, but each log only means something next to the others. Splitting
  the reading hands every agent half of each hand-off. One reasoner follows it.
- **Items bound by one shared constraint are one deliverable.** A budget cap, a
  chain of synchronous dependencies, one allocation. The per-item reading only
  counts as depth if each read is its own investigation, not a lookup in a source
  that is already attached.

When the gate fails, no card. Print exactly four things, in one
short paragraph, then do the work in the same turn:

1. the verdict: `Not a fan-out.`
2. the criterion that failed, named
3. the avoided cost, derived or bounded by the same rule COST uses below. Never bare
4. the inline alternative

A refusal with no number is invisible. The user cannot see a run that never
happened, so the spend it prevented is the only observable value of a no. Without
it every correct refusal looks like the skill doing nothing.

## Protocol

1. **Restate.** One line: what they're asking, plus the unstated constraint you're inferring.
2. **Gate.** Criteria above. If it fails, stop here.
3. **Shape.** Pick from `references/patterns.md`. Note the runner-up.
4. **Dials.** Set all five from `references/dials.md`. Dial 4 is casting: who runs each node, per `references/casting.md`.
5. **Rewrite.** Convert the ask into node prompts per `references/prompt-rubric.md`. Do not print them unless asked.
6. **Card.** Print the card. Stop. Wait.
7. **Run.** On `go`, emit the script and call Workflow. On `go but <change>`, see Verbs: the change can move the count into a higher band, which stops again. Print the returned run id and scriptPath, in that order, before anything else: the run id is what resume needs, and it is gone once the session is.

Read the references at the step that names them, not up front. `by-function.md` at step 2, only the section matching the ask's job, when the call is close. `patterns.md` at step 3, `dials.md` and `casting.md` at step 4, `prompt-rubric.md` at step 5.

Two guards before the card:

- **Shape 8 (debate) runs on agent teams, not Workflow.** Only pick it if
  `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set. It needs no Workflow tool: the
  card is still printed, and step 7 emits a spawn prompt instead of a script, per
  `patterns.md`. Without the flag, take the runner-up and say why in the SHAPE
  parenthetical.
- **Any other shape, no Workflow tool, no card.** If Workflow is unavailable, say
  so in one line and print the node prompts as a numbered pack instead. Skip COST:
  you cannot promise agents you cannot spawn.

## Card

The card block is exactly these five fields plus the diagram, in this order, and
nothing else inside the block:

```
INTENT   <what they want -> what they get>
BAR      <the definition that decides in/out. in their words>
SHAPE    <pattern name + modifiers>   (not <runner-up>: <why it lost>)

         <ascii diagram from patterns.md, barriers visible>

COST     <n agents, derived or bounded> · depth n · max n concurrent · any non-default casting
WATCH    <the single stage most likely to be wrong>
```

Auto-expand output and any ceiling negotiation go after the block, before you wait.

SHAPE names one of the eight by name. The parenthetical is not optional: name the
runner-up and the one condition that would flip the choice, so the user can
overturn it without reading anything else.

COST never carries a wall-clock estimate, and never a bare number. The agent
count is one of exactly two things:

- **derived**, when the input set is known: `42 agents (18 items x 2 stages + 6
  refuters)`. It is arithmetic. A run that spends 60 means the formula was
  wrong, and you can see where.
- **bounded**, when it is not: `up to 28 agents (4 finders/round, cap 4 rounds,
  + 3 refuters/candidate)`, followed by the variable that moves it.

A bare `42 agents` is a guess, cannot be checked, and hides drift.

Depth is a lower bound on wall clock, not the wall clock. Total agents divided by
peak concurrency is a second bound, and queueing puts the real number above both.
That is why both are printed and minutes never are.

`go` · `go but <change>` · `why` · `who` · `scope` · `prompts` · `cheaper`

BAR is the highest-value field. Most bad runs come from a loose definition, not a wrong shape. State it as a rule that decides membership, and name one thing it excludes.

## Verbs

| verb | print |
|---|---|
| `why` | shape reasoning, runner-up, what breaks if the pick is wrong |
| `who` | per stage: agent type, effort, model, which MCP tools it needs, what runs as plain code instead |
| `scope` | the input set, and what was cut plus the cut rule |
| `prompts` | every node prompt, schema, done-criteria |
| `cheaper` | 3 cost-cut variants, each with its tradeoff named. One of the three is always the inline baseline: do it in a single pass, and what that loses |
| `full` | all of the above |
| `go but <change>` | the card fields the change moved, and nothing else. Then run |

`go but <change>` is not a second approval. Apply the change, reprint only the
fields that moved with their old value alongside, then run without waiting:

```
go but drop the EMEA contracts

         6 contracts
            ├─ read ─ judge ─┐
            ├─ read ─ judge ─┼─▶ group
            └─ ...           ┘

COST     12 agents (6 contracts x 2 stages)   was 41
Run started: 12 agents on the US contract set.
```

The diagram carries the item count in its first line, so it goes stale whenever
COST moves, shape or no shape. **If COST moved, reprint the diagram**, or the old
count sits on screen contradicting the new one. Reprint the SHAPE line itself only
when the pattern actually changed, since the runner-up reasoning is unaffected by
scope. A change that moves nothing prints `unchanged` on one line and runs.

The delta is printed text, not a log entry. Recomputing the count and writing it
to the log is not the work, and never ends the turn on its own: a turn that logs
a new number without showing it leaves the user looking at the old card.

The exception is the ceiling. A change moves the input set, the input set moves
the agent count, and the count can land in a higher band than the card was
approved at. Recompute the band. If the change crosses into one, the Auto-expand
table applies again and it stops and waits, exactly as if that count had been on
the first card. Crossing downward never stops.

## Auto-expand

Default ceiling is 15 agents. What happens over it depends on the band, and every
count lands in exactly one:

| agents | after the card block |
|---|---|
| up to 15 | nothing. Stop and wait |
| 16 to 50 | one line: `41 agents, over the 15 ceiling. "cheaper" for 3 trims, "go" to run as-is.` Then wait |
| over 50 | that line, then print `full` unasked. `go` is only accepted after the expansion is on screen |

Offer to trim scope before offering to raise the ceiling.

Also print `full` unasked, at any count, when agents write files, or the output
goes outward (board doc, customer, published copy), or the user raised the
ceiling.

## Running

Inline `script` in the Workflow call. Never Write it to a file first.

Load the built-in `workflow-authoring` skill for the script API, its gotchas, and
resume. Do not restate it here. On top of it:

- open the script with the approved card as a comment block. The script source is
  stored verbatim in the run record, so this is the only copy of the card that
  outlives the session
- a derived count is a ceiling the script enforces, not a prediction. Cap the
  input set in code and `log()` everything dropped, with the cut rule
- a capped run is a partial sweep and the output must say so. Carry `complete`,
  `processed`, `unprocessed` and `stop_reason` into the final result. A coverage
  claim made from a capped run is the same lie as truncation reading as coverage
- cast every node before writing it: `agentType`, `effort`, and the MCP tool named in the prompt
- every fan-out agent gets `schema`
- default to `pipeline()`; a barrier needs a stated cross-item reason

## After

The moment Workflow returns, print this block and nothing fancier:

```
Run started: <n> agents <on what, in the user's terms>.

Script: <scriptPath>
Run ID: <runId>

If a stage comes back wrong, edit that stage in the file and resume with this run
ID. Stages that did not change reuse their saved results. Watch it with
/workflows. Results arrive when it finishes.
```

`<n>` is the real number the script will spawn, not the card's ceiling, when the
two differ. Both the path and the id, every time: the id is what resume needs and
it dies with the session, the file is the only copy of the card that does not.
Never a wall-clock estimate for when results arrive.

When output is wrong, edit the one bad stage in that file.

Same session: stop the prior run with `TaskStop`, then re-run with
`{scriptPath, resumeFromRunId}`. Unchanged earlier stages return cached. Say this
to the user rather than re-running whole.

New session: resume is gone. The cache does not survive the session, so a re-run
pays for every stage again. Before re-running, narrow the input set in the script
to the items that were actually wrong, and say the full-cost consequence out loud
rather than re-running silently. This is why the card is written into the script
as a comment block: the script outlives the session, the run cache does not.

Results over 15 rows or tabular: publish an Artifact, print the URL.

## Log

Last step of every invocation, refusals included. Append one JSON line to
`~/.toli/log.jsonl`:

```json
{"ts":"","ask":"","gate":"fanout|refuse","criteria_fired":[],
 "shape":"","runner_up":"","flipped":false,
 "agents_predicted":0,"agents_spent":0,"complete":true,"verb":"go",
 "agents_avoided":0}
```

`agents_avoided` on refusals only, `shape` onward on fan-outs only. One line, no
schema, no tooling.

This is the only instrumentation toli has. The gate itself is measured offline in
`evals/`, on cases written by agents that never read this skill, but two claims
here cannot be tested that way and need real usage: that naming the runner-up
ever causes anyone to overturn a shape, and that a derived agent count predicts
what a run actually spends. Each is a column in that line. Do not skip it because
a run went well.
