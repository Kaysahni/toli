"""Generate the single-revenue-calc fixture and compute the answer key.

Run: python3 build/generate.py  (from the task directory or anywhere)
Writes fixture/invoices.csv, fixture/customers.csv, fixture/pricing-notes.md
and checklist.json. Deterministic (fixed seed).
"""
import csv
import json
import random
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

SEED = 20260416
ROOT = Path(__file__).resolve().parent.parent
FIX = ROOT / "fixture"

Q2_START, Q2_END = date(2026, 4, 1), date(2026, 6, 30)
Q2_RATES = {"USD": Decimal("1"), "EUR": Decimal("1.0850"), "GBP": Decimal("1.2700"), "SEK": Decimal("0.0952")}
Q1_RATES = {"USD": Decimal("1"), "EUR": Decimal("1.0410"), "GBP": Decimal("1.2480"), "SEK": Decimal("0.0921")}
CENT = Decimal("0.01")

MOVED_ID = "C-1027"

# id, name, region (master), country, billing currency, account manager, since, notes
CUSTOMERS = [
    ("C-1001", "Brasserie Lune Verte", "EU", "FR", "EUR", "Odile Marchetti", "2019-05-14", ""),
    ("C-1002", "Kochwerk Haldenberg GmbH", "EU", "DE", "EUR", "Odile Marchetti", "2020-02-03", ""),
    ("C-1003", "Pantry & Pike Restaurants", "NA", "US", "USD", "Deshawn Albright", "2018-11-20", ""),
    ("C-1004", "Molinar Hospitality Group", "NA", "US", "USD", "Deshawn Albright", "2021-07-09", ""),
    ("C-1005", "Fjordkök Grossist AB", "EU", "SE", "SEK", "Ingrid Solvang", "2022-03-28", ""),
    ("C-1006", "Tallow Street Canteens Ltd", "UK", "GB", "GBP", "Priya Wexford", "2020-09-15", ""),
    ("C-1007", "Casa Ortelia Catering", "EU", "ES", "EUR", "Odile Marchetti", "2023-01-10", ""),
    ("C-1008", "Bluegum Kitchen Co", "APAC", "AU", "USD", "Marcus Teal", "2021-04-22", "Invoiced in USD per master agreement"),
    ("C-1009", "Vandermolen Horeca BV", "EU", "NL", "EUR", "Ingrid Solvang", "2019-08-01", ""),
    ("C-1010", "Northgale Bakeries", "NA", "CA", "USD", "Deshawn Albright", "2022-06-17", ""),
    ("C-1011", "Osteria Pellandi Srl", "EU", "IT", "EUR", "Odile Marchetti", "2024-02-05", ""),
    ("C-1012", "Harbour Lane Hotels plc", "UK", "GB", "GBP", "Priya Wexford", "2018-03-12", ""),
    ("C-1013", "Skarvik Storkök AB", "EU", "SE", "SEK", "Ingrid Solvang", "2023-10-30", ""),
    ("C-1014", "Redfern Campus Dining", "NA", "US", "USD", "Deshawn Albright", "2020-01-27", "Net 45 terms"),
    ("C-1015", "Maison Béraud Traiteur", "EU", "BE", "EUR", "Odile Marchetti", "2021-11-08", ""),
    ("C-1016", "Kinsale Quay Kitchens", "EU", "IE", "GBP", "Priya Wexford", "2022-08-19", "Bills in GBP at customer request"),
    ("C-1017", "Sakuragi Food Service", "APAC", "JP", "USD", "Marcus Teal", "2023-05-02", ""),
    ("C-1018", "Copper Kettle Diners", "NA", "US", "USD", "Luis Ferrante", "2019-12-11", ""),
    ("C-1019", "Grünhof Kantinen AG", "EU", "AT", "EUR", "Ingrid Solvang", "2020-04-06", ""),
    ("C-1020", "Wexmoor School Meals Trust", "UK", "GB", "GBP", "Priya Wexford", "2021-02-24", ""),
    ("C-1021", "Adelmar Cruise Provisioning", "EU", "PT", "USD", "Odile Marchetti", "2024-06-13", "USD pricing agreed for fleet contract"),
    ("C-1022", "Prairie Oak Steakhouses", "NA", "US", "USD", "Luis Ferrante", "2018-07-30", ""),
    ("C-1023", "Lindqvist Bageri", "EU", "DK", "EUR", "Ingrid Solvang", "2025-01-15", ""),
    ("C-1024", "Pacifica Resort Holdings", "LATAM", "MX", "USD", "Luis Ferrante", "2022-09-05", ""),
    ("C-1025", "Aldersgate Pub Company", "UK", "GB", "GBP", "Priya Wexford", "2019-03-18", ""),
    ("C-1026", "Tamsin Row Patisserie", "NA", "US", "USD", "Deshawn Albright", "2025-03-03", ""),
    (MOVED_ID, "Harrowgate Catering Group", "EU", "NL", "EUR",
     "Ingrid Solvang", "2021-10-04",
     "Region changed from UK to EU on 2026-04-01 when the account moved to the Netherlands subsidiary; billing currency changed from GBP to EUR on the same date"),
    ("C-1028", "Kowhai Bay Hospitality", "APAC", "NZ", "USD", "Marcus Teal", "2024-08-26", ""),
    ("C-1029", "Rialto Verde Pizzerie", "EU", "IT", "EUR", "Odile Marchetti", "2023-03-21", ""),
    ("C-1030", "Stonebridge Care Homes", "UK", "GB", "GBP", "Priya Wexford", "2020-10-12", ""),
    ("C-1031", "Big Sky Commissary", "NA", "US", "USD", "Luis Ferrante", "2021-05-06", ""),
    ("C-1032", "Hautvilliers Hôtellerie", "EU", "FR", "EUR", "Odile Marchetti", "2022-12-01", ""),
    ("C-1033", "Andes Norte Cocinas", "LATAM", "CL", "USD", "Luis Ferrante", "2025-05-19", ""),
    ("C-1034", "Beacon Hill Test Kitchen", "NA", "US", "USD", "Deshawn Albright", "2024-11-11", "Trade show sample account, low volume"),
]

