# Answer keys for review

12 test tasks, each a folder of files from a made-up company. Every task has answers hidden on purpose ("must find") and traps that look like answers but are not ("must not report"). Plain Claude, Claude told to coordinate, and Claude with toli each get the same task and files, and their answers get scored against these lists.

Tasks marked **held back** are never used while tuning toli, so they stay a fair test.

## 1. Halvard Payroll

**Type:** Sweep: find every instance across many files. **Files:** 64.

**The ask:** We shipped a lot in the January, February and March releases and I'm pretty sure the help center hasn't kept up. Before Thursday's help center review, can you go through the articles in articles/ against the release notes and deprecation schedule in releases/ and find every article that's now out of date? For each one I need the article, the exact text that's stale, and what it should say now based on the release that changed it. The meeting is short, so I need a list we can act on.

**Must find (11):**

1. add-a-new-employee.md tells admins to go to People > Add person; the January release renamed People to Team and Add person to Add team member.
2. rehiring-a-former-employee.md has a screenshot caption (deep in the article) showing the People menu with Former employees selected; now Team > Past members.
3. compare-plans.md plan table lists 25 custom earning types for Core; February raised Core to 40.
4. connect-tallyworks.md is a setup guide for Tallyworks Connect, which is the old name of the BrightBooks sync removed in February (alias only in deprecations.md).
5. month-end-close-checklist.md step 9 (deep in a long article) tells bookkeepers to confirm journal entries synced in Tallyworks; that sync no longer exists.
6. run-an-off-cycle-payroll.md says off-cycle payrolls go straight to processing after Submit; February added a required approval by a Payroll approver (or self-approval by email for single-admin accounts).
7. paying-bonuses.md comparison table says an off-cycle bonus payroll goes straight to processing after Submit; it now needs approval.
8. quarterly-tax-filings.md says quarterly filings wait for admin approval of the filing summary and are submitted on the due date (held if unapproved); March changed this to automatic submission 5 business days before the due date with no approval wait.
9. direct-deposit-timing.txt gives a 5:00 pm PT submission cutoff; February moved it to 3:00 pm PT.
10. 2026-bank-holiday-payroll-calendar.md table header says Submit by (5:00 pm PT); now 3:00 pm PT.
11. set-up-two-step-verification.md (updated January 22, 2026) says SMS codes are no longer supported; March restored SMS as a method.

**Must not report (9):**

- cant-sign-in.md describes text message verification codes as a working method.
- payroll-deadlines-faq.md mentions the old 5:00 pm PT cutoff.
- custom-earning-types.md says Starter allows up to 10 custom earning types.
- upload-timesheets-csv.md documents the classic timesheet CSV import, which is on the deprecation schedule.
- run-a-regular-payroll.md says submitted payrolls go straight to processing.
- annual-tax-filings.md says annual filings wait for approval and are submitted near the due date.
- getting-around-halvard.md mentions the People menu.
- paying-bonuses.md regular payroll column says bonus payrolls go straight to processing.
- cant-sign-in.md mentions a Former employee access link on the sign in page.

## 2. Orrinfield Health (held back)

**Type:** Sweep: find every instance across many files. **Files:** 35.

**The ask:** Renewals start next month and the new vendor data standard (policy/vendor-data-policy-2026.md) is now in effect, so I need to know which of our vendor agreements don't meet it. Please go through the contracts and amendments and give me every agreement that falls short, which requirement it misses, and the exact clause with the file it's in. The contract owners will take this straight into renewal negotiations.

**Must find (8):**

1. Quillon Telehealth: breach notice clock starts at Quillon's 'confirmation' of an incident, which can take up to 15 business days after first awareness, so notice is not guaranteed within 72 hours of discovery (Requirement 1).
2. Brasswick Lab Informatics: Schedule 3 (a separate file) lists a disaster recovery site in Montreal, Canada holding a nightly copy of the production database with patient results, and the main body binds hosting to Schedule 3 (Requirement 3).
3. Hollin & Marsh Transcription: new subcontractors are disclosed up to 15 days after they start work, not 30 days before (Requirement 2, notice part). The list itself is on the portal and is fine.
4. Imaging archive vendor (Brightwater Radiology Systems, now Pellucid Imaging per the index): Exhibit C, a separate file that does not name the vendor, allows 90 days after the Transition Period to purge images and backups (Requirement 4). The main body defers deletion to Exhibit C.
5. Sablemoor Data Vaulting: the base agreement is US-only, but Amendment No. 2 replaced Section 6.1 to allow a third replica in Frankfurt, Germany (Requirement 3). Requires reading the amendment against the agreement.
6. Nettlefield Messaging: the Data Processing Addendum (separate file) makes the subprocessor list available only on written request and promises only 'reasonable advance notice' of changes (Requirement 2, both parts).
7. Greyloft Technology Partners: production data is deleted and certified within 30 days (shortened to 20 by amendment), but backup media is only overwritten through a 180 day rotation, so backups are not deleted within 30 days (Requirement 4). The amendment does not touch Section 12.3.
8. Wrenfold Patient Payments: Exhibit A (at the end of the main file) hosts patient account records in Dublin, Ireland as well as Dallas (Requirement 3). The First Amendment fixed the breach notice clause but did not touch hosting.

