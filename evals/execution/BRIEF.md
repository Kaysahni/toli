# Building an execution eval task

Each task is a realistic piece of knowledge work done against a folder of files
from a fictional company. Three setups (plain Claude, Claude told to coordinate,
Claude with toli) each get the task and a copy of `fixture/`, and their answers
are scored against `checklist.json`. The setups never see `checklist.json`,
`build/` or this brief.

## What you produce

    evals/execution/tasks/<id>/
      task.md          the ask, as the employee would type it
      fixture/         the files the agents search. Only this is copied to them
      checklist.json   the answer key
      build/           optional: any generator script you used

Write only inside your own task directory. Do not run `claude`.

## Rules for the fixture

- **Fictional.** Invented company, people, products, places, laws. No real
  companies, products or public figures. Nothing about Flox or Nix.
- **Realistic and varied.** Different authors, dates, lengths, tones, formats
  (markdown, yaml, csv, txt, email exports, meeting notes). Never one template
  filled in N times: a reader who notices a template can skip the reading, which
  breaks the test. Include ordinary irrelevant content, as real folders have.
- **Findings need reading, not one keyword search.** Vary wording ("five seats",
  "up to 5 users", "a team of five"). Some findings should need two files
  together (an alias defined in one file and used in another, an amendment that
  changes a clause, a later note that reverses an earlier one).
- **Plant decoys.** Things a careless reader would wrongly report: historical
  mentions ("before March the limit was 5"), changes later reverted, a violation
  cured by an amendment, commented-out config, a department allowed to be
  stricter. Each goes in `exclusions`.
- **No accidental findings.** After writing, re-read the fixture against the
  checklist and make sure nothing else would legitimately count as a finding.
  If you find one, either remove it or add it to the checklist.
- **No em dashes or en dashes** anywhere, in any file. Use commas, colons,
  parentheses or separate sentences.
- **Size** is given per task. Hit it roughly. Longer documents are fine where a
  real one would be long.

## Rules for task.md

2 to 6 sentences, written the way a busy employee asks a colleague. Say what
they need and why. Do not reveal how many findings exist, do not hint at the
decoys, do not say how to split the work or whether to use agents.

## checklist.json

```json
{
  "id": "<id>",
  "company": "<fictional company>",
  "category": "sweep | staged | single",
  "held_out": false,
  "summary": "one plain sentence: what the task is and what a good answer contains",
  "findings": [
    {
      "id": "F1",
      "what": "plain description of the thing that must be found",
      "evidence": [{"file": "fixture-relative path", "quote": "verbatim text from that file"}],
      "counts_if": "what an answer must say for this to count as recovered"
    }
  ],
  "exclusions": [
    {
      "id": "X1",
      "what": "the decoy",
      "evidence": [{"file": "...", "quote": "verbatim"}],
      "why_not": "why reporting it is wrong"
    }
  ],
  "answer": null,
  "mistakes_that_matter": ["errors that would cause real harm if the answer were acted on"]
}
```

- Every `quote` must appear **verbatim** in the named file (it will be checked
  by script). Keep quotes short, one sentence or line.
- `answer` is for tasks with one correct result (a number, a date, a root
  cause, a recommendation). Otherwise null. When set, it is an object:
  `{"value": "...", "derivation": "how it follows from the files", "counts_if": "..."}`.
- For `single` tasks `findings` can hold the required parts of the answer
  (e.g. each link of a causal chain, each error fixed).

## When done

Reply with: file count, rough total words in fixture, number of findings,
number of exclusions, and anything you were unsure about. Nothing else.

---

# Task specs

## sweep-help-staleness
Company: Halvard Payroll (payroll software for small businesses). Category: sweep.
Size: 60 help center articles (150 to 900 words each, varied structure), plus
`releases/` with January, February and March release notes and a
`deprecations.md` schedule.
Ask: support lead needs every article that went stale after the Q1 releases
before a help center review meeting, with the stale text and what replaced it.
Plant ~11 stale articles. Staleness spread across at least 6 different changes
(renamed menus, changed limits, removed integration referred to by an old name,
new approval step, changed filing deadline behavior, etc). Some stale text sits
deep in long articles or in screenshots captions / tables. At least one change
announced in January and reverted in March (articles matching the reverted
state are NOT stale). Decoys: historical mentions, articles about a different
plan tier the change did not touch, a deprecation scheduled for later in the year.

