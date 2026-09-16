"""Generates the four system logs for single-incident-chain.
All log timestamps are UTC. changes.md uses US Eastern (EDT, UTC-4) and is hand written.
Run: python3 build/gen_logs.py (from the task dir)."""
import json
import re
import os
import random
from datetime import datetime, timedelta

random.seed(20260903)
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "fixture", "logs")

T0 = datetime(2026, 9, 1, 23, 0, 0)   # window start
T1 = datetime(2026, 9, 3, 9, 0, 0)    # window end
ROT = datetime(2026, 9, 3, 1, 10, 4)  # cert reload on relay
ALARM = datetime(2026, 9, 3, 2, 47, 13)
KILL = datetime(2026, 9, 3, 4, 30, 0)
PROG = [(datetime(2026, 9, 3, 1, 30, 30), 0), (datetime(2026, 9, 3, 1, 41, 0), 5204), (datetime(2026, 9, 3, 1, 58, 0), 7311), (ALARM, 36114)]


def progress(d):
    """statements rendered and published on the incident night (renderer, queue and scheduler agree)"""
    if d < PROG[0][0]:
        return 0
    for (a, x), (b, y) in zip(PROG, PROG[1:]):
        if a <= d <= b:
            return int(x + (y - x) * (d - a).total_seconds() / (b - a).total_seconds())
    return 36114


def ms(d):
    return d if d.microsecond else d + timedelta(milliseconds=random.randint(1, 999))


