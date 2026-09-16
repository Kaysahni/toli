# Evergreen Retirement: how contributions flow from Halvard

Written by Marcus Oyelaran, Benefits Support
Last updated: 2025-11-03

Halvard connects to Evergreen Retirement so that employee deferrals and any employer match are calculated on every payroll and sent to Evergreen automatically. This article explains what the connection does, what it does not do, and how to fix the most common mismatches.

If you have not connected yet, start with the section "Connecting your plan" below. If you are already connected and a number looks wrong, jump to "When amounts don't match."

## What the connection does

Once connected, Halvard and Evergreen share three kinds of information:

- **Employee eligibility and enrollment.** Evergreen tells Halvard who is enrolled and at what deferral percentage. You don't need to enter deferrals by hand.
- **Contributions.** After each payroll is processed, Halvard sends Evergreen the deferral amount, the employer match, and the pay period dates for each enrolled employee.
- **Census data.** Hire dates, termination dates, hours worked and compensation go to Evergreen so it can run eligibility and testing.

What it does not do: Halvard doesn't give investment advice, doesn't change fund elections, and can't see account balances. Employees manage those in their Evergreen account.

## Connecting your plan

1. Go to **Benefits** and click **Browse benefit partners**.
2. Choose **Evergreen Retirement** and click **Connect**.
3. Sign in with your Evergreen plan sponsor login. If you don't have one yet, your Evergreen onboarding contact can send an invite.
4. Review the list of employees Halvard matched to Evergreen participants. Anyone unmatched shows a yellow badge. Match them by hand or leave them for later.
5. Click **Finish connection**.

Screenshot: the matching screen with two employees flagged "Not matched" and a Match manually button beside each.

It usually takes one business day for the first deferral elections to appear in Halvard. You'll see them under each employee's **Benefits** tab as "Evergreen pre-tax" or "Evergreen Roth-style."

## Employer match

Match rules live in Evergreen, not in Halvard. Halvard reads the formula (for example, 100% of the first 3% deferred plus 50% of the next 2%) and applies it every payroll. If you change your match formula, change it in Evergreen, then wait for the next sync before running payroll.

Note: if your plan uses a true-up at year end, Evergreen calculates the true-up and sends Halvard a one-time employer contribution. It appears as a separate line on the payroll it's attached to.

## Contribution limits

Evergreen tracks each employee's yearly deferral limit. When an employee is close to the limit, Evergreen lowers the deferral it sends to Halvard so the employee doesn't go over. If an employee joined you mid-year and contributed to a different plan earlier in the year, ask them to tell Evergreen about those prior contributions, because neither system can see them otherwise.

## When amounts don't match

Most mismatches come from one of these:

| Symptom | Likely cause | What to do |
|---|---|---|
| Deferral is 0 but employee says they enrolled | Enrollment saved in Evergreen after the sync ran | Click **Sync now** on the Evergreen card, then refresh the payroll |
| Match is higher than expected | Bonus or commission counted as eligible compensation | Check the plan's compensation definition in Evergreen |
| Employee missing from contribution file | Employee not matched during connection | Match them under **Benefits > Evergreen Retirement > Participants** |
| Contribution sent twice | Payroll was voided and rerun | Contact Evergreen support to reverse the duplicate |

If none of these explain it, contact Halvard support with the pay date and employee name. We'll look at the contribution file we sent and tell you exactly what went over.

## Disconnecting

Go to **Benefits > Evergreen Retirement** and click **Disconnect**. Deductions stop on the next payroll that hasn't been processed yet. Contributions already sent are not recalled.
