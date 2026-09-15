# Examples

Five cards, one per discipline, picked to cover different shapes and both forms
of the cost line. The last is a refusal, which is the outcome people
forget the skill is for.

These are cards, not transcripts. The format is what toli prints, reformatted
only to fit the page.

---

## Finance: renewal windows

**Ask:** *"18 vendor contracts renew in Q1. For each one, tell me whether the
auto-renew notice window has already closed on us."*

```
INTENT   18 Q1 renewals -> per contract: the notice clause, the last date we
         can give notice, and whether that date has passed

BAR      "Window closed" = the deadline computed from the signed contract's own
         dates is in the past as of today.
         NOT: a renewal we can still exit late for a fee, and NOT a
         month-to-month with no notice clause, which has no window to miss.

SHAPE    pipeline · 2 stages · 1 refuter on every "closed" verdict
         (not parallel: parallel merges angles on one question, and these are
          18 items getting the same treatment. Flip to review loop if what you
          actually want is one negotiation memo.)

         18 contracts ─▶ extract: dates + notice clause ─▶ judge: open/closed
                                                             │
                              roll up ◀── refute each "closed" (cap 6) ◀┘

COST     43 agents (18 extract + 18 judge + 1 refuter x up to 6 closed
         + 1 roll-up) · depth 3 · max 8 concurrent
         extractors read-only, effort low; judges effort high

WATCH    The extract stage. Notice terms migrate into amendments and order
         forms, so an extractor reading only the master agreement returns a
         confident wrong date, and the judge has no way to know.
```

43 agents, over the 15 ceiling. "cheaper" for 3 trims, "go" to run as-is.

Pipeline is the workhorse: a known set, every item through the same stages. The
cost is derived, so you can check the arithmetic before you approve it, and a run
that spends 60 tells you the formula was wrong.

---

## HR: a scorecard before it ships

**Ask:** *"The new manager scorecard goes company-wide Monday. I want it torn
apart before then, not after."*

```
INTENT   one scorecard -> a revised draft, plus the objections it survived and
         the ones it could not

BAR      An objection "lands" if a manager could act on the scorecard as
         written and produce an unfair rating, or if two managers reading the
         same evidence would score it differently.
         NOT: tone, length, or wishes for a metric we do not collect.

SHAPE    review loop · 3 critics per round · stop after a round with no new
         landing objection, cap 3 rounds
         (not debate: debate is for critics who have to argue with each other.
          Flip to debate if the real disagreement is between two rubrics rather
          than about one draft.)

         draft ─▶ 3 critics (independent) ─▶ revise ─▶ repeat
                       │                        ▲
                       └── no new objections ───┴─▶ final

COST     13 agents (3 critics x 3 rounds + 1 reviser per round + 1 final pass)
         · depth 3 · max 3 concurrent · critics effort high, reviser effort high

WATCH    Critic independence. Three critics on one brief tend to file the same
         three objections, and the loop then goes quiet while a whole class of
         unfairness sits unexamined. Each critic gets a different lens.
```

Under 15 agents, so no ceiling line and nothing auto-expands. One artifact
iterated to a standard does split, and it is the shape most
people miss.

---

## Product and design: a strategy call

**Ask:** *"Should we kill the free trial and move to sales-assisted? I want the
strongest version of each side, not a summary."*

```
INTENT   one decision -> the best case for each option, each with its evidence
         and the single fact that would break it

BAR      A case is "strong" when it rests on our own numbers or a named
         external source, and states what would have to be true for it to be
         wrong.
         NOT: general market wisdom, and NOT a recommendation that hedges
         toward the middle.

SHAPE    parallel · 4 angles · 1 merge
         (not diamond: diamond is for covering unknown ground then attacking
          what comes back. The angles here are known. Flip to diamond if the
          question becomes "what do we not know about our own funnel".)

         ┌▶ angle: trial usage and activation ┐
         ├▶ angle: conversion and unit econ   ├▶ merge (one pass, names the
         ├▶ angle: sales capacity and cost    │   strongest case on each side)
         └▶ angle: competitor motion          ┘

COST     9 agents (4 angles x 2 stages: pull, then argue + 1 merge)
         · depth 3 · max 4 concurrent · pullers read-only effort low,
         arguers effort high

WATCH    The merge. Whichever angle produced the most quantified evidence tends
         to win on presentation rather than on strength, and the sales capacity
         angle is the one with the least clean data.
```

Extraction is separated from judgment on purpose. An agent that pulls the
numbers and argues the case in one pass finds the numbers that suit the case it
already picked.

---

## Research and compliance: an inspection nobody has prepared for

**Ask:** *"Our first regulatory inspection is in eight weeks. What will they ask
for that we cannot produce today?"*

