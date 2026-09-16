# pipelines

Data Platform owns the warehouse (`warehouse.data.tesselwick.internal`) and the
jobs in this folder. Business teams own the logic of their own reports.

- `sql/` holds scheduled warehouse queries. They are run by `dwh-run` from the
  crontab on reporting-01 (see `cron/`). Output goes to a `reports.*` table and
  optionally to a Google Sheet.
- The `.md` files describe larger pipelines that run in the workflow scheduler.
- `warehouse-sources.md` lists where each source schema comes from.

Conventions:

- Every SQL file starts with a header comment: owner, consumers, schedule.
- Never `SELECT *` from a source schema. Columns get added without warning.
- Dates are UTC unless the column name ends in `_local`.