**Must not report (10):**

- Ostrander Pharmacy Connect Section 7.4: subprocessor list on request and only 10 days notice.
- Kellbrook Survey Co. Section 10.3: destruction within 120 days and confirmation only on request.
- Lindqvist Workforce Scheduling: 10 business day breach notice.
- Mercator Dictation Services: 30 day notice of unauthorized disclosure.
- Wrenfold breach notice of ten days in the main body.
- Tallowmere Systems: mention of a Canadian replica.
- Marrowby Health Analytics: data stored in Toronto.
- Harrowgate Answering Service: agents in the Philippines.
- Veldt Clinical Staffing: files kept in Vancouver.
- Policy history: the 2023 guidelines allowed five business day breach notice and subprocessor disclosure on request.

## 3. Tesselwick Logistics

**Type:** Sweep: find every instance across many files. **Files:** 69.

**The ask:** We're switching off the RouteCalc v1 API next month and I need a list of everything at Tesselwick that still depends on it, so we can tell each owner before it breaks on them. The request logs don't tell us much because a lot of the traffic comes from shared IPs. Everything we have is in this folder: service configs, runbooks, crontab exports, pipelines, the partner integrations sheet and the internal DNS aliases. For each dependent, tell me what it is, the owner, and the evidence (file and line) that it still uses v1.

**Must find (9):**

1. dock-scheduler service (Yard Systems) calls the v1 host directly for onward leg estimates, deep in its upstreams block
2. eta-notifier (Customer Comms) uses the alias pathfinder-old.tsw.internal, which the DNS file defines as a CNAME to the v1 host
3. yard-balancer (Yard Systems) uses tw-routing-client 3.1.2 but explicitly sets RC_API_MODE to classic, which the library doc maps to RouteCalc v1
4. pallet-optimizer (Warehouse Tech) pins tw-routing-client 2.7.1 and does not set RC_API_MODE; releases before 3.0.0 default to classic (v1)
5. Weekday cron job pull_spot_rates.py on ops-batch-01 (Network Planning) calls the v1 bulk quote endpoint
6. lane_margin_weekly.sql (Commercial Analytics, run weekly from reporting-01 and published to the commercial weekly sheet) reads routecalc_v1.quote_results, which stops receiving rows at retirement so the report would silently go stale
7. Active partner Norrbeck Haulage (P-0090, Partner Integrations) calls the v1 bulk quote endpoint directly from an allowlisted IP range
8. Month-end tariff close runbook step 4, run manually by Finance Operations analysts, pulls tariff inputs from the v1 tariffs export endpoint
9. fuel_surcharge_backfill pipeline (Commercial Analytics) sends lane distance batches to qe1.tsw.internal, an alias for the v1 host

**Must not report (10):**

- invoice-builder has a v1 routing_url, but it is commented out and the active line points at v2
- load-matcher runbook describes calling the v1 host, but only historically; the service config uses v2
- RouteCache v1 consumers: lane-cache-warmer, sla-monitor probe, cache_hit_ratio.sql on routecache_v1.hits, the rcache alias, and partner Lindqvarn Mills
- legacy-quote-portal calls the v1 host directly but is itself being switched off on 2026-09-30, before the v1 retirement
- route-preview uses the legs.tsw.internal alias, which used to point at the v1 host but was repointed to v2 in March 2026
- Disabled warm_quotes.sh cron line on ops-batch-01 pointing at v1
- Fjellmark Freight partner row points at v1 but the partner is terminated
- carrier-onboarding pins an old 2.x tw-routing-client, but explicitly sets RC_API_MODE to current
- capacity-forecast has RC_API_MODE classic, but commented out, on library 3.2.0 which defaults to v2
- Other routecalc_v1 and v1 mentions that are not consumers: data retention table row, warehouse sources table, quote_volume_daily.sql comment about a removed UNION, new-service checklist

