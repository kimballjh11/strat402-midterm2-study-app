# Build guide: STRAT 402 Midterm 2 study app

This guide is the plan Claude Code follows. You run it, it builds. Everything below reflects the decisions you made. Where I had to assume something, it says ASSUMPTION so you can overrule it.

## 1. What you are building

A static, local, dark web app (open app/index.html, no server needed) that:
1. Teaches Sessions 15, 16, 18, 19, 20 from zero, one scrolling page per session. S21 and S22 are added when class materials arrive.
2. Drills every learning objective on the study guide (41 tonight, 51 total) until you hit 9 of your last 10 correct, with a missed question queue that keeps resurfacing misses.
3. Runs timed mock exams in the real format, calculator only.
4. Grows as you drop new files in inbox/ and run /ingest.

### Locked decisions
| Topic | Decision |
|---|---|
| Form | Local web app, dark, plain, no gamification, no accordions or modals |
| Layout | One page per session. Sidebar: sessions, Missed queue, Mock exam. A Continue button jumps to the next unmastered objective |
| Per objective, inline on the session page | Plain English lesson, definition, formula box, derivation, worked example, inline graph, exam traps, then its practice block |
| Teaching depth | Zero to exam, every calculation worked by hand, calculus shown, math refreshers inline where needed (ASSUMPTION: shown as a plain highlighted block, never collapsed) |
| Answering | Instant feedback, keyboard first: 1 to 4 or A to D picks, T or F, Enter submits numbers and goes to the next question |
| Mastery | At least 10 attempts on the objective and 9 or more correct in the last 10. Rolling, so it can be lost |
| Missed queue | Any miss enters the queue. It leaves after 2 consecutive correct answers. One queue item is mixed in after every 3 questions anywhere |
| Questions | Professor questions imported verbatim, plus a pre-built bank, plus parametric generators that make unlimited fresh calculation variants offline. About 15 or more per objective |
| Mock exams | Included. Real format (conceptual block then case blocks with parts), no feedback until submit, then full review and misses go to the queue |
| Graphs | Interactive, inline, vanilla SVG, always visible (no click to open) |
| Math | KaTeX bundled locally |
| Checking | Python solver recomputes every calculation answer, then an independent audit pass in a fresh session |
| Hosting | Local first. Optional GitHub Pages step at the end (prompts/40-publish.md). Professor approved publishing for Midterm 2 as well |
| Built from scratch | Do not reuse the Midterm 1 site or its pipeline |

## 2. Facts that shape the build (read these)

1. The equation sheet for this exam is the Midterm 1 sheet. It gives: HHI, elasticity, AFC, AVC, ATC, MC (cubic and power forms), MP (linear and Cobb-Douglas), AP, MRTS, isocost slope. It gives nothing for value marginal product, the cost minimizing rule beyond MRTS and isocost slope, game theory, repeated games (discount factor math), or any oligopoly model. Those must be derived or memorized, so lessons flag every formula as "On the sheet" or "Not on the sheet, know it cold".
2. The practice exam is not comprehensive. Practice Midterm 2 has 14 conceptual questions then 6 cases, 38 numbered questions, at about two thirds of the real exam length. The real exam draws from every study guide objective and includes questions the practice exam never touches. Rough topic weights from the study guide's Practice Exam column: production about 26 percent, barriers to entry about 13 percent, game theory about 34 percent, oligopoly (S21 and S22) about 27 percent. Oligopoly is over a quarter of the exam and is not in tonight's build. Ingest S21 and S22 as soon as materials exist.
3. The study guide cites Comprehension Quizzes 7 to 10 and the Practice Midterm 2 by question number. None of these are in your folder yet. When they arrive via inbox/, scripts/import_quizzes.py maps them to objectives automatically using the study guide columns.
4. The "Textbook Study Notes" HTML files are Claude-made summaries and use made-up numbers. They are secondary. Professor slides, in-class exercises, reading quizzes, comprehension quizzes and the study guide are authoritative. The S21 notes say the S21 slides were never posted.
5. S17 is a group project day and S14 is AI use. Neither is on Midterm 2.
6. Slide pages that are mostly figures are listed in sources/index.md after extraction. Look at those page images only when a lesson needs the figure.
7. Pro plan: expect several 5 hour usage windows. The build is split into small, resumable pieces for this reason. Switch to the Sonnet model for bulk writing (`/model`). Finishing everything in one night is possible only if you start early and keep the session running. The order of work puts a usable app first.

