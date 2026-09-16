# Build a custom report

*Written by Tomasz Oyelaran, Support Team. Last updated March 3, 2026.*

The standard reports cover most needs, but sometimes you want a very specific view: say, overtime hours by department for the last two quarters, or every employee in Marren County with an active retirement deduction. That's what the custom report builder is for.

Custom reports are available on Core and Plus.

## Starting a new report

Go to **Reports** and click **New custom report** in the top right. You'll land on a blank canvas with three panels:

- **Fields** on the left, grouped into Employee, Earnings, Deductions, Taxes, Time off and Benefits
- **Preview** in the middle
- **Settings** on the right, where you name the report and set its date range

Drag any field into the preview area to add it as a column. You can reorder columns by dragging their headers.

Screenshot: the custom report builder with Employee name, Department and Overtime hours added as columns.

## Grouping and totals

Open **Settings** and turn on **Group rows by**. Pick one field, usually Department or Work location. Each group gets a subtotal row, and the report gets a grand total at the bottom. Only numeric columns are totaled.

## Filters

Filters live under the preview. A few tips from tickets we see often:

1. Filters on employee fields (like Department) use the value as of the end of the date range. If someone transferred from Sales to Support mid-quarter, they show up under Support.
2. "Is empty" is useful for cleanup. Filter on **Emergency contact** is empty to find records that need finishing.
3. Date filters on the report settings control which pay dates are included. Filters on a date field (like Hire date) control which people are included. Mixing them up is the number one reason reports look empty.

## Saving and sharing

Click **Save**. Saved reports appear under **Reports > My reports**. To share with another admin, open the report, click **Share**, and choose people from your team. They get view access; they can duplicate it if they want to edit.

## Things the builder can't do (yet)

- Calculated columns (for example, overtime as a percent of gross)
- Charts
- Combining contractor and employee data in one report

If one of these would help you, tell us through **Help > Send feedback**. We do read those.
