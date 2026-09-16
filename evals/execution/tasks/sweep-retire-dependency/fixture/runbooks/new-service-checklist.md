# New service checklist

Before a new service takes production traffic:

1. Service config in the deploy repo with an `owner` field that names a team,
   not a person.
2. Health endpoint and readiness probe.
3. Dashboards: request rate, error rate, latency, saturation.
4. At least one alert that pages, routed to the owning team's rota.
5. Secrets in vault, never in the config file.
6. If it calls RouteCalc, use RouteCalc v2 or tw-routing-client 3.x. New
   consumers of v1 are not accepted.
7. If it exposes anything to partners, go through Partner Integrations.
8. Runbook in `runbooks/` with at least the top three failure modes.
9. Added to sla-monitor if customer facing.
10. Cost estimate reviewed by your manager.
