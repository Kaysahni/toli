# Decommission tracker

Kept by Platform (Arvid Sundqvist). Anything being switched off goes here so
that nobody spends effort migrating something that is about to disappear.

| Item | Type | Owner | Switch-off date | Status | Notes |
|---|---|---|---|---|---|
| oldwms sync jobs | batch | Warehouse Tech | 2025-11-20 | done | WMS 6 cutover |
| axle-check sidecar | sidecar | Warehouse Tech | 2026-02-01 | done | moved in-process in pallet-optimizer 1.40 |
| legacy-quote-portal | web app | Web Team | 2026-09-30 | on track | Remaining 7 accounts notified 2026-08-15; compute and DNS go on the switch-off date. Do not migrate. |
| fax-gateway | service | Customer Comms | 2026-12-31 | planning | Two customers still send faxed PODs |
| reporting-01 host | VM | Data Platform | 2027-Q1 | planning | Crons move to the workflow scheduler first |

## Rules

- An item is "done" only when compute, DNS and secrets are all gone.
- If you find a dependency on something in this table, post in #platform
  rather than fixing it yourself.
