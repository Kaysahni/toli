# The eight shapes

Seven run as `Workflow`. The eighth runs as an agent team.

Diagrams here are the ones to print in the card. Keep them under 6 lines. Barriers must be visible.

---

## 1. Sequential

```
research ─▶ analyze ─▶ draft ─▶ review ─▶ deliver
```

**When:** each step genuinely needs the previous step's output. One artifact moving forward.

**When not:** the steps are independent and you chained them out of habit. This is the shape people over-pick.

```js
const facts = await agent('...', {schema: FACTS})
const draft = await agent(`Write from: ${JSON.stringify(facts)}`, {schema: DRAFT})
```

---

## 2. Router

```
request ─▶ classify ─┬─▶ path A
                     ├─▶ path B
                     └─▶ escalate to human
```

**When:** one input, mutually exclusive handling paths, and misrouting is cheap to detect.

**When not:** the branches overlap. Overlapping branches means you wanted parallel.

Classifier must return a schema with a closed enum plus a confidence field. Route low confidence to the human branch.

```js
const r = await agent(prompt, {schema: {type:'object',
  required: ['route','confidence'], properties:{
    route: {enum: ['a','b','human']},
    confidence: {type:'number', minimum: 0, maximum: 1}}}})
if (!(r.confidence >= 0.7)) return escalate(r)   // catches missing and NaN too
```

`required` is not optional here. Without it `{}` validates, and `undefined < 0.7`
is false, so the escalation you just wrote never fires.

---

## 3. Parallel

```
plan ─┬─▶ researcher A ─┐
      ├─▶ researcher B ─┼─▶ synthesis
      └─▶ researcher C ─┘
```

**When:** several angles on one question, and synthesis genuinely needs all of them at once.

**When not:** the workers are processing separate items rather than separate angles. That is pipeline.

The barrier is the point of this shape. If you cannot state why synthesis needs all three simultaneously, use pipeline.

---

## 4. Pipeline (the workhorse)

```
20 items
   ├─ read ─ judge ─ verify ─┐
   ├─ read ─ judge ─ verify ─┼─▶ group
   └─ ...                    ┘   (only barrier)
```

**When:** many independent items, each needing the same multi-stage treatment. The default for audits and sweeps.

**When not:** stage 2 needs to compare item A against item B.

Wall clock is bounded below by the slowest single chain, not by the sum of
slowest-per-stage. On uneven inputs that is a large difference. It is also
bounded below by total agents divided by concurrency: 20 chains through 4 slots
is 5 waves however fast each chain is. The real number is above both bounds.

```js
const out = await pipeline(items,
  it => agent(`Extract from ${it.ref}`, {phase:'Read', effort:'low', schema: EXTRACT}),
  (ex, it) => agent(`Judge: ${JSON.stringify(ex)}`, {phase:'Judge', schema: VERDICT}))
```

---

## 5. Orchestrator

```
goal ─▶ planner ─┬─▶ worker ─┐
                 ├─▶ worker ─┼─▶ report
                 └─▶ worker ─┘
```

**When:** you do not know the task list until an agent looks. Planner returns a schema'd task array, the script fans out over it.

**When not:** you already know the task list. Then it is pipeline and the planner is a wasted hop.

Cap the planner's output length in its prompt, or it will invent forty tasks.

---

## 6. Review loop

```
create ─▶ review ─┬─ approve ─▶ done
                  └─ revise ──┘  max 3
```

**When:** one artifact, iterated to a standard. Copy, a doc, a spec.

**When not:** many artifacts. Loop each one inside a pipeline stage instead.

Always cap iterations. Always require the reviewer to return `{pass, gaps[]}` so a fail is actionable rather than vibes.

---

## 7. Diamond

```
plan ─┬─▶ explore ─┐
      ├─▶ explore ─┼─▶ consolidate ─▶ verify each ─▶ synthesize
      └─▶ explore ─┘   (code, barrier)
```

**When:** open-ended research where you diverge to cover ground, then need the surviving findings merged into one view.

**When not:** you need per-item verdicts rather than one merged view. That is pipeline.

The verify layer is what separates this from Parallel. Findings get independently attacked before synthesis sees them.

Consolidate is a barrier and it is code, not an agent: dedupe on a stable identity,
merge findings the explorers reported separately, drop anything the bar excludes.
Skipping it is the common way this shape gets expensive. Three explorers surfacing
the same finding become three verify fan-outs of the same claim, and the duplicate
confirmations then read as three independent confirmations in the synthesis. See
`casting.md` for the identity-key rule: `new Set()` does not dedupe objects.

Compose with until-dry termination when the finding count is unknown.

---

## 8. Debate (runs as an agent team, not a Workflow)

```
   hypothesis A ◀──▶ hypothesis B
        ▲  ╲          ╱  ▲
        │   ╲        ╱   │
        ▼    hypothesis C ▼
        └──── consensus ───┘
```

**When:** competing explanations for one thing, and the workers need to attack each other's theories, not just report up. Root-cause hunts, "why did this number move", strategy calls with real disagreement.

**When not:** anything where siblings are independent. Which is most work.

**Why it is not a Workflow:** Workflow subagents have no edges between siblings. They report to the caller and never see each other. Peer-to-peer needs agent teams.

Cost and constraints, state these in the card:

- meaningfully more expensive than a Workflow of the same agent count. Each teammate is a full session with its own context load, and nothing is summarized on the way back
- no resume. `/resume` does not restore teammates
- experimental. Needs `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` in settings
- 3 to 5 teammates. Three focused beats five scattered

Output for this shape is a spawn prompt the user pastes, not a script:

```
Spawn 5 teammates, each holding one hypothesis for <the thing>.
Have them message each other to try to disprove each other's theories,
like a scientific debate. Record whatever consensus survives in <file>.
```

Naming each teammate in the spawn prompt makes them addressable later.

---

## Picking

| signal | shape |
|---|---|
| many independent items, same treatment | pipeline |
| one question, several angles, merged answer | parallel or diamond |
| findings need attacking before you trust them | diamond |
| task list unknown until an agent looks | orchestrator |
| one artifact, iterate to a standard | review loop |
| mutually exclusive handling paths | router |
| workers must argue with each other | debate |
| genuinely dependent steps | sequential |

Sequential is the default people reach for and is usually wrong. Check pipeline first.