## 3. Folder layout

```
M2-STUDY-APP/
  CLAUDE.md  BUILD-GUIDE.md  STATUS.md  config.json
  prompts/            numbered stage prompts, prompts/sessions/ has one brief per session
  scripts/            collect.py extract.py objectives.py import_quizzes.py validate.py preflight.sh (+ build_data.js made in stage 01)
  sources/raw|text|quizzes   copies and extractions of your course files (generated)
  reference/          objectives.json (master objective list), exam-facts.md
  content/lessons/    one JSON per objective, e.g. S15-04.json
  content/questions/  one JSON array per objective (S15-04.json) plus pro/ (imported, verbatim)
  content/cases/      one JSON per session, multi-part case questions
  content/generators/ one JS file per session, parametric question generators
  verify/             Python independent solvers, one file per session
  app/                index.html, css, js, vendor/katex, data/data.js (generated by scripts/build_data.js)
  tests/              node checks
  inbox/              you drop new material here
  coverage/           slide ledger (every slide page assigned to an objective or marked non-testable)
```

## 4. Data formats

Lesson, content/lessons/S15-04.json
```json
{ "id": "S15-04", "title": "Marginal product", "calc": true,
  "plain": "Plain English from zero. Markdown with \\(inline math\\). A single $ is currency.",
  "why": "Why a manager cares.",
  "definition": "One precise sentence in the professor's wording.",
  "formulas": [{"name": "Marginal product of labor", "tex": "MP_L=\\frac{\\Delta Q}{\\Delta L}", "onSheet": true}],
  "derivation": "Step by step, or empty if none.",
  "math": [{"title": "Refresher: derivative of a power", "body": "..."}],
  "worked": [{"title": "", "problem": "", "steps": ["", ""], "answer": ""}],
  "traps": ["How the exam tries to trick you."],
  "graph": {"component": "production", "params": {}},
  "sources": {"slides": "S15 slides pp. 12 to 15", "read": "Ch. 5 pp. 140 to 143", "exercise": "J Dawgs", "quiz": "Reading Quiz Q2"} }
```
Question, content/questions/S15-04.json (array)
```json
{ "id": "S15-04-q007", "los": ["S15-04"], "type": "mc", "kind": "concept",
  "diff": 2, "stem": "...", "choices": ["...", "...", "...", "..."], "answer": 2,
  "explain": "Why right and why each wrong choice is wrong.", "trap": "optional",
  "source": "generated", "verbatim": false }
```
types: mc, tf (answer is index), multi (answer is index list), num (answer is a number, optional "tol" relative tolerance default 0.01, "unit"). kinds: concept, apply, calc. Calc questions must include the full hand solution in "explain".

Case, content/cases/S15.json: `[{"id":"S15-case1","title":"","stem":"","los":[...],"parts":[{question objects without stem repetition}]}]`. Each part is a question with kind apply or calc. At least 2 cases per session tonight, written like the practice exam cases: a short business scenario then 3 to 5 numeric or conceptual parts.

Generator, content/generators/S15.js
```js
M2.gen({ id: "S15-04-g1", los: ["S15-04"], kind: "calc",
  make(r) { /* r.int(a,b), r.pick(list), r.num(a,b,step) */
    const a = r.int(2,9), ...;
    return { stem: "...", type: "num", answer: ..., unit: "", tol: 0.01, explain: "full hand solution", params: {a, ...} }; } });
```
`M2.gen` registers in the browser and exports to node for tests. Seeded RNG so the same seed gives the same question (used by verification).

Objective list: reference/objectives.json, made by scripts/objectives.py from the study guide. IDs are S15-01 and so on, in study guide row order.

Progress (browser localStorage key m2.progress.v1): attempts per question id and per objective, queue, settings. Include Export and Import buttons (JSON file) in the sidebar footer so a cleared browser does not lose progress. IDs are stable forever, so ingest never breaks progress: add, never rename or reuse ids.

## 5. UI specification

Theme: background #0f1115, panels #161a21, text #d7dae0, muted #8b93a1, accent #6ea8fe, correct #5fb878, wrong #e06c75. System font, 17px base, content column max 860px, left sidebar 230px fixed. No animations, no emojis, no confetti, no streak badges.

