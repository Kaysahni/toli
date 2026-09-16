# How Halvard calculates overtime

*By Leon Achterberg. Updated 2026-01-08.*

Overtime is where a lot of payroll mistakes happen, so this article walks through exactly what Halvard does, what it doesn't do, and where you have to make choices.

## The basics

For non-exempt employees, overtime is owed for hours worked beyond a threshold. The most common threshold is 40 hours in a workweek, paid at 1.5 times the regular rate. Some states add daily overtime, and some add double time.

Halvard applies the rules for each employee's work location automatically. You enter hours; we split them into regular, overtime and double time.

## Which employees get overtime

Only employees marked **Non-exempt** on the Job tab. If someone is marked **Exempt**, Halvard will not calculate overtime for them even if you enter 50 hours. Classification is a legal decision based on duties and salary, not job title. If you're unsure, ask your employment attorney before changing it.

## Workweek

Your workweek is set under **Settings > Payroll policies > Workweek start**. It must be a fixed, recurring seven-day period. Changing it mid-year can create a partial week that gets calculated oddly, so pick one and stick with it.

## State rules we apply

| State | Weekly overtime | Daily overtime | Double time |
|---|---|---|---|
| Delmora | Over 40 hours | Over 10 hours in a day | Over 14 hours in a day |
| North Carrow | Over 40 hours | None | None |
| Everywhere else | Over 40 hours | Per state rule if one applies | Per state rule if one applies |

When daily and weekly overtime overlap, we never count the same hour twice. Daily overtime hours are set aside first, then weekly overtime is calculated on the remaining regular hours.

## Regular rate

The overtime rate is 1.5 times the **regular rate**, which isn't always the same as the hourly wage. Nondiscretionary bonuses, shift differentials and some commissions must be folded into the regular rate. Halvard does this automatically for earnings types flagged "Include in regular rate."

Example: Marta earns $20 an hour and works 45 hours. She also earns a $90 production bonus that week.

- Straight time: 45 × $20 = $900
- Plus bonus: $90, total $990
- Regular rate: $990 ÷ 45 = $22
- Overtime premium: 5 × ($22 × 0.5) = $55
- Total: $1,045

If you'd only used her hourly wage, you'd have paid $1,040 and underpaid her by $5.

## Employees with two rates

If someone works two different jobs at two different rates in the same week, the default is a weighted average regular rate. You can switch to "rate in effect when overtime was worked" under Payroll policies, but only if you have an agreement with the employee in writing.

## Salaried non-exempt employees

Enter their hours like anyone else. We calculate an hourly equivalent from their salary and weekly hours.

## What Halvard does not do

- We don't check whether your exempt classifications are correct.
- We don't track meal and rest break penalties. Add those as a separate earning if you owe them.
- If you import hours from ClockNest, ClockNest's overtime split is used as a starting point, but Halvard recalculates using your Halvard workweek.
