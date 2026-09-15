# Node prompt contract

Most failed runs are vague node prompts, not wrong topology. Weight effort here.

Every node prompt contains these five parts, in this order:

1. **Role and input.** What this agent is looking at. Interpolate the actual item, do not describe it.
2. **The one job.** A single verb. Extract, or judge, or refute, or group. Never two.
3. **Output shape.** The schema, restated in one line of prose so the model knows what it is filling.
4. **The bar.** The rule that decides membership, plus one thing it explicitly excludes.
5. **The null case.** State that empty or zero is a valid and common answer.

## The rules that matter

**Separate extraction from judgment.** An agent that extracts and judges in one pass will find what it already decided to find. Stage 1 pulls claims with quotes. Stage 2 rules on them. This alone fixes most false-positive floods.

**Quote the evidence.** Every finding carries the verbatim source text. Findings without quotes cannot be verified in the next stage and cannot be checked by the user.

**Refuters are told to kill.** A verify prompt that says "check whether this is right" gets agreement. It must say: try to refute this. Return `refuted` only with quoted counter-evidence, `confirmed` only if it survived a real attempt to kill it, `unresolved` otherwise. See `dials.md`: defaulting to refuted when uncertain turns missing evidence into a clearance claim.

**Name the null case out loud.** Without it, an agent handed a clean input invents a finding to justify its existence. "An empty array is a valid and common answer" costs six words.

**No meta-instructions about being thorough.** "Be comprehensive" produces length, not coverage. Coverage comes from the shape: more finders, more modalities, until-dry termination.

## Example

Bad:

```
Review this document against our position and flag issues.
```

Good, as two stages:

```js
// stage 1, extraction only
`Read ${ref}. Extract every claim it makes about who this is for and what
job it does. Return {ref, title, date, claims: [{text, quote}]} where quote is
verbatim from the source. A claim is a statement about audience or job. Feature
descriptions, pricing and benchmarks are NOT claims and are excluded. Do not
judge whether claims are right. An empty claims array is a valid and common
answer.`

// stage 2, judgment only
`Position: ${POSITION}
Claims: ${JSON.stringify(claims)}
Which claims contradict the position?
Return {contradictions: [{claim, why, severity}]}.
Contradiction means it states a different primary audience or a different
primary job. Sounding dated, using old names, or weak writing are NOT
contradictions. An empty array is a valid and common answer.`
```

Both stages carry all five parts in order: role and input, one job, output shape,
the bar with its exclusion, then the null case. The difference from the bad
version is the bar sentence and the exclusion after it.

## Schemas

Every fan-out agent gets one. Validation happens at the tool layer and the model retries on mismatch, so a schema is also the cheapest reliability win available.

- closed enums for anything routed on
- a `confidence` number wherever a downstream branch depends on the answer
- arrays default to empty, never null
- keep it flat. Nested objects raise retry rates for no benefit
