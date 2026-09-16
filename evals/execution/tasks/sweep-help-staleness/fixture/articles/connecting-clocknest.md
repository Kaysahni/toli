---
title: Connect ClockNest time tracking
slug: connecting-clocknest
author: Imani Castellanos
last_updated: 2025-04-22
plans: [Core, Plus]
---

# Connect ClockNest time tracking

If your team clocks in and out with ClockNest, you can pull approved hours straight into Halvard instead of typing them in each pay period.

## What syncs

| From ClockNest | Into Halvard |
|---|---|
| Approved regular hours | Regular hours on the payroll draft |
| Approved overtime hours | Overtime hours |
| Paid breaks | Regular hours |
| Time off entries | Not synced (manage time off in Halvard) |
| Tips | Not synced |

Only hours a manager has approved in ClockNest come across. Unapproved shifts stay in ClockNest.

## Set it up

1. In Halvard, go to **Settings > Integrations**.
2. Find **ClockNest** and click **Connect**.
3. Sign in to ClockNest with an admin account and allow access.
4. Back in Halvard, match people. We auto-match by work email; anyone we couldn't match shows up in a list for you to pair manually.
5. Choose which pay schedules should use ClockNest hours.

Screenshot: the ClockNest matching screen showing two unmatched team members.

## Each pay period

When you start a payroll draft for a connected pay schedule, click **Import hours**. We pull everything approved within the pay period dates. You can still edit the hours in the draft; your edits don't flow back to ClockNest.

## Troubleshooting

**Someone's hours are zero.** Check that they are matched (Settings > Integrations > ClockNest > Matching) and that their shifts are approved.

**Overtime looks wrong.** ClockNest calculates overtime using the rules configured in ClockNest. If your ClockNest workweek starts on a different day than your Halvard workweek, the split between regular and overtime hours can differ. Align the workweek start in both tools.

**I disconnected and reconnected, and people are unmatched.** Reconnecting creates a fresh link, so you'll need to confirm matches again. Existing payroll history isn't affected.