def t(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


def jitter(start, end):
    return start + timedelta(seconds=random.uniform(0, (end - start).total_seconds()))


def hexid():
    return "%09X" % random.getrandbits(36)


# ---------------------------------------------------------------- relay
def relay():
    ev = []
    host = "mx-relay01"

    def add(d, proc, msg):
        d = ms(d)
        ev.append((d, f"{d.strftime('%Y-%m-%dT%H:%M:%S.')}{d.microsecond // 1000:03d}Z {host} quillmail/{proc}: {msg}"))

    clients_ok = [
        ("peoplehub-app1.jvb.internal", "10.40.30.8", "hr-notices@junipervale.example"),
        ("fraud-notify02.jvb.internal", "10.40.18.5", "fraud-alerts@junipervale.example"),
        ("itsm-core.jvb.internal", "10.40.9.14", "servicedesk@junipervale.example"),
    ]
    mailers = [("mailer-1.jvb.internal", "10.40.12.21"), ("mailer-2.jvb.internal", "10.40.12.22")]
    domains = ["harbormail.example", "tallowpost.example", "greyfinch.example", "ostlermail.example", "quarrynet.example"]
    pid = {"smtpd": 2211, "tlsmgr": 1874, "qmgr": 1990, "smtp": 3120, "housekeep": 1702}

    def session(d, name, ip, sender, size=None):
        d = ms(d)
        qid = hexid()
        size = size or random.randint(3200, 9100)
        add(d, f"smtpd[{pid['smtpd']}]", f"connect from {name}[{ip}]")
        add(d + timedelta(milliseconds=40), f"smtpd[{pid['smtpd']}]", f"STARTTLS ok from {name}[{ip}] proto=TLSv1.3 cipher=TLS_AES_256_GCM_SHA384")
        add(d + timedelta(milliseconds=220), f"smtpd[{pid['smtpd']}]", f"{qid}: queued from=<{sender}> size={size} nrcpt=1")
        dom = random.choice(domains)
        add(d + timedelta(seconds=random.uniform(0.6, 2.4)), f"smtp[{pid['smtp']}]", f"{qid}: to=<{hexid().lower()[:7]}@{dom}> relay=in.{dom}:25 delay={random.uniform(0.5, 2.3):.2f} status=sent (250 accepted)")

    def fail(d, name, ip):
        d = ms(d)
        add(d, f"smtpd[{pid['smtpd']}]", f"connect from {name}[{ip}]")
        add(d + timedelta(milliseconds=31), f"smtpd[{pid['smtpd']}]", f"TLS handshake failed from {name}[{ip}]: peer sent alert unknown_ca (48)")
        add(d + timedelta(milliseconds=33), f"smtpd[{pid['smtpd']}]", f"lost connection after STARTTLS from {name}[{ip}]")

    add(T0 + timedelta(seconds=3), f"housekeep[{pid['housekeep']}]", "log file reopened after rotation")
    # background traffic from other clients, all night, both nights
    d = T0
    while d < T1:
        d += timedelta(seconds=random.randint(900, 2400))
        n, ip, s = random.choice(clients_ok)
        session(d, n, ip, s)

    # mailer notification traffic before rotation (low volume, succeeds)
    d = T0
    while d < ROT:
        d += timedelta(seconds=random.randint(300, 1100))
        if d >= ROT:
            break
        n, ip = random.choice(mailers)
        session(d, n, ip, "noreply@notify.junipervale.example")

    # previous night statement run, mailers sending bulk, summarized
    prev_start, prev_end = t("2026-09-02 01:41:10"), t("2026-09-02 03:04:40")
    d = prev_start
    while d < prev_end:
        n, ip = random.choice(mailers)
        session(d, n, ip, "statements@notify.junipervale.example", size=random.randint(61000, 88000))
        burst = random.randint(17000, 20000)
        add(d + timedelta(seconds=5), f"smtpd[{pid['smtpd']}]", f"rate-limited logging: {burst} similar session records suppressed in last 600s")
        d += timedelta(minutes=10)

    # rotation
    add(ROT - timedelta(seconds=2), f"tlsmgr[{pid['tlsmgr']}]", "SIGHUP received, reloading TLS material")
    ev.append((ROT, f"2026-09-03T01:10:04.118Z {host} quillmail/tlsmgr[1874]: loaded server certificate /etc/quillmail/tls/relay.pem subject=CN=mx-relay.jvb.internal issuer=CN=JVB Issuing CA G3 notAfter=2027-09-02"))
    ev.append((ROT + timedelta(milliseconds=2), f"2026-09-03T01:10:04.120Z {host} quillmail/tlsmgr[1874]: certificate chain length 1 (previous 2)"))
    add(ROT + timedelta(seconds=1), f"tlsmgr[{pid['tlsmgr']}]", "TLS reload complete, new sessions use updated material")
    add((t("2026-09-03 01:10:22") + timedelta(milliseconds=7)), f"smtpd[{pid['smtpd']}]", "connect from ops-jump01.jvb.internal[10.40.2.10]")
    add((t("2026-09-03 01:10:22") + timedelta(milliseconds=7)) + timedelta(milliseconds=51), f"smtpd[{pid['smtpd']}]", "STARTTLS ok from ops-jump01.jvb.internal[10.40.2.10] proto=TLSv1.3 cipher=TLS_AES_256_GCM_SHA384")
    add(t("2026-09-03 01:10:24"), f"smtpd[{pid['smtpd']}]", "disconnect from ops-jump01.jvb.internal[10.40.2.10] ehlo=2 starttls=1 quit=1")

    # first failure: verbatim anchor
    add(t("2026-09-03 01:12:47") + timedelta(milliseconds=499), f"smtpd[{pid['smtpd']}]", "connect from mailer-1.jvb.internal[10.40.12.21]")
    ev.append((t("2026-09-03 01:12:47"), f"2026-09-03T01:12:47.530Z {host} quillmail/smtpd[2211]: TLS handshake failed from mailer-1.jvb.internal[10.40.12.21]: peer sent alert unknown_ca (48)"))
    add(t("2026-09-03 01:12:47") + timedelta(milliseconds=600), f"smtpd[{pid['smtpd']}]", "lost connection after STARTTLS from mailer-1.jvb.internal[10.40.12.21]")
    d = t("2026-09-03 01:13:30")
    while d < t("2026-09-03 01:31:00"):
        d += timedelta(seconds=random.randint(50, 240))
        fail(d, *random.choice(mailers))
    # statement flood of failures, summarized
    d = t("2026-09-03 01:36:02")
    while d < t("2026-09-03 04:30:10"):
        fail(d, *random.choice(mailers))
        n = random.randint(9500, 12500)
        add(d + timedelta(seconds=4), f"smtpd[{pid['smtpd']}]", f"rate-limited logging: {n} similar session records suppressed in last 300s")
        d += timedelta(minutes=5)
    d = t("2026-09-03 04:31:00")
    while d < T1:
        d += timedelta(seconds=random.randint(200, 900))
        fail(d, *random.choice(mailers))

    # noise
    for _ in range(14):
        d = jitter(T0, T1)
        add(d, f"smtpd[{pid['smtpd']}]", f"warning: dnsbl lookup timed out for 198.51.100.{random.randint(2, 250)} (list=blk.greyfinch.example)")
    for _ in range(5):
        d = jitter(T0, T1)
        add(d, f"smtpd[{pid['smtpd']}]", "NOQUEUE: reject: RCPT from printer-3f.jvb.internal[10.40.77.3]: 554 5.7.1 relay access denied")
    add(t("2026-09-02 03:18:40"), f"housekeep[{pid['housekeep']}]", "warning: spool filesystem /var/spool/quillmail at 82% (threshold 80%)")
    add(t("2026-09-02 03:41:02"), f"housekeep[{pid['housekeep']}]", "spool filesystem /var/spool/quillmail at 64% after log compression")
    add(t("2026-09-03 03:19:55"), f"housekeep[{pid['housekeep']}]", "warning: spool filesystem /var/spool/quillmail at 81% (threshold 80%)")
    add(t("2026-09-03 03:42:10"), f"housekeep[{pid['housekeep']}]", "spool filesystem /var/spool/quillmail at 63% after log compression")
    add(t("2026-09-02 11:02:13"), f"smtpd[{pid['smtpd']}]", "warning: TLS handshake failed from vulnscan-02.jvb.internal[10.40.250.6]: no shared cipher")
    add(t("2026-09-02 11:02:14"), f"smtpd[{pid['smtpd']}]", "warning: TLS handshake failed from vulnscan-02.jvb.internal[10.40.250.6]: unsupported protocol SSLv3")
    add(t("2026-09-02 16:40:00"), f"qmgr[{pid['qmgr']}]", "deferred queue: 3 messages older than 4h (harbormail.example greylisting)")
    add(t("2026-09-02 21:00:00"), f"qmgr[{pid['qmgr']}]", "deferred queue: 0 messages")
    return ev


# ---------------------------------------------------------------- queue
def queue():
    ev = []

    def add(d, node, level, msg, **kw):
        d = ms(d)
        rec = {"ts": d.strftime("%Y-%m-%dT%H:%M:%S.") + "%03dZ" % (d.microsecond // 1000), "node": node, "level": level, "msg": msg}
        rec.update(kw)
        ev.append((d, json.dumps(rec)))

    def stmt_depth(d):
        return 0 if d >= t("2026-09-03 04:30:03") else progress(d)

    # periodic stats
    d = T0
    while d < T1:
        busy_prev = t("2026-09-02 01:30:00") <= d <= t("2026-09-02 03:05:00")
        busy_now = t("2026-09-03 01:30:00") <= d <= t("2026-09-03 04:35:00")
        step = 5 if (busy_prev or busy_now) else 15
        add(d, "lq-1", "info", "queue stats", queue="cards.auth.events", ready=random.randint(0, 40), unacked=random.randint(0, 20), publish_rate=round(random.uniform(3, 30), 1), ack_rate=round(random.uniform(3, 30), 1))
        add(d + timedelta(milliseconds=5), "lq-1", "info", "queue stats", queue="ledger.posting", ready=random.randint(0, 12), unacked=random.randint(0, 8), publish_rate=round(random.uniform(0.2, 6), 1), ack_rate=round(random.uniform(0.2, 6), 1))
        nd = 0 if d < ROT else int((d - ROT).total_seconds() / 400) + 1
        add(d + timedelta(milliseconds=9), "lq-2", "info", "queue stats", queue="notify.email.send", ready=nd, unacked=0 if nd == 0 else 1, publish_rate=round(random.uniform(0, 0.4), 2), ack_rate=0.0 if d >= ROT else round(random.uniform(0, 0.4), 2), redeliver_rate=0.0 if d < ROT else round(random.uniform(0.01, 0.1), 2))
        if busy_prev:
            add(d + timedelta(milliseconds=12), "lq-2", "info", "queue stats", queue="stmt.email.send", ready=random.randint(0, 60), unacked=16, publish_rate=round(random.uniform(7.2, 8.4), 1), ack_rate=round(random.uniform(7.2, 8.4), 1), redeliver_rate=0.0)
        elif busy_now:
            depth = stmt_depth(d)
            pub = 0.0 if d >= ALARM else (round(random.uniform(1.8, 2.4), 1) if t("2026-09-03 01:41:00") <= d <= t("2026-09-03 01:58:00") else round(random.uniform(7.3, 10.1), 1))
            if d < t("2026-09-03 01:30:09") or d >= t("2026-09-03 04:30:03"):
                pub = 0.0
            add(d + timedelta(milliseconds=12), "lq-2", "info", "queue stats", queue="stmt.email.send", ready=max(depth - 16, 0), unacked=16 if depth else 0, publish_rate=pub, ack_rate=0.0, redeliver_rate=round(random.uniform(10.5, 14.8), 1) if depth else 0.0)
        else:
            add(d + timedelta(milliseconds=12), "lq-2", "info", "queue stats", queue="stmt.email.send", ready=0, unacked=0, publish_rate=0.0, ack_rate=0.0, redeliver_rate=0.0)
        d += timedelta(minutes=step)

    # memory reports on lq-2
    d = t("2026-09-03 01:30:00")
    while d < t("2026-09-03 04:40:00"):
        depth = stmt_depth(d + timedelta(seconds=20))
        used = 0.21 + depth * 71500 / 2**30
        add(d + timedelta(seconds=20), "lq-2", "info", "memory", used_gib=round(used, 2), watermark_gib=2.6)
        d += timedelta(minutes=10)

    # redelivery traces on stmt and notify queues
    add(t("2026-09-03 01:12:48"), "lq-2", "warn", "message redelivered", queue="notify.email.send", consumer="mailer-1", attempt=2, last_error="smtp starttls mx-relay.jvb.internal:587: x509: certificate signed by unknown authority")
    ev.append((t("2026-09-03 01:12:48"), '{"ts": "2026-09-03T01:12:48.004Z", "node": "lq-2", "level": "info", "msg": "tracing sample", "queue": "notify.email.send", "note": "consumer reports errors via nack header x-last-error"}'))
    d = t("2026-09-03 01:14:00")
    while d < t("2026-09-03 01:30:00"):
        d += timedelta(seconds=random.randint(180, 320))
        add(d, "lq-2", "warn", "message redelivered", queue="notify.email.send", consumer=random.choice(["mailer-1", "mailer-2"]), attempt=random.randint(2, 7), last_error="smtp starttls mx-relay.jvb.internal:587: x509: certificate signed by unknown authority")
    add(t("2026-09-03 01:52:31"), "lq-2", "warn", "message dead-lettered", queue="notify.email.send", dlq="notify.email.dlq", attempts=8, reason="max delivery attempts (8) reached")
    d = t("2026-09-03 01:31:40")
    ev.append((d, '{"ts": "2026-09-03T01:31:40.662Z", "node": "lq-2", "level": "warn", "msg": "message redelivered", "queue": "stmt.email.send", "consumer": "mailer-2", "attempt": 3, "last_error": "smtp starttls mx-relay.jvb.internal:587: x509: certificate signed by unknown authority"}'))
    while d < t("2026-09-03 04:29:00"):
        d += timedelta(seconds=random.randint(420, 900))
        if d >= t("2026-09-03 04:30:00"):
            break
        add(d, "lq-2", "warn", "message redelivered", queue="stmt.email.send", consumer=random.choice(["mailer-1", "mailer-2"]), attempt=random.randint(4, 60), last_error="smtp starttls mx-relay.jvb.internal:587: x509: certificate signed by unknown authority")
    for day in ("2026-09-02", "2026-09-03"):
        add(t(day + " 01:30:09"), "lq-2", "info", "queue policy applied", queue="stmt.email.send", policy="stmt-outbound", max_delivery_attempts="unlimited", requeue_backoff="5s")

    # alarm
    ev.append((ALARM, '{"ts": "2026-09-03T02:47:13.402Z", "node": "lq-2", "level": "warn", "msg": "memory high watermark reached, blocking publishers", "used_gib": 2.61, "watermark_gib": 2.6}'))
    ev.append((ALARM + timedelta(milliseconds=3), '{"ts": "2026-09-03T02:47:13.405Z", "node": "lq-2", "level": "warn", "msg": "connection blocked", "connection": "stmt-render@bat-app04:51344", "reason": "resource alarm: memory"}'))
    for i in range(1, 6):
        add(ALARM + timedelta(minutes=20 * i), "lq-2", "warn", "memory alarm still active", used_gib=2.61, blocked_connections=1)
    ev.append((t("2026-09-03 04:30:03"), '{"ts": "2026-09-03T04:30:03.117Z", "node": "lq-2", "level": "info", "msg": "queue purged", "queue": "stmt.email.send", "messages": 36114, "requested_by": "stmt-render@bat-app04"}'))
    add(t("2026-09-03 04:30:04"), "lq-2", "info", "memory alarm cleared, unblocking publishers", used_gib=0.22, watermark_gib=2.6)
    add(t("2026-09-03 04:30:05"), "lq-2", "info", "connection closed", connection="stmt-render@bat-app04:51344")

    # noise
    ev.append((t("2026-09-02 23:48:02"), '{"ts": "2026-09-02T23:48:02.771Z", "node": "lq-1", "level": "error", "msg": "peer unreachable", "peer": "lq-3", "detail": "no heartbeat for 30s"}'))
    add(t("2026-09-02 23:48:03"), "lq-2", "error", "peer unreachable", peer="lq-3", detail="no heartbeat for 30s")
    add(t("2026-09-02 23:50:57"), "lq-3", "info", "rejoined cluster", after="top-of-rack switch tor-b7 link restored")
    add(t("2026-09-02 23:51:10"), "lq-1", "info", "cluster healthy", members=["lq-1", "lq-2", "lq-3"])
    for day in ("2026-09-02", "2026-09-03"):
        add(t(day + " 00:05:00"), "lq-1", "warn", "disk free below advisory", free_gib=12.4 if day.endswith("02") else 12.1, advisory_gib=15)
        add(t(day + (" 06:14:00" if day.endswith("02") else " 06:11:00")), "lq-1", "info", "disk free above advisory after segment compaction", free_gib=18.9 if day.endswith("02") else 18.6, advisory_gib=15)
        add(t(day + " 06:00:00"), "lq-2", "warn", "management listener certificate expires soon", days_remaining=42 if day.endswith("02") else 41)
    for _ in range(6):
        add(jitter(T0, T1), "lq-1", "warn", "consumer heartbeat timeout, cancelling", queue="cards.auth.events", consumer="cardsvc-%d" % random.randint(1, 9))
    add(t("2026-09-02 14:12:00"), "lq-1", "info", "policy updated", policy="cards-default", by="lqadmin", change="message_ttl 3600000 -> 1800000")
    return ev


# ---------------------------------------------------------------- scheduler
def scheduler():
    ev = []

    def add(d, level, msg):
        ev.append((d, f"[{d.strftime('%Y-%m-%d %H:%M:%S')} UTC] {level:<5} {msg}"))

    run_ids = iter(r for r in range(88090, 89000) if r != 88213)  # 88213 is the incident run

    def job(start, name, host, dur_s, rc=0, extra=None):
        rid = next(run_ids)
        add(start, "INFO", f"job={name} run={rid} state=STARTED host={host}")
        for off, level, m in (extra or []):
            add(start + timedelta(seconds=off), level, f"job={name} run={rid} {m}")
        end = start + timedelta(seconds=dur_s)
        state = "SUCCEEDED" if rc == 0 else "FAILED"
        add(end, "INFO" if rc == 0 else "ERROR", f"job={name} run={rid} state={state} rc={rc} elapsed={dur_s // 3600}h{(dur_s % 3600) // 60:02d}m{dur_s % 60:02d}s")
        return rid

    for day in ("2026-09-02", "2026-09-03"):
        prev = (datetime.strptime(day, "%Y-%m-%d") - timedelta(days=1)).strftime("%Y-%m-%d")
        base = datetime.strptime(prev, "%Y-%m-%d")
        if base >= datetime(2026, 9, 1):
            job(t(prev + " 23:05:00"), "BRANCH_CASH_POSITION", "bat-app01", random.randint(300, 600))
            job(t(prev + " 23:30:00"), "EOD_LEDGER_CLOSE", "bat-app02", random.randint(2700, 3300))
        job(t(day + " 00:15:00"), "DB_BACKUP_CORE_INCR", "bat-app03", random.randint(1500, 2100))
        job(t(day + " 00:45:00"), "STMT_EXTRACT", "bat-app04", 2280 if day.endswith("02") else 2231)
        add(t(day + " 01:29:58"), "INFO", "job=STMT_NIGHTLY dependency STMT_EXTRACT satisfied")
        if day.endswith("02"):
            job(t(day + " 01:30:00"), "STMT_NIGHTLY", "bat-app04", 5553, extra=[
                (1800, "INFO", "heartbeat progress=14000/41790"),
                (3600, "INFO", "heartbeat progress=28000/41790"),
                (5400, "INFO", "heartbeat progress=41500/41790"),
            ])
            add(t(day + " 03:02:40"), "INFO", "job=STMT_ARCHIVE_PUSH dependency STMT_NIGHTLY satisfied")
            job(t(day + " 03:02:41"), "STMT_ARCHIVE_PUSH", "bat-app04", 612)
        job(t(day + " 02:00:00"), "GL_RECON", "bat-app02", 44 if day.endswith("03") else 1210, rc=2 if day.endswith("03") else 0,
            extra=[(41, "ERROR", "stderr: input file /data/inbound/gl/GLX_20260902.dat not found")] if day.endswith("03") else None)
        if day.endswith("03"):
            add(t(day + " 02:00:45"), "INFO", "job=GL_RECON retry 1 of 2 scheduled at 02:30:00")
            add(t(day + " 02:21:17"), "INFO", "filewatch /data/inbound/gl: GLX_20260902.dat arrived (sftp from ledgerbridge, 48211904 bytes)")
            job(t(day + " 02:30:00"), "GL_RECON", "bat-app02", 1188)
        job(t(day + " 03:00:00"), "CARD_SETTLE_FILE", "bat-app01", random.randint(1400, 1900))
        job(t(day + " 04:00:00"), "AML_SCREEN_DELTA", "bat-app03", random.randint(2400, 3000))
        job(t(day + " 05:15:00"), "DB_BACKUP_CORE_VERIFY", "bat-app03", random.randint(900, 1300))
        job(t(day + " 06:30:00"), "BRANCH_OPEN_RATES_PUSH", "bat-app01", random.randint(60, 140))
        job(t(day + " 07:00:00"), "LOAN_DELINQ_REPORT", "bat-app02", random.randint(700, 1000))
        for _ in range(3):
            d = jitter(t(prev + " 23:00:00") if base >= datetime(2026, 9, 1) else t(day + " 00:00:00"), t(day + " 08:59:00"))
            add(d, "WARN", f"agent bat-app0{random.randint(1, 4)} clock offset {random.uniform(0.5, 1.4):.1f}s from ntp (tolerance 2.0s)")

    d = t("2026-09-01 23:20:00")
    while d < T1:
        job(d, "FX_RATES_PULL", "bat-app01", random.randint(8, 25))
        d += timedelta(minutes=30)
    d = t("2026-09-01 23:40:00")
    while d < T1:
        job(d, "ATM_JOURNAL_SWEEP", "bat-app03", random.randint(90, 240))
        d += timedelta(hours=1)

    # the incident run
    add(t("2026-09-03 01:30:00"), "INFO", "job=STMT_NIGHTLY run=88213 state=STARTED host=bat-app04 maxrun=3h00m")
    for hb in ("02:00:00", "02:30:00"):
        add(t("2026-09-03 " + hb), "INFO", f"job=STMT_NIGHTLY run=88213 heartbeat progress={progress(t('2026-09-03 ' + hb))}/41862")
    add(t("2026-09-03 03:00:00"), "INFO", "job=STMT_NIGHTLY run=88213 heartbeat progress=36114/41862")
    add(t("2026-09-03 03:30:00"), "WARN", "job=STMT_NIGHTLY run=88213 heartbeat progress=36114/41862 (no change in 2 intervals)")
    add(t("2026-09-03 04:00:00"), "WARN", "job=STMT_NIGHTLY run=88213 heartbeat progress=36114/41862 (no change in 3 intervals)")
    ev.append((KILL, "[2026-09-03 04:30:00 UTC] ERROR job=STMT_NIGHTLY run=88213 exceeded maxrun 3h00m, sending SIGTERM to pid 40517"))
    add(t("2026-09-03 04:30:08"), "ERROR", "job=STMT_NIGHTLY run=88213 state=TERMINATED rc=143 elapsed=3h00m08s")
    add(t("2026-09-03 04:30:09"), "WARN", "job=STMT_ARCHIVE_PUSH skipped: upstream STMT_NIGHTLY not SUCCEEDED")
    add(t("2026-09-03 04:30:09"), "INFO", "notify: page sent to rota stmt-ops for job=STMT_NIGHTLY run=88213")
    add(t("2026-09-03 08:12:31"), "INFO", "job=STMT_NIGHTLY run=88213 acknowledged by user=okafor.n comment=\"hold rerun, investigating with messaging team\"")
    return ev


# ---------------------------------------------------------------- renderer
def renderer():
    ev = []

    def add(d, level, comp, msg, **kw):
        extra = "".join(f' {k}="{v}"' if " " in str(v) else f" {k}={v}" for k, v in kw.items())
        d = ms(d)
        ev.append((d, f"time={d.strftime('%Y-%m-%dT%H:%M:%S.')}{d.microsecond // 1000:03d}Z level={level} component={comp} msg=\"{msg}\"{extra}"))

    def run(day, batch, total, end_published, sign_slow=None):
        s = t(day + " 01:30:02")
        add(s, "info", "main", "stmt-render 4.18.2 starting", pid=40517 if day.endswith("03") else 39880, host="bat-app04")
        add(s + timedelta(seconds=1), "info", "config", "loaded /etc/stmt-render/render.yaml", profile="nightly")
        add(s + timedelta(seconds=1), "info", "config", "outbound target", broker="lanternq://lq-2.jvb.internal:5672", queue="stmt.email.send", on_abort="purge_outbound")
        add(s + timedelta(seconds=2), "warn", "template", "template footer_v6 is deprecated, footer_v7 available", template="retail_monthly")
        add(s + timedelta(seconds=3), "info", "batch", "batch opened", batch=batch, accounts=total, source="STMT_EXTRACT")
        add(s + timedelta(seconds=7), "info", "publisher", "connected to broker", conn=f"stmt-render@bat-app04:{51344 if day.endswith('03') else 50912}")
        return s

    # previous night: clean
    s = run("2026-09-02", "B-20260902", 41790, 41790)
    for i, n in enumerate(range(500, 41790, 500)):
        add(s + timedelta(seconds=10 + i * 65 + random.randint(0, 5)), "info", "batch", "progress", batch="B-20260902", rendered=n, published=n - random.randint(0, 9))
    add(t("2026-09-02 03:02:31"), "info", "batch", "progress", batch="B-20260902", rendered=41790, published=41790)
    add(t("2026-09-02 03:02:33"), "info", "batch", "batch completed", batch="B-20260902", published=41790, skipped_no_email=73, state="COMPLETED")
    add(t("2026-09-02 03:02:34"), "info", "main", "exit 0")

    # incident night
    s = run("2026-09-03", "B-20260903", 41862, 36114)
    for n in range(500, 36114, 500):
        for (a, x), (b, y) in zip(PROG, PROG[1:]):
            if x <= n <= y:
                d = a + timedelta(seconds=(b - a).total_seconds() * (n - x) / (y - x))
        add(d, "info", "batch", "progress", batch="B-20260903", rendered=n, published=n)
    add(t("2026-09-03 01:41:06"), "warn", "signer", "PDF signing latency high", p95_ms=2810, hsm="hsm-a.jvb.internal")
    add(t("2026-09-03 01:44:40"), "warn", "signer", "hsm-a returned 503 maintenance, failing over", target="hsm-b.jvb.internal")
    add(t("2026-09-03 01:44:52"), "info", "signer", "signing via hsm-b", p95_ms=1960)
    add(t("2026-09-03 01:57:48"), "info", "signer", "PDF signing latency normal", p95_ms=118, hsm="hsm-b.jvb.internal")
    for _ in range(9):
        add(jitter(s, ALARM), "info", "batch", "account skipped", reason="no deliverable email on file", acct="****%04d" % random.randint(0, 9999))
    for _ in range(4):
        add(jitter(s, KILL), "warn", "jvm", "GC pause exceeded 200ms", pause_ms=random.randint(210, 380), heap_used_pct=random.randint(61, 78))
    for _ in range(3):
        add(jitter(t("2026-09-02 01:30:10"), t("2026-09-02 03:00:00")), "warn", "jvm", "GC pause exceeded 200ms", pause_ms=random.randint(210, 340), heap_used_pct=random.randint(58, 74))
    add(t("2026-09-03 02:12:09"), "warn", "template", "font fallback used for glyph", font="JVB Sans", glyph="U+20B9", acct="****8830")

    ev.append((ALARM + timedelta(seconds=1), 'time=2026-09-03T02:47:14.019Z level=warn component=publisher msg="broker blocked connection" reason="resource alarm: memory" conn=stmt-render@bat-app04:51344'))
    add(ALARM + timedelta(seconds=2), "info", "batch", "render workers paused, outbound buffer full", batch="B-20260903", rendered=36114, published=36114)
    d = ALARM
    while d + timedelta(minutes=10) < KILL:
        d += timedelta(minutes=10)
        mins = int((d - ALARM).total_seconds() // 60)
        add(d, "warn", "publisher", "publish still blocked", blocked_for=f"{mins}m", batch="B-20260903", published=36114, remaining=5748)
    ev.append((KILL + timedelta(milliseconds=400), 'time=2026-09-03T04:30:00.412Z level=warn component=main msg="SIGTERM received, aborting batch"'))
    add(KILL + timedelta(seconds=2), "info", "batch", "on_abort=purge_outbound: requesting purge of stmt.email.send", batch="B-20260903")
    ev.append((KILL + timedelta(seconds=4), 'time=2026-09-03T04:30:04.006Z level=error component=batch msg="batch failed" batch=B-20260903 state=FAILED reason=terminated published=36114 purged=36114 delivered_confirmed=0'))
    add(KILL + timedelta(seconds=6), "info", "main", "exit 143")
    return ev


def write(path, ev):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    ev = [e for e in ev if T0 <= e[0] < T1]
    ev.sort(key=lambda e: re.search(r"\d{4}-\d\d-\d\d[T ]\d\d:\d\d:\d\d(\.\d{3})?", e[1]).group(0).replace("T", " ").ljust(23, "0"))
    with open(path, "w") as f:
        f.write("\n".join(line for _, line in ev) + "\n")
    print(path, len(ev))


write(os.path.join(OUT, "mail-relay", "mx-relay01.log"), relay())
write(os.path.join(OUT, "message-queue", "lanternq-cluster.jsonl"), queue())
write(os.path.join(OUT, "batch-scheduler", "tidewell.log"), scheduler())
write(os.path.join(OUT, "statement-renderer", "stmt-render.log"), renderer())
