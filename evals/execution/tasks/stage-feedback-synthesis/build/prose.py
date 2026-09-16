# Hand-written sales call notes and forum threads.
# Each entry: path (fixture-relative), text, raises = [(canonical company, tag)].
# Tags T1..T5 are the true themes. Anything else is noise or a decoy tag.

SALES_CALLS = [
dict(path="sales-calls/2026-07-09-birchway-dental-renewal.md", raises=[("Birchway Dental Group", "T1"), ("Birchway Dental Group", "T2")], text="""# Birchway Dental Group: renewal call

Date: July 9, 2026
Pinmoor: Theo Marchetti (AM), Ruth Okafor (CSM)
Birchway: Colleen Draper (Director of People Ops), Sanjay Iyer (Controller)
Renewal date: Sept 30, 2026. 14 locations, about 410 employees. Modules: Core, Time Off, Payroll Bridge.

## Notes

- Colleen opened by saying they want to renew but not on autopilot this year.
- Sanjay: the Ledgerline export changed after our July release. Employer match landed in the wrong column on the 7/3 run. They caught it in review, but he now has someone eyeballing every file before it goes out.
- Sanjay, close to verbatim: I can't have my team proofreading a payroll file every two weeks, that's the whole reason we bought the bridge.
- Colleen: hygienists who work part time are accruing PTO like full timers. Around 60 people affected. Front desk managers noticed first because people were requesting time they should not have had.
- They like the directory and the new onboarding flows. No interest in the Reviews module right now, maybe 2027.
- Pricing: asked for a flat renewal. Theo said he would check but pointed to the 5% uplift in the contract.
- Ruth to open tickets for both issues if not already open (Sanjay thinks there is one for the export already).

## Next steps

- Ruth: confirm ticket numbers, send an ETA on the export fix by 7/12
- Theo: renewal quote with and without uplift
- Follow-up call booked for Aug 6
"""),

dict(path="sales-calls/2026-07-14-hallam-veterinary-discovery.md", raises=[], text="""Discovery call: Hallam Veterinary Partners (prospect)
July 14, 2026 | AE: Priya Venkataraman | SE: Marcus Bell

Attendees (Hallam): Jo Pritchard, HR Manager; Allan Reyes, Practice Operations

Current stack: Staffory for HR and time off, separate payroll provider (Tallybook). 9 clinics, 230 staff, lots of part-time vet techs.

Why they are looking:
Jo was blunt about Staffory. Their accrual engine does not handle part-time schedules, so every quarter she exports balances to a spreadsheet and fixes them by hand. She said the vet techs have stopped trusting the numbers they see in the Staffory app. Allan added that Staffory support told them a fix was on the roadmap for over a year.

Other pain: onboarding paperwork is still paper at 4 of the 9 clinics.

What they asked us:
- Can Pinmoor prorate accruals by scheduled hours? (Marcus showed the policy setup. They liked the tiering screen.)
- Does Payroll Bridge push to Tallybook? Yes, showed the mapping screen.
- Price per employee for 230 staff, and whether clinics can be separate entities.

Signals: Budget approved for Q4. Decision by end of September. Jo is the champion, Allan is cautious and wants references from other vet groups.

Next: send two references, pricing proposal by 7/18, sandbox access for Jo.
"""),

dict(path="sales-calls/2026-07-16-copperlane-hotels-expansion.md", raises=[("Copperlane Hotels", "T3"), ("Copperlane Hotels", "T5")], text="""Copperlane Hotels, expansion conversation, 16 July 2026

Present: Dominic Farrant (VP People, Copperlane), Esther Lund (HRIS Analyst, Copperlane), Theo Marchetti and Nadia Brooks from Pinmoor.

Copperlane runs 19 properties and has roughly 2,300 employees on Pinmoor today. They opened the call interested in adding the Reviews module for their salaried managers, around 280 people, starting in January.

Before we got to that, Dominic wanted to talk about the mobile app. Housekeeping and front desk staff clock in on Pinmoor Go, and since the summer app update they get logged out whenever they lock their phones. Esther said the property GMs have started keeping a shared tablet at the time clock because people could not get back into the app fast enough at shift change. Dominic said this is the thing he hears about at every GM meeting and he did not want to expand until it is fixed.

Esther also raised reporting. Their monthly headcount and turnover pack for the ownership group comes out of Insights, and the company-wide version has not finished loading since mid July. She has been running it property by property, 19 separate exports, and stitching them together in a spreadsheet. She said it takes her most of a day each month.

We did get to Reviews. They want calibration and a 5 point scale. Nadia walked through the cycle setup. Dominic asked for a written proposal but said the timing depends on the two issues above.

Actions:
Nadia to get product to confirm whether the mobile logout is known and whether there is a date.
Theo to send a Reviews proposal for 280 seats, start date flexible.
Esther to send a sample of the headcount report definition so support can reproduce the timeout.
"""),

dict(path="sales-calls/2026-07-22-greyloch-qbr.txt", raises=[("Greyloch Manufacturing", "T1"), ("Greyloch Manufacturing", "T4")], text="""CALL SUMMARY (auto-generated, edited by CSM)
Account: Greyloch Manufacturing
Meeting: Q3 business review
Date: 2026-07-22, 45 min
Speakers: Ruth Okafor (Pinmoor CSM), Helen Szabo (Greyloch HR Director), Bart Nowak (Greyloch Payroll Lead)

KEY MOMENTS

[04:12] Ruth reviewed adoption: 96% of 640 employees active in the last 30 days. Time Off requests up 20% since they turned on the mobile app.

[09:40] Bart raised the payroll integration. Quote from transcript: "Tallybook has kicked back our file twice now with a mapping error, and both times it was the morning payroll was due." He said the error references code 412 and his workaround is to export manually and upload the file into Tallybook himself.

[14:05] Ruth confirmed there is an open engineering issue for Tallybook mapping failures after the July release.

[21:30] Helen on performance reviews: they launched the mid-year cycle on July 1 and then legal asked them to reword the question about attendance. Quote from transcript: "The template was locked the second we launched, so we either live with the wording or throw away two weeks of responses." They chose to leave it and send a clarifying email to all managers.

[29:00] Discussion of next year: Greyloch is opening a second plant in 2027, would add about 150 employees.

[38:20] Helen asked whether Pinmoor could support shift differentials in Time Off. Ruth to check.

ACTION ITEMS
- Ruth: share Tallybook issue status weekly until resolved
- Ruth: log feature feedback on editing launched review cycles
- Helen: send org structure for new plant when available
"""),

dict(path="sales-calls/2026-07-24-quenby-foods-reviews-upsell.md", raises=[], text="""## Quenby Foods: Reviews module upsell

**When:** Fri 24 Jul 2026, 11:00
**Who:** Lorenzo Quenby (COO), Abby Tran (HR Generalist) / Priya Venkataraman (AE)

Quick one. Quenby has used Core, Time Off and Payroll Bridge since 2024, about 175 employees across two production kitchens and a distribution site.

**Context from Abby:** they run reviews on paper forms today and managers hate the filing. She wants something that works on the shop floor tablets.

**Payroll Bridge:** I asked how it was going since I knew they had a rough patch. Abby said the export issue they had back in February was fixed within a week and it has been clean every pay period since. Lorenzo said it is one of the reasons they would buy more from us.

**Reviews questions:**
- Can hourly staff without email do a self review on a shared tablet? (Yes, with kiosk mode.)
- Can they use a simple 3 point scale? (Yes.)
- Price for 175 employees? Sent list price, Lorenzo asked for a first year discount.

**Next:** proposal with 10% first year discount pending approval from Sam. Target close Aug 15.
"""),

dict(path="sales-calls/2026-07-30-radleigh-senior-living-renewal-risk.eml.txt", raises=[("Radleigh Senior Living", "T2"), ("Radleigh Senior Living", "T3")], text="""From: Nadia Brooks <nadia.brooks@pinmoor.example>
To: Theo Marchetti <theo.marchetti@pinmoor.example>, Ruth Okafor <ruth.okafor@pinmoor.example>
Date: Thu, 30 Jul 2026 16:42:10 -0500
Subject: Radleigh Senior Living call recap (renewal at risk)

Hi both,

Recap from today's call with Radleigh. Attendees on their side were Gloria Mensah (Chief People Officer) and Kenji Albright (HR Systems).

The short version is that they are unhappy and the renewal in November is at risk.

1. Time off balances. Radleigh has a lot of part-time CNAs and their accrual balances have been wrong since the July pay periods. Gloria said caregivers are showing up to HR with screenshots of balances that went up by 80 hours overnight, and then down again after Kenji corrects them by hand. Her words: "My caregivers don't believe any number in that app anymore." Kenji has been fixing balances manually every Friday.

2. Mobile app. Most of their staff only use Pinmoor Go. Kenji said iOS users lose face unlock sign in after every app update and many just stop using the app and call HR instead. He thinks this is the same issue in the community forum.

3. They were positive about the onboarding module and about Ruth, which is good.

Gloria asked for an exec sponsor call before she presents the renewal to their CFO. I suggested Sam. Can one of you set that up for the week of Aug 10?

I have told them we would come back with a status on both issues by Aug 7.

Thanks,
Nadia
"""),

dict(path="sales-calls/2026-08-04-kittering-freight-checkin.md", raises=[("Kittering Freight", "T3")], text="""kittering freight / check-in / 2026-08-04
ruth + marlon (ops mgr, kittering)

- 310 drivers + dock staff, almost all mobile only
- marlon: drivers get signed out of pinmoor go constantly, have to sign back in at every stop to see schedule. \"its not a big deal until it is 5am and 40 guys are standing at the dock doing password resets\"
- drivers are on android mostly, some iphone
- asked if there is a way to extend the session. told him no admin setting today
- otherwise fine. wants year-end tax forms delivered through the app at year end (yes, supported)
- no renewal until april 2027
- todo: link marlon to known issue, follow up when app fix ships
"""),

dict(path="sales-calls/2026-08-06-dunleith-credit-collective-demo.md", raises=[], text="""# Demo: Dunleith Credit Collective

Date: 2026-08-06
AE: Priya Venkataraman
Prospect attendees: Rosa Kinsella (VP HR), Dev Halloran (InfoSec)

## Background

Dunleith is a 520 person lending cooperative moving off spreadsheets and an old on-premise HR system. They have no current HR SaaS vendor. The main drivers are audit findings about manual access reviews and a move to hybrid work.

## Demo flow

1. People directory and custom fields
2. Onboarding with e-signature
3. Time Off with accrual policies (Rosa asked about FMLA tracking)
4. Insights: headcount and attrition reports
5. Admin roles and audit log

## Questions

Dev spent most of his time on security:

- SOC 2 Type II report: will send under NDA.
- SSO with SAML and SCIM provisioning: supported.
- Data residency: US hosting only today.
- Pen test summary: available on request.

Rosa asked whether the reporting would cope with 520 people and five years of history. We showed a demo tenant of similar size and the reports loaded quickly. She asked for a reference with a similar sized financial services customer.

## Next steps

- Send SOC 2 and security questionnaire answers
- Reference call with a credit union customer
- Pricing for 520 employees, Core + Time Off + Insights
"""),

dict(path="sales-calls/2026-08-11-westmere-retail-exec-sponsor.md", raises=[("Westmere Retail Group", "T5"), ("Westmere Retail Group", "T2")], text="""Westmere Retail Group | Exec sponsor call | 11 Aug 2026

Pinmoor: Sam Adeyemi (CRO), Theo Marchetti
Westmere: Pauline Graves (CHRO), Ivo Castellanos (Director, Workforce Analytics)

Westmere is one of our larger accounts: 42 stores, about 3,100 employees, high seasonal hiring.

Pauline framed the call as a check on whether Pinmoor can keep up with their size. Two things came up.

Reporting. Ivo's team builds a weekly labor and turnover report per region for the ops leadership meeting. Since the end of July any Insights report that covers the full company runs until it times out. He has moved the weekly pack to a manual export into their BI tool, which he says defeats the point of paying for Insights. He asked directly whether Insights was built for companies with more than a couple thousand employees. Sam said yes and that engineering is looking at query performance.

Time off. Westmere has seasonal part-time staff who should accrue at a reduced rate. Pauline said store managers keep approving time off based on balances that turn out to be inflated, and then payroll has to claw hours back. She described it as a trust problem with store staff more than a math problem.

Pauline was complimentary about hiring and onboarding, which handled 900 seasonal hires last year without trouble.

Outcome: no renewal risk this year (contract runs through 2027) but Pauline wants a written plan on both issues. Sam committed to a plan by end of August.
"""),

dict(path="sales-calls/2026-08-13-fenwright-engineering-renewal.md", raises=[("Fenwright Engineering", "T4")], text="""# Fenwright Engineering renewal (13 Aug 2026)

**Attendees:** Carla Duggan (Head of Talent, Fenwright), Jonah Pike (People Partner, Fenwright), Theo Marchetti (Pinmoor)

**Account:** 380 employees, engineering consultancy. Core, Reviews, Insights. Renewal Oct 1.

Carla said they will renew. Most of the call was about the review cycle they ran in June and July.

What happened: Fenwright launched their annual review cycle with a competency framework that had one competency missing for the junior engineer track. They noticed two days after launch. The questions could not be changed in the running cycle, so they cancelled it and relaunched. About 70 people had already submitted self reviews and had to write them again. Jonah said the engineers were not gracious about it.

Carla also said that managers who were promoted mid-cycle could not be swapped in as reviewers.

Carla's ask: some way to edit wording or add a question to a live cycle, even if it creates a new version. She said she would be happy to join a customer advisory call on it.

Commercials: 3% uplift accepted, 2 year term. Theo to send paperwork.
"""),

dict(path="sales-calls/2026-08-18-sunderby-clinics-qbr.md", raises=[("Sunderby Clinics", "T1"), ("Sunderby Clinics", "T3")], text="""SUNDERBY CLINICS: QBR NOTES
Aug 18, 2026
CSM: Ruth Okafor
Customer: Mei Lin Fairbanks (HR Operations Manager), Rob Tennant (Payroll Supervisor)

Account snapshot
  Employees: 760 across 12 clinics
  Modules: Core, Time Off, Payroll Bridge, Insights
  Health score: yellow (was green in Q2)

Discussion

Payroll. Rob said the Ledgerline file has been wrong in some way on four of the last six runs. Issues he listed: cost center blank for employees who transferred, duplicated rows for people with two job codes, and the employer contribution columns shifted. He showed the reconciliation checklist he now runs before every upload. He said, "We went from trusting the export to auditing it line by line."

Mobile. Mei Lin said clinic staff complain that the mobile app forgets them. Nurses start a time off request, get signed out, and lose what they typed. She has asked clinic managers to tell staff to use a computer for requests for now.

Positives. They like the new document signing.

Health score reason: payroll export reliability. Rob said if it happens during year end he will push to move payroll integration off Pinmoor.

Follow-ups
  Ruth to attach Sunderby examples to the open export bug
  Ruth to send mobile logout workaround if one exists
  Next QBR in November
"""),

dict(path="sales-calls/2026-08-20-pellam-outdoor-payroll-bridge.md", raises=[], text="""Pellam Outdoor Supply | Payroll Bridge add-on scoping | 2026-08-20

Priya Venkataraman (AE), Marcus Bell (SE) with Tess Whitlow (Finance Manager, Pellam) and Owen Achebe (HR Lead, Pellam)

Pellam is on Core and Time Off today (290 employees, 6 stores and an e-commerce warehouse). They send payroll data to Ledgerline by exporting a report and re-keying it. They want Payroll Bridge from January 1.

Scoping questions we covered:
- Two pay groups (stores biweekly, HQ semi-monthly). Supported.
- Tips and commissions as separate earnings codes. Supported via custom earnings mapping.
- Multi-state tax (they have staff in three states). Supported, Marcus showed the state and local tax mapping.
- Parallel run for one pay period before cutover. Marcus recommended two.

Tess wanted to know how long implementation takes. Marcus said four to six weeks including the parallel runs.

Owen asked about time off data going to Ledgerline too, so that paid leave hours show on pay stubs. Yes, included in the bridge.

Next steps: quote for Payroll Bridge, implementation plan draft, intro to implementation team.
"""),

dict(path="sales-calls/2026-08-25-everleigh-staffing-renewal.md", raises=[("Everleigh Staffing", "T2"), ("Everleigh Staffing", "T5")], text="""# Everleigh Staffing, renewal prep call

2026-08-25. Theo (AM), Ruth (CSM). Everleigh: Hannah Voss (VP Operations), Luis Ferreira (HR Systems Admin).

Everleigh places temporary staff, so their internal headcount on Pinmoor swings between 1,200 and 1,900 depending on season. Renewal is Nov 15.

**Accruals.** Luis explained that a lot of their people are rehires who come back season after season. Pinmoor is accruing time off for rehires from the original hire date, so returning workers jump straight to the top accrual tier. He found about 140 employees with inflated balances. Hannah said this is a real cost for them, since balances pay out at separation in two of their states.

**Reports.** Luis also said the Insights placement and turnover reports do not finish when run for the whole company. He has been splitting them by branch. Hannah said the monthly board deck was late in July and August because of it.

**Other.** Mobile app works fine for them, they mainly use desktop. They asked about an API for their applicant tracking system; Ruth pointed them to the public API docs.

**Commercial.** Hannah hinted at asking for a credit for the accrual cleanup work. Theo to discuss internally.

Actions:
1. Ruth: escalate rehire accrual issue, get a fix date
2. Ruth: share tips for splitting large reports until performance fix ships
3. Theo: renewal proposal by Sept 15
"""),

dict(path="sales-calls/2026-08-27-lindqvist-architecture-checkin.md", raises=[("Lindqvist Architecture", "N:slack")], text="""Lindqvist Architecture: CSM check-in
27 August 2026
Ruth Okafor with Signe Lindqvist (Managing Partner) and Paul Oduya (Office Manager)

Small account, 64 employees, two studios. Core and Time Off.

Signe said they are happy and that Pinmoor mostly stays out of her way, which she meant as a compliment. Paul runs everything day to day.

Topics:
- Paul wants to connect Pinmoor to their project time tracking tool through the API so that approved time off blocks out project schedules. Ruth pointed him to the webhooks for approved requests.
- They are hiring 8 people this autumn and asked about offer letter templates. Ruth showed the template library.
- Signe asked if there is a Huddlepost integration for time off approvals, since the studio lives in Huddlepost. Ruth said it is on the ideas board and linked the forum thread.
- Paul mentioned the mobile app had a sign in bug a while ago but it has been fine for months.

No issues raised. Renewal is in March. Paul agreed to be a reference for small professional services firms.
"""),

dict(path="sales-calls/2026-09-01-marisol-home-care-escalation.md", raises=[("Marisol Home Care", "T3"), ("Marisol Home Care", "T1")], text="""# ESCALATION CALL: Marisol Home Care

**Date:** September 1, 2026
**Requested by:** customer (via CEO email to Sam)
**Pinmoor:** Sam Adeyemi, Ruth Okafor, Imogen Hart (Director of Support)
**Marisol:** Beatriz Salgado (CEO), Frank Obi (Director of HR and Payroll)

## Why the call

Beatriz emailed Sam directly on Aug 28 after a payroll run went wrong. Marisol employs about 540 home health aides who work across client homes.

## What the customer described

**Payroll export.** On the Aug 21 run the Payroll Bridge export included aides who had been terminated in July, with zero hours. Ledgerline generated zero dollar stubs for them and also mailed tax notices to former employees. On the same run, overtime approved in timesheets did not go through, so about 90 aides were underpaid until an off-cycle run on Aug 24. Frank: "Underpaying caregivers is not a software bug to them, it's rent."

**Mobile.** Aides clock in from client homes using Pinmoor Go on Android. The app drops them back to the login screen when the phone locks, so aides are clocking in late and the late clock-ins trigger attendance flags. Frank has turned attendance flags off as a workaround.

## What we committed to

- Imogen: root cause writeup on the Aug 21 export within 5 business days
- Sam: weekly update to Beatriz until both issues are fixed
- Ruth: help Frank with a pre-run export checklist

## Tone

Beatriz was calm but clear that they are evaluating alternatives for the payroll connection.
"""),

dict(path="sales-calls/2026-09-03-brightwater-charter-network.md", raises=[("Brightwater Charter Network", "T4"), ("Brightwater Charter Network", "T2")], text="""Brightwater Charter Network | Check-in | 3 Sep 2026
Attendees: Yolanda Price (HR Director), Martin Cho (Benefits and Leave Specialist); Ruth Okafor (Pinmoor)

Brightwater runs 11 charter schools, about 890 staff, most on 10 month contracts.

Reviews
Yolanda wanted to talk about the teacher evaluation cycle. They set it up in August with the wrong rating scale (4 levels instead of their 5 level rubric) and only noticed after launch. Cancelling to fix it wiped the self reflections teachers had already submitted during summer PD. Yolanda said about 120 teachers lost work. She was frustrated that nothing in setup warned her the scale could not be changed later. She also posted about it in the community.

Leave
Martin said paraprofessionals on reduced schedules accrue personal leave at the full time rate, and the 10 month staff are accruing through July and August when they should not be. He has been correcting balances at each pay period.

Other
- Asked for a way to bulk upload certifications. Ruth to share the import template.
- Renewal is next June, no concerns about renewing yet.

Actions
- Ruth to log both issues with product and send ticket numbers
- Martin to send the list of affected employees
"""),

dict(path="sales-calls/2026-09-08-canterfield-logistics-renewal.md", raises=[("Canterfield Logistics", "T1"), ("Canterfield Logistics", "T5")], text="""canterfield logistics renewal, 8 sept 2026

attendees: Theo Marchetti, Ruth Okafor (pinmoor); Darius Whelan (CFO), Nora Espinoza (HR manager), Kyle Brandt (payroll)

account: 1,050 employees, 8 cross dock facilities, renewal Oct 31

summary
Darius said up front that he is not signing a multi-year renewal this time. Two reasons.

1) the payroll export. Kyle has had the Tallybook sync sit in Pending for hours on two payroll days and on another day it failed outright with a mapping error. Kyle now exports a backup file by hand every payroll day just in case. Darius does not want finance depending on something that needs a backup plan.

2) reports. Nora runs a turnover and overtime report across all 8 facilities for Darius every Monday. It has timed out every week since late July. She runs it per facility and Darius gets it Tuesday or Wednesday now.

Nora said most facility staff clock in at kiosks, so the mobile app matters less for them.

Darius will do a 1 year renewal at current price if we can show a plan for both issues before Oct 15.

next steps
- Theo: 1 year renewal paperwork
- Ruth: pull engineering status for Tallybook sync and Insights performance
- Ruth: send Darius a status update every two weeks
"""),

dict(path="sales-calls/2026-09-09-orla-mae-cosmetics-evaluation.md", raises=[], text="""## Orla Mae Cosmetics: second call (evaluation)

Sept 9, 2026. Priya Venkataraman (AE), Marcus Bell (SE).
Orla Mae: Fiona Castellane (Head of People), Raj Dholakia (IT Manager).

Orla Mae is a 340 person beauty brand with a lab, a warehouse and a head office. They are choosing between Pinmoor and one other vendor. They currently use a patchwork of spreadsheets and a shared inbox.

This call was a deep dive for Raj:

- SSO with their identity provider and SCIM for provisioning. Marcus showed setup.
- Device requirements for warehouse staff who share Android handhelds. Marcus showed kiosk clock in and explained shared device mode for Pinmoor Go.
- Role based permissions so lab managers see only their teams.

Fiona asked about performance reviews for a team that has never done formal reviews. Marcus showed a lightweight template with three questions and recommended starting with a pilot cycle.

Raj asked for our uptime history for the last 12 months. Priya to send the status page summary.

Decision expected Sept 30. Fiona said Pinmoor is ahead on ease of use and the other vendor is ahead on price.
"""),

dict(path="sales-calls/2026-09-10-hollins-park-fitness-qbr.md", raises=[("Hollins Park Fitness", "T3")], text="""# Hollins Park Fitness QBR

- **Date:** 2026-09-10
- **CSM:** Ruth Okafor
- **Customer:** Kerry Lomax (People and Culture Lead), Simon Achterberg (Regional Operations)
- **Size:** 450 employees, 23 gyms. Most staff are part-time trainers and front desk.

### Adoption
Strong. 91% monthly active. Shift swaps via mobile are the most used feature.

### Issues raised
Simon: trainers get kicked out of Pinmoor Go when they switch between gym wifi and cellular data, which happens every time they walk onto the gym floor. They have to sign in with SSO again, and their identity provider sends an approval push each time. Some trainers have started ignoring the pushes, which his IT person says is a security problem of its own.

Kerry said she posted in the community forum about the mobile logout and saw a lot of other customers with the same problem.

Kerry also wants to reassign reviewers in their review cycle, she will post that separately.

### Next
- Ruth to share the mobile known issue page when published
- Simon to send an app version list from their MDM
"""),

dict(path="sales-calls/2026-09-11-moss-vane-legal-checkin.md", raises=[("Moss & Vane Legal", "T4"), ("pinmoor.example", "D2")], text="""Moss & Vane Legal, account check-in, 11 September 2026
Theo Marchetti (AM) with Harriet Moss (Director of Operations) and Keith Arundel (HR Coordinator)

Moss & Vane: 210 staff, 3 offices. Core, Time Off, Reviews.

Harriet: the associate review cycle launched last week. A partner wanted to add one question about pro bono hours and they were told by support that questions cannot be added once a cycle is live. Harriet said they will add it next year instead, but she does not understand why a question cannot be added to a cycle that has barely started.

Keith asked about bulk updating job titles after their restructure. Theo pointed him to the bulk edit import.

Harriet was otherwise positive. She said onboarding for the new Leeds Street office went smoothly.

Internal note (Theo): while showing Harriet the org chart during the call, I exported it to PDF and the names on the bottom row were cut off again. Harriet did not notice. Same thing I logged from our demo tenant last month.

Next: Theo to send Reviews roadmap summary if product can share one.
"""),
]


