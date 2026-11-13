# STRAT 402 Midterm 2 study app: project rules

Goal: a dark, minimal, local web app that teaches a student Sessions 15 to 22 of BYU STRAT 402 (Economics of Strategy) from zero and drills him until every learning objective is mastered. No gamification. Fewest possible clicks. He knows nothing about the content, so lessons start from zero. Exam: Midterm Exam 2, covers Sessions 15 to 22 only, no Excel, scientific or financial calculator, equation sheet only.

Read BUILD-GUIDE.md for decisions and schemas. Read STATUS.generated.md (run `.venv/bin/python scripts/validate.py`) to see what is done. Work one objective at a time and commit after each session.

## Hard rules
- Ground truth is the professor's material in sources/text and sources/quizzes: slides, in-class exercises, reading quizzes, comprehension quizzes, study guide. The files named "Textbook Study Notes" are Claude-made summaries: use them for explanation, but check every formula, number and claim against professor material before it goes into a lesson or answer key. Never invent a statement about what the professor said.
- Professor questions are imported by script, verbatim (scripts/import_quizzes.py). Never retype them.
- Every calculation question needs a worked solution a student can do by hand with a calculator. Show calculus steps. Never rely on Excel or Solver in an answer.
- Every calculation LO needs at least one parametric generator in content/generators and an independent Python check in verify/.
- Flag formulas that are NOT on the equation sheet (the sheet has HHI, elasticity, AFC, AVC, ATC, MC, MP, AP, MRTS, isocost slope only). Everything else must be derivable or memorized, and lessons must say which.
- Lessons: plain English first, then definition, formula, derivation, worked example with numbers, exam traps. No accordions, tabs, modals or collapsed sections anywhere in the UI.
- Writing style in all lesson and question text: plain, direct, no filler openers, no double hyphens, no em dashes.
- Pro plan limits apply. Work in small files (one lesson file and one question file per objective), run validate.py often, commit after each objective group, and update STATUS.md. If a usage limit stops you, the next session resumes with /resume-build.
- Do not read PDF page images unless the text extraction is missing a figure the lesson needs. Pages likely to need it are listed in sources/index.md.
- Sessions 21 and 22: the user chose (Nov 12) to build them now from the study guide objectives, the professor reading "Rivalry in Oligopoly" (S22), the professor's Midterm 2 overview, and the book-based study notes. The user has no class notes. Mark these lessons provisional in content/sessions/S21.json and S22.json and update them when slides or review materials arrive via /ingest.
- Never edit or delete anything outside this folder. Source folders one level up are read only.

## Math and money in text
- Math delimiters are \( ... \) inline and $$ ... $$ or \[ ... \] display. A single $ is ALWAYS currency, never math. In JSON strings write \\( and \\).
- Markdown subset: paragraphs, **bold**, *italic*, - lists, 1. lists, pipe tables, `code`.
- Session page text (overview, provisional banner) goes in content/sessions/Sxx.json.

## Commands
- /stage NN  runs prompts/NN-*.md
- /resume-build  continues from the first incomplete objective
- /ingest  processes new files dropped in inbox/
- /audit  independent audit (run in a fresh session)
