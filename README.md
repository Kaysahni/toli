# toli

**One screen you approve before any agent runs.**

Find everywhere we promise 24 hour support. Work out which of the 40 help center
articles went stale after the March release. Tell me what our eight competitors
changed this quarter. Check whether the four claims in this launch email are
actually true. Those asks are either one careful pass or twenty agents running at
once, and the wrong choice costs you either way: money and a muddled answer on
one side, a thin answer on the other.

Ask an agent to fan out and it will. It will also write you a confident plan for
why that was the right call. Even unasked it leans the same way, because more
agents looks like more diligence, and the machinery is ready: spawning is one
call, and nothing sits between the ask and the spend.

What comes back looks finished either way. A report built from half the sources
reads exactly like one that covered them all, so reviewing the output afterwards
does not save you. The judgment has to happen before anything spawns.

That is what toli does. It reads the ask, decides whether the work genuinely
splits, and if it does you get one card: what counts, what shape, how many
agents, and the stage most likely to be wrong. You say `go`. If it does not
split, toli says so and does the work in the same reply.

## How it works

Gate the ask, pick a shape from the eight, then set the five dials that decide
where work waits, how hard findings get attacked, when to stop, who runs each
node and what each one can see. Rewrite the ask into the prompt every agent
gets. Print the card. Wait. On `go` it writes the workflow script with the
approved card embedded as a comment, so the plan outlives the session, and the
caps on the card become limits enforced in code rather than hopes.

It covers the work most jobs actually repeat: renewals and contract terms in
legal, account digs before a QBR in sales, stale articles in support, month end
in finance, competitor moves in marketing, dashboards that disagree in data.
`references/by-function.md` lists the recurring asks for thirteen jobs and the
call toli makes on each.

## The gate

Fan out when **two or more** hold:

- more than 5 independent items to process, counted as the ask names them and not
  as you choose to slice them. Not when the result is one thing whose parts must
  agree, like a ranking or a questionnaire
- each item needs its own multi-step exploration rather than a lookup, even if
  there are only three or four
- nobody has a list of the input set, and building one means searching more than
  one place
- the output feeds a decision someone makes on the coverage claim itself, a
  retirement or a sign-off, not merely an artifact that has readers
- the verdict is a judgment call a single agent would be too agreeable about
- more than one separate source has to be searched, counting places rather than
  kinds of place

Otherwise inline. One source, one known change, one lookup, or one rewrite never
splits. Two more things look like fan-outs and are not: one causal chain
is one item, because an incident traced through four systems has four sources but
each log only means something next to the others; and items bound by one shared
constraint, like a budget cap or one allocation, are one deliverable.

The "one thing whose parts must agree" exception covers the deciding, not the
evidence. When each part is held by a different team, system or authority, the
items still count, and the reading fans out before one pass writes the artifact.

When the gate fails, toli names the check that failed and the agents it did not
spend, then does the work in one pass. When it does get a call wrong it is
three times more likely to be on a card than on a refusal, so the card is the
thing worth pushing back on.

## What a card looks like

Ask: *"the refund policy changes next month, find everywhere the old one is stated"*

```
INTENT   Find every place that states the current refund terms
         -> a list of locations with the exact wording quoted, each confirmed live

BAR      "States the refund terms" = text a customer could act on today.
         NOT: internal drafts, archived versions, changelog entries,
         or templates that are not in use anywhere.

SHAPE    diamond · until-dry termination · 3 refuters per candidate
         (not pipeline: pipeline needs the location list up front and you do
          not have one. Flip if someone hands you the list.)

         round N ─┬─▶ finder: published docs ─┐
                  ├─▶ finder: support macros ─┼─▶ refute each ─▶ synthesize
                  ├─▶ finder: contracts ──────┤   (barrier)
                  └─▶ finder: in-product ─────┘   stop after 2 dry rounds

COST     up to 41 agents (4 finders/round, cap 4 rounds, + 3 refuters per
         candidate, candidates capped at 8, + 1 synthesis) · depth 3 ·
         max 8 concurrent · finders read-only, effort low

WATCH    The finder rounds. Until-dry converges on what the finders can see.
         If all four search the same way, the rounds go dry while a whole
         channel is still unlooked-at.
```

41 agents, over the 15 ceiling. "cheaper" for 3 trims, "go" to run as-is.

Then: `go` · `go but <change>` · `why` · `who` · `scope` · `prompts` · `cheaper`

## Reading a card

| field | what it is |
|---|---|
| INTENT | your ask restated as a deliverable. What you want on the left of the arrow, what lands in your hands on the right |
| BAR | the rule that decides what counts, always naming something it excludes |
| SHAPE | the topology and its settings, plus a parenthetical naming the runner-up and the one condition that would flip the choice |
| the diagram | where work waits for other work |
| COST | agent count, either derived arithmetic you can check or a bound with the variable that moves it named |
| WATCH | the single stage most likely to be wrong, called before the run rather than after |

BAR is the one to read twice. Most bad runs come from a loose definition rather
than a wrong topology, and twenty agents given a vague bar will return twenty
readings of it, which the merge then buries.

COST is never a bare number, so if a run spends 60 when the card said 43 you can
see which part of the formula was wrong. There are no time estimates on it, since
depth and concurrency are the only honest bounds.

Cards use a few words in a particular way. A finder is sent to look, while a
refuter is told to kill a finding rather than check it, because a prompt that
asks for a check gets agreement. A barrier is where work waits, so nothing gets
written up on half-checked findings. Until-dry means stop after N rounds that
surface nothing new, which is what you use when nobody knows how big the set is.
The ceiling is 15 agents. Above it toli offers to trim, and above 50 it prints
the full breakdown before it will take `go` at all.

