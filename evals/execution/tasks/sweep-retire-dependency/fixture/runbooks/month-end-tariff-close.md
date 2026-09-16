# Month-end tariff close

**Who runs this:** Finance Operations analyst on the close rota (currently Ulla
Berg and Petter Gran, alternating). Engineering support: Finance Engineering.
**When:** Business day 2 of each month, before 11:00 Stockholm time.

This is a manual procedure. It reconciles the tariffs we actually invoiced
against the tariff tables the quotes were computed from, so that the
controller can sign off revenue.

## Before you start

- You need VPN and your personal client certificate (`~/.tw/certs/you.pem`).
- You need read access to the `finance_close` schema.
- Check #finance-close for any notes from the previous analyst.

## Steps

1. Create the working folder:

       mkdir -p ~/close/$(date +%Y-%m) && cd ~/close/$(date +%Y-%m)

2. Export last month's invoiced lines from the warehouse (saved query
   "close / invoiced lines", run it with the period parameter) and download as
   `invoiced.csv`.

3. Pull the tariff table snapshot from tariff-service:

       curl -s --cert ~/.tw/certs/you.pem \
         "http://tariff-service.finance.svc:8080/api/tariffs?as_of=$PERIOD_END" \
         > tariffs_service.json

4. Pull the tariff inputs the quote engine used during the month:

       curl -s --cert ~/.tw/certs/you.pem \
         "https://routecalc-v1.core.tesselwick.internal/tariffs/export?period=$PERIOD" \
         > tariffs_quote_engine.json

5. Run the comparison notebook `close/tariff_diff.ipynb` with both JSON files
   and `invoiced.csv`. It produces `diff.xlsx`.

6. Anything over 250 EUR absolute difference per lane goes on the exceptions
   tab with a short explanation. Typical explanations: mid-month rate card
   import, manual override by a key account manager, fuel surcharge step.

7. Post `diff.xlsx` in #finance-close and tag the controller.

## If something goes wrong

- Step 3 returns 403: your certificate expired. Renew through the IT portal.
- Step 4 times out: try again after 10 minutes, the export is slow on the
  first business days. If it still fails, ask Finance Engineering.
- The notebook complains about duplicate lanes: a rate card was imported twice.
  Tell procurement, then deduplicate by `import_id` keeping the latest.
