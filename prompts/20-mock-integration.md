# Stage 20: mock exam, integration, whole app test

1. Run `node scripts/build_data.js` and `.venv/bin/python scripts/validate.py`. Everything in build_sessions must pass.
2. Mock exam: confirm the mock builder uses config.json (21 conceptual questions, cases totaling 24 parts, topic weights renormalized over built sessions, banner for missing sessions). Questions flagged `emphasis` are drawn more often. Cases are drawn whole. No feedback until submit. Submit page shows score by session and objective and sends misses to the queue.
3. Run all node tests (`node tests/engine.test.js`) and every solver check (`node tests/gen_samples.js S15` and `.venv/bin/python verify/check_S15.py`, same for S16, S18, S19, S20).
4. Coverage: confirm coverage/slide-ledger.json has no unassigned slide pages and no unassigned reading sections for S15 to S20.
5. Open the app in a browser if a browser tool is available (the built-in browser can open file:// paths via preview, otherwise skip and rely on tests). Check: sidebar, Continue, a session page, KaTeX renders, graphs render, keyboard answering, queue, mock, export and import.
6. Write app/README.txt (3 lines: how to open, how to back up progress, how to add material with /ingest).
7. Commit "stage 20". Update STATUS.md. Report any unchecked item honestly.