## 4. Calloway Ridge Credit Union

**Type:** Sweep: find every instance across many files. **Files:** 37.

**The ask:** Before open enrollment I want our employee-facing documents cleaned up, because traffic to the handbook, wiki and FAQ spikes in November and people will act on whatever they read. The 2026 travel and expense policy and the remote work policy in hr/canonical/ are the source of truth. Can you go through everything else in the folder and find every place that tells employees something different from those two policies? For each one I need the file, the exact text that is wrong, and what the canonical policy actually says, so the owners can fix them.

**Must find (11):**

1. Handbook section 7 gives the old meals per diem of $55 per day; canonical is $65 ($85 high-cost).
2. HR FAQ says receipts are only needed for expenses over $50; canonical requires an itemized receipt for any expense of $30 or more.
3. Manager guide says employees have 60 days to submit expense reports; canonical deadline is 30 calendar days.
4. Member Services wiki lets team leads and supervisors approve reports up to $1,000 alone; canonical allows a manager alone only up to $500, and a department may not set more generous rules.
5. Handbook Appendix C lists the Connectivity Allowance as $75 per month (the rejected proposal); canonical stipend is $50 per month. Handbook section 9 points to Appendix C for the amount.
6. IT wiki says items bought with the home office allowance are Credit Union assets that must be returned on leaving; canonical says they belong to the employee and need not be returned.
7. Handbook section 9 says the Credit Union will give at least two weeks' notice to change or end a remote arrangement; canonical requires at least 30 calendar days' written notice.
8. Finance Operations wiki sets the Clearline L2 ceiling at $5,000, and the manager guide says department heads approve up to the L2 ceiling without the CFO. Together, reports between $2,500 and $5,000 skip CFO approval; canonical requires the CFO above $2,500.
9. Marketing wiki says hybrid staff only need to be in the office one day a week; canonical minimum is two days, and departments may not require fewer.
10. Facilities wiki gives mileage at 58.5 cents a mile; canonical rate is $0.62 per mile.
11. New hire orientation speaker notes tell new hires they can request remote work after their first 60 days; canonical requires completing the 90-day introductory period.

**Must not report (11):**

- Branch Operations requires hybrid back office staff in the office at least three days a week.
- Commercial Lending requires expense reports within 10 business days.
- Internal Audit caps lodging at $175 per night everywhere.
- November 2024 Finance email announcing 2025 rates ($55 per diem, $25 receipts, 60 days, $750 manager approval, 60 cents mileage).
- March 2025 HR email announcing a $40 stipend and two weeks' notice to end a hybrid arrangement.
- Contractor Engagement Guide lists different meal, lodging, mileage, receipt, submission and approval terms.
- Struck-through $25 receipt threshold on the Finance Operations wiki.
- Manager guide mentions managers could approve up to $750.
- Meeting notes discussing raising the connectivity stipend to $75.
- Handbook section 13 and HR FAQ ask for two weeks' notice of resignation.
- Tuition Assistance Program requires grade reports within 60 days.

## 5. Varnholt

**Type:** Multi-step: research several things, then decide. **Files:** 29.

**The ask:** Leadership is picking the next country for Varnholt at the September review, and I have to walk in with a recommendation between Germany, Brazil and Japan. Everything we've gathered is in this folder, and Ilse's brief spells out the criteria we have to use. Can you tell me which country we should launch next and lay out the evidence for each criterion for all three countries, with the actual numbers and which file they come from? Ilse will ask where every number came from, so it needs to hold up.

**Correct answer:** Brazil

**Must find (12):**

