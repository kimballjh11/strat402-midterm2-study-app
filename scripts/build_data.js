#!/usr/bin/env node
// Builds app/data/data.js (window.M2DATA) and app/data/generators.js from content/.
// Usage: node scripts/build_data.js   Never fails on empty content folders.
const fs = require("fs"), path = require("path");
const HERE = path.resolve(__dirname, "..");
const C = p => path.join(HERE, p);
const readJSON = f => JSON.parse(fs.readFileSync(f, "utf8"));
const listJSON = dir => {
  if (!fs.existsSync(dir)) return [];
  let out = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out = out.concat(listJSON(p));
    else if (e.name.endsWith(".json")) out.push(p);
  }
  return out.sort();
};

const config = readJSON(C("config.json"));
const objectives = readJSON(C("reference/objectives.json"));
const lessons = {};
for (const f of listJSON(C("content/lessons"))) { const l = readJSON(f); lessons[l.id] = l; }

const questions = [], seen = new Set(), problems = [];
for (const f of listJSON(C("content/questions"))) {
  const d = readJSON(f);
  for (const q of Array.isArray(d) ? d : d.questions || []) {
    if (seen.has(q.id)) { problems.push("duplicate question id " + q.id); continue; }
    seen.add(q.id); questions.push(q);
  }
}
const cases = [];
for (const f of listJSON(C("content/cases"))) {
  for (const c of readJSON(f)) {
    c.parts.forEach((p, i) => { p.case = c.id; p.part = i + 1; if (!p.id) p.id = `${c.id}-p${i + 1}`; });
    cases.push(c);
  }
}
let hints = "";
if (fs.existsSync(C("reference/review-hints.md"))) hints = fs.readFileSync(C("reference/review-hints.md"), "utf8");

// Optional per-session page text: content/sessions/S15.json {"overview": "...", "provisional": "..."}
const sessions = {};
for (const f of listJSON(C("content/sessions"))) sessions[path.basename(f, ".json")] = readJSON(f);

const data = { built: new Date().toISOString(), config, objectives, lessons, questions, cases, sessions, hints };
fs.mkdirSync(C("app/data"), { recursive: true });
fs.writeFileSync(C("app/data/data.js"), "window.M2DATA = " + JSON.stringify(data) + ";\n");

// Generators: concatenate content/generators/*.js
let gen = "/* built by scripts/build_data.js from content/generators */\n";
const gdir = C("content/generators");
if (fs.existsSync(gdir)) for (const f of fs.readdirSync(gdir).filter(f => f.endsWith(".js")).sort())
  gen += `\n/* ---- ${f} ---- */\n` + fs.readFileSync(path.join(gdir, f), "utf8") + "\n";
fs.writeFileSync(C("app/data/generators.js"), gen);

console.log(`data.js: ${objectives.length} objectives, ${Object.keys(lessons).length} lessons, ${questions.length} questions, ${cases.length} cases`
  + (problems.length ? "\nPROBLEMS:\n" + problems.join("\n") : ""));
if (problems.length) process.exit(1);
