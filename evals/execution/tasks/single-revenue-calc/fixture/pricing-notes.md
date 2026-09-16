# Pricing and reporting notes

Owner: Finance (Teodora Blix). Last edited 2026-07-08 after the Q2 close.

These notes sit next to the monthly invoice export so that anyone pulling numbers
from it gets the same result as the finance team. If something here disagrees
with a spreadsheet you were sent, this file wins. Ask in #finance-questions before
you improvise.

## Price lists

Oxtail Supply publishes three price lists: Trade (default for new accounts),
Hospitality Partner, and Institutional (schools, hospitals, care homes). The list
an account is on lives in the CRM, not in the export. Catalogue prices for 2026
were set in January and have not changed mid year, apart from the stainless steel
surcharge on gastronorm pans that ran from 9 February to 16 March and has ended.

## Discount rules

- Volume: orders over 5,000 (in the order currency) get 4% off the goods total.
  Orders over 12,000 get 7%. Shipping is never discounted.
- Loyalty: accounts that have bought from us for more than five full years get
  an extra 2%, applied after the volume discount.
- Institutional list customers do not stack loyalty on top of their list price.
- Trade show sample accounts pay list price with no discount.
- Rebates agreed in a master agreement are issued as credit notes during the quarter,
  not as a discount on the invoice.

Amounts in the invoice export are already net of all discounts, so do not apply them again.
They are also exclusive of VAT and sales tax.

## Payment terms

Net 30 unless the customer record says otherwise. Late payment interest is not
booked as revenue and does not appear in the export.

## Reading the invoice export

The export (`invoices.csv`) has one row per document. `type` is either `invoice`
or `credit_note`. Credit notes are exported as positive amounts. Subtract them.
A credit note belongs to the quarter of its own date, not the date of the invoice it corrects.

Amounts are in the document currency shown in the `currency` column. An account
can change billing currency, so check each row rather than assuming.

The region column in the invoice export is stamped when the account is created and is not updated if a customer moves.
For any regional split, customers.csv is the master record for region.

We report on calendar quarters. Q2 is 1 April to 30 June inclusive. The export
file is pulled with a few days of margin either side, so trim it to the quarter.

## Exchange rates

Management reporting uses one fixed rate per currency per quarter, set by the
treasury committee on the first business day of the quarter. Convert each
invoice or credit note line at the quarter rate, round the converted line to the
cent, then add up. Do not use daily or bank rates for reporting.

Q2 2026 rates (USD per 1 unit of currency):

| Currency | Rate |
|---|---|
| EUR | 1.0850 |
| GBP | 1.2700 |
| SEK | 0.0952 |
| USD | 1.0000 |

Q1 2026 rates (closed, kept for reference only):

| Currency | Rate |
|---|---|
| EUR | 1.0410 |
| GBP | 1.2480 |
| SEK | 0.0921 |
| USD | 1.0000 |

Q3 2026 rates will be added here once treasury confirms them.

## Regions

EU, UK, NA, LATAM and APAC. UK is its own region and is not part of EU for any
reporting. Region follows where the contracting entity sits, not the billing
currency, so an EU account billed in dollars is still EU.

## Changelog

- 2026-07-08: added Q2 close reminders, clarified that credit notes follow their own date.
- 2026-04-01: added Q2 rates.
- 2026-03-17: removed the pan surcharge note from the price list section.
- 2026-01-05: Q1 rates, 2026 discount tiers.
