// S22 Oligopoly II generators: standard Bertrand (equal and unequal costs), differentiated Bertrand (Bryce's demand and the general linear form), comparing the four models.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 2 : d);
  const PAIRS = [["Firm 1", "Firm 2"], ["Coke", "Pepsi"], ["Dell", "HP"], ["Snowbird", "Alta"], ["Delta", "United"]];

  M2.gen({ id: "S22-01-g1", los: ["S22-01", "S22-04"], kind: "calc", make(r) {
    const k = r.pick([1, 2, 5, 10]), c1 = r.pick([5, 10, 15, 20, 25]), unequal = r.chance(0.6), c2 = unequal ? c1 + r.pick([2, 4, 5, 8, 10]) : c1;
    const A = k * (2 * c2 + r.int(2, 20) * 5);              // monopoly price for firm 1 is above c2
    const p = c2, Q = A - k * p, ask = unequal ? r.pick(["P", "pi1", "Q"]) : r.pick(["P", "Q"]);
    const ans = ask === "P" ? p : ask === "Q" ? (unequal ? Q : Q / 2) : (p - c1) * Q;
    const pm = (A / k + c1) / 2;
    return { type: "num", answer: ans, unit: ask === "Q" ? "units" : "$", params: { A, k, c1, c2, ask },
      stem: `Two sellers of an identical product compete on price. Market demand is Q = ${A} − ${k}P. Consumers see all prices and have no switching costs. Firm 1's marginal cost is $${c1}; firm 2's is $${c2}. ` +
        (ask === "P" ? "What is the equilibrium price? (Treat 'just below' a cost as equal to it.)" : ask === "Q" ? (unequal ? "How many units does firm 1 sell?" : "How many units does each firm sell?") : "About how much profit does firm 1 earn? (Treat 'just below' a cost as equal to it.)"),
      explain: unequal ? `Firm 1 has the lower cost, so it prices just below firm 2's MC of $${c2} and takes the whole market (its monopoly price, (${A}/${k} + ${c1})/2 = $${fmt(pm)}, is higher, so $${c2} binds). Q = ${A} − ${k}(${c2}) = ${Q}. Profit ≈ (${c2} − ${c1}) × ${Q} = $${(c2 - c1) * Q}. Firm 2 sells nothing.`
        : `Equal costs: undercutting drives price to MC = $${c1}. Q = ${A} − ${k}(${c1}) = ${Q}, split evenly: ${fmt(Q / 2)} each. Profit is zero.` };
  } });

  M2.gen({ id: "S22-02-g1", los: ["S22-02", "S22-04"], kind: "calc", make(r) {
    const a = r.int(4, 20) * 10, c = r.pick([0, 5, 10, 15, 20, 25, 30]), [n1, n2] = r.pick(PAIRS), ask = r.pick(["p", "q", "pi"]);
    const p = a + c, q = a, pi = (p - c) * q, ans = { p, q, pi }[ask];
    return { type: "num", answer: ans, unit: ask === "q" ? "units" : "$", params: { a, c, ask },
      stem: `${n1} and ${n2} sell differentiated products and compete on price. Each firm's demand is Q_i = ${a} − p_i + p_j (Bryce's form), and each has marginal cost $${c}. ${ask === "p" ? "What is the equilibrium price?" : ask === "q" ? "How many units does each firm sell in equilibrium?" : "What is each firm's equilibrium profit?"}`,
      explain: `Profit (p_i − ${c})(${a} − p_i + p_j). Setting the derivative to zero: ${a} − 2p_i + p_j + ${c} = 0, so p_i = (${a} + p_j + ${c})/2. Symmetric: p = (${a + c} + p)/2, so p = a + c = $${p}. Q = ${a} − ${p} + ${p} = ${q}. Profit = (${p} − ${c}) × ${q} = $${pi}. Not on the equation sheet.` };
  } });

  M2.gen({ id: "S22-04-g1", los: ["S22-04", "S22-02"], kind: "calc", make(r) {
    let al, be, ga, c, pj, br; const [n1, n2] = r.pick(PAIRS);
    do { be = r.pick([1, 2, 4, 5]); ga = r.pick([1, 2].filter(g => g < 2 * be)); c = r.pick([0, 5, 10, 20]); al = r.int(5, 40) * 10; pj = r.int(2, 20) * 5;
      br = (al + be * c + ga * pj) / (2 * be); } while (Math.abs(br * 100 - Math.round(br * 100)) > 1e-9);
    const ask = r.pick(["br", "eq"]), eq = (al + be * c) / (2 * be - ga), ans = ask === "br" ? br : eq;
    return { type: "num", answer: ans, unit: "$", params: { al, be, ga, c, pj, ask },
      stem: `${n1}'s demand is q1 = ${al} − ${be}p1 + ${ga}p2 (${n2}'s is symmetric). Marginal cost is $${c} for both. ${ask === "br" ? `${n2} charges $${pj}. What price maximizes ${n1}'s profit?` : "What is the symmetric equilibrium price?"}`,
      explain: `Profit (p1 − ${c})(${al} − ${be}p1 + ${ga}p2). Derivative: ${al} − ${2 * be}p1 + ${ga}p2 + ${be * c} = 0, so p1 = (${al} + ${be * c} + ${ga}p2)/${2 * be}. ` +
        (ask === "br" ? `With p2 = ${pj}: p1 = (${al + be * c} + ${ga * pj})/${2 * be} = $${fmt(br)}.` : `Symmetric: p = (${al + be * c} + ${ga}p)/${2 * be}, so (${2 * be} − ${ga})p = ${al + be * c} and p = $${fmt(eq)}.`) + " Price reaction functions slope up." };
  } });

  M2.gen({ id: "S22-04-g2", los: ["S22-04", "S22-01", "S21-06"], kind: "calc", make(r) {
    const b = r.pick([1, 2]), c = r.pick([0, 2, 4, 10, 20]), a = c + 12 * b * r.int(3, 25);
    const model = r.pick(["Collusion", "Cournot", "Stackelberg (firm 1 leads)", "Bertrand"]);
    const Q = { "Collusion": (a - c) / (2 * b), "Cournot": 2 * (a - c) / (3 * b), "Stackelberg (firm 1 leads)": 3 * (a - c) / (4 * b), "Bertrand": (a - c) / b }[model];
    const P = a - b * Q;
    return { type: "num", answer: P, unit: "$", params: { a, b, c, model },
      stem: `Two identical firms face inverse demand P = ${a} − ${b === 1 ? "" : b}(Q1 + Q2) and marginal cost $${c}. What is the market price under ${model}${model === "Bertrand" ? " (identical products, price competition)" : ""}?`,
      explain: `${model === "Collusion" ? `Joint monopoly: MR = ${a} − ${2 * b}Q = ${c}, Q = ${fmt(Q)}.` : model === "Cournot" ? `Each makes (a − c)/(3b) = ${fmt((a - c) / (3 * b))}; Q = ${fmt(Q)}.` : model === "Bertrand" ? `P = MC, so Q = (a − c)/b = ${fmt(Q)}.` : `Leader (a − c)/(2b) = ${fmt((a - c) / (2 * b))}, follower half that = ${fmt((a - c) / (4 * b))}; Q = ${fmt(Q)}.`} P = ${a} − ${b} × ${fmt(Q)} = $${fmt(P)}. Price falls from collusion to Cournot to Stackelberg to Bertrand.` };
  } });
})();
