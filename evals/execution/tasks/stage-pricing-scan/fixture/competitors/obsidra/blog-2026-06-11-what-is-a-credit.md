---
title: "What exactly is a compute credit?"
author: Sunniva Adeyemi, Solutions Engineering
published: 2026-06-11
---

This is the question we get most on sales calls, so here is a plain answer with examples.

A compute credit is one unit of query work on Obsidra's engine. Roughly, one credit covers scanning about 25 GB of compressed data, or about 30 seconds of a medium-sized query cluster, whichever comes first. Cached results cost nothing, which matters a lot: most dashboard views hit the cache.

## Three real-ish examples

**A marketing team of 12.** Eight dashboards refreshed hourly during business hours, maybe 40 ad hoc queries a day. Typical usage: 90 to 130 credits a month.

**A company-wide KPI rollout, 400 viewers.** Five core dashboards refreshed every 15 minutes, everyone opens them a few times a week. Because views mostly hit the cache, this lands around 350 credits a month, which fits in Launch.

**A data science team running heavy exploratory SQL.** This is where credits add up. We have seen 1,500 to 3,000 credits a month for teams of six or seven people. Scale is the better fit.

## How to keep usage predictable

- Set a monthly credit budget with an alert at 80%.
- Use materialized views for your most-viewed dashboards.
- Check the credit usage page, which now lists your most expensive queries.

If you are going past your plan, extra credits cost $0.40 each. We will never cut off dashboards mid-month; we just bill the overage.

Questions? Book 20 minutes with a solutions engineer from the pricing page.
