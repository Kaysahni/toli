# Postgres failover (managed clusters)

Written after the June 2026 pg-yard incident. Owner: Data Platform.

We run three managed clusters: `pg-yard`, `pg-finance`, `pg-dispatch`. Each has
one primary and two replicas in different zones.

## Automatic failover

Happens when the primary is unreachable for 30 seconds. Expect 45 to 90 seconds
of write errors. Services using the `-primary` hostname reconnect on their own.

## Manual failover

Only with Data Platform on the call.

    twctl pg failover --cluster pg-yard --to replica-2 --reason "INC-xxxx"

## After a failover

- Check replication lag on the new replicas is under 5 seconds.
- dock-scheduler caches prepared statements; restart it if it logs
  `prepared statement does not exist`.
- File the incident note even if nobody noticed.
