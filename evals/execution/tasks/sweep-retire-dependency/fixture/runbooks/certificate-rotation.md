# Internal certificate rotation

Internal TLS certificates for `*.core.tesselwick.internal`,
`*.data.tesselwick.internal` and `*.tools.tesselwick.internal` are issued by the
internal CA and rotate every 60 days via cert-manager.

When rotation fails the alert `CertExpiringSoon` fires 14 days before expiry.

Steps:

1. `kubectl get certificate -A | grep -v True` to find the failing one.
2. Describe it and read the events. The usual cause is a DNS challenge record
   left behind by a previous attempt.
3. Delete the stale TXT record through the NET queue (Platform Networking),
   then `kubectl delete certificaterequest <name>` to retry.

Hosts outside Kubernetes (ops-batch-01, ops-batch-02, reporting-01,
edge-sync-03) use a cron-driven renewal script. Check `/var/log/tw/certrenew.log`.

Partner facing certificates (`api.tesselwick.example`) are NOT handled here.
They are bought externally and rotated by Partner Integrations once a year.
