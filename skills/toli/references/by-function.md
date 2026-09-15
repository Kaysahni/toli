# By function

Common recurring asks by job, with the call toli should make on each. Read only
the section that matches the ask. Use it to calibrate, not as a lookup table: the
same ask can flip with scale.

Gate names used below: **items** (more than 5), **depth** (each item is real
work), **no list** (the set has to be found), **coverage** (someone signs off on
it being complete), **judgment** (one agent would go easy), **sources** (more
than one place to search).

Two patterns show up in almost every job:

- **Scale flips it.** Three posts a week is one pass. The whole back catalog is a
  fan-out. Same work, different answer.
- **Fan out the reading, not the deciding.** Pull evidence per item or per
  source in parallel, then do one pass for anything whose parts must agree: the
  digest, the ranking, the final call. Only when each read stands on its own. If
  the reads explain each other (one incident's logs, one budget's line items),
  keep the reading in one pass too.

## Sales

**"prep me for every external call i have this week"**: fan out
- 8 to 15 meetings, each its own account in ~~crm, email, ~~call recordings and ~~web
- Fires: items, depth, sources
- Shape: one worker per account, not per meeting (two meetings with one company are one dig). One pass for the week overview on top.

**"write account plans for my top 20 accounts before QBRs"**: fan out
- Each plan is its own dig: stakeholders, 90 days of activity, news, expansion room
- Fires: items, depth, sources

**"clean up the pipeline before tomorrow's forecast call"**: one pass
- One ~~crm export. Stale deals, past close dates and single-threaded deals are rules on fields, and the forecast has to add up to one number.
- Flips to fan out if every "is this deal dead" call needs that deal's emails and calls read.

## Customer support

**"go through all our known-issue articles and update what's fixed"**: fan out
- 10 to 25 articles, each checked against ~~project tracker, ~~help desk, ~~chat and release notes
- Fires: items, depth, sources

**"which help articles are wrong, and what are people asking about that we have no article for"**: fan out
- Top 50 to 100 articles, each verified against the current product. The gap list does not exist until you build it from tickets.
- Fires: items, depth, no list, sources

**"find me the answer to this customer's question, check everywhere"**: one pass
- Many places to look, one answer. Conflicting sources need one reasoner, not a merge.

## Product

**"why did we win and lose deals last quarter"**: fan out
- 30 to 60 closed deals, each rebuilt from ~~crm, ~~call recordings and ~~chat. CRM notes are the rep's version.
- Fires: items, depth, judgment, sources
- Shape: one worker per deal pulls the real reasons, one pass clusters them into themes.

**"is anything on the roadmap actually off track? the tracker says it's all green"**: fan out
- 15 to 30 initiatives. The tracker says in progress, the Slack thread says it slipped two weeks ago.
- Fires: items, depth, judgment, sources

**"plan next sprint from the backlog"**: one pass
- One plan against one capacity. Every item trades off against every other, so splitting it breaks it.

## Marketing

**"weekly competitor watch: what did our 8 competitors ship, change or say"**: fan out
- Each competitor across blog, changelog, pricing page, social and reviews on ~~web
- Fires: items, depth, sources, judgment ("does this actually matter to us")
- Shape: one worker per competitor, one pass for the digest and 2 to 5 actions.
- Flips to one pass for a single competitor's changelog: one known page, check for new entries.

**"check everything we published this month for off-brand stuff or claims legal would hate"**: fan out
- 30 to 80 pieces across ~~cms, email, social and ads. Nobody has one list of what shipped.
- Fires: items, no list, judgment, sources

**"write the monthly marketing report"**: one pass
- Each channel is one export. Totals and attribution have to agree across the whole report.

## Legal

**"triage this week's NDAs against our playbook"**: fan out
- 15 to 30 NDAs. Green means it gets signed with no lawyer looking, so a lenient pass is expensive.
- Fires: items, judgment, coverage

**"anything new in privacy law this month we need to care about"**: fan out
- Nine or more jurisdictions, each with its own regulator and feeds, each checked against what we actually do with data
- Fires: items, depth, sources, judgment

**"review this MSA"**: one pass
- One contract. The liability cap and the indemnity read together, so splitting by clause loses the point.
- Flips to fan out when the redlines each change a promise a different team has to keep (data region, support response times, insurance limits, breach notice). Each one gets checked against what that team actually does, then one pass reads the contract as a whole.