FORUM = [
dict(path="forum/integrations/4471-ledgerline-export-columns-moved.md", raises=[("Nettlefield Brewing", "T1"), ("Ostrander Plumbing", "T1"), ("Birchway Dental Group", "T1")], text="""# Ledgerline export columns moved after July update?

**Category:** Integrations
**Started by:** amara.k (Payroll and Benefits, Nettlefield Brewing)
**Posted:** July 8, 2026

Has anyone else had their Ledgerline export file change layout after the July release? Our employer retirement match is now sitting under the employee deduction column. I did not change the mapping. Our finance team spotted it before we submitted, thankfully.

Is there a changelog for the export format somewhere? I can't find one.

---

**dwight_ostrander** (Office Manager, Ostrander Plumbing) replied July 8, 2026

Same here. Two columns shifted one position to the right. I fixed it by remapping in Ledgerline for now.

---

**colleen.d** (People Ops, Birchway Dental) replied July 9, 2026

Seeing this too, our controller caught it on the 7/3 run. We have a ticket open. Would really like to know if a fix is coming before the next run.

---

**Jana (Pinmoor Support)** replied July 9, 2026

Thanks all, we are aware of an issue affecting the column order in some Payroll Bridge exports since release 3.14. Engineering is working on it. Please keep your tickets open so we can notify you directly.

---

**amara.k** replied July 22, 2026

Any update? The hotfix last week did not change anything for us.
"""),

dict(path="forum/time-off/4480-part-time-accruals-full-time-rate.md", raises=[("Galloway Print Works", "T2"), ("Carrow Street Bakeries", "T2"), ("Wrenfield Pediatrics", "T2")], text="""# Part-time accruals calculating at full time rate

**Category:** Time Off
**Started by:** lwalsh_galloway (HR Administrator, Galloway Print Works)
**Posted:** July 13, 2026

We have a Part Time PTO policy that accrues 0.025 hours per hour worked. Since the start of July it looks like everyone on that policy is accruing the full time amount per pay period instead. Our part-timers have about 40% more PTO than they should.

I checked the policy settings and nothing looks wrong. Is anyone else seeing this?

---

**mateo.carrow** (Owner, Carrow Street Bakeries) replied July 14, 2026

Yes. We only have 30 people and 22 of them are part time, so this is basically everyone. Found out when a baker requested a full week off that she should not have had yet.

---

**ines_wrenfield** (Practice Administrator, Wrenfield Pediatrics) replied July 15, 2026

We are seeing it for our 0.6 FTE nurses. The balances are prorated wrong, not just for hourly accrual. I put in a support ticket.

---

**lwalsh_galloway** replied July 28, 2026

Support says it is a known issue. Mine is still not fixed. I am tracking balances in a spreadsheet in the meantime.
"""),

dict(path="forum/general/4481-part-time-accruals-full-time-rate.md", raises=[("Galloway Print Works", "T2")], text="""# Part-time accruals calculating at full time rate

**Category:** General
**Started by:** lwalsh_galloway (HR Administrator, Galloway Print Works)
**Posted:** July 13, 2026

(Also posted in Time Off, posting here too since that category is quiet.)

We have a Part Time PTO policy that accrues 0.025 hours per hour worked. Since the start of July it looks like everyone on that policy is accruing the full time amount per pay period instead. Our part-timers have about 40% more PTO than they should.

I checked the policy settings and nothing looks wrong. Is anyone else seeing this?

---

No replies yet.
"""),

dict(path="forum/mobile/4502-pinmoor-go-logging-out.md", raises=[("Bramblecote Nurseries", "T3"), ("Orwell Bay Seafoods", "T3"), ("Hollins Park Fitness", "T3")], text="""# Pinmoor Go logging out every time the app closes

**Category:** Mobile
**Started by:** greta.bramblecote (HR and Payroll, Bramblecote Nurseries)
**Posted:** July 20, 2026

Since updating to app version 5.2 our growers have to sign in every time they open Pinmoor Go. We use SSO. On 5.1 people stayed signed in for weeks. It is making clock in at 6am miserable.

Anyone found a setting for this?

---

**tobias.w** (Operations Coordinator, Orwell Bay Seafoods) replied July 20, 2026

Same issue. Our processing floor staff lock their phones in lockers during shifts, and every time they come back the app wants a full sign in. We have had people miss clock in because of it.

---

**psignal** (Office Manager, Lindqvist Architecture) replied July 21, 2026

We saw something similar back in March on the old app and it went away after the 5.0 update. Haven't seen it since, so maybe this is a new one.

---

**kerry_hpf** (People and Culture, Hollins Park Fitness) replied August 30, 2026

Still happening for us in late August on 5.2.1. Our trainers get logged out every time they move between wifi and cellular. Please fix this.

---

**greta.bramblecote** replied September 2, 2026

Bumping. Support told me it is with engineering.
"""),

dict(path="forum/general/4503-pinmoor-go-logging-out.md", raises=[("Bramblecote Nurseries", "T3")], text="""# Pinmoor Go logging out every time the app closes

**Category:** General
**Started by:** greta.bramblecote (HR and Payroll, Bramblecote Nurseries)
**Posted:** July 20, 2026

Since updating to app version 5.2 our growers have to sign in every time they open Pinmoor Go. We use SSO. On 5.1 people stayed signed in for weeks. It is making clock in at 6am miserable.

Anyone found a setting for this? Cross-posting from Mobile.

---

**Jana (Pinmoor Support)** replied July 21, 2026

Hi Greta, let's keep the conversation in the Mobile thread so everyone sees updates in one place. Locking this one.

*This thread has been locked.*
"""),

dict(path="forum/performance/4510-edit-review-questions-after-launch.md", raises=[("Tamsin Labs", "T4"), ("Aldercrest Schools Foundation", "T4")], text="""# Edit review questions after launch?

**Category:** Performance and Reviews
**Started by:** ffrost_tamsin (People Lead, Tamsin Labs)
**Posted:** July 27, 2026

We launched our mid-year cycle on Monday and a manager pointed out that question 4 asks about client work, which half our team does not do. The template now says Locked (in use). Do I really have to cancel the whole cycle to change one question? We have 85 people in it.

---

**r.okonkwo** (HR Manager, Aldercrest Schools Foundation) replied July 28, 2026

As far as I can tell, yes. We hit this in our spring cycle and again this summer. What we ended up doing this time was sending everyone an email telling them to skip the question. It would help a lot if you could at least edit wording without changing the structure.

---

**ffrost_tamsin** replied July 28, 2026

That is what I was afraid of. Added a vote on the ideas board.
"""),

dict(path="forum/reporting/4519-insights-report-timeouts.md", raises=[("Stonewick Veterinary", "T5"), ("Ivel River Credit Services", "T5")], text="""# Insights report timeouts on large datasets

**Category:** Reporting and Insights
**Started by:** hal.stonewick (HRIS, Stonewick Veterinary)
**Posted:** August 3, 2026

We have about 610 employees and three years of history. Custom reports that include terminated employees now spin for a few minutes and then show Request timed out. Filtering to active employees only works but that is not the report I need for our attrition analysis.

Has something changed? These ran in under 30 seconds in the spring.

---

**beth.ivelriver** (People Analytics, Ivel River Credit Services) replied August 4, 2026

Same thing for us since late July. Our scheduled monthly headcount report showed up in our inboxes with no rows, which I only noticed because the CFO asked why the chart was empty.

---

**hal.stonewick** replied August 19, 2026

Still timing out. Support gave me a workaround to split by year, which works but is a pain.
"""),

dict(path="forum/ideas/4523-huddlepost-integration-time-off-approvals.md", raises=[("Harlow & Pike Builders", "N:slack"), ("Lindqvist Architecture", "N:slack")], text="""# Huddlepost integration for time off approvals

**Category:** Ideas
**Started by:** jpike_builds (Office Manager, Harlow & Pike Builders)
**Posted:** August 5, 2026

It would save our site supervisors a lot of time if they could approve time off requests from a Huddlepost message instead of opening Pinmoor. Some of our other tools already do this. Upvote if you want it too.

---

**psignal** (Office Manager, Lindqvist Architecture) replied August 6, 2026

Yes please. Our studio lives in Huddlepost and approvals sit for days because nobody opens email.

---

**Owen (Pinmoor Product)** replied August 12, 2026

Thanks for the idea. We are collecting interest and will share if this makes it onto the roadmap.
"""),

dict(path="forum/integrations/4524-huddlepost-integration-time-off-approvals.md", raises=[("Harlow & Pike Builders", "N:slack")], text="""# Huddlepost integration for time off approvals

**Category:** Integrations
**Started by:** jpike_builds (Office Manager, Harlow & Pike Builders)
**Posted:** August 5, 2026

Posting here as well as in Ideas since it is an integration.

It would save our site supervisors a lot of time if they could approve time off requests from a Huddlepost message instead of opening Pinmoor. Some of our other tools already do this. Upvote if you want it too.

---

No replies.
"""),

dict(path="forum/general/4530-org-chart-pdf-cuts-off-names.md", raises=[("pinmoor.example", "D2")], text="""# Org chart PDF export cuts off names on the bottom row

**Category:** General
**Started by:** dana.whitcombe (Pinmoor team)
**Posted:** August 7, 2026

Posting this so it is findable. When exporting the org chart to PDF for any org with more than 4 levels, the names on the bottom row are cut off at the page edge. Reproduced in two different browsers on the Alderpoint Sample Co tenant.

---

**leo.fairweather** (Pinmoor team) replied August 7, 2026

Same on my demo tenant. Also happens when the chart is exported in landscape. Logged internally.

---

**dana.whitcombe** replied August 25, 2026

Still reproducible on the latest build.
"""),

dict(path="forum/time-off/4533-carryover-cap-anniversary.md", raises=[("Moss & Vane Legal", "T2"), ("Kittering Freight", "T2")], text="""# Carryover didn't respect our cap on anniversary dates

**Category:** Time Off
**Started by:** keith.arundel (HR Coordinator, Moss & Vane Legal)
**Posted:** August 10, 2026

Our PTO policy has a 40 hour carryover cap on each employee's work anniversary. Three associates with August anniversaries carried over their full balances, one of them 126 hours. The cap is set correctly in the policy.

Is this a known bug or am I missing a setting?

---

**marlon.kf** (Ops Manager, Kittering Freight) replied August 11, 2026

Not a setting as far as I know. Our dispatch staff with anniversaries in July kept everything too. We fixed them by manual adjustment.

---

**keith.arundel** replied August 12, 2026

Thanks. I will do the same and put in a ticket.

---

**keith.arundel** replied September 12, 2026

Update for anyone searching: support told me a fix went out on Sept 3 and our September anniversaries capped correctly. The August ones still had to be fixed by hand.
"""),

dict(path="forum/general/4538-onboarding-checklists-remote-hires.txt", raises=[], text="""Thread: How do you handle onboarding checklists for remote hires?
Category: General
Original post by ffrost_tamsin (People Lead, Tamsin Labs), August 12, 2026

We are hiring our first fully remote team (6 people in three countries) and I want an onboarding checklist that does not assume anyone walks into an office. What do you include? Laptop shipping, accounts, buddy assignment... what else?

Reply from lwalsh_galloway (HR Administrator, Galloway Print Works), August 12, 2026
We have a separate checklist template for remote. The main additions: shipping confirmation task for IT, a video welcome from their manager in week 1, and a check-in task on day 30 and day 60. Pinmoor lets you assign each task to a different owner which helps a lot.

Reply from ffrost_tamsin, August 13, 2026
The day 30 and 60 check-ins are a good idea. Do you make those tasks due relative to start date?

Reply from lwalsh_galloway, August 13, 2026
Yes, relative due dates. Set them to 30 and 60 days after start date in the template.

Reply from ffrost_tamsin, August 14, 2026
Perfect, thank you.
"""),

dict(path="forum/payroll-bridge/4541-tallybook-mapping-error-412.md", raises=[("Everleigh Staffing", "T1"), ("Harrowgate Tile Supply", "T1")], text="""# Tallybook sync: mapping error 412

**Category:** Payroll Bridge
**Started by:** luis.f (HR Systems, Everleigh Staffing)
**Posted:** August 14, 2026

Our Tallybook sync failed today with mapping error 412. The only change since last pay period is that we added a new earnings code for referral bonuses, but it is mapped. Worked fine through June.

Has anyone got past this without exporting manually?

---

**nhayes_harrowgate** (Controller, Harrowgate Tile Supply) replied August 14, 2026

We got the same 412 on our last two runs with no earnings code changes at all. Our workaround is to download the file and upload it into Tallybook by hand. It works but defeats the purpose.

---

**luis.f** replied August 15, 2026

Thanks. Support says it is tied to the July release and not to our mapping. Manual upload for now.
"""),

dict(path="forum/mobile/4546-face-id-not-remembered-ios.md", raises=[("Radleigh Senior Living", "T3"), ("Westmere Retail Group", "T3")], text="""# face unlock sign in not remembered on iOS

**Category:** Mobile
**Started by:** kenji.albright (HR Systems, Radleigh Senior Living)
**Posted:** August 17, 2026

After each Pinmoor Go update, and now sometimes just overnight, iOS users lose face unlock sign in and have to type their full password. Our caregivers mostly do not remember their passwords because they have used face unlock for a year. Result is a lot of calls to HR.

---

**ivo_westmere** (Workforce Analytics, Westmere Retail Group) replied August 18, 2026

Store associates are hitting this too. And our SSO users get sent back to the login page every few minutes, which I think is related.

---

**Jana (Pinmoor Support)** replied August 19, 2026

Thanks both. This is being tracked together with the session issues reported in the Pinmoor Go logging out thread.
"""),

dict(path="forum/announcements/4550-scheduled-maintenance-aug-23.md", raises=[], text="""# Scheduled maintenance: Sunday, August 23

**Category:** Announcements
**Posted by:** Pinmoor Status Team
**Posted:** August 18, 2026

Pinmoor will be unavailable for scheduled database maintenance on Sunday, August 23 from 02:00 to 04:00 US Eastern. The mobile app, web app and public API will all be affected. Kiosk clock ins taken during the window will queue and sync when service returns.

No action is needed from admins.

---

**jpike_builds** (Office Manager, Harlow & Pike Builders) replied August 18, 2026

Thanks for the notice. Will kiosk clock ins keep the original timestamp when they sync?

---

**Pinmoor Status Team** replied August 18, 2026

Yes, queued punches keep the time they were recorded on the device.

---

**Pinmoor Status Team** replied August 23, 2026

Maintenance completed at 03:12 US Eastern. All services are available.
"""),

dict(path="forum/performance/4553-lost-self-reviews-after-cancel.md", raises=[("Brightwater Charter Network", "T4")], text="""# Lost all submitted self reviews after cancelling a cycle

**Category:** Performance and Reviews
**Started by:** yprice_bcn (HR Director, Brightwater Charter Network)
**Posted:** August 24, 2026

We set up our teacher evaluation cycle with a 4 level scale by mistake. The setup screens never said the rating scale would be locked once the cycle launched. When we cancelled to fix it, every self reflection teachers had already written was gone. About 120 teachers.

Can support restore responses from a cancelled cycle? And can someone please add a warning before launch?

---

**Owen (Pinmoor Product)** replied August 26, 2026

Hi Yolanda, I'm sorry, cancelled cycles don't keep draft or submitted responses today. We have heard this from several customers this quarter and are looking at letting admins edit a live cycle. I'll follow up directly about recovery.
"""),

dict(path="forum/tips/4557-workaround-remap-export-columns.md", raises=[("Ostrander Plumbing", "T1"), ("Nettlefield Brewing", "T1")], text="""# Tip: workaround for the shifted Payroll Bridge export columns

**Category:** Tips and Tricks
**Started by:** dwight_ostrander (Office Manager, Ostrander Plumbing)
**Posted:** August 27, 2026

Since the export column problem is still not fixed for us, here is what I have been doing so payroll goes out on time:

1. Run the Payroll Bridge export as usual.
2. Open the CSV and check that the header row lists Employer Match right after Gross Pay. If it doesn't, the file is shifted.
3. In Ledgerline, use the saved import map I called Pinmoor shifted, which reads the columns one position to the right.
4. Spot check three employees against their pay statements before approving.

This is annoying but it has kept us from paying anyone wrong. When Pinmoor fixes it you will need to switch back to the normal map.

---

**amara.k** (Payroll and Benefits, Nettlefield Brewing) replied August 28, 2026

Thank you for writing this up. We are doing almost the same thing, plus checking the total against the summary screen, because ours has not matched on two runs.
"""),

dict(path="forum/reporting/4561-headcount-report-blank-company-wide.md", raises=[("Sunderby Clinics", "T5"), ("Copperlane Hotels", "T5")], text="""# Headcount over time report is blank for company-wide view

**Category:** Reporting and Insights
**Started by:** meilin.f (HR Operations, Sunderby Clinics)
**Posted:** August 29, 2026

The Headcount by department over time report shows nothing when I select All locations. If I pick one clinic it loads. We are only 760 people so I did not expect size to be the issue. Browser console shows a 504.

---

**esther.lund** (HRIS Analyst, Copperlane Hotels) replied August 30, 2026

Welcome to the club. We have 2,300 employees and nothing company-wide has loaded since July. I run 19 reports, one per property, and combine them.
"""),

dict(path="forum/general/4565-benefits-document-upload-fails.md", raises=[("Tollbridge Ceramics", "D1")], text="""# Benefits enrollment document upload keeps failing

**Category:** General
**Started by:** gwen.abernathy (HR Manager, Tollbridge Ceramics)
**Posted:** August 31, 2026

Employees trying to upload dependent verification documents during benefits enrollment get Upload failed, try again. It happens with PDFs and phone photos. We have filed a lot of tickets about this. Is anyone else seeing it or is it just our account?

---

**gwen.abernathy** replied September 4, 2026

Nobody? Support says they can only reproduce it on our tenant. Still broken.
"""),

dict(path="forum/time-off/4568-holiday-deducted-from-pto.md", raises=[("Pellam Outdoor Supply", "T2")], text="""# July 4 holiday deducted from PTO for part-time staff

**Category:** Time Off
**Started by:** owen.a (HR Lead, Pellam Outdoor Supply)
**Posted:** September 1, 2026

Our part-time store staff had 8 hours taken out of their PTO balance for July 4, even though the store was closed and the holiday calendar is set up. Full time staff were fine. I noticed it when doing a balance review last week.

Is the holiday calendar supposed to apply to part-time policies? The balances for our part-timers have been off in other ways too this summer so I'm not sure what to trust.
"""),

dict(path="forum/ideas/4570-dark-mode.md", raises=[("Orwell Bay Seafoods", "N:darkmode"), ("Stonewick Veterinary", "N:darkmode")], text="""# Dark mode for the web app

**Category:** Ideas
**Started by:** tobias.w (Operations Coordinator, Orwell Bay Seafoods)
**Posted:** September 2, 2026

Our night shift supervisors use Pinmoor on a dim processing floor. A dark theme would be easier on the eyes. The mobile app follows the phone setting, so hopefully this is not a huge change for web.

---

**hal.stonewick** (HRIS, Stonewick Veterinary) replied September 3, 2026

+1, our overnight emergency clinic staff would like this too.
"""),

dict(path="forum/mobile/4572-android-returns-to-login-when-locked.md", raises=[("Marisol Home Care", "T3"), ("Canterfield Logistics", "T3")], text="""# Android: app returns to login whenever the phone locks

**Category:** Mobile
**Started by:** frank.obi (HR and Payroll, Marisol Home Care)
**Posted:** September 3, 2026

Our aides use Android phones to clock in at client homes. Every time the screen locks, Pinmoor Go goes back to the login screen. If an aide unlocks their phone to clock in they have to sign in again first, and that is making clock ins late.

We are on app version 5.2.1. Phone models vary.

---

**kbrandt_cfld** (Payroll, Canterfield Logistics) replied September 4, 2026

Our yard supervisors use Android handhelds and see this too. They gave up and use the kiosk instead, but they would rather use the app.

---

**frank.obi** replied September 9, 2026

Any word from Pinmoor on this one?
"""),

dict(path="forum/integrations/4575-is-payroll-export-fixed-315.md", raises=[("Copperlane Hotels", "T1"), ("Galloway Print Works", "T1")], text="""# Is the payroll export fixed in 3.15?

**Category:** Integrations
**Started by:** dfarrant (VP People, Copperlane Hotels)
**Posted:** September 7, 2026

Release notes for 3.15 say Improvements to Payroll Bridge reliability. Can anyone confirm whether the export column problem and the duplicate rows problem are actually fixed? Our Sept 4 file still had duplicate rows for staff who work in two departments.

---

**lwalsh_galloway** (HR Administrator, Galloway Print Works) replied September 8, 2026

Not fixed for us. Our Sept 5 Ledgerline file had the bonus earnings under regular pay again, so they were taxed at the wrong rate.

---

**dfarrant** replied September 9, 2026

Thanks. Guess we keep checking by hand then.
"""),

dict(path="forum/performance/4579-reassign-reviewer-manager-left.md", raises=[("Hollins Park Fitness", "T4")], text="""# Reassign reviewer after a manager leaves mid-cycle

**Category:** Performance and Reviews
**Started by:** kerry_hpf (People and Culture, Hollins Park Fitness)
**Posted:** September 11, 2026

One of our regional managers left last week, halfway through our review cycle. His 14 direct reports now have a reviewer who no longer exists, and I cannot find any way to reassign them to the new regional manager without cancelling and relaunching the whole cycle for 450 people.

Am I missing something? This seems like a basic need.
"""),

dict(path="forum/general/4582-year-end-w2-prep-checklist.txt", raises=[], text="""Thread: Year-end tax form prep checklist, what is on yours?
Category: General
Original post by r.okonkwo (HR Manager, Aldercrest Schools Foundation), September 12, 2026

It is only September but I like to start early. Our list so far:
- Confirm every employee's mailing address and consent to electronic year-end tax forms
- Check that terminated employees have a forwarding address
- Reconcile benefits deductions with the payroll provider in November
- Remind staff to update withholding before the last pay period

What else do people add?

Reply from beth.ivelriver (People Analytics, Ivel River Credit Services), September 12, 2026
We send a reminder in October to anyone who moved during the year, and we run a report of employees whose state of residence differs from their work state. Catches multi-state tax surprises.

Reply from r.okonkwo, September 13, 2026
Good one, adding that.
"""),
]
