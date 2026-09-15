# Evals

One question: does toli decide correctly whether work should be split across
parallel agents?

That is the claim the gate makes, and the only one here that is cheap to
falsify. Nothing in this directory measures the quality of a run toli shapes,
only the decision to shape one at all.

## Running it

```bash
python3 evals/run.py                  # spends tokens. Re-run when SKILL.md or cases change
python3 evals/measure.py              # free, no API key, reads the committed snapshot
```

`run.py` needs the `claude` CLI on PATH and an account that can reach
`claude-opus-5` and `claude-haiku-4-5-20251001`. The default suite is 156 scored
cases against 2 arms, six at a time, and it spends real tokens. Python 3.8 or
newer.

Its flags are `--prompts <files...>`, `--only <ids>`, `--skill-dir`, `--control`,
`--min-raters`, `--workers`, `--skip-preflight` and `--out`. The first three and
`--skill-dir` all require `--out`, so nothing but a full default run can
overwrite the committed snapshot.

## Design

There are two arms, given the identical prompt and graded by the identical
judge. `baseline` is the bare model. `toli` is the same model with the full skill
bundle, SKILL.md plus every reference, in the system prompt. Injecting SKILL.md
on its own would measure a crippled skill, since its protocol routes to those
references at the steps that need them.

The judge assigns a category rather than a yes or no: `COMMITTED_PARALLEL`,
`CONDITIONAL_PARALLEL`, `SEQUENTIAL_WORKFLOW` or `INLINE`. Asking "did it fan
out" would hide the distinctions that matter. Which categories count as fanning
out is declared in `FANOUT_CATEGORIES` in `run.py` before the run rather than
after it. A plan that sends agents to gather evidence and then decides in one
pass counts as fanning out, because the agents were spent either way.

Every case in `cases/` was written by an agent that had never read the skill. The
writers were told what the decision is and asked to make the surface cues point
the wrong way, so the deciding fact usually sits mid-prompt: the four dashboards
that all read one dbt model, the 22 services behind one proxy, the audit log that
already covers the whole set.

Three more raters then labelled every case with no access to the skill or to the
writer's label, and `raters_agree` records how many of them backed it. Scoring
keeps the cases at 2 or more, which is what `--min-raters` controls. One case in
`round1` and three in `round2` were dropped that way. They stay in the fixtures,
so what was excluded is visible rather than quietly gone.

Isolation takes some work. A bare `claude -p` inherits the operator's working
directory, CLAUDE.md, plugins, hooks, skills and MCP connectors, so runs use
`--restricted --disable-slash-commands --strict-mcp-config` from an empty scratch
directory, and `preflight()` aborts if any MCP connector answers a probe. Account
identity survives every flag available, which is why each case names a fictional
company and carries its own facts. `preflight` records whatever identity still
leaked instead of pretending it is gone.

## Cases

| file | n | what it is |
|---|---|---|
| `cases/round1.jsonl` | 80 | first adversarial set, four job areas |
| `cases/round2.jsonl` | 80 | harder set, no trap type used twice |
| `cases/tricky.jsonl` | 60 | earlier matched pairs, kept for regression |

`round1` and `round2` are the default suite. Each case carries `should_graph`
(the label), `why` (one line for why), `category` (the trick) and
`raters_agree`.

## What this does not measure

Each of these limits how far the number travels.

- **Stated approach, not behavior.** Arms answer a planning question with no
  repository. A model describing a plan may reach for agents more readily than
  one actually doing the work.
- **Skill text, not triggering.** The bundle is injected into the system prompt.
  That is not the same as Claude Code loading the skill from a user's phrasing.
- **Nothing after the gate.** Shape choice, node prompts, caps and coverage
  claims are all unmeasured.
- **One model.** Everything here ran on Opus. The gate on a smaller model is
  unknown, which matters if cheaper node models become the default.
- **The judge is unvalidated.** One Haiku call, no hand-labelled agreement check.
  Spot checks found roughly one grading error per 80 cases, all of them scoring a
  correct refusal as a fan-out, so the real skill number is a point or two above
  the reported one.
- **Single sample per cell.** No median over N. Treat a few points as noise.
- **Card field presence is not card validation.** It checks that five labels
  appear on their own lines, not their order, content, diagram or arithmetic.