Sidebar: Continue (button), sessions list with objective mastery counts like "S15 Production I  4/11", S21 and S22 shown as "pending materials", Missed queue (count), Mock exam, Export, Import. Nothing else.

Session page (single scroll): session title and a 4 to 6 sentence overview of what it covers and why it matters for the exam. Then for each objective in order: heading with mastery readout (for example "7 of last 10 correct"), plain explanation, definition, formula box (each formula tagged On the sheet or Not on the sheet, know it cold), derivation, math refresher blocks, worked example, graph (always rendered), traps, then the practice block. Ends with a session mixed drill block that draws weakest objectives first.

Practice block: shows one question at a time in place. Selection rule: miss queue item every third question, otherwise the objective's unmastered pool, preferring unseen and previously missed questions, mixing generators in. Feedback appears directly under the question: correct or wrong, the correct answer, the full explanation, and the trap if any. Enter goes to the next question. When the objective reaches mastery the block says so in one line and keyboard focus moves to the next unmastered objective's block and scrolls to it. No dialogs.

Keyboard: 1 to 9 or A to D choose, T and F for true or false, Enter submits a number or advances, N also advances, Esc does nothing. Only the focused practice block listens. Clicking a block focuses it.

Numeric answers: input accepts decimals, fractions like 3/4, percent sign, dollar sign, commas. Tolerance 1 percent relative unless the question says otherwise. Show units.

Missed queue page: same question card, only queue items, shows how many remain.

Mock exam page: ASSUMPTION: 21 conceptual questions then cases totaling 24 parts (1.5 times the practice exam), configurable in config.json, untimed (user decision Nov 12: no time limit). Topic mix follows config.topic_weights, renormalized to the sessions that exist, with a visible banner that says which sessions are missing. No feedback during the test, calculator only reminder at top. On submit: score, score by session and objective, every question with explanation, and one button that sends all misses to the queue (done automatically, the button just says so).

Graphs (vanilla SVG, drawn on load, sliders and number inputs that update live, readouts beside them):
- production: total, average and marginal product against labor from Q equals a cubic or Cobb-Douglas function, three stages marked, VMP versus wage line for the profit maximizing input
- isoquant: linear, Leontief, Cobb-Douglas isoquants with MRTS readout
- costmin: isoquant plus isocost, sliders for wage, rental rate and output target, tangency point and cost minimizing inputs
- scale: average cost curve with minimum efficient scale, learning curve with learning rate slider, network effects adoption curve with critical mass
- payoff: editable 2 by 2 and 3 by 3 payoff matrix, best response highlights, dominant strategies, pure Nash equilibria, mixed strategy indifference probabilities for 2 by 2
- tree: editable extensive form tree with backward induction, subgame perfect path highlighted
- repeated: grim trigger calculator with discount factor slider, present value of cooperating versus deviating, threshold discount factor
Later (S21 and S22): reaction curves for Cournot, Stackelberg and Bertrand.

## 6. Question bank rules

Per objective: 15 or more total (config.json), with at least 5 conceptual, at least 3 apply, and for calculation objectives at least 4 static calc questions plus at least 1 generator. Professor imported questions count toward the 15. Generators count double in the check but never replace the static minimum.

Style: mirror the practice exam. Conceptual questions test definitions, relationships, and which concept a short scenario illustrates. Apply questions put the concept in a business situation. Calc questions are short hand calculations with clean numbers. Distractors must be the mistakes students actually make (mixing up AP and MP, using price instead of VMP, picking a dominated strategy, forgetting that Nash needs mutual best responses). Every explanation covers why the right answer is right and names the error each wrong answer represents.

Coverage rule, "nothing the exam can ask is untouched": scripts/validate.py checks the objective counts. In addition each session builds coverage/slide-ledger.json that lists every slide page and reading section with the objective ids it feeds, or the reason it is not testable (title slide, logistics, exercise instructions). A slide page with no assignment and no reason is a failure.

## 7. Verification

1. Schema and coverage: `.venv/bin/python scripts/validate.py` must pass for the session before moving on.
2. Solver check: for every generator, `node tests/gen_samples.js S15` writes 200 seeded samples to verify/samples/, and `verify/check_S15.py` recomputes each answer by a different method (numeric search, brute force best response, direct summation, never the same closed form the generator used) and fails on any mismatch. Every static num question has its answer recomputed in the same check file.
3. Audit, in a fresh session (`/clear` then `/audit`): prompts/30-audit.md. The auditor compares lessons to slides and exercises, compares answer keys to exercise solution sheets, confirms all verbatim professor questions byte match the source, and reports findings before anything is fixed.

