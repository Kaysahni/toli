# Emissions reporting (CSRD workstream)

Draft, Sofie Dahl and Henrik Aalto, August 2026

We need per-customer CO2e for road freight for the annual report and for the
customer statements that two large shippers asked for.

## Method (proposed)

- Distance: actual driven kilometres from `fleet` telemetry where available.
  For subcontracted carriers without telemetry, use planned distance from
  `routecalc_v2.quote_results`.
- Fuel: telemetry fuel burn for own fleet; default factors per vehicle class
  for subcontractors.
- Allocation to shipment: by weight share of the trailer on each leg.

## Open questions

1. Do we include empty repositioning moves (yard-balancer output) in the
   customer allocation? Proposal: no, report them as network overhead.
2. Ferry legs: use the operator's published factor or a default?
3. Who signs off the method? Probably the CFO, with the auditor reviewing.

## Not decided

Whether this becomes a scheduled pipeline or a yearly notebook. Until decided
there is no job, just this document.
