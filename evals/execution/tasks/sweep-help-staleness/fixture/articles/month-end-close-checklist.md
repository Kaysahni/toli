---
title: "Month-end payroll close: a checklist for bookkeepers"
author: Marguerite Ellison
last_updated: 2025-07-28
tags: [accounting, reports, bookkeeping]
---

# Month-end payroll close: a checklist for bookkeepers

Most of the calls we get in the first week of a month come from bookkeepers trying to tie payroll out to the general ledger. Payroll touches a lot of accounts (wages, employer taxes, benefits liabilities, garnishment payables, reimbursements) and small timing differences add up. This checklist is the process our own support accountants recommend. It assumes you close monthly; if you close quarterly, run it for each month in the quarter anyway, because problems are easier to find in a one month window.

You don't have to do every step every month. Steps marked *(optional)* are worth doing if your company is growing fast or you've had corrections recently.

## Part 1: Make sure payroll is final for the month

**1. Confirm every payroll with a pay date in the month is Paid.**
Go to Payroll > History and filter by pay date. Anything still showing *Processing* at month end will usually finish within two banking days, but don't close until it does. A payroll dated the 31st that is still processing on the 1st is normal.

**2. Look for voided or reversed paychecks.**
Voids create negative lines in the Payroll summary report. If a paycheck from last month was voided this month, the reversal is dated this month. Decide with your accountant whether to book it in the current period or reopen the prior period (most small businesses book it in the current period).

**3. Check manual checks were recorded.**
If anyone handed out a manual check (for example, a same day correction), confirm it was recorded in Halvard. Unrecorded manual checks are the number one reason wages in the books are higher than wages in Halvard.

**4. Check reimbursements.** *(optional)*
Reimbursements paid through payroll are not wages, but they do leave your bank account on payday. Make sure they're mapped to an expense account and not to wages.

## Part 2: Pull the reports

You'll want three reports, all from the Reports menu. Set the date range by **pay date**, not by pay period, unless your accountant has told you to accrue wages by period.

| Report | What you use it for |
|---|---|
| Payroll summary | Gross wages, employee taxes, employer taxes, deductions, net pay, by payroll |
| Tax liability | What was withheld and what Halvard paid to each agency, and when |
| Benefits and deductions | Amounts owed to benefits providers and retirement plans |

*Screenshot: Reports page with Payroll summary selected and the date filter set to "Pay date: March 1 to March 31".*

Export them to CSV if you want to build a tie-out spreadsheet. Many bookkeepers keep one workbook per year with a tab per month.

## Part 3: Tie out to the general ledger

**5. Gross wages.**
Total gross pay on the Payroll summary should equal the total debits to your wages expense accounts for the month. If you split wages by department, compare department by department.

**6. Employer taxes.**
Employer taxes on the Payroll summary should equal payroll tax expense. A difference here is almost always timing: an employer tax adjustment that Halvard made in a later payroll.

**7. Net pay and the bank.**
Net pay plus reimbursements should match the payroll debit on your bank statement for each pay date. Tax payments and garnishment payments come out as separate debits, so match them against the Tax liability report instead.

**8. Liabilities.**
Withheld employee taxes, benefits deductions and garnishments are liabilities until paid. At month end, the balance in each liability account should equal amounts withheld but not yet paid. The Tax liability report shows payment dates so you can see what's still outstanding.

**9. Confirm the journal entry synced.**
If you use the accounting integration, open Tallyworks and confirm that a journal entry posted for every payroll in the month, dated on its pay date. Missing entries usually mean the account mapping broke after someone renamed an account. Re-send the payroll from Payroll > History once the mapping is fixed.

If you don't use an integration, post the entries yourself from the Payroll summary CSV.

## Part 4: Look for things that will cause trouble later

**10. New locations.** *(optional)*
If anyone started working in a new state or in Marren County this month, check the Taxes page for a registration banner. Unregistered jurisdictions mean taxes are being withheld but not remitted.

**11. Negative balances.** *(optional)*
Negative year-to-date amounts for any employee (usually after a correction) should be reviewed before the end of the quarter.

**12. Pending corrections.**
If support is working on an amendment or correction ticket for you, note it in your close file so the adjustment isn't a surprise next month.

## A note on accruals

Halvard reports on a cash basis by pay date. If your company accrues wages earned but not yet paid at month end, calculate the accrual outside Halvard (days worked since the last pay period end, times daily wages) and reverse it on the first of the next month. The Payroll summary can be run by pay period end date to help with this.

## Need a hand?

Our support team includes people with bookkeeping backgrounds. Chat with us and ask for an accounting specialist, or book a screen share from the help icon.
