# Kafka consumer lag

Applies to cluster `kafka-a` (brokers a1 to a3).

1. Open Grafana, dashboard "Kafka / consumer groups".
2. Find the group with growing lag. Lag that grows and then plateaus is usually
   a slow consumer. Lag that grows without bound means the consumer is down.
3. For a slow consumer, check its pod CPU. If throttled, raise the limit.
4. For a dead consumer, check the last error in its logs before restarting.
5. Do not reset offsets without asking the owning team. Several consumers
   (invoice-builder in particular) are not idempotent.

Rebalance storms: if a group rebalances more than 5 times in 10 minutes, check
`max.poll.interval.ms`. Batch-heavy consumers need it above 10 minutes.
