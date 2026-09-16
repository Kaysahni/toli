# Import payroll history from your previous provider

*By Hollis Macready, Onboarding team. Last updated 2026-02-24.*

If you start using Halvard partway through the year, we need the payrolls you already ran this year somewhere else. Without them, year-to-date totals on pay stubs will be wrong, social insurance wage caps won't be applied correctly, and year-end statements for employees won't add up.

This is one of the longer parts of onboarding, so it helps to know what to expect before you start.

## What you need from your old provider

Ask your previous provider for a **payroll register** or **payroll details** report covering every pay date this year. For each pay date and each employee, we need:

- Gross earnings, split by type (regular, overtime, bonus, commission, tips, and so on)
- Every tax withheld from the employee, by tax
- Every employer tax, by tax
- Pre-tax and after-tax deductions, by type
- Net pay

A summary by quarter is acceptable if a per-payroll report isn't available, but per-payroll is better because it keeps pay stub history accurate.

## Two ways to get it in

### Option 1: Upload the file and let us map it

Best if your old provider gives you a spreadsheet.

1. Go to **Settings > Onboarding > Prior payroll**.
2. Click **Upload file** and choose the report (CSV or XLSX).
3. Halvard reads the column headers and suggests a match for each one, for example "Fed WH" to **Federal income tax (employee)**.
4. Review each suggested match. Columns we couldn't match show in yellow. Pick the right field from the list, or mark the column **Ignore**.
5. Click **Validate**. Halvard checks that gross minus taxes and deductions equals net for every row.
6. Fix any rows that fail, then click **Import**.

Screenshot: the column mapping step, with "Med EE" matched to Medical insurance (employee, pre-tax) and "Misc Ded 2" highlighted in yellow.

### Option 2: Enter totals by hand

Best if you only have a few employees or just a handful of pay dates.

1. Go to **Settings > Onboarding > Prior payroll** and click **Enter manually**.
2. Pick a pay date and fill in the grid for each employee.
3. Repeat for each pay date.

## Common problems

**"Row doesn't balance."** The most common cause is a deduction that your old provider reports in a separate section of the report, like a garnishment. Add the missing column and validate again.

**Employee not found.** The import matches employees by national ID number. If an employee's ID was typed differently in Halvard, fix it in **Team > Directory** and re-run validation.

**Employees who left before you switched.** Add them as past team members first (under **Team > Past members**) so their history can be imported. They still need year-end statements.

**Taxes in states you don't have accounts for yet.** Add the tax account under **Taxes > Tax accounts** before importing. The import can't create tax accounts.

## After import

Once imported, prior payrolls show in **Reports** with a small "Imported" tag. You can't edit them directly. If you find a mistake, delete the import for that pay date and upload it again.

Our onboarding team reviews every import before your first payroll in Halvard. If something looks off, we'll reach out.
