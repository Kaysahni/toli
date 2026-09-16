# Warehouse source schemas

Last updated 2026-07-22 (Mateusz Kowalczyk)

| Schema | Loaded by | Freshness | Notes |
|---|---|---|---|
| `shipments` | CDC from pg-dispatch | ~5 min | |
| `finance` | CDC from pg-finance | ~5 min | invoice lines, credit notes |
| `wms` | warehouse-sync | 15 min | stock positions per site |
| `fleet` | telemetry compaction job | hourly | aggregated from `fleet.telemetry.raw` |
| `routecalc_v1` | RouteCalc nightly results export | daily 02:00 | quotes computed by the old API |
| `routecalc_v2` | RouteCalc nightly results export | daily 02:00 | quotes computed by the current API |
| `routecache_v1` | RouteCache stats exporter | hourly | cache hits and misses |
| `planning` | capacity-forecast | weekly | |
| `claims` | CDC from claims-intake db | ~5 min | |
| `hr_hours` | driver timesheet import | daily | restricted, needs approval |

Access requests: #data-platform, include the schema and the reason.
