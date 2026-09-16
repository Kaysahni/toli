# Telemetry compaction job

Owner: Fleet Data (Jonas Reinholt)

Raw telemetry (`fleet.telemetry.raw`, about 55 million messages per day) is too
big to query directly. Every hour this job:

1. reads the last hour of raw messages from S3,
2. drops duplicates by (vehicle_id, ts),
3. snaps GPS points to 30 second buckets,
4. writes `fleet.position_30s` and `fleet.fuel_hourly`.

It runs on the Spark cluster, not in the workflow scheduler, because the
scheduler workers do not have enough memory.

If a run fails, the next run picks up both hours. After three consecutive
failures it pages Fleet Data. Backfills older than 7 days need the raw bucket
lifecycle rule paused first, otherwise the files may be gone.