## sweep-vendor-dpa
Company: Orrinfield Health (clinic network). Category: sweep. held_out: true.
Size: `policy/vendor-data-policy-2026.md` (the new standard, 4 hard
requirements: breach notification within 72 hours, published subprocessor list
with 30 days notice of changes, patient data stored only in the US, deletion
certified within 30 days of termination) plus `contracts/` with 22 vendor
agreements (1,000 to 3,000 words each, different drafting styles, some with
exhibits/schedules as separate files) and `amendments/` with 6 amendments.
Ask: compliance lead needs every vendor agreement that does not meet the new
policy, with the clause, before renewals start.
Plant ~8 non-compliant agreements, covering all 4 requirements, some violating in
an exhibit or schedule rather than the main body. Decoys: 2 agreements whose
violation is cured by an amendment, one with a longer deadline that only applies
to non-patient data, one terminated vendor (listed as terminated in an index file).

## sweep-retire-dependency
Company: Tesselwick Logistics (freight routing). Category: sweep.
Size: ~70 files: `services/` (30 service config yaml/env files), `runbooks/` (15
markdown), `cron/` (crontab exports), `pipelines/` (data pipeline docs and sql),
`integrations.csv` (partner integrations), `dns/internal-aliases.txt`.
Ask: platform lead is retiring the RouteCalc v1 API next month and needs
everything that still depends on it, so owners can be told.
Plant ~9 real dependents found through different routes: direct URL, an internal
alias hostname defined in the dns file, an env var name, a cron job, a SQL job
reading the v1 results table, a partner integration row, a runbook step that
humans run. Decoys: commented-out config, services already on v2 whose runbook
still mentions v1 historically, a v1 of a different API (RouteCache v1), a
service that is itself being decommissioned (marked so in a file).

## sweep-policy-drift
Company: Calloway Ridge Credit Union. Category: sweep.
Size: `hr/canonical/` with the 2026 travel & expense policy and remote work
policy (the source of truth, stated as such), plus ~35 other documents: employee
handbook sections, 8 department wiki pages, HR FAQ, manager guide, onboarding
slide notes, old announcement emails.
Ask: HR director needs every place where another document tells employees
something different from the canonical policies, so they can be corrected before
open enrollment.
Plant ~10 inconsistencies (per diem amounts, approval thresholds, receipt
deadlines, remote stipend, home office equipment rules, notice periods).
Decoys: the canonical policy explicitly lets departments set stricter limits, so
a stricter department rule is not drift; old announcement emails clearly dated
and superseded; a document for contractors, whom the policy does not cover.

## stage-market-entry
Company: Varnholt (a note-taking app). Category: staged.
Size: ~30 files: `brief.md` (leadership's decision criteria: payback under 18
months, no in-country data storage requirement, at least 2 of 3 target segments
reachable), and per country (Germany, Brazil, Japan): market research report,
competitor landscape pages, localization cost estimate, legal memo, plus
`support-tickets-by-region.csv` and `survey-results.csv`.
Ask: head of growth wants a recommendation on which country to launch next with
the evidence for each criterion.
The correct recommendation must follow strictly from the criteria and files.
Plant traps a skim would miss: one country's legal memo has a later addendum
adding a data storage requirement; one localization estimate double counts a
line item (the corrected payback flips a verdict); one competitor page is older
than a competitor blog post announcing a free tier; survey segments need the csv
to check reachability. `findings` = each fact that decides a criterion per
country; `answer` = the recommended country with derivation.

## stage-pricing-scan
Company: Ferrowind Analytics (B2B analytics tool). Category: staged.
Size: ~35 files: 6 competitors each with a pricing page snapshot (md, dated),
changelog excerpts and blog posts; `winloss/` with 18 deal notes; `internal/`
current Ferrowind pricing.
Ask: CEO wants a competitor pricing comparison (price model, entry price, seat
vs usage, free tier, annual discount) and a recommendation on whether Ferrowind
should drop per-seat pricing, backed by the deal notes.
Plant: one competitor moved to usage pricing in a blog post newer than its
pricing snapshot; one competitor's free tier was removed in its changelog; entry
prices in two snapshots are monthly vs annual billed and must be normalized;
deal notes where losses cite seat price (count them) vs losses citing missing
features (decoy for the recommendation). `findings` = the correct per-competitor
facts and the loss-reason counts; `answer` = recommendation that follows from
the evidence, with what it must cite.

