"""Generates fixture/survey/survey-results.csv and fixture/support-tickets-by-region.csv.
Deterministic. Asserts the segment reachability numbers used in checklist.json."""
import csv, random, datetime, os
from collections import defaultdict

R = random.Random(20260716)
HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "..", "fixture")

# (country, seg): (complete_n, complete_yes, partial_n, partial_yes)
PLAN = {
    ("DE", "S1"): (80, 33, 8, 2), ("DE", "S2"): (60, 23, 6, 1), ("DE", "S3"): (50, 11, 5, 1),
    ("BR", "S1"): (90, 47, 10, 4), ("BR", "S2"): (70, 26, 25, 3), ("BR", "S3"): (55, 10, 6, 1),
    ("JP", "S1"): (70, 20, 9, 3), ("JP", "S2"): (65, 29, 7, 2), ("JP", "S3"): (60, 28, 8, 3),
    ("FR", "S1"): (22, 9, 3, 1), ("FR", "S2"): (18, 6, 2, 0), ("FR", "S3"): (15, 5, 1, 0),
    ("MX", "S1"): (25, 12, 2, 1), ("MX", "S2"): (14, 4, 3, 1), ("MX", "S3"): (11, 2, 1, 0),
}
ROLES = {
    "S1": ["undergraduate, engineering", "master's student", "law student", "medical student",
           "PhD candidate", "high school senior", "nursing student", "undergrad, history",
           "exchange student", "MBA student", "design school"],
    "S2": ["freelance translator", "independent consultant", "self-employed architect",
           "freelance journalist", "solo UX designer", "tax advisor, own practice",
           "freelance developer", "photographer", "illustrator", "therapist, private practice",
           "sole trader, bookkeeping"],
    "S3": ["agency, 6 people", "startup, 12 staff", "dental practice team of 4", "small law firm (9)",
           "family business, 15 employees", "research group of 7", "marketing studio, 3 people",
           "NGO office, 18", "engineering consultancy, 11", "cafe chain back office (5)"],
}
COMMON_TOOLS = ["paper notebook", "Notes app that came with phone", "shared docs", "email to self", "none", "spreadsheet", ""]
TOOLS = {
    "DE": COMMON_TOOLS + ["Notiztafel", "Notiztafel", "Blattwerk", "office suite notes"],
    "BR": COMMON_TOOLS + ["Cadernia", "Cadernia", "Anotaki", "WhatsApp notes to self"],
    "JP": COMMON_TOOLS + ["Kumonote", "Kumonote", "Fudebako", "Shiori Works Memo"],
    "FR": COMMON_TOOLS + ["office suite notes"],
    "MX": COMMON_TOOLS + ["WhatsApp notes to self"],
}
COMMENTS = ["", "", "", "", "price matters most", "need offline mode", "would want handwriting support",
            "team sharing is key for us", "please support local payment methods", "too many apps already",
            "want export to PDF", "sync was the problem with my last app", "only if cheaper than current tool",
            "", "love the web clipper idea", "need it in my language"]

rows = []
def intent(yes):
    return R.choice(["4", "5"]) if yes else R.choice(["1", "2", "2", "3", "3", "3"])

start = datetime.datetime(2026, 6, 8, 7, 0)
for (c, s), (cn, cy, pn, py) in PLAN.items():
    for i in range(cn):
        rows.append([c, s, "complete", intent(i < cy)])
    for i in range(pn):
        rows.append([c, s, "partial", intent(i < py)])
    # partial rows that dropped out before q7: blank intent
    for i in range(R.randint(1, 4)):
        rows.append([c, s, "partial", ""])
for c in ["DE", "BR", "JP", "FR", "MX"]:
    for i in range(R.randint(4, 9)):
        rows.append([c, "", "screened_out", ""])
R.shuffle(rows)

out = []
for n, (c, s, st, q7) in enumerate(rows, 1):
    ts = start + datetime.timedelta(minutes=R.randint(0, 60 * 24 * 38))
    role = R.choice(ROLES[s]) if s else R.choice(["retired", "not currently working", "prefer not to say"])
    tool = R.choice(TOOLS[c]) if st != "screened_out" else ""
    com = R.choice(COMMENTS) if st == "complete" else ""
    out.append([f"VR-{26000 + n}", ts.strftime("%Y-%m-%d %H:%M"), c, s, role, st, q7, tool, com])
