# Stage 00: preflight and sources (almost no model use)

1. Run `bash scripts/preflight.sh`. Fix anything it reports as missing (it installs Python packages into .venv; if pdftotext is missing, ask the user to run `brew install poppler` only if a slide text extraction looks empty).
2. Run `.venv/bin/python scripts/collect.py`. It copies Sessions 15 to 22, the Midterm 2 module files, and S5 to S10 refresher text into sources/raw. It will report S21 and S22 files as not found yet. That is expected.
3. Run `.venv/bin/python scripts/extract.py`. Then open sources/index.md and confirm every S15, S16, S18, S19, S20 slide deck and exercise has text. Note the low-text slide pages for later.
4. Run `.venv/bin/python scripts/objectives.py`. Expect 51 objectives: S15 11, S16 6, S18 10, S19 6, S20 8, S21 6, S22 4. If counts differ, stop and report.
5. Run `.venv/bin/python scripts/import_quizzes.py`. Expect 25 professor questions (5 reading quiz questions each for S15, S16, S18, S19, S20). Open one S18 file and confirm the multi answer question has type multi.
6. Write reference/exam-facts.md (one page): exam scope, format from sources/text/S23_*Overview*, equation sheet contents (read sources/text/S23_Equation_Sheet*), topic weights from config.json.
7. Add a .gitignore containing `.venv/`, `node_modules/`, `sources/raw/`. Commit: "stage 00".
8. Update STATUS.md. Print a five line summary.
