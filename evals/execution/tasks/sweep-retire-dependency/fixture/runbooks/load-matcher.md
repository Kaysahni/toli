# load-matcher on-call notes

Team: Dispatch Platform. Written by Rafaela Monteiro, updated by Daniel Okafor.

## What it does

Takes `load.opened` events and tries to match them against capacity offers from
subcontracted carriers within `MATCH_RADIUS_KM`. Matches with margin below
`MIN_MARGIN_PCT` are dropped and the load goes to a human planner in the
dispatch console.

## History

load-matcher was one of the first RouteCalc v1 consumers: before the October
2025 migration it called `https://routecalc-v1.core.tesselwick.internal/quote`
for every candidate pair, which is why the old dashboards still have a
"v1 quote latency" panel. It was moved to v2 in release 9.0.0 and has not
touched v1 since. The panel can be deleted whenever someone has five minutes.

## Symptoms and what to do

**Match rate drops below 30% during business hours.**
Usually a carrier capacity feed stopped. Check `carrier.capacity.offered` lag
per partner. Ebbesen is the most common culprit on Monday mornings.

**Matches pile up with margin exactly 0.**
Tariff lookup failed and the code treated cost as revenue. Check tariff-service
health. Restarting load-matcher does not help.

**Pods OOM after a deploy.**
The candidate pair cache is sized from `MATCH_RADIUS_KM`. Someone probably
raised the radius. Put it back to 120 and redeploy.

## Scaling

Autoscaling is on CPU. On Black Friday week we pin min replicas to 8 by hand.