EARLY_OUT = [date(2026, 3, 27), date(2026, 3, 30), date(2026, 3, 31)]
LATE_OUT = [date(2026, 7, 1), date(2026, 7, 2), date(2026, 7, 6)]

REFS_INV = ["PO {n}", "Order {n}", "PO-{n}", "Web order {n}", "Standing order", "", "", "Replenishment {n}"]
CREDIT_REASONS = ["Damaged on delivery", "Returned: wrong size pans", "Short shipment", "Price adjustment per rebate",
                  "Duplicate billing", "Returned unopened", "Goodwill credit"]


def money(x):
    return Decimal(x).quantize(CENT, ROUND_HALF_UP)


def region_on_export(cust):
    # Export stamps region at account creation and never updates it.
    return "UK" if cust[0] == MOVED_ID else cust[2]


def build_rows(rng):
    by_id = {c[0]: c for c in CUSTOMERS}
    days = (Q2_END - Q2_START).days
    rows = []

    def add(d, cust, typ, amount, ref, currency=None):
        currency = currency or cust[4]
        if cust[0] == MOVED_ID and d < Q2_START:
            currency = "GBP"
        rows.append({"date": d, "customer_id": cust[0], "customer_name": cust[1],
                     "region": region_on_export(cust), "currency": currency,
                     "amount": money(amount), "type": typ, "reference": ref})

    weights = [3 if c[0] in ("C-1003", "C-1002", "C-1009", MOVED_ID, "C-1012", "C-1014") else 1 for c in CUSTOMERS]
    weights = [0.3 if c[0] == "C-1034" else w for c, w in zip(CUSTOMERS, weights)]
    for _ in range(214):
        cust = rng.choices(CUSTOMERS, weights)[0]
        d = Q2_START + timedelta(days=rng.randint(0, days))
        base = rng.uniform(180, 9500)
        if cust[4] == "SEK":
            base *= 10.5
        ref = rng.choice(REFS_INV).format(n=rng.randint(40000, 49999))
        add(d, cust, "invoice", base, ref)

    # boundary rows just outside Q2 (EU and non EU, incl. the moved customer)
    for d, cid, amt in [(EARLY_OUT[0], "C-1009", 4120.55), (EARLY_OUT[1], MOVED_ID, 6875.00),
                        (EARLY_OUT[2], "C-1002", 3310.40), (EARLY_OUT[2], "C-1003", 2275.10),
                        (LATE_OUT[0], "C-1015", 5288.90), (LATE_OUT[1], "C-1005", 41250.00),
                        (LATE_OUT[1], MOVED_ID, 2940.75), (LATE_OUT[2], "C-1012", 1880.00),
                        (LATE_OUT[2], "C-1019", 2604.30)]:
        add(d, by_id[cid], "invoice", amt, "Order %d" % rng.randint(40000, 49999))

    # credit notes
    invoices = [r for r in rows if r["type"] == "invoice"]
    for inv in rng.sample(invoices, 24):
        d = min(inv["date"] + timedelta(days=rng.randint(2, 20)), date(2026, 7, 6))
        amt = inv["amount"] * Decimal(str(rng.choice([0.05, 0.1, 0.15, 0.25, 0.5, 1.0])))
        add(d, by_id[inv["customer_id"]], "credit_note", amt, rng.choice(CREDIT_REASONS), currency=inv["currency"])
        rows[-1]["src"] = inv
    # a Q2 credit note against a March invoice, and a July credit note against a June invoice
    add(date(2026, 4, 3), by_id["C-1009"], "credit_note", Decimal("412.06"), "Short shipment")
    rows[-1]["src"] = [r for r in rows if r["date"] == EARLY_OUT[0] and r["customer_id"] == "C-1009"][0]
    for cid, amt, reason in [("C-1007", "1150.00", "Returned unopened"), (MOVED_ID, "735.20", "Damaged on delivery")]:
        june = [r for r in rows if r["customer_id"] == cid and r["type"] == "invoice" and r["date"].month == 6
                and r["amount"] > Decimal(amt)]
        add(date(2026, 7, 3), by_id[cid], "credit_note", Decimal(amt), reason)
        rows[-1]["src"] = june[-1]

    rows.sort(key=lambda r: (r["date"], r["customer_id"]))
    inv_n, cn_n = 26140, 1810
    for r in rows:
        if r["type"] == "invoice":
            r["no"] = "INV-%d" % inv_n
            inv_n += 1
        else:
            r["no"] = "CN-%d" % cn_n
            cn_n += 1
    return rows


