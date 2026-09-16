import json, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fix = os.path.join(root, "fixture")
ck = json.load(open(os.path.join(root, "checklist.json")))
bad = 0
for sec in ("findings", "exclusions"):
    for item in ck[sec]:
        for ev in item["evidence"]:
            if ev["quote"] not in open(os.path.join(fix, ev["file"]), encoding="utf-8").read():
                print("MISSING", item["id"], ev["file"], ev["quote"][:60]); bad += 1
words = files = 0
for d, _, fs in os.walk(root):
    for f in fs:
        p = os.path.join(d, f)
        t = open(p, encoding="utf-8").read()
        if chr(0x2014) in t or chr(0x2013) in t:
            print("DASH", p); bad += 1
        if p.startswith(fix):
            files += 1; words += len(t.split())
print("fixture files", files, "words", words, "problems", bad)
sys.exit(bad)
