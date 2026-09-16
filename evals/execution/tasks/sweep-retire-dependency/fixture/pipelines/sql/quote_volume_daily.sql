-- quote_volume_daily.sql
-- owner: Routing Core
-- consumers: RouteCalc capacity planning dashboard
-- schedule: daily 06:00

SELECT
    date_trunc('day', created_at) AS day,
    client_id,
    COUNT(*)                      AS quotes,
    AVG(latency_ms)               AS avg_latency_ms,
    PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY latency_ms) AS p95_latency_ms
FROM routecalc_v2.quote_results
WHERE created_at >= current_date - interval '1 day'
  AND created_at <  current_date
GROUP BY 1, 2
ORDER BY quotes DESC;

-- 2025-10: removed the UNION with the old API's results table after load-matcher moved over.
