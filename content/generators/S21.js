// S21 Oligopoly I generators: Cournot equilibrium, best response, Stackelberg, collusion and cheating. Linear demand P = a - b(Q1 + Q2), constant MC.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 2 : d);
  const dem = (a, b) => b === 1 ? `P = ${a} − (Q1 + Q2)` : `P = ${a} − ${b}(Q1 + Q2)`;
  const NAMES = [["Firm 1", "Firm 2"], ["Exxon", "Chevron"], ["Nucor", "U.S. Steel"], ["Saudi Aramco", "Rosneft"], ["Cemex", "Holcim"]];
  // Clean numbers: choose b and a so that (a - c) is divisible by 6b (Cournot thirds and Stackelberg quarters stay whole).
  function market(r, unequal) {
    const b = r.pick([1, 1, 2, 0.5]), c1 = r.pick([0, 2, 4, 5, 10, 20]);
    const c2 = unequal ? c1 + r.pick([3, 6, 9, 12]) : c1;
    const k = r.int(5, 30); const a = c1 + 6 * b * k + (unequal ? (c2 - c1) : 0);
    return { a, b, c1, c2 };
  }
  M2.gen({ id: "S21-02-g1", los: ["S21-02", "S21-06", "S21-04"], kind: "calc", make(r) {
    const unequal = r.chance(0.4), { a, b, c1, c2 } = market(r, unequal), [n1, n2] = r.pick(NAMES);
    const q1 = (a - 2 * c1 + c2) / (3 * b), q2 = (a - 2 * c2 + c1) / (3 * b), P = a - b * (q1 + q2);
    const ask = r.pick(["q1", "P", "pi1"]), ans = ask === "q1" ? q1 : ask === "P" ? P : (P - c1) * q1;
    return { type: "num", answer: ans, unit: ask === "q1" ? "units" : "$", params: { a, b, c1, c2, ask },
      stem: `${n1} and ${n2} choose output at the same time. Inverse demand is ${dem(a, b)}. Marginal costs: ${n1} $${c1}, ${n2} $${c2}. What is ${ask === "q1" ? `${n1}'s Cournot output` : ask === "P" ? "the Cournot market price" : `${n1}'s Cournot profit`}?`,
      explain: `Reaction functions from MR = MC: Q1 = (${a} − ${c1})/(${2 * b}) − 0.5Q2 = ${fmt((a - c1) / (2 * b))} − 0.5Q2 and Q2 = ${fmt((a - c2) / (2 * b))} − 0.5Q1. ` +
        (c1 === c2 ? `Identical costs: each makes (a − c)/(3b) = ${a - c1}/${3 * b} = ${fmt(q1)}. ` : `Solving: Q1 = (a − 2c1 + c2)/(3b) = (${a} − ${2 * c1} + ${c2})/${3 * b} = ${fmt(q1)}, Q2 = (${a} − ${2 * c2} + ${c1})/${3 * b} = ${fmt(q2)}. `) +
        `Total Q = ${fmt(q1 + q2)}, P = ${a} − ${b} × ${fmt(q1 + q2)} = $${fmt(P)}. Profit = (P − c1) × Q1 = ${fmt(P - c1)} × ${fmt(q1)} = $${fmt((P - c1) * q1)}. Not on the equation sheet.` };
  } });

  M2.gen({ id: "S21-04-g1", los: ["S21-04", "S21-06"], kind: "calc", make(r) {
    const { a, b, c1 } = market(r, false), base = (a - c1) / (2 * b), q2 = 2 * r.int(1, Math.floor(base / 2) - 1);
    const ans = base - q2 / 2;
    return { type: "num", answer: ans, unit: "units", params: { a, b, c1, q2 },
      stem: `Inverse demand is ${dem(a, b)} and your marginal cost is $${c1}. Your rival will produce ${q2} units. What output maximizes your profit?`,
      explain: `MR1 = ${a} − ${b}Q2 − ${2 * b}Q1. Set MR1 = ${c1}: Q1 = (${a} − ${c1})/${2 * b} − 0.5Q2 = ${fmt(base)} − 0.5(${q2}) = ${fmt(ans)}. This is your reaction function evaluated at the rival's output.` };
  } });

  M2.gen({ id: "S21-03-g1", los: ["S21-03", "S21-06"], kind: "calc", make(r) {
    const unequal = r.chance(0.3), [n1, n2] = r.pick(NAMES); let m;
    do { m = market(r, unequal); } while ((m.a - m.c2) / (2 * m.b) - (m.a + m.c2 - 2 * m.c1) / (4 * m.b) < 1);
    const { a, b, c1, c2 } = m, q1 = (a + c2 - 2 * c1) / (2 * b), q2 = (a - c2) / (2 * b) - q1 / 2, P = a - b * (q1 + q2);
    const ask = r.pick(["q1", "q2", "P", "pi1", "pi2"]);
    const ans = { q1, q2, P, pi1: (P - c1) * q1, pi2: (P - c2) * q2 }[ask];
    const lab = { q1: `${n1}'s (leader) output`, q2: `${n2}'s (follower) output`, P: "the market price", pi1: `${n1}'s profit`, pi2: `${n2}'s profit` }[ask];
    return { type: "num", answer: ans, unit: ask.startsWith("q") ? "units" : "$", params: { a, b, c1, c2, ask },
      stem: `${n1} builds capacity first; ${n2} sees it and then chooses its output. Inverse demand is ${dem(a, b)}. Marginal costs: ${n1} $${c1}, ${n2} $${c2}. What is ${lab}?`,
      explain: `Stackelberg, ${n1} leads. Leader: Q1 = (a + c2 − 2c1)/(2b) = (${a} + ${c2} − ${2 * c1})/${2 * b} = ${fmt(q1)}. Follower's reaction: Q2 = ${fmt((a - c2) / (2 * b))} − 0.5(${fmt(q1)}) = ${fmt(q2)}. ` +
        `P = ${a} − ${b} × ${fmt(q1 + q2)} = $${fmt(P)}. Profits: leader ${fmt(P - c1)} × ${fmt(q1)} = $${fmt((P - c1) * q1)}; follower ${fmt(P - c2)} × ${fmt(q2)} = $${fmt((P - c2) * q2)}.` };
  } });

  M2.gen({ id: "S21-06-g1", los: ["S21-06", "S21-02"], kind: "calc", make(r) {
    const { a, b, c1 } = market(r, false), c = c1;
    const Qm = (a - c) / (2 * b), Pm = a - b * Qm, quota = Qm / 2;
    const qc = (a - c) / (2 * b) - quota / 2, Pc = a - b * (qc + quota);
    const ask = r.pick(["collude", "cheat", "gain"]);
    const pc = (Pm - c) * quota, pch = (Pc - c) * qc, ans = ask === "collude" ? pc : ask === "cheat" ? pch : pch - pc;
    return { type: "num", answer: ans, unit: "$", params: { a, b, c, ask },
      stem: `Two firms face ${dem(a, b)} and each has marginal cost $${c}. They agree to split the monopoly output equally. ${ask === "collude" ? "What does each firm earn if both keep the agreement?" : ask === "cheat" ? "If firm 2 keeps its quota and firm 1 produces its best response instead, what does firm 1 earn?" : "How much more does firm 1 earn by cheating (best-responding to firm 2's quota) than by keeping the agreement?"}`,
      explain: `Monopoly: MR = ${a} − ${2 * b}Q = ${c} gives Q = ${fmt(Qm)}, P = $${fmt(Pm)}; quota ${fmt(quota)} each, profit ${fmt(Pm - c)} × ${fmt(quota)} = $${fmt(pc)}. ` +
        `Cheating: Q1 = ${fmt((a - c) / (2 * b))} − 0.5(${fmt(quota)}) = ${fmt(qc)}, P = ${a} − ${b} × ${fmt(qc + quota)} = $${fmt(Pc)}, profit ${fmt(Pc - c)} × ${fmt(qc)} = $${fmt(pch)}. ` +
        `Gain from cheating $${fmt(pch - pc)}, which is why one-shot cartels break down.` };
  } });
})();
