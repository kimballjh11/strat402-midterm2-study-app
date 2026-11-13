// Selection, mastery and missed-queue rules (BUILD-GUIDE section 1 and 5). Pure functions over (data, progress).
(function (M2) {
  const E = {};
  E.WINDOW = 10; E.REQUIRED = 9; E.QUEUE_EVERY = 3; E.QUEUE_CLEAR = 2;

  // Index static questions and case parts once. Case parts keep a pointer to their case for the shared stem.
  E.prepare = function (D) {
    if (D._idx) return D;
    D._idx = {}; D._byLO = {}; D._gensByLO = {};
    const add = q => {
      D._idx[q.id] = q;
      for (const lo of q.los || []) (D._byLO[lo] = D._byLO[lo] || []).push(q.id);
    };
    for (const q of D.questions || []) add(q);
    for (const c of D.cases || []) for (const p of c.parts) { p.caseRef = c; if (!p.los) p.los = c.los; add(p); }
    for (const g of Object.values(M2.generators || {})) for (const lo of g.los || []) (D._gensByLO[lo] = D._gensByLO[lo] || []).push(g.id);
    if (D.config) { E.WINDOW = D.config.mastery.window; E.REQUIRED = D.config.mastery.required_correct; }
    return D;
  };

  E.get = function (D, id) {
    if (D._idx[id]) return D._idx[id];
    const m = /^(.*)#(\d+)$/.exec(id);
    return m ? M2.makeGen(m[1], +m[2]) : null;
  };

  E.mastery = function (p, lo) {
    const h = p.lo[lo] || [];
    const last = h.slice(-E.WINDOW);
    const correct = last.reduce((s, x) => s + (x ? 1 : 0), 0);
    return { attempts: h.length, correct, window: last.length, mastered: h.length >= E.WINDOW && correct >= E.REQUIRED };
  };

  // Record an answer: per-question stats, per-objective rolling history, queue rule.
  E.record = function (p, q, correct, opts) {
    opts = opts || {};
    const s = p.q[q.id] || (p.q[q.id] = { n: 0, c: 0 });
    s.n++; if (correct) s.c++; s.last = !!correct; s.t = Date.now();
    for (const lo of q.los || []) {
      const h = p.lo[lo] || (p.lo[lo] = []);
      h.push(correct ? 1 : 0);
      if (h.length > 40) h.splice(0, h.length - 40);
    }
    const i = p.queue.findIndex(x => x.id === q.id);
    if (!correct) {
      if (i >= 0) p.queue[i].streak = 0;
      else p.queue.push({ id: q.id, streak: 0, added: Date.now() });
    } else if (i >= 0) {
      p.queue[i].streak++;
      if (p.queue[i].streak >= E.QUEUE_CLEAR) p.queue.splice(i, 1);
    }
  };

  // Called whenever a question is put on screen, so the every-third rule spans all blocks.
  E.served = function (p, fromQueue) {
    p.served = (p.served || 0) + 1;
    p.sinceQueue = fromQueue ? 0 : (p.sinceQueue || 0) + 1;
  };

  // After every 3 ordinary questions, the next one comes from the missed queue.
  E.queueDue = function (p) { return (p.sinceQueue || 0) >= E.QUEUE_EVERY && p.queue.length > 0; };

  E.pickQueue = function (D, p, exclude, rand) {
    const items = p.queue.filter(x => !(exclude || []).includes(x.id) && E.get(D, x.id));
    if (!items.length) return null;
    items.sort((a, b) => a.streak - b.streak || a.added - b.added);
    return E.get(D, items[0].id);
  };

  // Choose a question for one objective: unseen first, then last missed, then least recently seen. Mix in generators.
  E.pickForLO = function (D, p, lo, recent, rand) {
    rand = rand || Math.random;
    recent = recent || [];
    const ids = (D._byLO[lo] || []).filter(id => !recent.includes(id));
    const gens = D._gensByLO[lo] || [];
    const unseen = ids.filter(id => !p.q[id]);
    const missed = ids.filter(id => p.q[id] && p.q[id].last === false);
    const useGen = gens.length && (rand() < 0.34 || (!unseen.length && !missed.length && rand() < 0.5) || !ids.length);
    if (useGen) {
      const g = gens[Math.floor(rand() * gens.length)];
      return M2.makeGen(g, 1 + Math.floor(rand() * 2147483000));
    }
    let pool = unseen.length ? unseen : missed.length ? missed : ids;
    if (pool === ids && ids.length > 1) {          // least recently seen half
      pool = ids.slice().sort((a, b) => (p.q[a].t || 0) - (p.q[b].t || 0)).slice(0, Math.max(1, Math.ceil(ids.length / 2)));
    }
    if (!pool.length) {
      const all = D._byLO[lo] || [];
      if (!all.length) return null;
      pool = all;
    }
    return E.get(D, pool[Math.floor(rand() * pool.length)]);
  };

  // Next question for a practice block. scope: list of LO ids (one for an objective block, many for a mixed drill).
  // Returns {q, fromQueue}.
  E.next = function (D, p, scope, recent, rand) {
    rand = rand || Math.random;
    if (E.queueDue(p)) {
      const q = E.pickQueue(D, p, recent, rand);
      if (q) return { q, fromQueue: true };
    }
    let lo = scope[0];
    if (scope.length > 1) lo = E.weakest(p, scope, rand);
    const q = E.pickForLO(D, p, lo, recent, rand);
    return { q, fromQueue: false };
  };

  // Weakest objective first: unmastered before mastered, then lowest accuracy in the window, then fewest attempts.
  E.weakest = function (p, scope, rand) {
    const sc = scope.map(lo => {
      const m = E.mastery(p, lo);
      const acc = m.window ? m.correct / m.window : 0;
      return { lo, k: (m.mastered ? 10 : 0) + acc + m.attempts / 1000 + (rand ? rand() * 0.05 : 0) };
    });
    sc.sort((a, b) => a.k - b.k);
    return sc[0].lo;
  };

  // Answer checking. Numbers accept 3/4, 75%, $1,200, 1e3. Relative tolerance (default 1 percent).
  E.parseNum = function (s, unit) {
    if (typeof s === "number") return s;
    let t = String(s || "").trim().replace(/[$,\s]/g, "").replace(/[−–]/g, "-");
    if (!t) return NaN;
    let pct = false;
    if (t.endsWith("%")) { pct = true; t = t.slice(0, -1); }
    let v;
    const fr = /^(-?\d*\.?\d+)\/(-?\d*\.?\d+)$/.exec(t);
    if (fr) v = parseFloat(fr[1]) / parseFloat(fr[2]);
    else if (/^-?(\d+\.?\d*|\.\d+)(e-?\d+)?$/i.test(t)) v = parseFloat(t);
    else return NaN;
    if (pct && unit !== "%") v = v / 100;
    return v;
  };

  E.check = function (q, response) {
    if (q.type === "num") {
      const v = E.parseNum(response, q.unit);
      if (!isFinite(v)) return null;                 // not a number: ignore the submit
      const a = q.answer, tol = q.tol == null ? 0.01 : q.tol;
      return a === 0 ? Math.abs(v) <= 0.005 : Math.abs(v - a) <= Math.abs(a) * tol + 1e-9;
    }
    if (q.type === "multi") {
      const want = (q.answer || []).slice().sort().join(",");
      return (response || []).slice().sort().join(",") === want;
    }
    return response === q.answer;
  };

  E.sessionOf = lo => +String(lo).slice(1, 3);
  M2.engine = E;
})(globalThis.M2 = globalThis.M2 || {});
