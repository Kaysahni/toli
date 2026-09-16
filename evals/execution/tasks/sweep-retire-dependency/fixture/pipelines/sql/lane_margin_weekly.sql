-- lane_margin_weekly.sql
-- owner: Commercial Analytics (Sofie Dahl)
-- consumers: commercial weekly review, regional sales leads
-- schedule: Mondays 07:00 via reporting-01
--
-- Quoted revenue vs invoiced revenue vs estimated cost per lane, last 4 weeks.
-- Quoted numbers come from the quote engine results, not from the booking,
-- because bookings get edited by planners after the quote.

WITH quoted AS (
    SELECT
        q.quote_id,
        q.origin_hub,
        q.destination_hub,
        q.quoted_price_eur,
        q.distance_m / 1000.0 AS distance_km,
        q.created_at
    FROM routecalc_v1.quote_results AS q
    WHERE q.created_at >= date_trunc('week', current_date) - interval '4 weeks'
),
booked AS (
    SELECT s.shipment_id, s.quote_id, s.origin_hub, s.destination_hub
    FROM shipments.shipment AS s
    WHERE s.pickup_at >= date_trunc('week', current_date) - interval '4 weeks'
),
invoiced AS (
    SELECT il.shipment_id, SUM(il.amount_eur) AS invoiced_eur
    FROM finance.invoice_line AS il
    GROUP BY il.shipment_id
),
cost AS (
    SELECT c.shipment_id, SUM(c.cost_eur) AS cost_eur
    FROM finance.shipment_cost AS c
    GROUP BY c.shipment_id
)
SELECT
    b.origin_hub || '-' || b.destination_hub AS lane,
    date_trunc('week', q.created_at)         AS week,
    COUNT(*)                                 AS shipments,
    SUM(q.quoted_price_eur)                  AS quoted_eur,
    SUM(i.invoiced_eur)                      AS invoiced_eur,
    SUM(c.cost_eur)                          AS cost_eur,
    ROUND(100.0 * (SUM(i.invoiced_eur) - SUM(c.cost_eur)) / NULLIF(SUM(i.invoiced_eur), 0), 1) AS margin_pct,
    AVG(q.distance_km)                       AS avg_distance_km
FROM booked b
JOIN quoted q   ON q.quote_id = b.quote_id
LEFT JOIN invoiced i ON i.shipment_id = b.shipment_id
LEFT JOIN cost c     ON c.shipment_id = b.shipment_id
GROUP BY 1, 2
ORDER BY 2 DESC, 5 DESC;