## stage-feedback-synthesis
Company: Pinmoor (HR software for mid-size companies). Category: staged. held_out: true.
Size: `tickets.csv` (~300 support tickets), `nps-verbatims.csv` (~150),
`sales-calls/` (20 call notes), `forum/` (25 community threads),
`churn-survey.csv` (~60).
Ask: product lead needs the top customer problems this quarter across all
sources, with how many distinct customers raised each and real quotes.
Plant 5 true themes with known distinct-customer counts across sources (put the
counts and how to derive them in checklist). Decoys: one theme that looks big in
tickets but is one customer filing 30 tickets (distinct count is 1); a theme
only raised by internal staff accounts (email domain pinmoor.example); duplicated
forum cross-posts. `mistakes_that_matter` must include invented quotes: every
quote in the answer must exist in the files.

## stage-regulation-impact
Company: Marlowe Crest Insurance (home insurance), in the fictional State of Norvale. Category: staged.
Size: `regulation/norvale-hb-2231.md` (new consumer notice rule with 6
numbered requirements, effective date), plus ~40 company documents: policy
wordings, claims procedures, customer letter templates, call center scripts,
agent training modules, website FAQ export.
Ask: compliance manager needs to know what the new rule requires, which
documents must change for each requirement, and what is missing entirely.
Plant ~10 gaps mapped to requirements, including 1 requirement with no document
covering it at all (a missing process, not an edit). Decoys: documents for a
different state (Kessington) that the rule does not cover; a template already
updated (with a revision date after the rule); a requirement that only applies
to policies over a threshold, which one product line does not reach.

## single-contract-lookup
Company: Brackenford Holdings. Category: single (orchestration probably wasteful).
Size: `contracts/` with 30 agreements (1,000 to 3,000 words) and an index csv.
Ask: "What notice do we have to give to terminate the Kestrel Freight master
services agreement without cause, and by when for a year-end exit?"
One answer: notice period from the MSA as modified by a later amendment in the
same folder, and the resulting deadline date. Decoys: a different Kestrel
contract (a warehouse lease) with a different notice period; the for-cause
termination clause.

## single-incident-chain
Company: Juniper Vale Bank. Category: single (one causal chain, should not split).
Size: `logs/` from 4 systems (mail relay, message queue, batch scheduler,
statement renderer; a few hundred lines each, realistic formats), `changes.md`
(change calendar), `alerts.csv`.
Ask: "Nightly statement emails did not go out on September 3. What happened,
start to finish, and what was the root cause?"
One causal chain across all 4 systems (e.g. certificate rotation on the relay
at 01:10 causes TLS failures, retries back up the queue, the scheduler job times
out, renderer marks the batch failed). Each link only makes sense next to the
previous one. Decoys: noisy unrelated warnings in each log, an alert that fired
and auto-resolved for another reason, a change calendar item on a different
system. `findings` = each link with its log evidence; `answer` = root cause.

## single-email-fix
Company: Lumen Harrow (a coworking operator). Category: single (small rewrite).
Size: `draft-email.md` (a ~400 word customer email about a membership price
change) and `fact-sheet.md` (one page of the true facts), plus 2 unrelated files.
Ask: "Can you fix anything wrong in this email against the fact sheet and make it
plainer before I send it to members this afternoon?"
Plant 3 factual errors (a date, a price, a condition). Decoy: one sentence that
looks wrong but matches the fact sheet. `findings` = each error fixed;
`mistakes_that_matter` includes introducing any claim not in the fact sheet.

## single-revenue-calc
Company: Oxtail Supply (wholesale kitchen supplies). Category: single (direct calculation). held_out: true.
Size: `invoices.csv` (~250 rows: date, customer, region, currency, amount,
type invoice/credit_note), `customers.csv`, `pricing-notes.md` (discount rules and
the fixed quarter exchange rates to use).
Ask: "What was our Q2 net revenue from EU customers, in USD, after credit notes?"
Generate the data with a script in `build/` and compute the true answer with the
same script. Traps: credit notes, one customer whose region changed (use the
region in customers.csv), rows dated just outside Q2, non-USD currencies.
`answer` = the number to the cent with derivation.
