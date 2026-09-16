-- claims_aging.sql
-- owner: Claims Engineering / claims desk
-- schedule: 1st of month
SELECT
  CASE
    WHEN now() - opened_at < interval '30 days' THEN '0-29'
    WHEN now() - opened_at < interval '60 days' THEN '30-59'
    ELSE '60+'
  END AS age_bucket,
  status,
  COUNT(*) AS claims,
  SUM(claimed_eur) AS claimed_eur
FROM claims.claim
WHERE status NOT IN ('SETTLED', 'REJECTED')
GROUP BY 1, 2
ORDER BY 1, 2;
