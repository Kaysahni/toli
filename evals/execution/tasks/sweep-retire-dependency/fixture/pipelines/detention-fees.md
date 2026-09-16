Detention fee pipeline
======================

Owner: Finance Engineering. Business owner: Ulla Berg.

Detention is charged when a trailer waits more than 2 hours at a customer site.
The pipeline joins yard gate events with delivery windows and produces
chargeable detention minutes per shipment.

Flow:
  yard.gate.events (kafka) -> detention_events (warehouse, hourly)
  detention_events + shipments.shipment -> reports.detention_chargeable (daily)
  reports.detention_chargeable -> invoice-builder (surcharges.detention)

Edge cases we handle:
  - trailer dropped and left (drop and hook): no detention, the clock does not start
  - customer site closed on a public holiday: clock pauses
  - planner override flag on the shipment: detention waived, reason required

Edge cases we do NOT handle yet:
  - partial unloads split across two days
  - sites with two gates where only one has a camera (KLV customer Grenholt)

Disputes go to the account manager first. About 4% of detention charges are
disputed and roughly half of those are waived.
