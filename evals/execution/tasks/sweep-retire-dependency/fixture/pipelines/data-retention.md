# Warehouse data retention

| Schema | Retention | Why |
|---|---|---|
| shipments | 10 years | accounting and CMR claims |
| finance | 10 years | bookkeeping law |
| fleet | 3 years | driver disputes, fuel analysis |
| hr_hours | 5 years | working time rules |
| routecalc_v1 | 90 days after the API is retired, then dropped | historical quotes are also in the invoices |
| routecalc_v2 | 2 years | |
| routecache_v1 | 30 days | operational only |
| scratch | 7 days | |

Changes need sign-off from Data Platform and Legal.
