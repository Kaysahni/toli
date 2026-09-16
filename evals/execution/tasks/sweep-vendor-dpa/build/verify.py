import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
ck = json.loads((root / "checklist.json").read_text())
bad = 0
for item in ck["findings"] + ck["exclusions"]:
    for ev in item["evidence"]:
        if ev["quote"] not in (root / "fixture" / ev["file"]).read_text():
            print("MISSING", item["id"], ev["file"], ev["quote"][:60]); bad += 1
for f in root.rglob("*"):
    if f.is_file() and any(chr(c) in f.read_text() for c in (0x2013, 0x2014)):
        print("DASH", f); bad += 1
files = [f for f in (root / "fixture").rglob("*") if f.is_file()]
print(len(files), "fixture files,", sum(len(f.read_text().split()) for f in files), "words,",
      len(ck["findings"]), "findings,", len(ck["exclusions"]), "exclusions,", bad, "problems")
sys.exit(bad)
