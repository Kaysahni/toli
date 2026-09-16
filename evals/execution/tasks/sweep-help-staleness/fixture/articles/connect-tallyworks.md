Connect Tallyworks to Halvard
=============================

Last updated: 2024-08-19
Author: Jun Park, Integrations Support

Tallyworks Connect sends a journal entry to your Tallyworks company file every time a payroll is paid, so your books match your payroll without manual entry.

Who can set this up
-------------------
You need to be a Halvard admin with the Integrations permission, and an admin on the Tallyworks side.

Set up the connection
---------------------
1. In Halvard, go to Settings > Integrations.
2. Find Tallyworks Connect and click Connect.
3. Sign in to Tallyworks when prompted and choose which company file to use.
4. Map your accounts. Halvard suggests a mapping based on account names, for example:
   - Gross wages -> "Wages and salaries" expense account
   - Employer taxes -> "Payroll tax expense"
   - Net pay -> your operating bank account
   - Employee deductions -> the matching liability accounts
5. Choose whether to post one journal entry per payroll or one per department.
6. Click Save mapping.

From the next paid payroll onward, the journal entry appears in Tallyworks within about 15 minutes, dated on the pay date.

Syncing past payrolls
---------------------
Only payrolls paid after you connect are sent automatically. To send an earlier payroll, open it under Payroll > History and choose Send to Tallyworks from the actions menu.

Troubleshooting
---------------
"Account not found": someone renamed or archived an account in Tallyworks. Re-open the mapping and pick the account again.

Entries are doubled: check whether both Halvard and a bookkeeper are entering payroll. Turn one of them off.

Disconnecting: Settings > Integrations > Tallyworks Connect > Disconnect. Entries already posted are not removed.