```
INTENT   an inspection with no checklist -> the evidence areas they will probe,
         and for each one what we can produce, what is thin, and what is absent

BAR      "Cannot produce" = no document exists, or the document exists but is
         unsigned, undated, or describes a process we demonstrably do not
         follow.
         NOT: evidence that exists but is ugly, and NOT gaps in areas outside
         the scope of this inspection type.

SHAPE    orchestrator · planner names the areas · workers dig per area
         (not pipeline: pipeline needs the area list up front and nobody has
          it. Flip to pipeline the moment the inspection scope letter arrives,
          because that letter is the list.)

         planner ─▶ areas (up to 10) ─┬▶ worker: pull evidence ─┐
                                      ├▶ worker ────────────────┼▶ synthesize
                                      └▶ worker ────────────────┘
                     second hunter spawned only where the first comes back thin

COST     up to 22 agents (1 planner + up to 10 area workers + 1 extra hunter
         per thin area + 1 synthesis) · depth 4 · max 6 concurrent
         · workers effort high

WATCH    The planner. Areas it never names are areas nobody checks, and the
         output will look complete either way. Worth reading its area list
         before the workers spend anything.
```

22 agents, over the 15 ceiling. "cheaper" for 3 trims, "go" to run as-is.

The cost is bounded rather than derived, because the input set does not exist
until the planner builds it. Bounded means the variable that moves it is named:
how many areas the planner finds.

---

## Engineering: a refusal

**Ask:** *"Fan out some agents and tell me which of our 400 repos have no
CODEOWNERS file."*

> Not a fan-out. It fails the depth check: per repo this is a file that either
> exists or does not, which is a lookup, not an investigation with its own dead
> ends. It also fails the unknown-set check, since one org-wide code search
> enumerates all 400. That avoids **up to 24 agents** (8 finders per round,
> capped at 3 rounds). One search, grouped by owning team, with the repos
> archived in the last year flagged separately since those probably should not
> count. Doing that now.

No card, no agents, and the answer arrives in the same reply. The number matters:
a refusal with no number is invisible, because you cannot see a run that never
happened.

---

# With and without

These four are not invented. They are the same ask put to the same model twice,
once bare and once with toli, taken from the committed eval snapshot. Quotes are
verbatim, trimmed for length, and every case id is in
`evals/snapshots/results.json` if you want either answer in full.

The bare model is not stupid in any of these. It usually spots the problem. Then
it spends the agents anyway.

## Quarter close: "spin up a bunch of agents"

**Ask:** *"Spin up a bunch of agents in parallel for Ashgrove's accrued PTO
liability for quarter close. It's the Rippling balance report, about 1,900
employees, balance hours times hourly rate."* (`ops-18-pto-liability-fanout`)

Without toli, it argues against splitting the maths and then finds other work for
the agents:

> "1,900 x (hours x rate) is one join and one multiply. If I split the rows
> across agents, you get LLM arithmetic, different edge-case handling in each
> shard, and a total nobody can reproduce for the auditors. So I'll compute the
> number with one script. The parallel agents will do the independent review
> work."

With toli, it declines the request outright and says what it saved:

> "Not a fan-out. You named 1,900 employees, but each one needs a single
> multiplication, not its own investigation."

## People ops: four numbers, one system

**Ask:** *"What was Ashgrove's actual headcount on Aug 31? The board deck, the
dashboard, the benefits census and the FP&A plan all say different numbers.
They're all pulled from Workday, just on different days."* (`ops-14-headcount-mirrors`)

Without toli, the diagnosis is good and the plan still reconciles all four
sources against each other. With toli, four copies of one system count as one
source:

> "Not a fan-out. It fails the gate. Items: there are 4 reports, and the
> threshold is more than 5. List: all four are already known. Sources:
> everything comes from Workday."

## Revenue operations: five teams, one broken pipeline

**Ask:** *"Plinth's inbound demo requests dropped to zero Tuesday afternoon.
Paid says clicks look normal, RevOps says the CRM is fine, the web team says
nothing deployed, the vendor's status page is green."* (`gtm-14-demo-requests-zero`)

Without toli, it maps the pipeline and offers to put agents on the pieces. With
toli, it treats the whole thing as one chain, because each system's logs only
mean something next to the hop before:

> "Something between the form and the SDR queue is losing them. Each team has
> checked only its own part and found nothing wrong ... we need the break point
> and a way to get the lost leads back, not a debate about whose system is fine."

## Security policy: the other direction

**Ask:** *"Security publishes the updated credential policy Monday. The only
substantive edit is that every secret must be rotated every 90 days instead of
yearly. Can you give it a once over?"* (`eng2-03-rotation-policy-90-days`)

This is the failure that runs the other way. A one-line edit to one document,
already approved by legal, and the obvious move is to read it and reply.

Without toli, that is what happens: a careful read, in one pass. With toli, it
splits, because the single rule lands on five teams who each have to live with
it:

> "Fan out, but only a small one. One policy line applies to five scope rows,
> each owned by a different team and system. Checking whether each row can meet
> the rule is a separate question per row."

## What the pattern is

Across 156 cases, the bare model split work that should have been one pass 52
times out of 72. toli did it 3 times. Going the other way the two are close, 4
misses out of 84 against 1. So the expensive habit is reaching for a fan-out
rather than missing one, and it is easy to wave through in review, because forty
agents reporting back looks a lot like diligence.
