# Fuel surcharge backfill pipeline

**Owner:** Commercial Analytics (Sofie Dahl)
**Scheduler:** workflow scheduler, DAG `fuel_surcharge_backfill`
**Schedule:** every Sunday 23:00 UTC
**Config:** `pipelines/fuel-surcharge-backfill.yaml`

## Why it exists

Contract customers are billed a fuel surcharge that depends on the diesel index
in the week of pickup and on the distance of the lane. Quotes are made days or
weeks before pickup, so the surcharge on the quote is an estimate. This
pipeline recomputes the surcharge for every shipment picked up in the last
week, so account managers can see how far off the estimates were.

## Steps

1. **extract_shipments**: shipments with pickup in the last 7 days from
   `shipments.shipment`.
2. **load_diesel_index**: weekly index from the finance schema.
3. **lane_distances**: sends each distinct origin and destination pair to the
   routing API endpoint configured as `distance_source` in the yaml, in batches
   of 400. Distances are cached in `scratch.fsb_distances` for the run.
4. **compute**: surcharge = distance band factor x index delta x contract rate.
5. **publish**: writes `reports.fuel_surcharge_actual_vs_quoted` and posts a
   summary to #commercial-analytics.

## Known issues

- Step 3 is the slow part (about 25 minutes). Sofie looked at moving it to the
  newer bulk endpoint in May but the distance units differ and every contract
  band would need re-checking, so it was parked.
- Lanes with a ferry leg come out shorter than what we actually drive. The
  analysts correct these by hand for Sorrell Maritime crossings.

## Backfilling a past week

    twflow trigger fuel_surcharge_backfill --conf '{"week_start": "2026-08-03"}'
