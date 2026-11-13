# Stage 30: independent audit (fresh session, run /audit after /clear)

You did not write this content. Assume it contains errors. Goal: find them before the student studies them.

Work in this order and log every finding in audit/findings.md (file, objective id, what is wrong, evidence from the source with file name and page or cell). Do not fix while auditing.
1. Verbatim check: for every question with verbatim true, confirm the stem and choices match sources/quizzes JSON exactly, and the marked answer matches the professor's correct answer.
2. Answer key check: re-solve by hand (use python for arithmetic) all static num questions and 30 random generator samples per generator. Report mismatches with your working.
3. Lesson claims: for every lesson, compare each definition, formula, number and example against the slides and exercise solutions. Pay special attention to: onSheet flags (compare with sources/text/S23_Equation_Sheet*), the cost minimizing rule, VMP rule, Nash and dominant strategy definitions, the trigger threshold derivation, subgame perfect equilibrium, limit versus predatory pricing, the list of factors that influence collusion, the reading's strategies to crack markets.
4. Study guide coverage: every objective has a lesson and at least 15 questions, and the "Read", "Slides", "In Class" and "Spreadsheet Assignment" items cited in its row are actually reflected in the lesson.
5. Textbook notes contamination: search lessons and questions for any number or claim that appears only in the Claude-made Textbook Study Notes and not in professor material. List them.
6. Ambiguity: flag any question with two defensible answers.
7. Read three random lessons as a beginner would and flag any step that assumes knowledge not yet taught.
Then summarize counts by severity. Ask the user whether to fix now. When fixing, change content, re-run validate and the solver checks, and commit "audit fixes".
