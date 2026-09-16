-- hub_dwell_time.sql
-- owner: Yard Systems analytics (ad hoc, not scheduled)
-- How long trailers sit in each cross-dock between gate in and gate out.
SELECT
    hub_code,
    date_trunc('day', gate_in_at) AS day,
    percentile_cont(0.5) WITHIN GROUP (ORDER BY gate_out_at - gate_in_at) AS median_dwell,
    percentile_cont(0.9) WITHIN GROUP (ORDER BY gate_out_at - gate_in_at) AS p90_dwell
FROM yard.trailer_visit
WHERE gate_out_at IS NOT NULL
  AND gate_in_at >= current_date - interval '30 days'
GROUP BY 1, 2;
