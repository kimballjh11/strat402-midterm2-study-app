#!/usr/bin/env bash
# Checks tools, creates a private Python environment, installs the few packages the scripts need.
set -u
cd "$(dirname "$0")/.."
echo "python3: $(python3 -V 2>&1)"; echo "node: $(node -v 2>&1)"; echo "npm: $(npm -v 2>&1)"; echo "git: $(git version 2>&1)"
if command -v pdftotext >/dev/null; then echo "pdftotext: ok"; else echo "pdftotext: missing (optional, pypdf is the fallback; 'brew install poppler' improves slide text)"; fi
if command -v pdftoppm >/dev/null; then echo "pdftoppm: ok (can render slide pages to images)"; else echo "pdftoppm: missing (optional, only needed to view figure-heavy slides)"; fi
[ -d .venv ] || python3 -m venv .venv
.venv/bin/python -m pip install -q beautifulsoup4 openpyxl pypdf python-docx && echo "python packages: ok"
[ -d .git ] || (git init -q && echo "git repo created")
