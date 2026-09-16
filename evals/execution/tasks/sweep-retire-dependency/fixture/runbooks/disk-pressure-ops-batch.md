# Disk pressure on ops-batch hosts

ops-batch-01 and ops-batch-02 have 200 GB root volumes. Batch jobs write logs
and temporary files there and it fills up about once a quarter.

Quick look:

    df -h /
    sudo du -xh /var/log/tw | sort -h | tail -20
    sudo du -xh /tmp | sort -h | tail -20

Safe to delete:
- `/var/log/tw/*.log.[0-9]*` older than 14 days
- `/tmp/lanes-*` directories older than 2 days

Not safe to delete:
- `/opt/tesselwick/jobs/state/` (checkpoint files for resumable jobs)

If usage is back above 85% within a week, some job has started logging at
debug level. Grep the crontab for `--verbose`.
