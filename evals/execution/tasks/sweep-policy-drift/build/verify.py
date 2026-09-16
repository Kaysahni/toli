import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
fx = root / "fixture"
ck = json.loads((root / "checklist.json").read_text())
bad = 0
for item in ck["findings"] + ck["exclusions"]:
    for ev in item["evidence"]:
        if ev["quote"] not in (fx / ev["file"]).read_text():
            print("MISSING", item["id"], ev["file"], ev["quote"]); bad += 1
for p in root.rglob("*"):
    if p.is_file() and any(c in p.read_text() for c in ""+chr(0x2013)+chr(0x2014)+""):
        print("DASH", p); bad += 1
print("files", sum(1 for p in fx.rglob("*") if p.is_file()), "bad", bad)
sys.exit(bad)
