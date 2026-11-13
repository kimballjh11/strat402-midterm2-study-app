// node tests/gen_samples.js S15 : writes 200 seeded samples per generator of that session to verify/samples/<id>.json
const fs = require("fs"), path = require("path");
require("../app/js/rng.js");
const M2 = globalThis.M2;
const HERE = path.resolve(__dirname, "..");
const sess = process.argv[2];
const dir = path.join(HERE, "content", "generators");
const files = fs.existsSync(dir) ? fs.readdirSync(dir).filter(f => f.endsWith(".js") && (!sess || f.startsWith(sess))) : [];
for (const f of files) require(path.join(dir, f));
const out = path.join(HERE, "verify", "samples"); fs.mkdirSync(out, { recursive: true });
let n = 0, bad = 0;
for (const id of Object.keys(M2.generators)) {
  const rows = [];
  for (let s = 1; s <= 200; s++) {
    const q = M2.makeGen(id, s * 7919);
    if (!q.stem || !q.explain || (q.type === "num" && !isFinite(q.answer)) || (q.type !== "num" && !(q.choices && q.choices.length >= 2))) { bad++; console.log("BAD sample", q.id); }
    rows.push({ seed: q.seed, params: q.params, answer: q.answer, type: q.type, choices: q.choices, tol: q.tol });
  }
  fs.writeFileSync(path.join(out, id + ".json"), JSON.stringify(rows, null, 0)); n++;
}
console.log(`${n} generators sampled${sess ? " for " + sess : ""}, ${bad} bad samples`);
process.exit(bad ? 1 : 0);
