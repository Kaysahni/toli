-- driver_hours.sql
-- owner: Fleet Operations (Henrik Aalto)
-- consumers: depot managers
-- schedule: daily 08:15
-- NOTE: hr_hours is restricted. Output table reports.driver_hours_summary only
-- contains aggregates per depot, never per driver.

SELECT
    t.depot_code,
    t.work_date,
    COUNT(DISTINCT t.driver_ref)                         AS drivers,
    SUM(t.driving_minutes) / 60.0                        AS driving_hours,
    SUM(CASE WHEN t.driving_minutes > 540 THEN 1 ELSE 0 END) AS days_over_9h,
    SUM(t.rest_violations)                               AS rest_violations
FROM hr_hours.timesheet AS t
WHERE t.work_date >= current_date - 14
GROUP BY t.depot_code, t.work_date;