## Finance

**"run month-end recs"**: fan out
- 50 to 150 balance sheet accounts, each against its own source (bank, subledger, schedule) in ~~erp. Close sign-off rests on every one reconciling.
- Fires: items, depth, coverage, sources
- Shape: one worker per account, one pass for the aging rollup.

**"what did we get this month that nobody has invoiced us for yet"**: fan out
- There is no list. It gets built from open POs, contracts and department owners.
- Fires: no list, items, sources

**"put together the financial statements"**: one pass
- One trial balance. Net income flows into cash flow and the balance sheet has to balance.

## Data

**"before the business review, make sure every number on the exec dashboard is actually right"**: fan out
- 20 to 40 tiles, each recomputed in ~~data warehouse and checked against its definition and last week's number
- Fires: items, depth, coverage, sources

**"build me a dashboard for activation"**: one pass
- Shared filters, one data payload, one period definition. It is one artifact.

## Engineering

**"are we good to ship this release?"**: depends on size
- Release train with 25 to 60 PRs, each checked for approval, green CI, migrations and open bugs across ~~code host, CI and ~~project tracker: fan out (items, coverage, sources)
- Single service, 3 PRs: one pass

**"did we actually finish the postmortem action items from last quarter"**: fan out
- 40 to 100 items across a quarter of postmortems. A closed ticket is not a fix, so each one gets checked against the PR, the deploy and the alert.
- Fires: items, depth, no list, coverage, sources

**"write the postmortem for yesterday's outage"**: one pass
- One timeline and one causal chain. Fifteen services touched does not make fifteen items.

## Design and research

**"what are customers complaining about this month? tickets, NPS, app reviews, the feature board"**: fan out
- Four or five separate places, each needing its own pull and tagging
- Fires: sources, no list, depth
- Shape: one worker per source, one pass to merge themes and count them.

**"accessibility audit of the main flows before the enterprise deal"**: fan out
- 15 to 40 screens, each through keyboard, screen reader, contrast and zoom. It backs a compliance claim.
- Fires: items, depth, coverage, judgment

**"synthesize these 8 interviews"**: one pass
- The patterns across participants are the whole point. Splitting by interview hides them.

## HR

**"screen this week's applicants for the backend role against the scorecard"**: fan out
- 40 to 80 applicants, one fixed rubric, each with a resume and public work to read
- Fires: items, depth, judgment

**"pull together evidence for everyone's reviews"**: fan out
- Each person's year of tickets, projects and goals is its own dig across ~~project tracker and ~~hris
- Fires: items, depth, sources

**"prep calibration"**: one pass
- Ratings only mean something relative to each other. Fan out the evidence first, calibrate once.

## Ops and IT

**"get the SOC 2 evidence together and tell me what's missing"**: fan out
- 80 to 120 controls. Nobody knows where half the evidence lives: ~~docs, tickets, ~~chat approvals, email.
- Fires: items, depth, no list, coverage, judgment, sources

**"which runbooks are out of date"**: fan out
- 30 to 60 docs, each checked against recent incidents, the on-call roster and whether the systems it names still exist
- Fires: items, depth, no list, sources

**"capacity plan for next quarter"**: one pass
- One export from ~~project tracker or ~~hris. The totals have to reconcile.

## Bio-research

**"anything new on our 8 targets this month? papers, preprints, trials"**: fan out
- Each target across ~~literature databases, preprint servers and trial registries, each hit judged for "did someone get there first"
- Fires: items, depth, sources, judgment

**"rescore the risk matrix for every project in the lab"**: fan out
- Each project re-scores 10 to 20 assumptions against new results. One pass tends to keep last quarter's scores.
- Fires: items, depth, judgment

**"integrate these 12 single-cell datasets"**: one pass
- One joint model. Batch correction only works on all of it together.

## Anyone

**"i'm back from two weeks off, what did i miss"**: fan out
- Two weeks across ~~chat, email, ~~docs, ~~project tracker, ~~crm and calendar, each with real volume
- Fires: sources, no list, depth
- Flips to one pass for "what happened yesterday": same places, small enough for one agent.

**"what did i tell people i'd do this week and haven't"**: fan out
- There is no list of promises. Find them across ~~chat, email and meeting notes, then check each one got done.
- Fires: no list, sources, depth

**"what did i get done this week"**: one pass
- Same places as above, but one summary with nothing to check per item.
