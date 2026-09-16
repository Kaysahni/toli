Varnholt pricing survey, wave 3 (June to July 2026): codebook
============================================================

Fielded by Tallow Research Panels on behalf of Varnholt Growth.
Field dates: 8 June 2026 to 16 July 2026. Owner on our side: Duc Anh Vo.

File: survey-results.csv (one row per respondent who opened the survey)

Columns
-------

response_id        Panel ID, prefix VR-. Not linkable to Varnholt accounts.
started_at         Local panel server time (UTC), YYYY-MM-DD HH:MM.
country            ISO 3166 alpha-2. Wave 3 covered DE, BR, JP, plus small
                   FR and MX boosts that were requested by the EMEA and
                   LATAM teams for a separate study.
seg_code           Assigned by the screener (Q1 and Q2):
                     S1 = student (enrolled full or part time)
                     S2 = independent professional (self-employed,
                          freelancer, sole practitioner)
                     S3 = small team (respondent works in an organization
                          of 2 to 20 people and would buy for the team)
                   Blank when the respondent was screened out.
role_text          Free text from Q2, lightly cleaned. Do not re-code
                   segments from this field; the screener logic is final.
status             complete      finished all 14 questions
                   partial       closed the survey before Q14
                   screened_out  did not match any segment
q7_pay_intent      "Would you pay for Varnholt Plus at [local test price]
                   per month?"
                     5 = definitely would pay
                     4 = probably would pay
                     3 = not sure
                     2 = probably would not pay
                     1 = definitely would not pay
                   Blank if the respondent left before Q7.
q3_current_tool    What they use for notes today (free text, cleaned).
q12_open_comment   Optional open comment. Only shown to people who reach Q12.

Local test prices
-----------------

DE: EUR 7.49 per month
BR: BRL 24.90 per month
JP: JPY 1,080 per month
FR and MX: see the separate EMEA/LATAM study.

Notes
-----

- Partial responses are kept in the file because the panel invoices us for
  them, not because they are analysis-ready. A partial respondent may have
  answered Q7 and then quit, often right after the price question.
- Weighting: none applied. Quotas were set per country and segment.
- Row order is by start time.
