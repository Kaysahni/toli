# Change Calendar: Technology Operations

Owner: Change Advisory Board (CAB). Exported from the change register on 2026-09-03 at 12:05.

**All times below are US Eastern (EDT, UTC-4) unless stated otherwise.** Status values: Scheduled, Completed, Completed with issues, Postponed, Cancelled.

Freeze reminder: no production changes to core ledger or card authorization between 2026-09-28 and 2026-10-02 (quarter end).

---

## Week of Monday 2026-08-31

### Mon 2026-08-31

**CHG-4455** · POS acquiring gateway: apply vendor firmware 11.4 to gw-pos-a and gw-pos-b
- Window: 22:00 to 23:30
- Implementer: Lucia Brandvold (Payments Infrastructure)
- Risk: Medium. Rolling, one gateway at a time.
- Status: Completed. gw-pos-b took two attempts (first reboot hung at POST, power cycled via iLO).

**CHG-4457** · Intranet: publish new expense policy page
- Window: 12:00 to 12:15
- Implementer: Marta Vickery (Internal Comms)
- Risk: Low
- Status: Completed

### Tue 2026-09-01

**CHG-4460** · Branch teller workstations: monthly OS patch ring 2 (Westbrook, Holm Ferry, Caddon Mills branches)
- Window: 19:30 to 23:00
- Implementer: Desktop Engineering rota
- Risk: Low
- Status: Completed. 3 workstations at Holm Ferry deferred (powered off).

**CHG-4461** · Online banking: raise session idle timeout from 10 to 15 minutes
- Window: 06:00 to 06:10
- Implementer: Anand Sethuraman
- Risk: Low. Approved by Digital Risk (ticket DR-1182).
- Status: Completed

### Wed 2026-09-02

**CHG-4464** · Lanternq cluster: shorten message TTL on the `cards-default` policy from 60 to 30 minutes
- Window: 10:00 to 10:30
- Implementer: Pieter Osei (Integration Platform)
- Affects: queues bound to `cards-default` only (card authorization events). No other policies touched.
- Risk: Low
- Status: Completed at 10:12.

**CHG-4466** · Tidewell scheduler: patch agents on bat-app01 to bat-app04 to 5.2.1
- Requested window: 22:00 to 23:00
- Implementer: Greta Lindqvist (Batch Operations)
- Risk: Medium. Agents restart; running jobs are drained first.
- Status: **Postponed.** Vendor pulled 5.2.1 on 2026-09-01 over a cron parsing regression. New window Thu 2026-09-10 22:00, pending 5.2.2.

**CHG-4471** · Outbound mail relay: annual TLS server certificate rotation (mx-relay01 active, mx-relay02 standby)
- Window: 21:00 to 21:30
- Implementer: Dario Pelletier (Messaging & Collaboration)
- Reason: current certificate expires 2026-09-16. New certificate issued by JVB Issuing CA G3 via the internal PKI portal.
- Plan: copy new PEM to /etc/quillmail/tls/relay.pem, send SIGHUP to quillmail, verify STARTTLS. Standby relay updated in the same window, not reloaded (not in service).
- Reload quillmail TLS on mx-relay01 at 21:10.
- Post check: STARTTLS test from ops-jump01 OK.
- Rollback: previous PEM kept at /etc/quillmail/tls/relay.pem.2025
- Risk: Low
- Status: Completed

**CHG-4472** · HSM pool: hsm-a firmware maintenance (hsm-b carries signing load during the window)
- Window: 21:40 to 22:00
- Implementer: Oskar Faulkner (Cryptographic Services)
- Risk: Low. Clients fail over automatically; expect higher signing latency for a few minutes.
- Status: Completed. hsm-a back in pool at 21:58.

**CHG-4473** · Branch network: replace DNS forwarders at regional hubs North and Coastal
- Window: 23:00 to 23:45
- Implementer: Network Engineering rota (lead: Samir Haddad)
- Affects: branch LAN name resolution only. Data center resolvers unchanged.
- Risk: Medium
- Status: Completed. Coastal hub cutover 11 minutes late, no customer impact reported.

### Thu 2026-09-03

**CHG-4476** · Data warehouse: add nightly partition for `txn_fact_2026_09`
- Window: 01:00 to 01:15
- Implementer: automated (dw-maint)
- Risk: Low
- Status: Completed

**CHG-4478** · Mobile app: staged rollout of release 7.31 to 20% of Android users
- Window: 09:00
- Implementer: Mobile Release Train
- Risk: Low
- Status: Scheduled

### Fri 2026-09-04

**CHG-4469** · Corporate Wi-Fi: rotate guest SSID pre-shared key (HQ and Harlow Street)
- Window: 07:00 to 07:15
- Implementer: Samir Haddad
- Risk: Low
- Status: Scheduled

---

## Week of Monday 2026-09-07 (draft, not yet reviewed by CAB)

- **CHG-4481** Mon 2026-09-07: bank holiday. No changes.
- **CHG-4466** Thu 2026-09-10 22:00: Tidewell agent patch (moved from 2026-09-02), pending vendor 5.2.2.
- **CHG-4483** Thu 2026-09-10 21:00: Lanternq cluster: add fourth node lq-4 (capacity planning item CP-77). Owner Pieter Osei.
- **CHG-4484** Sat 2026-09-12 02:00: Core ledger database: minor version upgrade on the reporting replica only.

## Notes from CAB, 2026-08-27

Approved all Low risk items for the week of 2026-08-31 in bulk. Asked Network Engineering for a written rollback for CHG-4473 before Wednesday; received 2026-08-31. Reminder to implementers that "Completed" must be set in the register within one business day of the window.