## 8. Stages

| Stage | File | What it does | Cost note |
|---|---|---|---|
| 00 | prompts/00-preflight.md | Install check, collect and extract sources, build objectives.json, import professor quizzes | Almost no model use, scripts do the work |
| 01 | prompts/01-app-shell.md | Build the app: layout, engine, mastery, queue, mock, graphs, KaTeX, data build, tests | Biggest single code job, do it once |
| 10 | prompts/10-session-template.md with prompts/sessions/S15.md etc. | Per session: lessons, graphs, questions, cases, generators, verification | Run S15, S16, S18, S19, S20 in order |
| 20 | prompts/20-mock-integration.md | Mock exam tuning, whole app test, ledger check | Short |
| 30 | prompts/30-audit.md | Fresh session independent audit | Run after 20 |
| 40 | prompts/40-publish.md | Optional GitHub Pages | Only if you want phone access |
Run a stage inside Claude Code with `/stage 00`, `/stage 01`, `/stage 10 S15`. If you hit a usage limit, wait for the reset, start `claude` again, type `/resume-build`.

## 9. Ingest workflow (S21, S22, review materials, new quizzes)

Trigger: `/ingest` with files in inbox/. For each file:
1. Run `.venv/bin/python scripts/extract.py inbox sources/ingest` to get text and quiz JSON. Photos and images: view them directly and transcribe faithfully into sources/text/ with the transcribe-notes approach (verbatim, no summarizing).
2. Identify the session or exam role from the file name and contents. Copy originals into sources/raw/<S##>/ and re-run extract on that folder.
3. Quizzes (reading, comprehension, practice midterm): run `.venv/bin/python scripts/import_quizzes.py`. For the Practice Midterm 2, extend the importer so each question keeps its practice exam number, then mark that question set as practice exam material: its numbers appear in the study guide's Practice Exam column, so each maps to objectives. Check every imported question against the raw_lines in the JSON, resolve any needs_review flags, and make numeric questions properly num type.
4. Class notes and slides: for each affected objective, update the lesson (merge new emphasis, examples, numbers, professor wording) without deleting ids or existing content that is still correct, add questions in the professor's style, add generators if the notes show a new calculation type. Mark content that came from class notes or review materials with `"emphasis": true` so mock exams weight it up.
5. S21 and S22 first time: move the session from pending_sessions to build_sessions in config.json, then run prompts/10-session-template.md for it using prompts/sessions/S21.md or S22.md. The brief contains the expected content so you know what the notes must confirm.
6. Midterm review quiz, notes, slides, video transcript: treat as the professor telling you what is on the exam. Extract every explicit hint ("know this", "will be on the exam", specific question styles), save them in reference/review-hints.md with their source, tag the matching objectives `"emphasis": true`, and add extra questions for each hint.
7. Re-run validate, solver checks for new generators, update coverage/slide-ledger.json, update STATUS.md, commit.
Progress is never reset: ids are stable and new questions simply join the pools.

## 10. Morning checklist (5 minutes)

1. `open app/index.html` from Finder or Terminal. Dark page, sidebar with sessions.
2. Click Continue. You land on the first unmastered objective. Press 1 to answer, read the feedback, press Enter.
3. Open S16 and check the isocost graph moves when you drag the wage slider.
4. Open Mock exam, start one, answer two questions, submit, confirm the review and the queue count.
5. Export progress, import it back.
6. Check STATUS.generated.md says Complete for every build session.
7. Read one lesson slowly. If a statement does not match the slides, tell Claude Code: "Lesson S15-04 contradicts slide N. Fix it and re-audit."

## 11. Open items for you

- Export from Canvas into inbox/: Practice Midterm 2, Comprehension Quizzes 7 to 10, Session 21 and 22 reading quizzes (due Nov 14), and any class notes or slides. Save the page as .mhtml like you did for the earlier comprehension quizzes.
- Confirm whether a separate Midterm 2 equation sheet is posted. The one in the folder is the Midterm 1 sheet.
- Class notes for S21 and S22 are the most important missing source. The S21 slides were not posted per your study notes, so your own notes are the professor's content for Cournot and Stackelberg.
