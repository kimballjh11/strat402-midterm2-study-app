// S19 Game Theory I generators: payoff matrices with dominant strategies, unique pure Nash equilibria, mixed strategies, dilemmas.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 3 : d);
  const mat = (rp, cp, rows, cols, pay) => `| ${rp} \\ ${cp} | ${cols.join(" | ")} |\n|${"---|".repeat(cols.length + 1)}\n` +
    rows.map((r, i) => `| ${r} | ${pay[i].map(c => c.join(", ")).join(" | ")} |`).join("\n");
  const nash = pay => { const out = []; const R = pay.length, C = pay[0].length;
    for (let i = 0; i < R; i++) for (let j = 0; j < C; j++) {
      const rb = pay.every(row => row[j][0] <= pay[i][j][0]), cb = pay[i].every(c => c[1] <= pay[i][j][1]);
      if (rb && cb) out.push([i, j]); }
    return out; };
  const domRow = pay => { for (let i = 0; i < pay.length; i++) if (pay[0].every((_, j) => pay.every((row, k) => k === i || row[j][0] < pay[i][j][0]))) return i; return null; };
  const domCol = pay => { for (let j = 0; j < pay[0].length; j++) if (pay.every(row => row.every((c, k) => k === j || c[1] < row[j][1]))) return j; return null; };
  const NAMES = [["Firm A", "Firm B", ["Low price", "High price", "Match"], ["Low price", "High price", "Match"]], ["Delta", "United", ["Add flights", "Hold", "Cut"], ["Add flights", "Hold", "Cut"]],
                 ["Nike", "Adidas", ["Advertise", "Don't", "Sponsor"], ["Advertise", "Don't", "Sponsor"]], ["Row", "Column", ["Top", "Middle", "Bottom"], ["Left", "Center", "Right"]]];
  function randGame(r, n) { const pay = []; for (let i = 0; i < n; i++) { pay.push([]); for (let j = 0; j < n; j++) pay[i].push([r.int(0, 12), r.int(0, 12)]); } return pay; }
  const distinct = pay => { const n = pay.length;
    for (let j = 0; j < n; j++) { const s = new Set(pay.map(row => row[j][0])); if (s.size < n) return false; }
    for (let i = 0; i < n; i++) { const s = new Set(pay[i].map(c => c[1])); if (s.size < n) return false; } return true; };
  const brText = (pay, rows, cols, rp, cp) =>
    `${rp}'s best responses: ${cols.map((c, j) => `vs ${c}, ${rows[pay.reduce((b, row, i) => row[j][0] > pay[b][j][0] ? i : b, 0)]}`).join("; ")}. ` +
    `${cp}'s best responses: ${rows.map((rw, i) => `vs ${rw}, ${cols[pay[i].reduce((b, c, j) => c[1] > pay[i][b][1] ? j : b, 0)]}`).join("; ")}.`;

  M2.gen({ id: "S19-04-g1", los: ["S19-04", "S19-02"], kind: "calc", make(r) {
    const n = r.chance(0.35) ? 3 : 2, [rp, cp, R0, C0] = r.pick(NAMES), rows = R0.slice(0, n), cols = C0.slice(0, n);
    let pay, ne; do { pay = randGame(r, n); ne = nash(pay); } while (!distinct(pay) || ne.length !== 1);
    const [i, j] = ne[0], cells = []; for (let a = 0; a < n; a++) for (let b = 0; b < n; b++) if (a !== i || b !== j) cells.push([a, b]);
    const pickd = r.shuffle(cells).slice(0, 3), all = r.shuffle([[i, j], ...pickd]);
    const choices = all.map(([a, b]) => `${rp} ${rows[a]}, ${cp} ${cols[b]}`);
    return { type: "mc", choices, answer: all.findIndex(([a, b]) => a === i && b === j), params: { pay, ne: [i, j] },
      stem: `${rp} chooses a row and ${cp} a column. Payoffs: (${rp}, ${cp}).\n\n${mat(rp, cp, rows, cols, pay)}\n\nWhat is the Nash equilibrium?`,
      explain: `${brText(pay, rows, cols, rp, cp)} Only (${rows[i]}, ${cols[j]}) = (${pay[i][j].join(", ")}) has both players best-responding, so neither can gain by changing alone.` };
  } });

  M2.gen({ id: "S19-03-g1", los: ["S19-03", "S19-02"], kind: "calc", make(r) {
    const [rp, cp, R0, C0] = r.pick(NAMES), rows = R0.slice(0, 2), cols = C0.slice(0, 2);
    const target = r.pick(["row", "col", "both", "none"]);
    let pay, dr, dc, ok;
    do { pay = randGame(r, 2); dr = domRow(pay); dc = domCol(pay);
      ok = distinct(pay) && (target === "row" ? dr !== null && dc === null : target === "col" ? dc !== null && dr === null : target === "both" ? dr !== null && dc !== null : dr === null && dc === null); } while (!ok);
    const T = { row: `Only ${rp}`, col: `Only ${cp}`, both: "Both players", none: "Neither player" };
    const choices = [T.row, T.col, T.both, T.none];
    return { type: "mc", choices, answer: ["row", "col", "both", "none"].indexOf(target), params: { pay },
      stem: `${rp} chooses a row and ${cp} a column. Payoffs: (${rp}, ${cp}).\n\n${mat(rp, cp, rows, cols, pay)}\n\nWho has a dominant strategy?`,
      explain: `${brText(pay, rows, cols, rp, cp)} ${dr !== null ? `${rp}'s best response never changes, so ${rows[dr]} is dominant.` : `${rp}'s best response changes, so it has no dominant strategy.`} ${dc !== null ? `${cp}'s best response never changes, so ${cols[dc]} is dominant.` : `${cp}'s best response changes, so it has no dominant strategy.`}` };
  } });

  M2.gen({ id: "S19-05-g1", los: ["S19-05"], kind: "calc", make(r) {
    let pay, p, q;
    const nice = x => x > 0 && x < 1 && Math.abs(x * 20 - Math.round(x * 20)) < 1e-9;
    do {
      const r11 = r.int(2, 12), r21 = r.int(0, r11 - 1), r12 = r.int(0, 10), r22 = r.int(r12 + 1, 12);
      const c11 = r.int(0, 10), c12 = r.int(c11 + 1, 12), c22 = r.int(0, 10), c21 = r.int(c22 + 1, 12);
      pay = [[[r11, c11], [r12, c12]], [[r21, c21], [r22, c22]]];
      p = (c22 - c21) / ((c11 - c21) - (c12 - c22)); q = (r22 - r12) / ((r11 - r12) - (r21 - r22));
    } while (!nice(p) || !nice(q));
    const ask = r.pick(["p", "q", "val"]);
    const rows = ["Monitor", "Don't Monitor"], cols = ["Work", "Shirk"];
    const [[[r11, c11], [r12, c12]], [[r21, c21], [r22, c22]]] = pay;
    const vRow = q * r11 + (1 - q) * r12;
    const ans = ask === "p" ? p : ask === "q" ? q : vRow;
    const ex = ask === "p" ? `The boss's p must make the EMPLOYEE indifferent. Work: ${c11}p + ${c21}(1 - p). Shirk: ${c12}p + ${c22}(1 - p). Set equal and solve: p = ${fmt(p)}.` :
      ask === "q" ? `The employee's q must make the BOSS indifferent. Monitor: ${r11}q + ${r12}(1 - q). Don't: ${r21}q + ${r22}(1 - q). Set equal and solve: q = ${fmt(q)}.` :
      `First find q (makes the boss indifferent): ${r11}q + ${r12}(1 - q) = ${r21}q + ${r22}(1 - q) gives q = ${fmt(q)}. Boss's expected payoff from Monitor = ${r11}(${fmt(q)}) + ${r12}(${fmt(1 - q)}) = ${fmt(vRow)}; Don't Monitor gives the same.`;
    return { type: "num", answer: ans, unit: ask === "val" ? "" : "probability", params: { pay, ask },
      stem: `Boss (rows) and Employee (columns). Payoffs: (Boss, Employee).\n\n${mat("Boss", "Employee", rows, cols, pay)}\n\nThere is no pure-strategy Nash equilibrium. ${ask === "p" ? "With what probability should the boss monitor?" : ask === "q" ? "With what probability should the employee work?" : "What is the boss's expected payoff in the mixed strategy equilibrium?"}`,
      explain: ex + " Mixed strategy formulas are not on the equation sheet." };
  } });

  M2.gen({ id: "S19-06-g1", los: ["S19-06", "S19-04"], kind: "calc", make(r) {
    const both = r.int(0, 4), coop = both + r.int(3, 10), sucker = both - r.int(1, 5), temp = coop + r.int(2, 15);
    const [rp, cp, rows] = r.pick([["Coke", "Pepsi", ["Cut price", "Keep price"]], ["Kellogg's", "General Mills", ["Advertise", "Don't"]], ["Visa", "Mastercard", ["Lower fee", "Maintain fee"]]]);
    const pay = [[[both, both], [temp, sucker]], [[sucker, temp], [coop, coop]]];
    const ask = r.pick(["loss", "gain"]);
    const ans = ask === "loss" ? 2 * (coop - both) : temp - coop;
    return { type: "num", answer: ans, unit: "", params: { both, coop, sucker, temp, ask },
      stem: `${rp} chooses a row and ${cp} a column. Payoffs: (${rp}, ${cp}).\n\n${mat(rp, cp, rows, rows, pay)}\n\n${ask === "loss" ? "How much combined payoff do the two firms give up by playing the Nash equilibrium instead of both choosing the second strategy?" : `If ${cp} plays the second strategy as agreed, how much does ${rp} gain by defecting to the first?`}`,
      explain: `${rows[0]} is dominant for each (${both} > ${sucker} and ${temp} > ${coop}), so the Nash equilibrium is (${rows[0]}, ${rows[0]}) = (${both}, ${both}). ${ask === "loss" ? `Cooperating pays ${coop} + ${coop} = ${2 * coop}; equilibrium pays ${2 * both}. Lost: ${ans}.` : `Keeping the agreement pays ${coop}; defecting pays ${temp}. Gain: ${ans}. That temptation is why a one-shot agreement fails.`} This is a prisoner's dilemma.` };
  } });
})();