1. Contribution margin for payback math is the current Finance figure of 70%, not the older 64% used in Slack and old decks
2. Germany payback passes: entry cost US$318,400; 4,300 subscribers x US$8.10 x 70% = about US$24,381 per month; payback about 13.1 months. No direct German competitor has a free plan (Notiztafel and Blattwerk offer trials only), so the base case applies.
3. Germany fails the storage criterion: counsel's 17 June 2026 update (forwarded by the GC as an addendum to the March memo) reports the CAVV ordinance, adopted 11 June 2026 and effective 1 January 2027, requiring in-scope providers (over 10,000 German users; Varnholt plans about 60,000) to store German users' content in Germany. The March memo's 'no requirement' conclusion is withdrawn.
4. Germany segments pass 2 of 3 on completed survey responses: students 33/80 = 41.3%, independent professionals 23/60 = 38.3% reachable; small teams 11/50 = 22.0% not reachable (contrary to Feldhaus's 3 of 3 view).
5. Brazil's cost estimate double counts the help center: line 1 (Lusofona quote LT-2291, US$64,000) already covers all 412 help center articles, and line 2 adds help center translation again for US$55,000. Corrected entry cost is US$250,000, not US$305,000.
6. Brazil payback passes once corrected: 4,700 subscribers x US$4.60 x 70% = about US$15,134 per month; US$250,000 / 15,134 = about 16.5 months (the uncorrected US$305,000 would give about 20.2 months and fail). No direct Brazilian competitor currently has a free plan, so base case applies.
7. Brazil has no in-country storage requirement: current law permits foreign hosting, and Bill PL 4.117/2025 was archived and never adopted.
8. Brazil segments pass 2 of 3 on completed responses: students 47/90 = 52.2%, independent professionals 26/70 = 37.1% reachable; small teams 10/55 = 18.2% not. This settles the segment Mirante called 'unclear'.
9. Japan's direct competitor Kumonote launched Kumonote Free on 22 July 2026 (unlimited notes, sync across all devices). The Kumonote pricing profile saying 'Free plan: none' is a February 2026 snapshot and is out of date. So the free-plan scenario applies to Japan.
10. Japan payback fails under the free-plan scenario: 3,000 subscribers x US$7.20 x 70% = US$15,120 per month; US$336,000 / 15,120 = about 22.2 months (base case would be about 12.8).
11. Japan has no in-country storage requirement; the cross-border transfer consent rule is a disclosure obligation, not a storage rule.
12. Japan segments pass 2 of 3 on completed responses: independent professionals 29/65 = 44.6% and small teams 28/60 = 46.7% reachable; students 20/70 = 28.6% not reachable (contrary to Kasumi's interview view that students are easiest).

**Must not report (14):**

- Germany's March legal memo saying there is no in-country storage requirement
- Brazil's stated total entry cost of US$305,000 and the resulting ~20 to 22 month payback (including Haruki's Slack calculation)
- Kumonote pricing profile stating it has no free plan
- Shiori Works free plan in Japan treated as the free-plan trigger
- Anotaki's free plan (or Cadernia's old free tier) triggering Brazil's free-plan treatment
- Brazil Bill PL 4.117/2025 as an in-country storage requirement
- Japan's cross-border transfer consent rule, or Brazil's encarregado appointment, treated as failing the storage criterion
- Using the 64% contribution margin
- Counting partial survey responses (Brazil independent professionals would drop to 29/95 = 30.5% and fail)
- Using the non-free-plan downside cases for payback: Germany's macro downside (3,600 subscribers) or Brazil's currency downside (US$4.05 price)
- Agency qualitative segment calls used as the verdict (Feldhaus 3 of 3 for Germany; Mirante 1 clear of 3 for Brazil; Kasumi students easiest in Japan)
- Japan's high support ticket volume (localization requests) as a reason to pick Japan
- Notiztafel's 14-day trial or Blattwerk's 2024 Austria free tier test as a German free plan
- France (or FR/MX survey rows) as a candidate

## 6. Ferrowind Analytics

**Type:** Multi-step: research several things, then decide. **Files:** 39.

**The ask:** Gideon wants a competitor pricing comparison before the board offsite: for each competitor, their pricing model, entry price, whether they charge per seat or by usage, whether there's a free tier, and the annual discount. He also wants a recommendation on whether we should drop per-seat pricing, and he wants it backed by what our win/loss deal notes actually say, not gut feel. Everything we have is in the folder: competitor pricing snapshots, changelogs and blog posts, our deal notes, and our current pricing.

**Correct answer:** Yes: Ferrowind should stop charging a full seat for every user. Move off pure per-seat pricing to usage-based pricing or a hybrid that charges builders/editors (or a platform fee) and makes view-only or occasional users free or near free.

**Must find (10):**

