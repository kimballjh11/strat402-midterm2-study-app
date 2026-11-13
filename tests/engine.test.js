// node tests/engine.test.js : mastery, queue and selection rules, plus numeric answer parsing.
require("../app/js/rng.js"); require("../app/js/engine.js");
const M2 = globalThis.M2, E = M2.engine;
let fails = 0;
const ok = (c, m) => { if (!c) { fails++; console.log("FAIL", m); } else console.log("ok  ", m); };
const blank = () => ({ v: 1, q: {}, lo: {}, queue: [], served: 0, sinceQueue: 0 });
const q = (id, lo) => ({ id, los: [lo || "S15-01"], type: "mc", choices: ["a", "b"], answer: 0, kind: "concept", stem: "s", explain: "e" });

// mastery
let p = blank();
for (let i = 0; i < 9; i++) E.record(p, q("x" + i), true);
ok(!E.mastery(p, "S15-01").mastered, "9 correct of 9 attempts is not mastery (needs 10 attempts)");
E.record(p, q("x9"), true);
ok(E.mastery(p, "S15-01").mastered, "10 of 10 is mastery");
E.record(p, q("y1"), false);
ok(E.mastery(p, "S15-01").mastered, "9 of last 10 still mastered");
E.record(p, q("y2"), false);
ok(!E.mastery(p, "S15-01").mastered, "8 of last 10 loses mastery (rolling)");
for (let i = 0; i < 9; i++) E.record(p, q("z" + i), true);
ok(E.mastery(p, "S15-01").correct === 9 && E.mastery(p, "S15-01").mastered, "back to 9 of last 10 regains mastery");

// queue
p = blank();
const m = q("m1");
E.record(p, m, false);
ok(p.queue.length === 1 && p.queue[0].id === "m1", "a miss queues the item");
E.record(p, m, false);
ok(p.queue.length === 1 && p.queue[0].streak === 0, "a second miss keeps one entry, streak 0");
E.record(p, m, true);
ok(p.queue.length === 1 && p.queue[0].streak === 1, "one correct keeps it queued");
E.record(p, m, false); E.record(p, m, true);
ok(p.queue.length === 1, "a miss resets the streak, so correct, miss, correct does not clear");
E.record(p, m, true);
ok(p.queue.length === 0, "two consecutive correct clears it");

// queue cadence: after every 3 ordinary questions the next comes from the queue
const D = { questions: [q("a1"), q("a2"), q("a3"), q("a4"), q("a5"), q("qq", "S16-01")], cases: [], config: { mastery: { window: 10, required_correct: 9 } } };
E.prepare(D);
p = blank();
E.record(p, D._idx.qq, false);
const seq = [];
for (let i = 0; i < 8; i++) { const r = E.next(D, p, ["S15-01"], [], Math.random); seq.push(r.fromQueue ? "Q" : "o"); E.served(p, r.fromQueue); }
ok(seq.join("") === "oooQoooQ", "queue item appears after every third question: " + seq.join(""));
const r0 = E.next(D, blank(), ["S15-01"], [], () => 0.9);
ok(r0.q && r0.q.los[0] === "S15-01", "selection draws from the objective pool");
p = blank(); ["a1", "a2", "a3", "a4"].forEach(id => E.record(p, D._idx[id], true));
ok(E.pickForLO(D, p, "S15-01", [], () => 0.9).id === "a5", "unseen questions come first");

// numeric parsing and checking
ok(E.parseNum("3/4") === 0.75, "fraction 3/4");
ok(E.parseNum("$1,200.50") === 1200.5, "dollar and comma");
ok(E.parseNum("75%") === 0.75 && E.parseNum("75%", "%") === 75, "percent sign");
ok(E.check({ type: "num", answer: 100 }, "100.9") === true && E.check({ type: "num", answer: 100 }, "101.5") === false, "1 percent tolerance");
ok(E.check({ type: "num", answer: 0 }, "0") === true, "zero answer");
ok(E.check({ type: "num", answer: 5 }, "abc") === null, "non number is ignored");
ok(E.check({ type: "multi", answer: [0, 2] }, [2, 0]) === true, "multi any order");

// seeded generators
M2.gen({ id: "T-g1", los: ["S15-01"], kind: "calc", make(r) { const a = r.int(2, 9); return { stem: "a=" + a, answer: a * 2, explain: "x" }; } });
ok(M2.makeGen("T-g1", 42).answer === M2.makeGen("T-g1", 42).answer && M2.makeGen("T-g1", 42).id === "T-g1#42", "same seed, same question");
console.log(fails ? `${fails} FAILED` : "all engine tests passed");
process.exit(fails ? 1 : 0);
