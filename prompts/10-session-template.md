# Stage 10: build one session (use with prompts/sessions/Sxx.md)

Input: a session id like S15. Read CLAUDE.md, the matching brief in prompts/sessions/, reference/objectives.json entries for that session, and the session's text files in sources/text. Work objective by objective, in study guide order. Do not skip ahead and do not batch the whole session into one giant file.

Per session, first:
A. Read all the session's sources once: slides text, in-class exercise dumps, exercise solution sheets (solutions are often a second sheet or hidden in cell comments), reading quiz JSON, Claude-made textbook notes (secondary), and the Overview page. List the slide pages in sources/index.md flagged as low text and view only those page images that a lesson needs (`pdftoppm -png -r 80 -f N -l N file.pdf /tmp/p` if installed).
B. Build coverage/slide-ledger.json entries for the session: every slide page and reading section mapped to objective ids, or a reason it is not testable.

Then for each objective Sxx-NN:
1. Lesson: write content/lessons/Sxx-NN.json following the schema. Start from zero knowledge. Use the professor's definitions and notation from the slides. Every formula gets onSheet true or false. Include a derivation when the formula is not on the sheet. Include math refreshers (derivative rules, solving two equations, discounting, probability, percent change, whichever the objective uses) written for someone who has not done calculus recently, with a tiny worked example each. Include at least one fully worked numeric example that reuses the numbers or setup from the professor's exercise when one exists. Include at least 3 traps. Set calc true if the objective involves a calculation.
2. Graph: reference the component named in the session brief and set sensible default params. Implement the component in app/js/graphs/ the first time it is needed.
3. Questions: write content/questions/Sxx-NN.json. Count the professor imported questions that already map to this objective (content/questions/pro). Add enough original questions to reach at least 15 total, respecting the mix rules in the guide (5 concept, 3 apply, 4 calc plus a generator for calculation objectives). Make distractors reflect real student errors. Full explanation on every question.
4. Generators: for calculation objectives add generators to content/generators/Sxx.js. Clean numbers, answers that a calculator can verify, full hand solution in explain.
5. Verification file verify/check_Sxx.py: recompute every static num answer and every sampled generator answer by an independent method. Run `node scripts/build_data.js && node tests/gen_samples.js Sxx && .venv/bin/python verify/check_Sxx.py`. Fix any mismatch in the content, not the checker, unless the checker is wrong.

After every 2 or 3 objectives: run `.venv/bin/python scripts/validate.py Sxx`, then git commit "Sxx objectives N to M".

After the last objective:
6. Cases: write content/cases/Sxx.json with at least 2 cases in the practice exam style, 3 to 5 parts each, every part mapped to objectives.
7. Run validate.py for the session until it passes with no problems. Run the node engine tests. Update coverage ledger so no slide page is unassigned.
8. Commit "Sxx complete". Update STATUS.md with one line. Print: objectives done, questions, generators, cases, open issues.
