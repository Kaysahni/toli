# Shipment held at customs

For planners and the trade compliance desk. Not an engineering runbook, but
engineering is sometimes pulled in.

A shipment is "held" when the broker returns status HOLD or when the border
crossing ETA is more than 4 hours past plan.

1. Open the shipment in the dispatch console and check the customs tab.
2. If the declaration was rejected, the reason code is shown. Codes starting
   with D are data errors on our side; send to Trade Compliance (Elif Kaya).
3. If no declaration exists, customs-docs did not generate it. Check the
   customs-docs logs for the shipment id. Most often the commodity code is
   missing on the booking.
4. Tell the customer through the account manager, never directly from the
   planner desk.
5. For perishable goods, escalate to the duty manager after 2 hours.

Norway crossings: remember that the T1 must be closed at the destination
office, otherwise the guarantee stays open.
