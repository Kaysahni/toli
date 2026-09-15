# Casting: who runs each node

Cast per stage, never per run. A run where every node is the same generic agent is leaving both money and accuracy on the table.

First question is not which agent. It is **whether a node needs an agent at all.**

## Cast nobody

Do these in plain script code, not an agent:

- fetching a list, index, or item set
- filtering, sorting, deduping, flattening
- grouping results by a key
- counting, thresholding, early-exit checks

An agent that dedupes a list costs tokens and gets it wrong sometimes. Code
costs nothing and never does. Dedupe against everything seen, in code, between
rounds.

`new Set()` only works on primitives. Two findings with identical contents are
distinct objects and both survive, so until-dry never goes dry. Define a stable
identity first, then key a `Map` on it:

```js
const key = f => `${f.source}:${f.locator}:${f.claim.trim().toLowerCase()}`
for (const f of found) if (!seen.has(key(f))) seen.set(key(f), f)
```

## Roster

| agentType | what it is | cast it for |
|---|---|---|
| *(omit)* | default workflow subagent, full tools | judgment, synthesis, anything unclassified |
| `Explore` | read-only, reads excerpts not whole sources | locate stages, broad sweeps, "where does X appear" |
| `general-purpose` | full tools, multi-step | nodes that must act, not just read |
| `Plan` | read-only, designs an approach | work out what a change would involve without making it |

Those four ship with Claude Code. If your setup adds specialist agent types,
extend the table. Confirm a type exists before casting it: a node cast to a
missing agent type fails at spawn, not at review.

`agentType` composes with `schema`. The custom agent's system prompt stays and the structured-output instruction is appended.

Read-only stages should be cast to a read-only type. Not for cost. So a stage that was only supposed to look cannot write.

## Model and effort

Omit `model` on any stage that produces evidence. Extraction, judgment, refutation
and synthesis inherit the session model. A cheap model that misses a claim during
extraction poisons every stage downstream, and it fails silently: the output looks
the same either way.

Tier down freely on stages that only move evidence someone else already produced.
Reformatting, grouping, labelling, deduping a set that is already quoted. Most of
those should not be agents at all, see above.

`effort` is the second lever, and it moves reasoning tokens, not input tokens. A
high-fan-out extract stage still reads every input in full, so effort buys little
there. It pays on stages that think hard about small inputs:

| stage kind | effort |
|---|---|
| extract, read, reformat, locate | `low` |
| classify, route | `low` unless the taxonomy is subtle |
| judge, refute, verify | default |
| synthesize, final critic | default or raise |

Raising effort on a 40-agent fan-out to buy accuracy on a 3-agent verify stage is backwards. Raise it on the verify stage.

## Tool reach

Workflow agents reach every session-connected MCP server through `ToolSearch`, loading schemas on demand.

Three rules:

**Think in categories, resolve to tools.** Examples and plans in this skill name
tools by category with a `~~` prefix: `~~crm`, `~~help desk`, `~~knowledge base`,
`~~chat`, `~~docs`, `~~code host`, `~~data warehouse`, `~~contract repository`.
Before writing node prompts, resolve each category to a tool that is actually
connected in this session. If a category the plan needs has no connected tool,
say so on the card in WATCH: that source will not be searched, and a coverage
claim that silently skips it is the truncation-reads-as-coverage failure. Never
leave a `~~` placeholder in a node prompt.

**Name the tool in the prompt.** Do not hope the agent finds it. Write `Load the tool with ToolSearch("select:<exact_tool_name>") then use it.` A node that has to guess which of hundreds of deferred tools it needs wastes a turn and sometimes picks wrong.

**Interactively-authenticated MCP servers may be absent in headless or cron runs.** That covers most connector-style servers. A run whose nodes depend on those must run interactively. Do not put it behind a scheduled routine and assume it works. If a scheduled version is wanted, fetch the data inline in the parent session and pass it into the run as text.

## Casting a debate team

Agent teams cast differently. A teammate can be spawned from a subagent definition by name:

```
Spawn a teammate using the Explore agent type to ...
```

The teammate honors that definition's `tools` allowlist and `model`, and the definition's body is appended to its system prompt rather than replacing it.

But: the `skills` and `mcpServers` frontmatter fields in a subagent definition are **not** applied to teammates. Teammates load skills and MCP from project and user settings like a normal session. Do not cast a teammate expecting a definition-scoped MCP server to come with it.

Teammates also inherit the lead's permission mode at spawn and cannot be given per-teammate modes at spawn time.

## One node, one type

If a node seems to need two agent types, it is two nodes. Splitting is nearly free in a pipeline and makes both halves cheaper to cast.