def link_credit_refs(rows, rng):
    for r in rows:
        if r["type"] == "credit_note":
            r["reference"] = "%s, ref %s" % (r["reference"], r["src"]["no"])


def compute(rows, *, region="master", in_q2=True, credits="subtract", convert=True, rates=Q2_RATES):
    master = {c[0]: c[2] for c in CUSTOMERS}
    total = Decimal("0")
    for r in rows:
        reg = master[r["customer_id"]] if region == "master" else r["region"]
        if reg != "EU":
            continue
        if in_q2 and not (Q2_START <= r["date"] <= Q2_END):
            continue
        amt = money(r["amount"] * rates[r["currency"]]) if convert else r["amount"]
        if r["type"] == "credit_note":
            if credits == "exclude":
                continue
            if credits == "subtract":
                amt = -amt
        total += amt
    return total


def main():
    rng = random.Random(SEED)
    rows = build_rows(rng)
    link_credit_refs(rows, rng)
    FIX.mkdir(parents=True, exist_ok=True)

    with open(FIX / "invoices.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["document_no", "date", "customer_id", "customer_name", "region", "currency", "amount", "type", "reference"])
        for r in rows:
            w.writerow([r["no"], r["date"].isoformat(), r["customer_id"], r["customer_name"], r["region"],
                        r["currency"], "%.2f" % r["amount"], r["type"], r["reference"]])

    with open(FIX / "customers.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["customer_id", "name", "region", "country", "billing_currency", "account_manager", "customer_since", "notes"])
        w.writerows(CUSTOMERS)

    (FIX / "pricing-notes.md").write_text(PRICING_NOTES)

    correct = compute(rows)
    traps = {
        "credit_notes_excluded": compute(rows, credits="exclude"),
        "credit_notes_added_as_positive": compute(rows, credits="add"),
        "old_region_from_invoice_export": compute(rows, region="export"),
        "out_of_quarter_rows_included": compute(rows, in_q2=False),
        "no_currency_conversion": compute(rows, convert=False),
        "q1_rates_used": compute(rows, rates=Q1_RATES),
        "all_four_main_traps": compute(rows, region="export", in_q2=False, credits="exclude", convert=False),
    }

    # components for derivation
    master = {c[0]: c[2] for c in CUSTOMERS}
    q2eu = [r for r in rows if master[r["customer_id"]] == "EU" and Q2_START <= r["date"] <= Q2_END]
    by_cur = {}
    for r in q2eu:
        k = (r["currency"], r["type"])
        by_cur[k] = by_cur.get(k, Decimal("0")) + r["amount"]
    inv_usd = sum(money(r["amount"] * Q2_RATES[r["currency"]]) for r in q2eu if r["type"] == "invoice")
    cn_usd = sum(money(r["amount"] * Q2_RATES[r["currency"]]) for r in q2eu if r["type"] == "credit_note")
    moved_usd = sum((money(r["amount"] * Q2_RATES[r["currency"]]) * (-1 if r["type"] == "credit_note" else 1))
                    for r in q2eu if r["customer_id"] == MOVED_ID)
    total_by_currency_first = sum(money((by_cur.get((c, "invoice"), 0) - by_cur.get((c, "credit_note"), 0)) * Q2_RATES[c])
                                  for c in Q2_RATES)
    eu_out = [r for r in rows if master[r["customer_id"]] == "EU" and not (Q2_START <= r["date"] <= Q2_END)]

    def line(r):
        return ",".join([r["no"], r["date"].isoformat(), r["customer_id"], r["customer_name"], r["region"],
                         r["currency"], "%.2f" % r["amount"], r["type"]])

    moved_q2 = [r for r in q2eu if r["customer_id"] == MOVED_ID]
    q2_cns = [r for r in q2eu if r["type"] == "credit_note"]
    late_q2_cn = [r for r in q2_cns if r["date"] == date(2026, 4, 3)][0]

    cur_lines = "; ".join("%s invoices %s, credit notes %s" % (c, by_cur.get((c, "invoice"), 0), by_cur.get((c, "credit_note"), 0))
                          for c in ["EUR", "GBP", "SEK", "USD"])
    trap_text = "; ".join("%s = %s" % (k, v) for k, v in traps.items())

    checklist = {
        "id": "single-revenue-calc",
        "company": "Oxtail Supply",
        "category": "single",
        "held_out": True,
        "summary": "Compute Q2 2026 net revenue from EU customers in USD after credit notes; a good answer gives %s with the region taken from customers.csv, only rows dated 2026-04-01 to 2026-06-30, credit notes subtracted, and each line converted at the fixed Q2 rates." % correct,
        "findings": [
            {"id": "F1", "what": "Credit notes are stored as positive amounts with type credit_note and must be subtracted. Q2 EU credit notes total %s USD against %s USD of Q2 EU invoices." % (cn_usd, inv_usd),
             "evidence": [{"file": "pricing-notes.md", "quote": "Credit notes are exported as positive amounts. Subtract them."},
                          {"file": "invoices.csv", "quote": line(q2_cns[0])}],
             "counts_if": "The answer subtracts credit notes (not ignored, not added), shown by the final number or by an explicit invoice minus credit note derivation."},
            {"id": "F2", "what": "Harrowgate Catering Group (C-1027) is an EU customer per customers.csv even though every row in invoices.csv still shows region UK. Its Q2 net contribution is %s USD." % moved_usd,
             "evidence": [{"file": "customers.csv", "quote": "Region changed from UK to EU on 2026-04-01 when the account moved to the Netherlands subsidiary"},
                          {"file": "pricing-notes.md", "quote": "customers.csv is the master record for region."},
                          {"file": "invoices.csv", "quote": line(moved_q2[0])}],
             "counts_if": "The answer includes Harrowgate Catering Group / C-1027 in EU revenue, or its total matches the correct value."},
            {"id": "F3", "what": "Only rows dated 2026-04-01 through 2026-06-30 count. %d EU rows sit just outside the quarter (late March, early July), including a Q2 credit note dated 2026-04-03 against a March invoice that does count." % len(eu_out),
             "evidence": [{"file": "pricing-notes.md", "quote": "Q2 is 1 April to 30 June inclusive."},
                          {"file": "invoices.csv", "quote": line(eu_out[0])},
                          {"file": "invoices.csv", "quote": line(late_q2_cn)}],
             "counts_if": "The answer excludes the late March and early July rows and includes the 2026-04-03 credit note, or its total matches the correct value."},
            {"id": "F4", "what": "Non-USD lines (EUR, GBP, SEK) are converted at the fixed Q2 2026 rates (EUR 1.0850, GBP 1.2700, SEK 0.0952 USD per unit), not the Q1 rates, rounding each line to the cent.",
             "evidence": [{"file": "pricing-notes.md", "quote": "| EUR | 1.0850 |"},
                          {"file": "pricing-notes.md", "quote": "| SEK | 0.0952 |"}],
             "counts_if": "The answer converts using the Q2 rates (stated, or evident from a total within the tolerance of the correct value)."},
        ],
        "exclusions": [
            {"id": "X1", "what": "The region column in invoices.csv for C-1027 (shows UK).",
             "evidence": [{"file": "pricing-notes.md", "quote": "The region column in the invoice export is stamped when the account is created and is not updated if a customer moves."}],
             "why_not": "customers.csv is the master for region; filtering on the export column drops an EU customer. Result would be %s." % traps["old_region_from_invoice_export"]},
            {"id": "X2", "what": "The Q1 2026 exchange rate table.",
             "evidence": [{"file": "pricing-notes.md", "quote": "Q1 2026 rates (closed, kept for reference only)"}],
             "why_not": "Q1 rates apply to Q1 reporting only. Result with Q1 rates would be %s." % traps["q1_rates_used"]},
            {"id": "X3", "what": "Rows dated 2026-03-27 to 2026-03-31 and 2026-07-01 to 2026-07-06, including July credit notes that reference June invoices.",
             "evidence": [{"file": "pricing-notes.md", "quote": "A credit note belongs to the quarter of its own date, not the date of the invoice it corrects."}],
             "why_not": "Outside Q2. Result if included would be %s." % traps["out_of_quarter_rows_included"]},
            {"id": "X4", "what": "The volume and loyalty discount rules in pricing-notes.md.",
             "evidence": [{"file": "pricing-notes.md", "quote": "Amounts in the invoice export are already net of all discounts, so do not apply them again."}],
             "why_not": "Discounts are already reflected in the exported amounts; reapplying them understates revenue."},
            {"id": "X5", "what": "UK region customers, and EU customers billed in GBP or USD being treated as non-EU.",
             "evidence": [{"file": "customers.csv", "quote": "Bills in GBP at customer request"}],
             "why_not": "Region, not billing currency, decides EU membership. UK is its own region and is not EU."},
        ],
        "answer": {
            "value": "%s USD" % correct,
            "derivation": "Filter invoices.csv to customers whose region in customers.csv is EU (including C-1027, shown as UK in the export) and dates 2026-04-01 to 2026-06-30. Native Q2 EU totals: %s. Convert each line at the Q2 rates (EUR 1.0850, GBP 1.2700, SEK 0.0952, USD 1) rounded to the cent: invoices %s USD minus credit notes %s USD = %s USD. Trap results for diagnosis: %s." % (cur_lines, inv_usd, cn_usd, correct, trap_text),
            "counts_if": "Answer states %s USD. Allow up to 1.00 USD difference for converting per currency total instead of per line (that method gives %s). Any of the trap values counts as wrong." % (correct, total_by_currency_first),
        },
        "mistakes_that_matter": [
            "Ignoring credit notes or adding them as positive revenue (overstates revenue: %s or %s)." % (traps["credit_notes_excluded"], traps["credit_notes_added_as_positive"]),
            "Using the stale region column in invoices.csv, dropping Harrowgate Catering Group (%s)." % traps["old_region_from_invoice_export"],
            "Including late March or early July rows (%s)." % traps["out_of_quarter_rows_included"],
            "Summing mixed currencies without conversion (%s) or using Q1 rates (%s)." % (traps["no_currency_conversion"], traps["q1_rates_used"]),
            "Reapplying discounts from pricing-notes.md to amounts that are already net.",
        ],
    }
    (ROOT / "checklist.json").write_text(json.dumps(checklist, indent=2, ensure_ascii=False) + "\n")

    print("rows", len(rows), "correct", correct, "per-currency-first", total_by_currency_first)
    for k, v in traps.items():
        print(k, v)


PRICING_NOTES = """# Pricing and reporting notes

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
"""

if __name__ == "__main__":
    main()
