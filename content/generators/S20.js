// S20 Game Theory II generators: repeated-game present values, threshold interest rates, backward induction, entry deterrence.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 2 : d);
  const FIRMS = [["Kellogg's", "General Mills", "not advertising"], ["Coke", "Pepsi", "keeping prices high"], ["Delta", "United", "limiting capacity"], ["Visa", "Mastercard", "maintaining fees"]];
  const RATES = [0.05, 0.08, 0.1, 0.12, 0.15, 0.2, 0.25, 0.4, 0.5, 0.8, 1, 1.5, 2];
  function payoffs(r) { const n = r.int(0, 6), c = n + r.int(2, 12), d = c + r.int(1, 20); return { c, d, n }; }

  // PV of colluding vs cheating at a given rate: ask for one PV or the decision.
  M2.gen({ id: "S20-01-g1", los: ["S20-01", "S20-03"], kind: "calc", make(r) {
    const [a, b, act] = r.pick(FIRMS), { c, d, n } = payoffs(r); let i;
    do { i = r.pick(RATES); } while (Math.abs((c + c / i) - (d + n / i)) < 0.5);
    const pc = c + c / i, pd = d + n / i, ask = r.pick(["collude", "cheat", "decide"]);
    const setup = `${a} and ${b} collude by ${act}. Each earns ${c} per period while both collude. If ${a} cheats, it earns ${d} this period, then ${b} punishes forever and ${a} earns ${n} per period. The interest rate is ${fmt(i * 100)}%.`;
    const ex = `Professor's convention: PV collude = ${c} + ${c}/${fmt(i)} = ${fmt(pc)}. PV cheat = ${d} + ${n}/${fmt(i)} = ${fmt(pd)}.`;
    if (ask === "decide") {
      const coll = pc > pd, choices = r.shuffle([`Collude: ${fmt(pc)} > ${fmt(pd)}`, `Cheat: ${fmt(pd)} > ${fmt(pc)}`, `Cheat: ${d} > ${c}`, `Collude: ${c} > ${n}`]);
      const right = coll ? `Collude: ${fmt(pc)} > ${fmt(pd)}` : `Cheat: ${fmt(pd)} > ${fmt(pc)}`;
      return { type: "mc", choices, answer: choices.indexOf(right), params: { c, d, n, i, ask },
        stem: setup + `\n\nShould ${a} keep colluding or cheat?`, explain: ex + ` ${coll ? "Colluding" : "Cheating"} has the higher present value. Comparing one-period payoffs alone ignores the future.` };
    }
    return { type: "num", answer: ask === "collude" ? pc : pd, unit: "", params: { c, d, n, i, ask },
      stem: setup + `\n\nWhat is the present value of ${ask === "collude" ? "colluding forever (count this period's payoff)" : "cheating this period and being punished forever after"}?`, explain: ex };
  } });

  // Threshold interest rate i* = (c - n)/(d - c).
  M2.gen({ id: "S20-03-g1", los: ["S20-03", "S20-01"], kind: "calc", make(r) {
    const [a, b, act] = r.pick(FIRMS); let p; do { p = payoffs(r); } while (Math.abs(((p.c - p.n) / (p.d - p.c)) * 100 - Math.round(((p.c - p.n) / (p.d - p.c)) * 100)) > 1e-9);
    const { c, d, n } = p, is = (c - n) / (d - c);
    return { type: "num", answer: is, unit: "decimal rate", params: { c, d, n },
      stem: `${a} and ${b} each earn ${c} per period while ${act}. A firm that cheats earns ${d} once, then ${n} per period forever under a trigger strategy. What is the highest interest rate (as a decimal) at which collusion can be sustained?`,
      explain: `Set the present values equal: ${c} + ${c}/i = ${d} + ${n}/i. So (${c} − ${n})/i = ${d} − ${c}, and i* = ${c - n}/${d - c} = ${fmt(is, 3)}. Collusion holds for any i up to ${fmt(is * 100, 1)}%. Not on the equation sheet.` };
  } });

  // Backward induction on a random 2 or 3 stage tree.
  const ACTS = [["Enter", "Stay out"], ["Expand", "Wait"], ["Launch", "Hold"], ["Cut price", "Keep price"], ["Match", "Ignore"], ["Advertise", "Don't"]];
  function build(r, depth, players, mover) {
    if (depth === 0) return null;
    const [x, y] = r.pick(ACTS), cont = r.chance(depth > 1 ? 0.75 : 0);
    const leaf = () => ({ pay: [r.int(-4, 12), r.int(-4, 12)] });
    const kid = a => { const sub = cont ? build(r, depth - 1, players, 1 - mover) : null; return sub ? { a, n: sub } : { a, ...leaf() }; };
    return { p: mover, children: [kid(x), { a: y, ...leaf() }] };
  }
  function solve(n) { if (n.pay) return n.pay; let best = null, bi = 0;
    n.children.forEach((c, k) => { const v = solve(c.n || c); if (!best || v[n.p] > best[n.p]) { best = v; bi = k; } }); n.best = bi; n.val = best; return best; }
  function ties(n) { if (n.pay) return false; const v = n.children.map(c => solve(c.n || c)[n.p]); return v[0] === v[1] || n.children.some(c => ties(c.n || c)); }
  function outline(n, P, pre, out) { n.children.forEach(c => { const lab = [...pre, `${P[n.p]} ${c.a}`]; if (c.n) outline(c.n, P, lab, out); else out.push(`- ${lab.join(" → ")}: (${c.pay.join(", ")})`); }); return out; }
  function steps(n, P, out) { if (n.pay) return out; n.children.forEach(c => { if (c.n) steps(c.n, P, out); });
    out.push(`${P[n.p]} compares ${n.children.map(c => `${c.a} (${solve(c.n || c)[n.p]})`).join(" with ")} and picks ${n.children[n.best].a}.`); return out; }

  M2.gen({ id: "S20-06-g1", los: ["S20-06", "S20-04", "S20-05"], kind: "calc", make(r) {
    const P = r.pick([["Firm A", "Firm B"], ["Leader", "Follower"], ["Startup", "Incumbent"], ["Union", "Management"]]);
    let t; do { t = build(r, r.chance(0.5) ? 3 : 2, P, 0); } while (!t.children[0].n || ties(t));
    const v = solve(t), who = r.int(0, 1);
    return { type: "num", answer: v[who], unit: "", params: { tree: t, who },
      stem: `${P[0]} moves first. Payoffs: (${P[0]}, ${P[1]}).\n\n${outline(t, P, [], []).join("\n")}\n\nWhat is ${P[who]}'s payoff in the subgame perfect equilibrium?`,
      explain: `Backward induction, last moves first. ${steps(t, P, []).join(" ")} Outcome (${v.join(", ")}).` };
  } });

  // Entry deterrence: is the threat credible, and what happens?
  M2.gen({ id: "S20-08-g1", los: ["S20-08", "S20-06"], kind: "calc", make(r) {
    let mono, fE, fI, aE, aI; do { mono = r.int(8, 20); fE = -r.int(1, 6); fI = r.int(0, 10); aE = r.int(1, 8); aI = r.int(1, mono - 1); } while (fI === aI);
    const credible = fI > aI, outcome = credible ? "stay" : "enter";
    const choices = [`The entrant stays out: fighting pays the incumbent ${fI} > ${aI}, so the threat is credible`, `The entrant enters and the incumbent accommodates: ${aI} > ${fI}, so the threat to fight is not credible`,
      `The entrant enters and the incumbent fights, since ${mono} is the incumbent's best payoff`, `The entrant stays out, since the incumbent earns ${mono} when it does`];
    const order = r.shuffle([0, 1, 2, 3]), ans = order.indexOf(credible ? 0 : 1);
    return { type: "mc", choices: order.map(k => choices[k]), answer: ans, params: { mono, fE, fI, aE, aI, outcome },
      stem: `An entrant decides whether to enter. If it enters, the incumbent fights or accommodates. Payoffs (Entrant, Incumbent): Stay out (0, ${mono}); Enter and Fight (${fE}, ${fI}); Enter and Accommodate (${aE}, ${aI}). What is the subgame perfect equilibrium?`,
      explain: `Start with the incumbent after entry: Fight ${fI} vs Accommodate ${aI}, so it ${credible ? "fights" : "accommodates"}. The entrant compares Enter (${credible ? fE : aE}) with Stay out (0) and ${credible ? "stays out" : "enters"}. The incumbent's ${mono} matters only if the entrant stays out.` };
  } });
})();
