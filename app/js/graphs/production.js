// Production: total, average and marginal product of labor, marginal returns ranges, and VMP = P x MP against the wage.
// params: {form: "cubic"|"cd"|"table", a, b, c (Q = aL + bL^2 - cL^3), A, K, alpha, beta (Q = A K^alpha L^beta),
//          table: [[L, Q], ...], P, w, Lmax}
(function (M2) {
  const G = M2.G, C = G.C;
  M2.graphs.production = function (holder, params) {
    const pr = Object.assign({ form: "cubic", a: 2, b: 3, c: 0.1, A: 2, K: 9, alpha: 0.5, beta: 0.5, P: 4, w: 60, Lmax: 25 }, params);
    const isTable = pr.form === "table";
    const specs = [{ key: "form", label: "Function", value: pr.form, options: [["cubic", "Cubic: aL + bL² − cL³"], ["cd", "Cobb-Douglas, K fixed"], ["table", "Table"]].filter(o => o[0] !== "table" || pr.table) }];
    specs.push({ key: "P", label: "Price P", min: 0.5, max: 50, step: 0.5, value: pr.P }, { key: "w", label: "Wage w", min: 1, max: 400, step: 1, value: pr.w });
    if (!isTable) specs.push(
      { key: "a", label: "a", min: 0, max: 20, step: 0.5, value: pr.a }, { key: "b", label: "b", min: 0, max: 10, step: 0.1, value: pr.b },
      { key: "c", label: "c", min: 0.01, max: 1, step: 0.01, value: pr.c }, { key: "K", label: "K (CD)", min: 1, max: 100, step: 1, value: pr.K },
      { key: "beta", label: "β on L (CD)", min: 0.1, max: 0.95, step: 0.05, value: pr.beta });
    const v = G.controls(holder, specs, draw);
    const top = G.plot(holder, { h: 260, xlabel: "Labor L", ylabel: "Total product Q", title: "Total product" });
    const mid = G.plot(holder, { h: 260, xlabel: "Labor L", ylabel: "Units per worker", title: "Average and marginal product" });
    const bot = G.plot(holder, { h: 240, xlabel: "Labor L", ylabel: "Dollars", title: "Value marginal product vs wage" });
    const out = G.readout(holder);

    function model() {
      if (v.form === "table" && pr.table) {
        const T = pr.table, L = T.map(r => r[0]), Q = T.map(r => r[1]);
        const MP = Q.map((q, i) => i ? q - Q[i - 1] : null), AP = Q.map((q, i) => L[i] ? q / L[i] : null);
        return { discrete: true, L, Q, MP, AP, Lmax: Math.max(...L) };
      }
      if (v.form === "cd") {
        const A = pr.A, Ka = Math.pow(v.K, pr.alpha), be = v.beta;
        const Q = L => A * Ka * Math.pow(L, be), MP = L => be * A * Ka * Math.pow(L, be - 1), AP = L => A * Ka * Math.pow(L, be - 1);
        const Lstar = Math.pow(v.P * be * A * Ka / v.w, 1 / (1 - be));
        return { Q, MP, AP, Lmax: Math.max(pr.Lmax, Math.min(Lstar * 1.6, 2000)), Lstar, apMax: null, mp0: null };
      }
      const a = v.a, b = v.b, c = v.c;
      const Q = L => a * L + b * L * L - c * L * L * L, MP = L => a + 2 * b * L - 3 * c * L * L, AP = L => a + b * L - c * L * L;
      const mp0 = (2 * b + Math.sqrt(4 * b * b + 12 * c * a)) / (6 * c);      // MP = 0
      const apMax = b / (2 * c);                                               // AP peaks, MP = AP
      const mpMax = b / (3 * c);
      const disc = 4 * b * b - 12 * c * (v.w / v.P - a);
      const Lstar = disc >= 0 ? (2 * b + Math.sqrt(disc)) / (6 * c) : null;   // VMP = w on the falling part of MP
      return { Q, MP, AP, Lmax: mp0 * 1.15, Lstar, apMax, mp0, mpMax };
    }

    function draw() {
      const m = model();
      if (m.discrete) {
        const qmax = Math.max(...m.Q) * 1.1, mpmax = Math.max(...m.MP.filter(x => x != null), ...m.AP.filter(x => x != null)) * 1.15;
        const mpmin = Math.min(0, ...m.MP.filter(x => x != null)) * 1.15;
        top.clear(m.Lmax, qmax, 0); mid.clear(m.Lmax, mpmax, mpmin); bot.clear(m.Lmax, mpmax * v.P, mpmin * v.P);
        top.poly(m.L.map((l, i) => [l, m.Q[i]]), C.a);
        m.L.forEach((l, i) => top.dot(l, m.Q[i], C.a));
        mid.poly(m.L.map((l, i) => [l, m.MP[i]]).filter(p => p[1] != null), C.b);
        mid.poly(m.L.map((l, i) => [l, m.AP[i]]).filter(p => p[1] != null), C.c);
        bot.poly(m.L.map((l, i) => [l, m.MP[i] == null ? null : v.P * m.MP[i]]).filter(p => p[1] != null), C.e);
        bot.hline(v.w, C.d, "6 4", "wage $" + G.fmt(v.w));
        let Lstar = 0;
        m.L.forEach((l, i) => { if (m.MP[i] != null && v.P * m.MP[i] >= v.w && l > Lstar) Lstar = l; });
        if (Lstar) { bot.vline(Lstar, C.c, "3 3", "L* = " + Lstar); top.vline(Lstar, C.c, "3 3"); }
        mid.legend([["MP (change in Q)", C.b], ["AP = Q/L", C.c]]); bot.legend([["VMP = P × MP", C.e], ["wage", C.d]]);
        out.innerHTML = `Hire while VMP ≥ w. Last worker with P × MP ≥ $${G.fmt(v.w)}: <b>L* = ${Lstar || "none"}</b>. MP by worker: ${m.MP.slice(1).map((x, i) => `${m.L[i + 1]}:${x}`).join("  ")}`;
        return;
      }
      const L1 = m.Lmax;
      let qmax = 0, apmax = 0;
      for (let i = 1; i <= 100; i++) { const L = L1 * i / 100; qmax = Math.max(qmax, m.Q(L)); apmax = Math.max(apmax, m.MP(L), m.AP(L)); }
      if (v.form === "cd") apmax = Math.max(m.AP(L1 * 0.08), 1);
      top.clear(L1, qmax * 1.1, 0); mid.clear(L1, apmax * 1.15, Math.min(0, m.MP(L1)) * 1.1); bot.clear(L1, apmax * 1.15 * v.P, Math.min(0, m.MP(L1)) * 1.1 * v.P);
      if (m.apMax) {
        [top, mid].forEach(P => { P.band(0, m.mpMax, C.c, "increasing MP"); P.band(m.mpMax, m.mp0, C.b, "diminishing MP"); P.band(m.mp0, L1, C.d, "negative MP"); });
      }
      top.fn(m.Q, C.a, 0.001);
      mid.fn(m.MP, C.b, 0.001); mid.fn(m.AP, C.c, 0.001);
      if (m.apMax) mid.dot(m.apMax, m.AP(m.apMax), C.c, "MP = AP, AP max");
      bot.fn(L => v.P * m.MP(L), C.e, 0.001); bot.hline(v.w, C.d, "6 4", "wage $" + G.fmt(v.w));
      if (m.Lstar && m.Lstar < L1 * 1.5) { bot.dot(m.Lstar, v.w, C.c, "VMP = w"); bot.vline(m.Lstar, C.c, "3 3"); top.dot(m.Lstar, m.Q(m.Lstar), C.c, "L*"); }
      mid.legend([["MP = dQ/dL", C.b], ["AP = Q/L", C.c]]); bot.legend([["VMP = P × MP", C.e], ["wage", C.d]]);
      const eq = v.form === "cd" ? `Q = ${pr.A}·K^${pr.alpha}·L^${G.fmt(v.beta)}, K = ${v.K}` : `Q = ${v.a}L + ${v.b}L² − ${v.c}L³`;
      out.innerHTML = `${eq}. Profit maximizing labor where P × MP = w: <b>L* = ${G.fmt(m.Lstar)}</b>, Q = ${G.fmt(m.Lstar ? m.Q(m.Lstar) : null)}` +
        (m.apMax ? `. Diminishing returns start at L = ${G.fmt(m.mpMax)}; MP turns negative at L = ${G.fmt(m.mp0)}.` : ". Cobb-Douglas with β < 1 has diminishing MP everywhere.");
    }
    draw();
  };
})(globalThis.M2 = globalThis.M2 || {});
