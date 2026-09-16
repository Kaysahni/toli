-- on_time_delivery.sql
-- owner: Customer Experience analytics
-- schedule: daily 06:20
-- on time = delivered within the customer's booked window, 15 min grace

SELECT
    s.customer_id,
    date_trunc('week', s.delivered_at) AS week,
    COUNT(*) AS delivered,
    AVG(CASE WHEN s.delivered_at <= s.window_end + interval '15 minutes' THEN 1.0 ELSE 0.0 END) AS on_time_rate
FROM shipments.shipment s
WHERE s.status = 'DELIVERED'
  AND s.delivered_at >= current_date - interval '8 weeks'
GROUP BY 1, 2;
