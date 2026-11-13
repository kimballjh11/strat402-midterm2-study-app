// S16 Production II generators: isoquants, MRTS, isocosts, cost minimization. Same seed, same question.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 3 : d);
  const SQ = [4, 9, 16, 25, 36, 49, 64, 81, 100];

  M2.gen({ id: "S16-01-g1", los: ["S16-01"], kind: "calc", make(r) {
    const A = r.pick([1, 2, 4, 5, 10]), K = r.pick(SQ), L = r.pick(SQ.filter(x => x !== K));
    const Q = A * Math.sqrt(K) * Math.sqrt(L);
    const c = (Q / A) ** 2;
    return { type: "num", unit: "units of capital", answer: K, params: { A, a: 0.5, b: 0.5, Q, L },
      stem: `A firm's production function is \\(Q = ${A === 1 ? "" : A}K^{0.5}L^{0.5}\\). Its target is Q = ${Q}. How much capital does it need if it uses L = ${L}?`,
      explain: `Set the function equal to the target and solve for K. \\(${Q} = ${A === 1 ? "" : A}\\sqrt{K}\\sqrt{${L}}\\)${A === 1 ? "" : `, so \\(\\sqrt{K}\\sqrt{${L}} = ${Q / A}\\)`}. \\(\\sqrt{${L}} = ${Math.sqrt(L)}\\), so \\(\\sqrt{K} = ${Math.sqrt(K)}\\) and K = ${K}. The general isoquant is \\(K = ${fmt(c)}/L\\).` };
  } });

  M2.gen({ id: "S16-02-g1", los: ["S16-02"], kind: "calc", make(r) {
    const [a, b] = r.pick([[0.5, 0.5], [0.25, 0.75], [0.75, 0.25], [0.4, 0.6], [0.3, 0.7], [0.6, 0.4]]);
    const A = r.pick([1, 2, 3, 5, 10]), K = r.int(2, 60), L = r.int(2, 60);
    const m = (b * K) / (a * L);
    return { type: "num", unit: "", answer: m, params: { A, a, b, K, L },
      stem: `A firm's production function is \\(Q = ${A === 1 ? "" : A}K^{${a}}L^{${b}}\\). What is the MRTS at K = ${K} and L = ${L}? Round to 3 decimals.`,
      explain: `\\(MRTS = MP_L/MP_K\\). For Cobb-Douglas this simplifies to \\(\\frac{bK}{aL}\\); the constant ${A} cancels. \\(\\frac{${b}(${K})}{${a}(${L})} = \\frac{${fmt(b * K)}}{${fmt(a * L)}} = ${fmt(m)}\\). Do not flip it: \\(\\frac{aL}{bK}\\) would give ${fmt(1 / m)}.` };
  } });

  M2.gen({ id: "S16-03-g1", los: ["S16-03", "S16-01"], kind: "calc", make(r) {
    const Q = r.pick([12, 24, 60]), c = Q * Q;
    const Ls = []; for (let L = 2; L <= 12; L++) if (c % L === 0 && c % (L - 1) === 0) Ls.push(L);
    const L = r.pick(Ls), extra = c / (L - 1) - c / L;

    return { type: "num", unit: "units of capital", answer: extra, params: { Q, L },
      stem: `A firm's production function is \\(Q = K^{0.5}L^{0.5}\\) and it must keep producing Q = ${Q}. It cuts labor from L = ${L} to L = ${L - 1}. How many additional units of capital does it need?`,
      explain: `Isoquant: \\(K = ${Q}^2/L = ${c}/L\\). At L = ${L}, K = ${fmt(c / L)}. At L = ${L - 1}, K = ${fmt(c / (L - 1))}. Extra capital = ${fmt(c / (L - 1))} - ${fmt(c / L)} = ${fmt(extra)}. The fewer workers the firm has, the more capital it takes to replace each one: that is the law of diminishing MRTS.` };
  } });

  M2.gen({ id: "S16-04-g1", los: ["S16-04"], kind: "calc", make(r) {
    const w = r.pick([8, 10, 12, 15, 20, 25, 30, 40]), rr = r.pick([5, 10, 20, 25, 40, 50]);
    const C = w * rr * r.int(2, 10);
    const ask = r.pick(["maxL", "maxK", "slope", "cost"]);
    if (ask === "cost") {
      const L = r.int(2, 40), K = r.int(2, 40), cost = w * L + rr * K;
      return { type: "num", unit: "$", answer: cost, params: { w, r: rr, L, K, ask },
        stem: `Labor costs $${w} per hour and capital rents for $${rr} per hour. What is the total cost of using ${L} labor hours and ${K} machine hours?`,
        explain: `C = wL + rK = ${w}(${L}) + ${rr}(${K}) = ${w * L} + ${rr * K} = $${cost}. The isocost equation C = wL + rK is not on the equation sheet.` };
    }
    const ans = ask === "maxL" ? C / w : ask === "maxK" ? C / rr : -w / rr;
    const q = ask === "maxL" ? "What is the most labor it can hire if it uses no capital?" : ask === "maxK" ? "What is the most capital it can rent if it hires no labor?" : "With capital on the vertical axis, what is the slope of its isocost line? Round to 3 decimals.";
    const ex = ask === "maxL" ? `Horizontal intercept = C/w = ${C}/${w} = ${fmt(ans)}. C/r (${fmt(C / rr)}) is the capital intercept.` :
      ask === "maxK" ? `Vertical intercept = C/r = ${C}/${rr} = ${fmt(ans)}. C/w (${fmt(C / w)}) is the labor intercept.` :
      `Slope = -w/r = -${w}/${rr} = ${fmt(ans)}. It is negative, and the wage is on top because labor is on the horizontal axis. The budget does not affect the slope.`;
    return { type: "num", unit: ask === "maxL" ? "labor hours" : ask === "maxK" ? "machine hours" : "", answer: ans, params: { w, r: rr, C, ask },
      stem: `A firm has a budget of $${C.toLocaleString("en-US")}. Labor costs $${w} per hour and capital rents for $${rr} per hour. ${q}`, explain: ex };
  } });

  const MORE_L = "Use more labor and less capital", MORE_K = "Use more capital and less labor", KEEP = "Keep the same mix; it is cost minimizing";
  M2.gen({ id: "S16-05-g1", los: ["S16-05"], kind: "apply", make(r) {
    const w = r.pick([5, 8, 10, 12, 15, 20, 25, 30]), rr = r.pick([5, 10, 15, 20, 25, 40, 50]);
    const x = r.int(1, 9), y = r.chance(0.3) ? x : r.pick([1, 2, 3, 4, 5, 6, 7, 8, 9].filter(v => v !== x));
    const MPL = x * w, MPK = y * rr;
    const right = x > y ? MORE_L : x < y ? MORE_K : KEEP;
    const choices = r.shuffle([MORE_L, MORE_K]).concat([KEEP]);
    const big = MPL > MPK ? "labor" : "capital";
    return { type: "mc", choices, answer: choices.indexOf(right), params: { w, r: rr, MPL, MPK },
      stem: `A firm pays w = $${w} and r = $${rr}. At its current mix, MP_L = ${MPL} and MP_K = ${MPK}. What should it do to lower the cost of producing the same output?`,
      explain: `Compare bang for the buck. MP_L/w = ${MPL}/${w} = ${x}. MP_K/r = ${MPK}/${rr} = ${y}. ${x === y ? "They are equal, so the mix is already cost minimizing." : `${x > y ? "Labor" : "Capital"} gives more output per dollar, so shift spending toward ${x > y ? "labor" : "capital"}.`}${MPL !== MPK && ((MPL > MPK) !== (x > y) || x === y) ? ` Raw marginal products point to ${big}, which is the trap: compare per dollar.` : ""} The rule MP_L/w = MP_K/r is not on the equation sheet.` };
  } });

  M2.gen({ id: "S16-06-g1", los: ["S16-06", "S16-05"], kind: "calc", make(r) {
    const s = r.pick([1, 2, 3, 0.5, 1 / 3]);           // s = sqrt(w/r) = sqrt(K/L) at the optimum
    const A = r.pick([1, 2, 5, 10]);
    let L, K, w, rr;
    if (s >= 1) { L = r.int(2, 20); K = s * s * L; rr = r.pick([2, 4, 5, 10, 20]); w = rr * s * s; }
    else { K = r.int(2, 20); L = K / (s * s); w = r.pick([2, 4, 5, 10, 20]); rr = w / (s * s); }
    const Q = Math.round(A * Math.sqrt(K * L)), C = w * L + rr * K;
    const ask = r.pick(["L", "K", "C"]);
    const ans = ask === "L" ? L : ask === "K" ? K : C;
    const ratio = w / rr, kTxt = s >= 1 ? `${s * s}L` : `L/${Math.round(1 / (s * s))}`;
    return { type: "num", unit: ask === "C" ? "$" : ask === "L" ? "units of labor" : "units of capital", answer: ans, params: { A, a: 0.5, b: 0.5, Q, w, r: rr, ask },
      stem: `A firm's production function is \\(Q = ${A === 1 ? "" : A}K^{0.5}L^{0.5}\\). It must produce ${Q} units. The wage is $${w} and the rental rate is $${rr}. What is the cost-minimizing ${ask === "L" ? "amount of labor" : ask === "K" ? "amount of capital" : "total cost"}?`,
      explain: `Step 1, tangency: MRTS = K/L must equal w/r = ${w}/${rr} = ${fmt(ratio)}, so K = ${kTxt}. Step 2, plug into the isoquant: \\(${Q} = ${A === 1 ? "" : A}\\sqrt{(${kTxt}) \\cdot L} = ${s >= 1 ? fmt(A * s) + "L" : (A === 1 ? "" : A) + "L/" + Math.round(1 / s)}\\), so L = ${fmt(L)} and K = ${fmt(K)}. Step 3, cost: C = ${w}(${fmt(L)}) + ${rr}(${fmt(K)}) = $${fmt(C)}. Check: MP_L/w = MP_K/r at this point.` };
  } });

  M2.gen({ id: "S16-06-g2", los: ["S16-06", "S15-07"], kind: "calc", make(r) {
    let a, b, w, rr;
    do { a = r.int(1, 8); b = r.int(1, 8); w = r.pick([5, 10, 15, 20, 25]); rr = r.pick([5, 10, 15, 20, 30, 40]); } while (Math.abs(b / w - a / rr) < 1e-9);
    const Q = a * b * r.int(2, 10);
    const costL = (Q / b) * w, costK = (Q / a) * rr, C = Math.min(costL, costK), useL = costL < costK;
    return { type: "num", unit: "$", answer: C, params: { a, b, Q, w, r: rr },
      stem: `A firm's production function is \\(Q = ${a}K + ${b}L\\). The wage is $${w} and the rental rate is $${rr}. What is the lowest cost of producing ${Q} units?`,
      explain: `Inputs are perfect substitutes, so use only the better deal. MP_L/w = ${b}/${w} = ${fmt(b / w)} and MP_K/r = ${a}/${rr} = ${fmt(a / rr)}. ${useL ? `Labor wins: L = ${Q}/${b} = ${Q / b}, cost = ${Q / b} × $${w} = $${costL}.` : `Capital wins: K = ${Q}/${a} = ${Q / a}, cost = ${Q / a} × $${rr} = $${costK}.`} Using only the other input would cost $${useL ? costK : costL}.` };
  } });

  M2.gen({ id: "S16-06-g3", los: ["S16-06", "S15-08"], kind: "calc", make(r) {
    const a = r.int(1, 6), b = r.int(1, 6), w = r.pick([5, 10, 15, 20, 25]), rr = r.pick([5, 10, 20, 30, 50]);
    const Q = a * b * r.int(2, 8), L = Q / b, K = Q / a, C = w * L + rr * K;
    return { type: "num", unit: "$", answer: C, params: { a, b, Q, w, r: rr },
      stem: `A firm's production function is \\(Q = \\min(${a}K, ${b}L)\\). The wage is $${w} and the rental rate is $${rr}. What is the lowest cost of producing ${Q} units?`,
      explain: `Fixed proportions: set both parts equal to ${Q}. K = ${Q}/${a} = ${K} and L = ${Q}/${b} = ${L}. Any extra of either input adds nothing. C = ${w}(${L}) + ${rr}(${K}) = $${C}. Prices change the cost, not the mix.` };
  } });
})();
