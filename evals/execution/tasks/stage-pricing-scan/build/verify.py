import json, re, pathlib
T = pathlib.Path(__file__).resolve().parent.parent
F = T / "fixture"
ck = json.loads((T / "checklist.json").read_text())
bad = 0
for item in ck["findings"] + ck["exclusions"]:
    for ev in item["evidence"]:
        if ev["quote"] not in (F / ev["file"]).read_text():
            print("MISSING", item["id"], ev["file"], repr(ev["quote"])); bad += 1
for p in list(T.rglob("*")):
    if p.is_file() and re.search("[" + chr(0x2013) + chr(0x2014) + "]", p.read_text()):
        print("DASH", p); bad += 1
# classify each deal note by its LAST reason/outcome statement
cls = {}
for p in sorted((F / "winloss").iterdir()):
    t = p.read_text().lower()
    if re.search(r"closed_won|\bwon\b|closed won|outcome: won", t) and "lost" not in t.split("\n")[0] and not re.search(r"closed.lost|result: lost|\(lost|lost to|loss", t):
        cls[p.name] = "win"; continue
    if "no decision" in t and not re.search(r"lost to|closed lost|closed_lost", t):
        cls[p.name] = "no_decision"; continue
    hits = [(m.start(), k) for k, pat in [("seat", r"seat pric|seat price|seat cost|pricing_seats|price: seats|seat pricing"),
                                          ("feature", r"missing feature"), ("build", r"build_in_house")]
            for m in re.finditer(pat, t) if not t[max(0, m.start()-10):m.start()].count("not a")]
    reason_lines = [h for h in hits]
    cls[p.name] = max(reason_lines)[1] if reason_lines else "?"
from collections import Counter
print(cls); c = Counter(cls.values()); print(c)
f8 = {e["file"].split("/")[-1] for e in ck["findings"][7]["evidence"]}
f9 = {e["file"].split("/")[-1] for e in ck["findings"][8]["evidence"]} - {"bellhaven-foods.yaml"}
assert f8 == {k for k, v in cls.items() if v == "seat"}, "F8 mismatch"
assert f9 == {k for k, v in cls.items() if v == "feature"}, "F9 mismatch"
assert c["seat"] == 7 and c["feature"] == 3 and c["build"] == 1 and c["win"] == 5 and c["no_decision"] == 2
print("OK" if not bad else f"{bad} problems")
