// Oligopoly reaction curves.
// mode "quantity": inverse demand P = a - b(Q1 + Q2), constant marginal costs c1, c2. Shows Cournot, Stackelberg (firm 1 leads),
//   collusion (joint monopoly split equally, needs c1 = c2 for the split to be the textbook one) and homogeneous Bertrand.
// mode "price": differentiated Bertrand with demand q1 = al - be P1 + ga P2 (symmetric), marginal cost c.
// params: {mode, a, b, c1, c2, al, be, ga, c}
(function (M2) {
  const G = M2.G, C = G.C;
  M2.graphs.reaction = function (holder, params) {
    const pr = Object.assign({ mode: "quantity", a: 1000, b: 1, c1: 4, c2: 4, al: 100, be: 2, ga: 1, c: 10 }, params);
    (pr.mode === "price" ? price : quantity)(holder, pr);
  };

  function quantity(holder, pr) {
    const v = G.controls(holder, [
      { key: "a", label: "Intercept a", min: 10, max: 2000, step: 1, value: pr.a },
      { key: "b", label: "Slope b", min: 0.1, max: 10, step: 0.1, value: pr.b },
      { key: "c1", label: "Firm 1 MC", min: 0, max: 500, step: 1, value: pr.c1 },
      { key: "c2", label: "Firm 2 MC", min: 0, max: 500, step: 1, value: pr.c2 }], draw);
    const P = G.plot(holder, { h: 400, xlabel: "Q1", ylabel: "Q2", title: "Cournot reaction functions" });
    const out = G.readout(holder);
    function draw() {
      const { a, b, c1, c2 } = v;
      const r1 = Q2 => Math.max(0, (a - c1) / (2 * b) - Q2 / 2), r2 = Q1 => Math.max(0, (a - c2) / (2 * b) - Q1 / 2);
      const q1 = (a - 2 * c1 + c2) / (3 * b), q2 = (a - 2 * c2 + c1) / (3 * b);
      const Pc = a - b * (q1 + q2);
      const s1 = (a - 2 * c1 + c2) / (2 * b), s2 = r2(s1), Ps = a - b * (s1 + s2);
      const Qm = (a - c1) / (2 * b), Pm = a - b * Qm;
      const m = Math.max((a - c1) / b, (a - c2) / b);
      P.clear(m * 1.02, m * 1.02, 0);
      P.poly([[(a - c1) / (2 * b), 0], [0, (a - c1) / b]], C.a);             // r1: Q1 = (a-c1)/2b - Q2/2
      P.poly([[0, (a - c2) / (2 * b)], [(a - c2) / b, 0]], C.d);             // r2
      P.poly([[Qm, 0], [0, Qm]], C.muted, { "stroke-dasharray": "4 4", "stroke-width": 1.2 });
      P.dot(q1, q2, C.c, "Cournot"); P.dot(s1, s2, C.b, "Stackelberg"); P.dot(Qm / 2, Qm / 2, C.e, "Collusion");
      P.legend([["Firm 1 reaction r1", C.a], ["Firm 2 reaction r2", C.d], ["Q1 + Q2 = monopoly output", C.muted]]);
      const pi = (q, p, c) => (p - c) * q;
      const row = (name, a1, a2, p) => `<tr><td>${name}</td><td>${G.fmt(a1)}</td><td>${G.fmt(a2)}</td><td>${G.fmt(a1 + a2)}</td><td>$${G.fmt(p)}</td><td>$${G.fmt(pi(a1, p, c1))}</td><td>$${G.fmt(pi(a2, p, c2))}</td></tr>`;
      const bq = c1 === c2 ? (a - c1) / b : null;
      out.innerHTML = `P = ${G.fmt(a)} − ${G.fmt(b)}Q. Reaction functions: Q1 = (a − c1)/(2b) − Q2/2 = ${G.fmt((a - c1) / (2 * b))} − 0.5 Q2, Q2 = ${G.fmt((a - c2) / (2 * b))} − 0.5 Q1.` +
        `<table class="qt"><tr><th>Model</th><th>Q1</th><th>Q2</th><th>Q</th><th>P</th><th>π1</th><th>π2</th></tr>` +
        row("Collusion (split)", Qm / 2, Qm / 2, Pm) + row("Cournot", q1, q2, Pc) + row("Stackelberg (1 leads)", s1, s2, Ps) +
        (bq != null ? row("Bertrand (homogeneous)", bq / 2, bq / 2, c1) : "") + `</table>` +
        (c1 !== c2 ? "With unequal costs, homogeneous Bertrand has the low cost firm take the market at a price just under the rival's cost." : "");
    }
    draw();
  }

  function price(holder, pr) {
    const v = G.controls(holder, [
      { key: "al", label: "Demand intercept α", min: 10, max: 500, step: 1, value: pr.al },
      { key: "be", label: "Own price effect β", min: 0.1, max: 10, step: 0.1, value: pr.be },
      { key: "ga", label: "Rival price effect γ", min: 0, max: 5, step: 0.1, value: pr.ga },
      { key: "c", label: "Marginal cost c", min: 0, max: 200, step: 1, value: pr.c }], draw);
    const P = G.plot(holder, { h: 400, xlabel: "P1", ylabel: "P2", title: "Differentiated Bertrand reaction functions" });
    const out = G.readout(holder);
    function draw() {
      const { al, be, ga, c } = v;
      const r = Pr => (al + be * c + ga * Pr) / (2 * be);                      // from d(profit)/dP1 = 0
      const Ps = (al + be * c) / (2 * be - ga);
      const m = Math.max(Ps * 2, r(Ps * 2) * 1.2);
      P.clear(m, m, 0);
      P.fn(P1 => (2 * be * P1 - al - be * c) / ga, C.a, r(0), m);              // P1 = r(P2) drawn as P2 in terms of P1
      P.fn(P1 => r(P1), C.d, 0, m);
      P.dot(Ps, Ps, C.c, "Nash prices");
      P.legend([["Firm 1 reaction r1", C.a], ["Firm 2 reaction r2", C.d]]);
      const q = al - be * Ps + ga * Ps;
      out.innerHTML = `Demand q1 = ${G.fmt(al)} − ${G.fmt(be)}P1 + ${G.fmt(ga)}P2. Profit (P1 − c)q1; set dπ/dP1 = 0 to get the reaction function P1 = (α + βc + γP2)/(2β) = ${G.fmt((al + be * c) / (2 * be))} + ${G.fmt(ga / (2 * be))}P2. ` +
        `Symmetric equilibrium P* = (α + βc)/(2β − γ) = <b>$${G.fmt(Ps)}</b>, each firm sells ${G.fmt(q)} and earns $${G.fmt((Ps - c) * q)}. ` +
        "Prices are strategic complements: the reaction curves slope up, so a rival's higher price lets you charge more.";
    }
    draw();
  }
})(globalThis.M2 = globalThis.M2 || {});
