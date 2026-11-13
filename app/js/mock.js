// Mock exam: conceptual block then cases, real-exam mix, no feedback until submit, then full review. Misses go to the queue.
(function (M2) {
  const R = M2.render, h = (...a) => R.h(...a), E = M2.engine;
  const TOPIC = { 15: "production", 16: "production", 18: "barriers", 19: "game_theory", 20: "game_theory", 21: "oligopoly", 22: "oligopoly" };
  const ALL = [15, 16, 18, 19, 20, 21, 22];

  function shuffle(a) { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
  const sessOf = q => E.sessionOf((q.los || [])[0] || "S00");
  const lessonEmph = lo => { const L = M2.D.lessons[lo]; return L && L.emphasis; };

  // Sessions with usable content and the renormalized topic weights over them.
  M2.mockPlan = function () {
    const D = M2.D, cfg = D.config;
    const have = ALL.filter(n => (D.questions.some(q => sessOf(q) === n) || D.cases.some(c => sessOf(c) === n)) && !(cfg.pending_sessions || []).includes(n));
    const missing = ALL.filter(n => !have.includes(n));
    const topics = {};
    for (const n of have) topics[TOPIC[n]] = cfg.topic_weights[TOPIC[n]];
    const tot = Object.values(topics).reduce((s, x) => s + x, 0) || 1;
    for (const k in topics) topics[k] /= tot;
    return { have, missing, topics };
  };

  function alloc(total, weights) {
    const keys = Object.keys(weights), out = {};
    let used = 0;
    keys.forEach(k => { out[k] = Math.floor(total * weights[k]); used += out[k]; });
    keys.sort((a, b) => (total * weights[b] % 1) - (total * weights[a] % 1)).slice(0, total - used).forEach(k => out[k]++);
    return out;
  }

  // Weighted sample without replacement; emphasis content counts double, spread across objectives.
  function sample(pool, n) {
    const out = [], usedLO = {};
    let rest = shuffle(pool);
    while (out.length < n && rest.length) {
      rest.sort((a, b) => ((usedLO[a.los[0]] || 0) - (lessonEmph(a.los[0]) || a.emphasis ? 1 : 0)) - ((usedLO[b.los[0]] || 0) - (lessonEmph(b.los[0]) || b.emphasis ? 1 : 0)));
      const q = rest.shift(); out.push(q); usedLO[q.los[0]] = (usedLO[q.los[0]] || 0) + 1;
    }
    return out;
  }

  M2.buildMock = function () {
    const D = M2.D, cfg = D.config.mock, plan = M2.mockPlan();
    const inTopic = (q, t) => plan.have.includes(sessOf(q)) && TOPIC[sessOf(q)] === t;
    const concept = [], app = [];
    const nC = alloc(cfg.conceptual, plan.topics), nA = alloc(cfg.case_parts, plan.topics);
    for (const t in plan.topics) {
      const pool = D.questions.filter(q => inTopic(q, t) && q.kind === "concept" && q.type !== "num");
      concept.push(...sample(pool, nC[t]));
      let parts = 0;
      for (const c of shuffle(D.cases.filter(c => inTopic(c, t)))) {   // whole cases only, and only those that fit the topic's quota
        if (parts + c.parts.length > nA[t]) continue;
        app.push(...c.parts.map(p => p.id)); parts += c.parts.length;
      }
      if (parts < nA[t]) {                      // not enough cases yet: fill with standalone apply and calc questions
        const pool = D.questions.filter(q => inTopic(q, t) && q.kind !== "concept" && !concept.includes(q));
        app.push(...sample(pool, nA[t] - parts).map(q => q.id));
      }
    }
    return { started: Date.now(), ids: shuffle(concept).map(q => q.id).concat(app), responses: {},
      nConcept: concept.length };
  };

  M2.renderMock = function (main) {
    const p = M2.store.get(), plan = M2.mockPlan(), cfg = M2.D.config.mock;
    main.append(h("h1", { text: "Mock exam" }));
    if (plan.missing.length) main.append(h("div.banner", { text: "Not in this mock yet: " + plan.missing.map(n => "S" + n).join(", ") + ". Topic weights are renormalized over the sessions that exist." }));
    main.append(h("div.banner.calc", { text: "Calculator only. Scientific or financial calculator, scratch paper, the equation sheet. No notes." }));
    if (!p.mock) {
      main.append(h("p", { text: `${cfg.conceptual} conceptual questions, then cases totaling ${cfg.case_parts} parts. The real exam is 59 multiple choice questions: 25 conceptual and 34 application. No feedback until you submit. Untimed.` }));
      main.append(h("button.primary", { type: "button", text: "Start mock exam", onclick: () => { p.mock = M2.buildMock(); M2.store.commit(); M2.route(); } }));
      if (p.mockHistory.length) {
        const t = h("table.qt", {}, h("tr", {}, h("th", { text: "Date" }), h("th", { text: "Score" })));
        for (const r of p.mockHistory.slice(-10).reverse()) t.append(h("tr", {}, h("td", { text: new Date(r.t).toLocaleString() }), h("td", { text: `${r.right} of ${r.n} (${Math.round(100 * r.right / r.n)}%)` })));
        main.append(h("div.sec-title", { text: "Past mocks" }), t);
      }
      if (p.lastReview) renderReview(main, p.lastReview);
      return;
    }
    const m = p.mock, D = M2.D;
    let lastCase = null;
    m.ids.forEach((id, i) => {
      const q = E.get(D, id);
      if (!q) return;
      if (i === 0) main.append(h("h2", { text: "Part 1: Conceptual" }));
      if (i === m.nConcept) main.append(h("h2", { text: "Part 2: Application" }));
      const showCase = q.caseRef && q.caseRef !== lastCase; lastCase = q.caseRef || null;
      const card = M2.Card(q, { mode: "exam", label: "Question " + (i + 1), hideCase: !showCase, response: m.responses[id],
        onChange: v => { m.responses[id] = v; M2.store.commit(); } });
      main.append(card.el);
    });
    main.append(h("button.primary", { type: "button", text: "Submit exam", onclick: submit }));
    R.math(main);

    function submit() {
      const rows = [];
      let right = 0;
      for (const id of m.ids) {
        const q = E.get(D, id); if (!q) continue;
        const resp = m.responses[id];
        const ok = resp != null && resp !== "" && E.check(q, resp) === true;
        if (ok) right++;
        E.record(p, q, ok);
        rows.push({ id, resp, ok });
      }
      const review = { t: Date.now(), rows, right, n: rows.length, misses: rows.filter(r => !r.ok).length };
      p.mockHistory.push({ t: review.t, right, n: rows.length });
      p.lastReview = review; p.mock = null;
      M2.store.commit(); M2.emit("progress");
      main.innerHTML = ""; main.append(h("h1", { text: "Mock exam review" }));
      renderReview(main, review);
      window.scrollTo(0, 0);
    }
  };

  function renderReview(main, rv) {
    const D = M2.D;
    main.append(h("div.score", { text: `Score: ${rv.right} of ${rv.n} (${Math.round(100 * rv.right / Math.max(1, rv.n))}%). ${rv.misses} misses were added to the missed queue.` }));
    const bySess = {}, byLO = {};
    for (const r of rv.rows) {
      const q = E.get(D, r.id); if (!q) continue;
      const s = "S" + sessOf(q);
      (bySess[s] = bySess[s] || [0, 0])[1]++; if (r.ok) bySess[s][0]++;
      for (const lo of q.los || []) { (byLO[lo] = byLO[lo] || [0, 0])[1]++; if (r.ok) byLO[lo][0]++; }
    }
    const tbl = (title, obj) => {
      const t = h("table.qt", {}, h("tr", {}, h("th", { text: title }), h("th", { text: "Right" }), h("th", { text: "Of" })));
      for (const k of Object.keys(obj).sort()) t.append(h("tr" + (obj[k][0] < obj[k][1] ? ".weak" : ""), {}, h("td", { text: k }), h("td", { text: obj[k][0] }), h("td", { text: obj[k][1] })));
      return t;
    };
    main.append(h("div.sec-title", { text: "By session" }), tbl("Session", bySess), h("div.sec-title", { text: "By objective" }), tbl("Objective", byLO));
    main.append(h("div.sec-title", { text: "Every question" }));
    rv.rows.forEach((r, i) => {
      const q = E.get(D, r.id); if (!q) return;
      const c = M2.Card(q, { mode: "review", label: "Question " + (i + 1), response: r.resp });
      c.reveal(r.ok, r.resp == null || r.resp === "" ? "Not answered." : null);
      main.append(c.el);
    });
    R.math(main);
  }
})(globalThis.M2 = globalThis.M2 || {});
