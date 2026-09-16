# Onboarding a new API partner

Owner: Partner Integrations

Since January 2025 all new partners use the v3 partner API behind
`api.tesselwick.example`. Do not give partners direct access to internal
hostnames, allowlisted IP ranges or static API keys. Existing exceptions are
tracked in `integrations.csv` and each has an owner.

## Checklist

- [ ] Signed data processing agreement on file
- [ ] Partner record created, status `onboarding`
- [ ] OAuth client created in the partner realm, scopes limited to what they need
- [ ] Sandbox credentials sent through the secure share tool
- [ ] Partner has completed the sandbox test script (booking, quote, cancel)
- [ ] Rate limits agreed (default 600 rpm)
- [ ] Production credentials issued
- [ ] Status changed to `pilot` or `active`, `last_reviewed` updated
- [ ] Technical contact added to the partner status mailing list

## Offboarding

Revoke the OAuth client, set status to `terminated <date>`, and open a NET
ticket for any firewall rules. Keep the row for audit.