out.sort(key=lambda r: r[1])
with open(os.path.join(FIX, "survey", "survey-results.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["response_id", "started_at", "country", "seg_code", "role_text", "status", "q7_pay_intent", "q3_current_tool", "q12_open_comment"])
    w.writerows(out)

# verify
agg = defaultdict(lambda: [0, 0, 0, 0])
for r in out:
    c, s, st, q7 = r[2], r[3], r[5], r[6]
    if not s or q7 == "":
        continue
    a = agg[(c, s)]
    y = q7 in ("4", "5")
    if st == "complete":
        a[0] += 1; a[1] += y
    a[2] += 1; a[3] += y
for c in ["DE", "BR", "JP"]:
    for s in ["S1", "S2", "S3"]:
        a = agg[(c, s)]
        print(c, s, f"complete {a[1]}/{a[0]} = {100*a[1]/a[0]:.1f}%", f"| incl partial {a[3]}/{a[2]} = {100*a[3]/a[2]:.1f}%")
comp = {k: v[1] / v[0] >= 0.35 for k, v in agg.items()}
allr = {k: v[3] / v[2] >= 0.35 for k, v in agg.items()}
assert [comp[("DE", s)] for s in "S1 S2 S3".split()] == [True, True, False]
assert [comp[("BR", s)] for s in "S1 S2 S3".split()] == [True, True, False]
assert [comp[("JP", s)] for s in "S1 S2 S3".split()] == [False, True, True]
assert allr[("BR", "S2")] is False  # the partial-response trap
assert allr[("DE", "S2")] and allr[("JP", "S2")] and allr[("JP", "S3")] and not allr[("JP", "S1")]

# support tickets
REG = [("EMEA-DE", "de", 34), ("LATAM-BR", "pt-BR", 29), ("APAC-JP", "ja", 47), ("NA-US", "en", 38), ("EMEA-FR", "fr", 14), ("EMEA-UK", "en", 16)]
BILLING_EXTRA = {"EMEA-DE": ["VAT number on receipt"], "EMEA-FR": ["VAT number on receipt"], "EMEA-UK": ["VAT number on receipt"],
                 "LATAM-BR": ["Charged in USD, bank added IOF"], "APAC-JP": ["Need a qualified invoice for my company"], "NA-US": ["Sales tax on receipt"]}
PAYMENTS = {"EMEA-DE": ["Local payment method not accepted", "SEPA direct debit"],
            "EMEA-FR": ["Local payment method not accepted", "SEPA direct debit"],
            "EMEA-UK": ["Direct Debit instead of card"],
            "LATAM-BR": ["Local payment method not accepted", "Pix support?", "Boleto option"],
            "APAC-JP": ["Local payment method not accepted", "Konbini payment option", "Carrier billing"],
            "NA-US": ["PayPal instead of card", "Apple Pay on web"]}
SUBJ = {
    "billing": ["Charged twice this month", "Can I pay by invoice?", "Refund for annual plan", "Card declined at renewal"],
    "sync": ["Notes not syncing to tablet", "Conflict copies keep appearing", "Sync stuck at 94%", "Lost edits after offline session"],
    "localization": ["Is the app available in my language?", "Date format shows US style", "Spellcheck ignores my language", "Keyboard input issue with IME", "Help articles only in English"],
    "feature_request": ["Handwriting recognition please", "Tags inside shared notebooks", "Calendar integration", "Export to Markdown", "Dark mode on web"],
    "account": ["Cannot reset password", "Merge two accounts", "Delete my account", "Change login email"],
    "payments": [],
}
rows = []
tid = 88100
for reg, lang, n in REG:
    for _ in range(n):
        cat = R.choice(list(SUBJ))
        if reg == "APAC-JP" and R.random() < 0.35:
            cat = "localization"
        tid += R.randint(1, 9)
        d = datetime.date(2026, 4, 1) + datetime.timedelta(days=R.randint(0, 150))
        subjects = SUBJ[cat] + (BILLING_EXTRA[reg] if cat == "billing" else PAYMENTS[reg] if cat == "payments" else [])
        if reg in ("NA-US", "EMEA-UK") and cat == "localization":
            subjects = ["Date format shows US style", "Spellcheck flags British spelling"] if reg == "EMEA-UK" else ["Spellcheck in Spanish notes"]
        if reg != "APAC-JP":
            subjects = [x for x in subjects if "IME" not in x]
        rows.append([d.isoformat(), reg, lang, cat, R.choice(subjects), R.choice(["Free", "Free", "Plus", "Plus", "Team"]), R.choice(["solved", "solved", "solved", "open", "pending"])])
rows.sort()
with open(os.path.join(FIX, "support-tickets-by-region.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ticket_id", "created", "region", "customer_language", "category", "subject", "plan", "status"])
    for i, r in enumerate(rows):
        w.writerow([f"T-{88100 + i * 3 + 1}"] + r)
print("tickets", len(rows), "survey rows", len(out))