1. Quillmark Insights: per-seat (every user including viewers), free tier for up to 3 users, entry paid plan Team at $30 per user per month billed monthly or $24 billed annually, 20% annual discount.
2. Tallowbeam moved from per-seat to usage pricing (rows scanned) effective August 1, 2026, per a blog post newer than the February pricing snapshot. Entry is Launch at $150 per month; no per-person charge; still no free plan (14-day trial); annual discount unchanged at 15%, which requires the older snapshot to know.
3. Sorrelgate Data retired its free Community plan on 2026-06-30 (changelog), so it has no free tier today even though the April snapshot and a May blog post say Community is free and here to stay. Model is hybrid: platform fee with included seats plus per-seat charges; entry Growth at $400/month including 5 seats, extra seats $35; annual discount is two months free (about 17%).
4. Brisklane Metrics quotes yearly prices: Essentials $468 per editor per year is $39 per editor per month billed annually, versus $45 month to month (about 13% annual discount). Charges only editors; viewers unlimited and free. No free plan (21-day trial).
5. Obsidra is usage-based (compute credits, unlimited users). Its headline $180/month for Launch is billed annually; the monthly-billed price is $225, so the annual discount is 20%. Free Sandbox tier exists (1 user, 10 GB processed per month).
6. Kettleridge BI workspace plans remain per-user (every member and guest billed), entry Team $18 per user per month, 10% annual discount, free Personal plan for 1 user. The August 2026 usage-based change applies only to the separate Embed product.
7. Ferrowind's current pricing charges a full seat for every named user including view-only users ($55 per seat monthly, $46 annual on Standard), with no free plan and no viewer seat offered today.
8. Seven of the eleven lost deals were lost primarily on seat price: Arvelo Logistics, Sunmere Hotels, Greyfield Components, Halden Mutual, Picton Veterinary Partners, Westray Outdoor, Carrow Street Media. In every one the complaint was paying a seat for occasional or view-only users.
9. Three losses were on missing features: Nightjar Biotech (RLS on Standard), Ellery Rail Services (white-label embedding), and Quarrydown Credit Union, which was first logged as seat price but reclassified to missing audit log export in a later update. One further loss (Bellhaven Foods) was an in-house build, neither price nor features.
10. Six of the seven seat-price losses went to competitors that do not charge a seat for every user: Tallowbeam (2, after its usage switch), Obsidra (2), Brisklane (2, free viewers). The seventh (Picton) went to Sorrelgate, whose platform fee includes 5 seats with cheaper extra seats. The pure per-seat competitors Quillmark and Kettleridge only beat Ferrowind on features.

**Must not report (11):**

- Tallowbeam's February snapshot and November 2025 blog describe per-seat pricing ($25 Starter, $40 Pro).
- Sorrelgate's Community free plan in the April snapshot, and the May blog post saying Community is here to stay.
- Kettleridge moving to usage-based pricing.
- Quillmark Team at $19 per user.
- Brisklane entry price of $468 compared directly with monthly prices, or Obsidra $180 treated as a monthly-billed price.
- Quarrydown Credit Union counted as a seat-price loss.
- Maplethorn Retail counted as a seat-price loss because they flinched at 140 seats.
- Pellam & Rourke seat objection counted as evidence of a price loss.
- Feature mentions inside seat-price losses (Halden Mutual alerting, Arvelo alerting) counted as feature losses, or used to argue losses are feature-driven.
- Ferrowind's $15 viewer seat, or the old $49 Standard price, reported as current Ferrowind pricing.
- Bellhaven Foods or Fenwick Hollow counted as price or feature losses.

## 7. Pinmoor (held back)

**Type:** Multi-step: research several things, then decide. **Files:** 48.

**The ask:** I'm putting together the top customer problems for this quarter for Q4 roadmap planning, and I want it grounded in everything we have: support tickets, NPS verbatims, the churn survey, sales call notes and the community forum. For each problem, tell me how many distinct customers raised it and give me a few real quotes. These numbers are going in front of the exec team next week, so they need to hold up if someone checks.

**Must find (6):**

1. Payroll Bridge export to the payroll provider is broken or unreliable since the July 3.14 release (Ledgerline file columns shifted, Tallybook sync mapping error 412 or stuck pending, duplicated or missing rows, wrong earnings codes)
2. Time Off accrual balances are calculated wrong (part-time and reduced schedules accrue at full time rate, no proration, carryover cap ignored, rehires accruing from original hire date, tiers not applied)
3. Pinmoor Go mobile app keeps logging users out (sign in required on every open, lock screen or network change, SSO sessions of minutes, face unlock not remembered)
4. Performance review cycles cannot be edited after launch (questions, rating scale and template locked, reviewers cannot be reassigned, cancelling to fix loses submitted responses)
5. Insights reports time out or never load for company-wide or large datasets (blank dashboards, 504s, scheduled reports arriving empty)
6. Ranking of the themes by distinct customers

