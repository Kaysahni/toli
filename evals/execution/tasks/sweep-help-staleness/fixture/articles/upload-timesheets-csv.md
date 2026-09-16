Upload hours from a CSV file (classic import)
Last updated 2026-01-28 | Author: Femi Adeyemi

If you track hours in a spreadsheet or in a time clock that isn't connected to Halvard, you can upload a CSV file of hours instead of typing them in.

Heads up: there's also a newer Timesheet importer under Payroll > Import hours that can map columns for you. Both work. This article covers the classic upload, which many long time customers still use.

FILE FORMAT

Your file needs one row per team member per earning type, with these columns, in this order:

  employee_id, earning_type, hours, rate (optional), department (optional)

- employee_id must match the ID in Team > Directory.
- earning_type must match an earning type name exactly, for example "Regular" or "Overtime".
- Leave rate empty to use the team member's rate on file.

Example:

  1042, Regular, 80,,
  1042, Overtime, 4.5,,
  1107, Regular, 72, 24.50, Kitchen

UPLOADING

1. Start your regular payroll from the Payroll page.
2. On the hours step, click Import hours, then Classic upload.
3. Choose your CSV file.
4. Review the preview. Rows with problems are highlighted in red, with the reason.
5. Click Apply hours.

Hours from the file replace anything already entered for those team members and earning types. Other team members aren't touched.

COMMON ERRORS

"Unknown employee": the employee_id doesn't exist or belongs to a past member.
"Unknown earning type": check spelling and capitalization.
"Hours must be a number": remove text like "hrs" from the hours column.
"File must be CSV": save from your spreadsheet as CSV (comma delimited), not as a workbook.

TIP: Save a template file once with your team's IDs and reuse it each pay period.
