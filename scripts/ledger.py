#!/usr/bin/env python3
"""Merge one session's entries into coverage/slide-ledger.json.
Usage: python3 scripts/ledger.py S15 < entries.json   where entries = {"<source>": {"<page or section>": {"los": [...], "reason": "..."}}}"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
f = HERE / "coverage" / "slide-ledger.json"
led = json.loads(f.read_text()) if f.exists() else {}
led[sys.argv[1]] = json.load(sys.stdin)
f.write_text(json.dumps(led, indent=1, ensure_ascii=False))
print(sys.argv[1], {k: len(v) for k, v in led[sys.argv[1]].items()})