**Must not report (7):**

- Benefits enrollment document upload failure: 30 tickets, the largest single cluster in tickets.csv
- Org chart PDF export cuts off names (12 tickets, 4 NPS comments, a forum thread, a sales call note)
- Forum cross-posts that duplicate threads in a second category
- Hallam Veterinary Partners complaint about part-time accruals being wrong
- Quenby Foods payroll export issue
- Lindqvist Architecture mobile sign in problem
- Minor requests that look like themes (Huddlepost chat integration for approvals, dark mode, pricing complaints, slower support responses)

## 8. Marlowe Crest Insurance

**Type:** Multi-step: research several things, then decide. **Files:** 43.

**The ask:** Norvale passed HB 2231 on consumer notices and it hits us on January 1, so I need to get ahead of it before the Q4 forms filing. Can you go through the rule and our Marlowe Crest docs in this folder and tell me what each requirement actually asks of us, which of our documents have to change for each one (and what in them is wrong), and anything the rule requires that we don't have at all? I'm taking this to the claims, underwriting and contact center leads next week, so please point to the exact text.

**Must find (13):**

1. Requirement 4(1) non-renewal: the Norvale nonrenewal notice template MC-NR-02 promises only 30 days notice (rule requires 60) and its reason text is the generic underwriting guidelines statement the rule says is not sufficient.
2. Requirement 4(1) non-renewal: the Norvale Crestline HO-3 policy wording's Nonrenewal condition gives 30 days notice.
3. Requirement 4(1) non-renewal: agent training Module 4 tells agents a Norvale customer gets a month's notice of nonrenewal.
4. Requirement 4(1) non-renewal, operational: the renewal schedule lets underwriting enter nonrenewal decisions until day 50 before renewal, so notices cannot reach the 60 day minimum. Needs the schedule read against the rule.
5. Requirement 4(2) premium increase: although MC-RN-14 was updated, it is mailed inside the renewal offer, which is released 35 days before renewal, short of the 45 days the rule requires. Needs the schedule plus the rule (and the template's own 45 day promise).
6. Requirement 4(2) premium increase: the website FAQ tells Norvale customers a letter comes only for increases over 15% and at least 30 days before renewal (rule: 10% or more, 45 days, with principal factors).
7. Requirement 4(3) claim acknowledgment: procedure CP-02 sets the acknowledgment deadline at 15 business days, rule requires 10 business days.
8. Requirement 4(3) claim acknowledgment: template MC-CL-01 does not name the assigned adjuster or give a direct phone or email for them, only the general Claims Service Center line; CP-03 confirms adjuster direct contacts are deliberately kept off system letters.
9. Requirement 4(4) claim denial: the Norvale denial template MC-CL-07 gives a 30 day review window (rule: not less than 60), has no Department of Insurance consumer assistance contact, and has no field citing the specific policy provision (only a generic reference to terms, conditions and exclusions).
10. Requirement 4(4) claim denial: the Claims Service Center status call script tells denied Norvale callers they have 30 days to request a review.
11. Requirement 4(5) replacement cost estimate at renewal: the Crestline and Crestline Premier renewal cover letter MC-RN-01 lists the renewal packet contents with no written replacement cost estimate summary, although Crestline Coverage A starts at $150,000 (most Norvale policies are at or above $300,000) and Premier starts at $750,000.
12. Requirement 4(5) replacement cost estimate at issuance: agent training Module 3 forbids sharing the RebuildIQ replacement cost estimate with customers, which conflicts with the duty to give a written summary at issuance (the welcome letter MC-NB-01 also includes none).
13. Requirement 4(6) secondary notice designee is missing entirely: no document offers policyholders a designee at issuance or renewal, and no process sends copies of nonrenewal or cancellation notices (including nonpayment cancellations) to a designee. This is a new process (capture, storage, dual mailing), not an edit. Authorized contacts do not satisfy it because they receive no mail.

**Must not report (8):**

- Kessington documents with 30 day nonrenewal notice, 15%/30 day premium letter, and 15 calendar day acknowledgment: the Kessington amendatory endorsement, Kessington renewal notes, Module 7, and FAQ-1011.
- Kessington denial letter MC-CL-07-KS and the Kessington Claims Handling Supplement with a 30 day review window and no Norvale Department contact.
- The current premium change notice template MC-RN-14 (Rev. 2026-08-04) already meets Section 4(2) on its face: 10% trigger, 45 day promise, top rating factors.
- The archived 2023 edition of MC-RN-14 with a 20% trigger and 30 day timing.
- Cottage Basic renewal letter MC-RN-03 includes no replacement cost estimate summary.
- Commercial Landlord Package nonrenewal condition with 30 days notice.
- 10 day notice for cancellation for nonpayment (MC-CX-05 template, HO-3 wording cancellation condition).
- Authorized contacts procedure presented as already satisfying the secondary notice designee requirement.

## 9. Brackenford Holdings

**Type:** Small job: splitting it up is probably a waste. **Files:** 31.

**The ask:** What notice do we have to give to terminate the Kestrel Freight master services agreement without cause, and by when for a year-end exit? We're looking at moving that freight to another carrier as of December 31, 2026, and I need to tell the COO the latest date we can give notice and what form it has to take. All our agreements are in contracts/, with the index csv alongside.

**Correct answer:** At least 90 days' prior written notice under MSA Section 15.1 as replaced by Amendment No. 2. For a December 31, 2026 termination, the notice must be received by Kestrel no later than October 2, 2026, delivered by hand, courier or certified mail (not email alone) to the Director of Contracts, stating December 31, 2026 as the termination date.

**Must find (3):**

1. The without-cause notice period is 90 days, because Amendment No. 2 (effective July 15, 2025) deleted and replaced MSA Section 15.1, which originally said 60 days.
2. For a December 31, 2026 termination date, notice must be received by Kestrel no later than October 2, 2026. Notice is effective on receipt, the day of receipt is not counted and the termination day is counted (Oct 3 to Dec 31 is 90 days). The termination date must be the last day of a month, which December 31 satisfies.
3. Form of notice: in writing, delivered by hand, overnight courier or certified mail (email alone is not effective for termination), addressed to Kestrel Freight Services, Inc., 1180 Harbor Line Road, Dunlow, Attention: Director of Contracts, and stating the termination date.

**Must not report (7):**

- The original MSA Section 15.1 notice period of 60 days (which would give a November 1, 2026 deadline).
- The Dunlow warehouse lease with Kestrel Freight Properties LLC, whose early termination option requires 180 days' notice plus a termination fee.
- Termination for cause under MSA Section 15.2 (30 day cure period after notice of material breach).
- Non-renewal notice under MSA Section 3.2 (60 days before the end of the current term).
- The Ardent Line freight brokerage agreement's 30 day with-or-without-cause termination right.
- The Altamira Cloud 'Master Services Agreement' early termination on 120 days' notice.
- The Tilbury Grove sublease early termination effective December 31, 2026 with notice by March 31, 2026.

## 10. Juniper Vale Bank

**Type:** Small job: splitting it up is probably a waste. **Files:** 6.

**The ask:** Nightly statement emails did not go out on September 3. What happened, start to finish, and what was the root cause? I have the post-incident review with ops and the retail banking lead tomorrow and need a timeline I can defend, so please back each step with what the logs actually show. Everything I pulled is in this folder.

**Correct answer:** Root cause: CHG-4471, the TLS certificate rotation on outbound mail relay mx-relay01 at 01:10 UTC (21:10 ET Sep 2), installed the new certificate without its intermediate (chain length 1 instead of 2). The mailer workers could not verify it (unknown CA), so every statement email failed, was retried without limit, backed up stmt.email.send until broker lq-2 hit its memory alarm at 02:47 and blocked the renderer, the scheduler killed STMT_NIGHTLY at its 3 hour maxrun at 04:30, and the renderer failed the batch and purged all 36,114 queued emails.

**Must find (6):**

1. Change CHG-4471 rotated the outbound mail relay TLS certificate. The calendar gives 21:10 ET on Sep 2, which is 01:10 UTC on Sep 3, matching the relay log reload. The new certificate was loaded with a chain of length 1 instead of 2, i.e. the intermediate (JVB Issuing CA G3 chain) was not served.
2. From 01:12 UTC the mailer workers (mailer-1, mailer-2) that consume the email queues can no longer complete STARTTLS with the relay: the relay sees unknown_ca alerts and the consumers report x509 certificate signed by unknown authority. Other relay clients and the ops-jump01 post check still succeed, which is why the change looked fine.
3. Statement messages published by the renderer from 01:30 UTC are never acknowledged; the stmt.email.send queue policy retries without limit, so messages are redelivered over and over and the queue backs up (ack_rate 0, ready count climbing to about 36,000).
4. At 02:47:13 UTC broker node lq-2 hit its memory high watermark (the backlog of PDF-carrying messages) and blocked the renderer's publishing connection; the renderer logs the block and stops at 36,114 of 41,862 statements.
5. With progress stuck at 36114/41862, the Tidewell job STMT_NIGHTLY (run 88213, maxrun 3h from 01:30) exceeded its maximum runtime at 04:30 UTC and was sent SIGTERM; STMT_ARCHIVE_PUSH was skipped.
6. On SIGTERM the renderer aborted, marked batch B-20260903 FAILED and, per its on_abort=purge_outbound setting, purged the 36,114 queued statement emails, so none were delivered (delivered_confirmed=0).

**Must not report (9):**

- PDF signing latency spike and hsm-a failover on the renderer (alert A-77338), from planned HSM maintenance CHG-4472.
- Lanternq peer lq-3 unreachable at 23:48 UTC on Sep 2 (alert A-77335).
- GL_RECON job failure at 02:00 UTC.
- CHG-4466 Tidewell scheduler agent patch listed for Sep 2 22:00 ET.
- CHG-4473 branch DNS forwarder replacement and CHG-4464 cards-default TTL change on the same day.
- Relay spool disk above 80% at 03:20 UTC (alert A-77343) and other relay noise (dnsbl timeouts, printer relay rejects).
- Lanternq management listener certificate expiring soon (alert A-77297, queue log warning).
- Renderer warnings: deprecated footer template, font fallback, GC pauses, accounts skipped for no email on file.
- CHG-4476 data warehouse partition change with a 01:00 to 01:15 window on Sep 3, which lines up with the 01:10 failures only if the ET window is misread as UTC.

## 11. Lumen Harrow

**Type:** Small job: splitting it up is probably a waste. **Files:** 4.

**The ask:** Can you fix anything wrong in this email against the fact sheet and make it plainer before I send it to members this afternoon? It's the price change announcement in draft-email.md, and the fact sheet is fact-sheet.md. Finance signed off on the fact sheet, so that's what the email has to match. Send me back the corrected email ready to paste.

**Must find (3):**

1. Effective date is wrong: the email says 1 October 2026, the fact sheet says 1 November 2026.
2. Dedicated Desk new price is wrong: the email says $455, the fact sheet says $445.
3. Rate-lock condition is wrong: the email adds an exception for members of more than two years; the fact sheet says annual billing by 15 October is the only way and there is no length-of-membership exception.

**Must not report (4):**

- The Day Pass price going down from $35 to $30 looks like a mistake in a price increase email.
- The cancellation deadline of 1 October 2026 looks like it should move to 1 November once the effective date is corrected.
- The 15 October 2026 annual billing deadline sits in the same sentence as the wrong condition.
- The internal history of the last price change (March 2024, Flex Desk $220 to $240).

## 12. Oxtail Supply (held back)

**Type:** Small job: splitting it up is probably a waste. **Files:** 3.

**The ask:** Finance needs our Q2 net revenue from EU customers, in USD, after credit notes, for the board pack going out tomorrow. The invoice export, the customer list and the pricing notes are all in the folder. Can you work out the number to the cent and show me how you got there?

**Correct answer:** 493834.22 USD

**Must find (4):**

1. Credit notes are stored as positive amounts with type credit_note and must be subtracted. Q2 EU credit notes total 12399.78 USD against 506234.00 USD of Q2 EU invoices.
2. Harrowgate Catering Group (C-1027) is an EU customer per customers.csv even though every row in invoices.csv still shows region UK. Its Q2 net contribution is 31392.98 USD.
3. Only rows dated 2026-04-01 through 2026-06-30 count. 11 EU rows sit just outside the quarter (late March, early July), including a Q2 credit note dated 2026-04-03 against a March invoice that does count.
4. Non-USD lines (EUR, GBP, SEK) are converted at the fixed Q2 2026 rates (EUR 1.0850, GBP 1.2700, SEK 0.0952 USD per unit), not the Q1 rates, rounding each line to the cent.

**Must not report (5):**

- The region column in invoices.csv for C-1027 (shows UK).
- The Q1 2026 exchange rate table.
- Rows dated 2026-03-27 to 2026-03-31 and 2026-07-01 to 2026-07-06, including July credit notes that reference June invoices.
- The volume and loyalty discount rules in pricing-notes.md.
- UK region customers, and EU customers billed in GBP or USD being treated as non-EU.
