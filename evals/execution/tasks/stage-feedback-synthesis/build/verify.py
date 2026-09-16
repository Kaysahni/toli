"""Check every checklist quote is verbatim in its file and no file has an em or en dash."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASHES = (chr(0x2014), chr(0x2013))
ck = json.loads((ROOT / "checklist.json").read_text())
bad = []
for item in ck["findings"] + ck["exclusions"]:
    for ev in item["evidence"]:
        if ev["quote"] not in (ROOT / "fixture" / ev["file"]).read_text():
            bad.append(f"{item['id']}: quote not found in {ev['file']}: {ev['quote']}")
for p in ROOT.rglob("*"):
    if p.is_file() and "__pycache__" not in p.parts:
        t = p.read_text()
        if any(d in t for d in DASHES):
            bad.append(f"dash in {p.relative_to(ROOT)}")
print("\n".join(bad) or "all quotes verbatim, no em/en dashes")
sys.exit(1 if bad else 0)
