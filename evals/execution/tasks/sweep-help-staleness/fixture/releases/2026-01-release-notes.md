# Halvard Payroll release notes: January 2026

Release 2026.01, rolled out to all accounts on January 20, 2026.

Posted by the Product team. Questions about anything below can go to your account manager or to support through the in-app chat.

## Navigation: "People" is now "Team"

We've renamed the **People** menu in the left sidebar to **Team**. Everything that lived under People is still there, in the same order:

- People > Directory is now Team > Directory
- People > Add person is now Team > Add team member
- People > Former employees is now Team > Past members

Bookmarked URLs keep working. We made this change because a growing share of Halvard customers pay contractors alongside employees, and "People" was often read as "employees only." The Team menu covers both.

## Security: two-step verification by text message is being retired

Starting with this release, new two-step verification setups can only use an authenticator app or a hardware security key. Existing text message (SMS) enrollments will stop working on February 3, 2026, and affected admins will be prompted to switch the next time they sign in.

Text message codes are the weakest of the three methods and have been the source of most account takeover attempts we've investigated in the past year.

## Pay stub redesign (preview)

Admins can turn on the new pay stub layout from Settings > Pay stubs > Try the new design. The new layout groups pre-tax and post-tax deductions and shows year-to-date totals in a single column. Employees see the new layout only after an admin turns it on. The classic layout remains the default for now.

## Bulk edit departments

From Team > Directory, select multiple team members and choose **Edit department** to move them in one step. Previously this had to be done one profile at a time.

## Improvements and fixes

- CSV exports from Reports are noticeably faster for companies with more than 200 team members.
- Fixed an issue where time off balances could display with a rounding difference of 0.01 hours after an accrual adjustment.
- The Home dashboard now shows the next three pay dates instead of just the next one.
- Fixed a display bug where the Benefits tab showed an empty state for a few seconds before loading plans.
- Reports > Payroll summary can now be filtered by work location.