What you can say back:

| | |
|---|---|
| `go` | run it as shown |
| `go but <change>` | override anything on the card |
| `why` | shape reasoning, the runner-up, what breaks if the pick is wrong |
| `who` | per stage: agent type, effort, model, tools, what runs as plain code |
| `scope` | the input set, what got cut, and the rule that cut it |
| `prompts` | every node prompt, its schema and done condition |
| `cheaper` | 3 cost-cut variants with the tradeoff named. One is always "do it in one pass", and what that loses |
| `full` | all of the above |

## What a refusal looks like

Ask: *"fan out some agents and review our onboarding emails"*

> Not a fan-out. One sequence, one concern, and the set is six emails you can
> hand me. Reading them in one pass costs less and reads better than twelve
> agents reporting fragments. Doing that now.

No card, and nothing spent.

## Measured

On 156 adversarial cases, toli made the right call 152 times. The same model
without it managed 100.

|  | bare model | toli |
|---|---|---|
| split work that should have been one pass | 52 of 72 | 3 of 72 |
| did in one pass what should have been split | 4 of 84 | 1 of 84 |
| **correct** | **100 of 156 (64%)** | **152 of 156 (97%)** |

Agents that had never read the skill wrote the cases, under instructions to make
the surface cues point the wrong way. Three more raters then labelled every case
blind, and cases that fewer than two of them backed were dropped. Every run
happens in an empty directory with no plugins, hooks or connectors reachable, and
the whole suite is in `evals/`, so you can re-run it yourself with `python3
evals/run.py` and read the method and the limits in `evals/README.md`.

## Install

As a Claude Code plugin, which is two steps, the first only registers the source:

```bash
claude plugin marketplace add Kaysahni/toli
claude plugin install toli@toli
```

Or as a plain skill, for any agent that reads `SKILL.md`:

```bash
npx skills add Kaysahni/toli
```

Or clone `skills/toli/` into `~/.claude/skills/toli/`.

Then just ask for the work: "find every place we...", "check each of these...",
"what changed across...". Saying "fan out" or "parallelize" calls it explicitly.
Installed as a plugin the explicit form is `/toli:toli`; installed
standalone it is `/toli`.

## The eight shapes

| shape | when |
|---|---|
| sequential | genuinely dependent steps, one artifact moving forward |
| router | one input, mutually exclusive handling paths |
| parallel | one question, several angles, merged answer |
| pipeline | many independent items, same multi-stage treatment. The workhorse |
| orchestrator | task list unknown until an agent looks |
| review loop | one artifact, iterated to a standard |
| diamond | diverge to cover ground, then attack findings before synthesis |
| debate | workers must argue with each other. Runs as an agent team, not a workflow |

Sequential is the shape people reach for and it is usually wrong. toli checks
pipeline first, and always names the runner-up so you can overturn it.

## What the skill actually enforces

Four habits do most of the work, and none of them is about topology.

The definition matters more than the shape, so every card states the membership
rule and one thing it excludes. Extraction is kept apart from judgment, because
an agent doing both at once finds what it had already decided to find: stage one
pulls claims with verbatim quotes, stage two rules on them.

Refuters are told to kill a finding rather than check it, since a prompt asking
whether something is right tends to get agreement. They return `confirmed`,
`refuted` or `unresolved`, one verdict only.

Anything that can be code is code. Filtering, deduping and grouping belong in the
script, because an agent that dedupes a list costs tokens and sometimes gets it
wrong, while `new Set()` costs nothing and never does.

## Going deeper

| | |
|---|---|
| [`examples/`](examples/) | five worked cards across disciplines, plus four asks run with and without toli, taken from the eval snapshot |
| [`evals/`](evals/) | the suite, the 220 labelled cases and how to re-run it |
| [`references/patterns.md`](skills/toli/references/patterns.md) | the eight shapes, each with a diagram and when it is wrong |
| [`references/dials.md`](skills/toli/references/dials.md) | the five settings on a shape: barrier, verify depth, termination, casting, isolation |
| [`references/casting.md`](skills/toli/references/casting.md) | who runs each node, and what should be plain code instead of an agent |
| [`references/prompt-rubric.md`](skills/toli/references/prompt-rubric.md) | what a node prompt has to carry to be checkable |
| [`references/by-function.md`](skills/toli/references/by-function.md) | recurring asks by job, with the call toli should make on each |

## Requirements

Claude Code with the Workflow tool available. If it is not, toli prints the
node prompts as a numbered pack instead of a card so the shaping work is still
usable. Shape 8 (debate) additionally needs `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

toli appends one line per invocation to `~/.toli/log.jsonl`: your ask, the gate
verdict, the shape, and the predicted against the actual agent count. It stays on
your machine, nothing reads it but you, and deleting the file or the directory is
safe. It is there so predicted spend can be checked against real spend over
time.

## Prior art

Five of the eight shapes come from Anthropic's
[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
(prompt chaining, routing, parallelization, orchestrator-workers,
evaluator-optimizer). Pipeline, diamond and debate are additions.

Aakash Gupta's [Graphs](https://www.news.aakashg.com/p/graphs) tested graphs
against optimized single prompts across 40 tasks: graphs won 25, single prompts
won 15. That 15 is the case toli exists for. It is the only external evidence
either way that the gate is the question worth asking, and it was not collected
by anyone with a stake in toli.

For writing the workflow scripts themselves, Claude Code's built-in
`workflow-authoring` skill is the reference and toli defers to it. toli sits
above that: it decides whether there should be a workflow at all, and what shape
it is.

## License

MIT
