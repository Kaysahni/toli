# Personal Lines Renewal Offer Schedule

**Owner:** Policy Operations (Marguerite Delacroix-Ansah)
**System:** PolicyCenter renewal batch, print feed to Corvid Print & Mail
**Last updated:** 2026-01-20

## Timeline for a standard renewal (days before renewal effective date)

| Day | What happens | Who |
| --- | --- | --- |
| 75 | Renewal record created and rated | PolicyCenter batch |
| 70 | Renewal rules run; flagged policies routed to Underwriting work queue | PolicyCenter batch |
| 70 to 50 | Underwriting reviews flagged policies; decides renew, renew with conditions, or nonrenew | Underwriting Services |
| 60 | Mortgagee billing file sent to escrow servicers | Billing batch |
| 50 | Nonrenewal cutoff: any nonrenewal decision must be entered by this day | Underwriting Services |
| 35 | Renewal offer released: Declarations, cover letter, bill, and any conditional letters | PolicyCenter batch to print feed |
| 33 | Corvid prints and mails (2 business day SLA) | Corvid |
| 20 | Reminder email to eDelivery customers who have not opened their renewal | Marketing automation |
| 0 | Renewal effective | |

Renewal offers are released by the batch job 35 days ahead of the renewal effective date. The release date is a single parameter (RENEWAL_OFFER_LEAD_DAYS) in the PolicyCenter batch configuration.

## Conditional letters in the renewal offer

These letters are generated inside the renewal offer and are printed and mailed in the same envelope. None of them are mailed on their own schedule.

- **MC-RN-14 Notice of Renewal Premium Change.** Generated when the premium trigger rule is met. It is released with the renewal offer on day 35 and mailed in the same envelope.
- **Roof surcharge explanation.** Generated when a roof age surcharge is added at renewal.
- **Inspection recommendations reminder.** Generated when an inspection recommendation remains open.

## Nonrenewals

Nonrenewal notices (MC-NR-02) are not part of the renewal offer. Underwriting Services generates them on demand once the nonrenewal decision is entered, and Corvid mails them within 2 business days.

## Exceptions

- Premier policies with an open inspection are held until day 45 for underwriter review.
- If the print feed fails, Policy Operations reruns the day's batch the next morning. Two consecutive failures escalate to the IT on call.

## Change log

- 2026-01-20: Day 20 reminder email added.
- 2025-06-02: Offer release moved from day 30 to day 35 after print vendor delays in spring 2025.
- 2024-10-15: Nonrenewal cutoff moved from day 40 to day 50 to give underwriters more review time.
