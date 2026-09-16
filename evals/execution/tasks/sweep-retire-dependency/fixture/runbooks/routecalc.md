# RouteCalc runbook

Owner: Routing Core (Anneli Farstad, tech lead). On-call rota: `routing-core`.
Last edited: 2026-08-19 by Anneli Farstad

RouteCalc computes lane distances, drive times, toll estimates and quote
inputs for everything that moves at Tesselwick. It is called by internal
services, some partners, and a few batch jobs.

## Versions and where they live

| Version | Base URL | Status |
|---|---|---|
| v2 | `https://routecalc.core.tesselwick.internal/v2` | current |
| v1 | `https://routecalc-v1.core.tesselwick.internal` | frozen since 2025-06, retirement scheduled |

The v1 API has no version prefix in its paths (`/quote`, `/quote/bulk`,
`/tariffs/export`, `/health`). That was one of the reasons v2 exists.

**v1 retirement date: Tuesday 20 October 2026.** On that day the v1 pods are
scaled to zero, the `routecalc-v1` hostname is removed, and its API keys are
revoked. No extension is planned: the v1 cluster runs on the old node pool
that is being returned.

## Warehouse outputs

Both versions write every computed quote to the data warehouse through the
nightly results export:

- v1 writes `routecalc_v1.quote_results`
- v2 writes `routecalc_v2.quote_results`

After retirement `routecalc_v1.quote_results` will stay readable for 90 days
but will receive no new rows. Anything reading it will silently report on
stale data.

## Common alerts

### RoutecalcV2LatencyHigh
p95 over 900 ms for 10 minutes. Usually the graph cache was evicted after a
map data reload. Check the `graph_cache_hit_ratio` panel. If it is climbing
back, wait. If it is flat, restart one pod at a time:

    kubectl -n routing rollout restart deploy/routecalc-v2

### RoutecalcMapDataStale
Map snapshot older than 21 days. The weekly import job failed. See the
import job logs in Grafana (dashboard "RouteCalc / imports").

### RoutecalcTollTableMissing
A country toll table did not load. Tolls fall back to zero, which undercharges.
Page Finance Engineering as well, they may need to hold invoices.

## Differences between v1 and v2 that trip people up

- v1 returns distance in metres as an integer, v2 in kilometres as a decimal.
- v1 ignores ferry crossings unless `allow_ferry=1`; v2 includes them by default.
- v1 quote responses have no `currency` field; the caller had to assume EUR.

## Contacts

- Routing Core: #routing-core
- Map data vendor escalations: through Anneli only
