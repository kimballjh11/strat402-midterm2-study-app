# Stage 01: app shell

Build the app exactly as BUILD-GUIDE.md sections 4 and 5 specify. Static files only, no framework, no bundler, must work by double clicking app/index.html (file://). Keep each JS file under 400 lines.

Steps:
1. KaTeX: `npm init -y`, `npm install katex`, copy node_modules/katex/dist/katex.min.js, katex.min.css, contrib/auto-render.min.js and the fonts folder to app/vendor/katex/. Render with auto-render on every lesson and question render (delimiters $...$ and $$...$$).
2. scripts/build_data.js (node): reads reference/objectives.json, content/lessons/*.json, content/questions/**/*.json, content/cases/*.json, config.json and writes app/data/data.js as `window.M2DATA = {...};`. Generators are plain JS files concatenated into app/data/generators.js. Run it as `node scripts/build_data.js`. It must not fail on empty content folders.
3. app/js: storage.js (progress model, export and import), rng.js (seeded RNG with int, num, pick), engine.js (selection rule, mastery rule, queue rule exactly as in the guide), render.js (markdown subset plus KaTeX), session.js (session page), practice.js (practice block and keyboard), mock.js, queue.js, graphs/*.js (one file per component listed in the guide), app.js (hash router: #/s15, #/queue, #/mock).
4. app/css/style.css: the dark theme in the guide. No animations. Readable at laptop size.
5. Mastery and queue unit tests in tests/engine.test.js (node, no framework): mastery needs 10 attempts and 9 correct in the last 10; a miss queues an item; two consecutive correct clears it; queue item appears after every third question.
6. tests/gen_samples.js: loads app/data/generators.js in node with a stub M2.gen, writes 200 seeded samples per generator to verify/samples/<id>.json including params and answer.
7. Seed content so the shell can be tested: copy the imported professor questions through build_data. Create a throwaway test lesson in memory only (not on disk) for a smoke test. Do not leave placeholder lessons in content/.
8. Smoke test with the built-in or any available browser if tools allow; otherwise run the node tests and check that app/index.html references only files that exist.
9. Sessions S21 and S22 show as "pending materials" in the sidebar, driven by config.pending_sessions.
10. Commit: "stage 01". Update STATUS.md.
