/* built by scripts/build_data.js from content/generators */

/* ---- S15.js ---- */
// S15 Production I generators. Each make(r) returns a fresh question; same seed, same question.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 3 : d);
  // cubic short-run production Q = -cL^3 + bL^2 + aL with integer output
  function cubic(r) {
    const c = 1, b = r.int(6, 10), a = r.int(1, 8);
    const Q = L => -c * L * L * L + b * L * L + a * L;
    const Ls = [], Qs = [];
    for (let L = 0; L <= 8; L++) { if (L > 0 && Q(L) <= 0) break; Ls.push(L); Qs.push(Q(L)); }
    return { a, b, c, Q, Ls, Qs };
  }
  const tableMd = (Ls, Qs, unit) => "| Labor (L) | Output (Q) |\n|---|---|\n" + Ls.map((l, i) => `| ${l} | ${Qs[i]} |`).join("\n");
  const mpList = Qs => Qs.map((q, i) => i ? q - Qs[i - 1] : null);

  M2.gen({ id: "S15-02-g1", los: ["S15-02", "S15-01"], kind: "calc", make(r) {
    const m = cubic(r), L = r.int(2, Math.min(6, m.Ls.length - 1));
    const q = m.Q(L);
    return { type: "num", unit: "units", answer: q, params: { a: m.a, b: m.b, c: m.c, L },
      stem: `With capital fixed, a firm's production function is \\(Q = -L^3 + ${m.b}L^2 + ${m.a}L\\). What is total product with ${L} workers?`,
      explain: `Plug in L = ${L}: \\(-(${L})^3 + ${m.b}(${L})^2 + ${m.a}(${L}) = ${-(L ** 3)} + ${m.b * L * L} + ${m.a * L} = ${q}\\). Total product is the output itself, not output per worker.` };
  } });

  M2.gen({ id: "S15-04-g1", los: ["S15-04"], kind: "calc", make(r) {
    const m = cubic(r), n = r.int(2, m.Ls.length - 1), mp = m.Qs[n] - m.Qs[n - 1];
    return { type: "num", unit: "units", answer: mp, params: { a: m.a, b: m.b, c: m.c, n, Ls: m.Ls, Qs: m.Qs },
      stem: `Use the table.\n\n${tableMd(m.Ls, m.Qs)}\n\nWhat is the marginal product of worker number ${n}?`,
      explain: `MP of worker ${n} = Q(${n}) - Q(${n - 1}) = ${m.Qs[n]} - ${m.Qs[n - 1]} = ${mp}. ${m.Qs[n]} is total product and ${fmt(m.Qs[n] / n, 2)} is average product; neither is the marginal product.` };
  } });

  M2.gen({ id: "S15-03-g1", los: ["S15-03"], kind: "calc", make(r) {
    const m = cubic(r), n = r.int(1, m.Ls.length - 1), ap = m.Qs[n] / n;
    return { type: "num", unit: "units per worker", answer: ap, params: { a: m.a, b: m.b, c: m.c, n, Ls: m.Ls, Qs: m.Qs },
      stem: `Use the table.\n\n${tableMd(m.Ls, m.Qs)}\n\nWhat is the average product of labor with ${n} workers? Round to 2 decimals if needed.`,
      explain: `AP = Q / L = ${m.Qs[n]} / ${n} = ${fmt(ap, 2)}. Do not use the change from the previous row; that is marginal product (${n ? m.Qs[n] - m.Qs[n - 1] : "n/a"}).` };
  } });

  M2.gen({ id: "S15-05-g1", los: ["S15-05", "S15-04"], kind: "calc", make(r) {
    const m = cubic(r), mp = mpList(m.Qs);
    let first = null;
    for (let i = 2; i < mp.length; i++) if (mp[i] < mp[i - 1]) { first = i; break; }
    return { type: "num", unit: "th worker", answer: first, params: { a: m.a, b: m.b, c: m.c, Ls: m.Ls, Qs: m.Qs },
      stem: `Use the table.\n\n${tableMd(m.Ls, m.Qs)}\n\nWhich worker is the first to show diminishing marginal returns (a marginal product lower than the worker before)?`,
      explain: `MPs by worker: ${mp.slice(1).map((x, i) => `${i + 1}: ${x}`).join(", ")}. MP rises through worker ${first - 1} and first falls at worker ${first}. Diminishing returns begin when MP starts falling, even though output is still rising.` };
  } });

  M2.gen({ id: "S15-06-g1", los: ["S15-06"], kind: "calc", make(r) {
    const m = cubic(r), n = r.int(1, m.Ls.length - 1), P = r.pick([2, 3, 4, 5, 6, 8, 10, 12]);
    const mp = m.Qs[n] - m.Qs[n - 1];
    return { type: "num", unit: "$", answer: P * mp, params: { a: m.a, b: m.b, c: m.c, n, P, Ls: m.Ls, Qs: m.Qs },
      stem: `Use the table. Output sells for $${P} per unit.\n\n${tableMd(m.Ls, m.Qs)}\n\nWhat is the value marginal product of worker number ${n}?`,
      explain: `MP of worker ${n} = ${m.Qs[n]} - ${m.Qs[n - 1]} = ${mp}. VMP = P × MP = $${P} × ${mp} = $${P * mp}. Multiplying price by total product ($${P * m.Qs[n]}) gives total revenue, not VMP.` };
  } });

  M2.gen({ id: "S15-10-g1", los: ["S15-10", "S15-06"], kind: "calc", make(r) {
    // retry until the VMP = w staffing level is also profitable overall (otherwise hiring nobody would win)
    let m, mp, t, P, w, best, tries = 0;
    do {
      m = cubic(r); mp = mpList(m.Qs);
      const falling = [];
      for (let i = 2; i < mp.length - 1; i++) if (mp[i] < mp[i - 1] && mp[i] > 0 && mp[i + 1] < mp[i]) falling.push(i);
      if (!falling.length) continue;
      t = r.pick(falling); P = r.pick([2, 3, 4, 5, 10]);
      const hi = P * mp[t], lo = P * Math.max(mp[t + 1], 0);
      w = Math.max(1, hi - r.int(0, Math.max(0, hi - lo - 1)));
      best = 0;
      for (let i = 1; i < mp.length; i++) if (P * mp[i] >= w) best = i;
    } while ((!best || P * m.Qs[best] - w * best <= 0) && ++tries < 100);
    const vm = mp.slice(1).map((x, i) => `${i + 1}: $${P * x}`).join(", ");
    return { type: "num", unit: "workers", answer: best, params: { a: m.a, b: m.b, c: m.c, P, w, Ls: m.Ls, Qs: m.Qs },
      stem: `Use the table. Output sells for $${P} and the wage is $${w} per worker.\n\n${tableMd(m.Ls, m.Qs)}\n\nHow many workers maximize profit?`,
      explain: `Hire while VMP = P × MP is at least the wage. VMP by worker: ${vm}. The last worker with VMP ≥ $${w} is worker ${best}; the next one adds less than $${w}. Hire ${best}. Check: revenue $${P * m.Qs[best]} minus wages $${w * best} is positive, so hiring beats shutting down.` };
  } });

  M2.gen({ id: "S15-10-g2", los: ["S15-10", "S15-09"], kind: "calc", make(r) {
    const k = r.pick([2, 3, 4, 5, 6]), A = r.pick([1, 2, 4]), s = r.int(3, 20), j = r.pick([2, 3, 4, 5, 10]);
    const K = k * k, m = A * 0.5 * k;            // MP_L = m / sqrt(L)
    const w = j * r.pick([5, 10, 15, 20]), P = M2.round(w * s / m, 2);
    const L = Math.pow(P * m / w, 2);
    const Atxt = A === 1 ? "" : A;
    return { type: "num", unit: "units of labor", answer: L, params: { A, a: 0.5, b: 0.5, K, P, w },
      stem: `A firm's production function is \\(Q = ${Atxt}K^{0.5}L^{0.5}\\). Capital is fixed at K = ${K}. Output sells for $${M2.fmt(P, 2)} and the wage is $${w}. What is the profit-maximizing amount of labor?`,
      explain: `Step 1: \\(MP_L = ${A === 1 ? "" : A + " \\times "}0.5K^{0.5}L^{-0.5} = ${M2.fmt(m, 3)}/\\sqrt{L}\\) with \\(\\sqrt{${K}} = ${k}\\).\nStep 2: Set \\(VMP_L = w\\): \\(${M2.fmt(P, 2)} \\times ${M2.fmt(m, 3)}/\\sqrt{L} = ${w}\\).\nStep 3: \\(\\sqrt{L} = ${M2.fmt(P, 2)} \\times ${M2.fmt(m, 3)} / ${w} = ${M2.fmt(Math.sqrt(L), 3)}\\).\nStep 4: Square it: \\(L = ${M2.fmt(L, 2)}\\). Stopping at the square root is the common mistake.` };
  } });

  const roots = [1, 16, 81, 256, 625];         // perfect fourth powers keep 0.25 and 0.75 exponents clean
  M2.gen({ id: "S15-09-g1", los: ["S15-09", "S15-04"], kind: "calc", make(r) {
    const a = r.pick([0.25, 0.5, 0.75]), b = r.pick([0.25, 0.5, 0.75]), K = r.pick(roots.slice(1)), L = r.pick(roots.slice(1));
    const wrt = r.pick(["L", "K"]);
    const mp = wrt === "L" ? b * Math.pow(K, a) * Math.pow(L, b - 1) : a * Math.pow(K, a - 1) * Math.pow(L, b);
    const form = wrt === "L" ? `bK^aL^{b-1} = ${b}K^{${a}}L^{${M2.round(b - 1, 2)}}` : `aK^{a-1}L^b = ${a}K^{${M2.round(a - 1, 2)}}L^{${b}}`;
    return { type: "num", unit: "", answer: mp, tol: 0.01, params: { A: 1, a, b, K, L, wrt },
      stem: `\\(Q = K^{${a}}L^{${b}}\\). What is \\(MP_${wrt}\\) at K = ${K} and L = ${L}? Round to 3 decimals.`,
      explain: `Sheet formula: \\(MP_${wrt} = ${form}\\). Fourth roots: \\(${K}^{0.25} = ${Math.round(Math.pow(K, 0.25))}\\), \\(${L}^{0.25} = ${Math.round(Math.pow(L, 0.25))}\\). Plugging in gives \\(MP_${wrt} = ${fmt(mp, 4)}\\). Remember a goes with K and b with L, and a negative exponent means divide.` };
  } });

  M2.gen({ id: "S15-08-g1", los: ["S15-08"], kind: "calc", make(r) {
    const a = r.int(2, 10), b = r.int(2, 10), K = r.int(2, 12), L = r.int(2, 12);
    const ask = r.pick(["Q", "MPL", "MPK"]);
    const q = Math.min(a * K, b * L);
    let ans, stem, ex;
    if (ask === "Q") { ans = q; stem = `What is output with K = ${K} and L = ${L}?`; ex = `Q = min(${a} × ${K}, ${b} × ${L}) = min(${a * K}, ${b * L}) = ${q}.`; }
    else if (ask === "MPL") { const q2 = Math.min(a * K, b * (L + 1)); ans = q2 - q; stem = `With K = ${K} and L = ${L}, by how much does output change if the firm adds one more worker?`;
      ex = `Before: min(${a * K}, ${b * L}) = ${q}. After: min(${a * K}, ${b * (L + 1)}) = ${q2}. Change = ${ans}. ${ans === 0 ? "Capital binds, so extra labor adds nothing." : "Labor binds, so the extra worker adds output (up to the point where capital starts to bind)."}`; }
    else { const q2 = Math.min(a * (K + 1), b * L); ans = q2 - q; stem = `With K = ${K} and L = ${L}, by how much does output change if the firm adds one more unit of capital?`;
      ex = `Before: min(${a * K}, ${b * L}) = ${q}. After: min(${a * (K + 1)}, ${b * L}) = ${q2}. Change = ${ans}. ${ans === 0 ? "Labor binds, so extra capital adds nothing." : "Capital binds, so the extra unit adds output (up to the point where labor starts to bind)."}`; }
    return { type: "num", unit: "units", answer: ans, params: { a, b, K, L, ask }, stem: `A firm's production function is \\(Q = \\min(${a}K, ${b}L)\\). ${stem}`, explain: ex + " Leontief output is the smaller of aK and bL." };
  } });

  M2.gen({ id: "S15-07-g1", los: ["S15-07"], kind: "calc", make(r) {
    const a = r.int(1, 12), b = r.int(1, 12), K = r.int(1, 30), L = r.int(1, 30);
    const ask = r.pick(["Q", "MPL", "MPK"]);
    const ans = ask === "Q" ? a * K + b * L : ask === "MPL" ? b : a;
    const stem = ask === "Q" ? `What is output with K = ${K} and L = ${L}?` : `What is the marginal product of ${ask === "MPL" ? "labor" : "capital"} at K = ${K} and L = ${L}?`;
    const ex = ask === "Q" ? `Q = ${a}(${K}) + ${b}(${L}) = ${a * K} + ${b * L} = ${ans}.` : `For a linear function the marginal product is the coefficient: MP_${ask === "MPL" ? "L" : "K"} = ${ans}, at every K and L. The values of K and L do not matter.`;
    return { type: "num", unit: "units", answer: ans, params: { a, b, K, L, ask }, stem: `A firm's production function is \\(Q = ${a}K + ${b}L\\). ${stem}`, explain: ex };
  } });
})();


/* ---- S16.js ---- */
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


/* ---- S18.js ---- */
// S18 Barriers to Entry generators: average cost and scale, learning curves, per-user results, limit pricing. Same seed, same question.
(function () {
  const fmt = (x, d) => M2.fmt(x, d == null ? 2 : d);
  const money = x => (x < 0 ? "-$" : "$") + fmt(Math.abs(x));

  M2.gen({ id: "S18-01-g1", los: ["S18-01", "S18-09"], kind: "calc", make(r) {
    const F = r.pick([1000, 2000, 5000, 10000, 20000, 50000]), c = r.pick([1, 2, 3, 4, 5, 8, 10]);
    const Qs = r.pick([10, 20, 25, 50]), Qb = Qs * r.pick([4, 5, 10, 20]);
    const ac = Q => F / Q + c, ask = r.pick(["small", "big", "gap"]);
    const ans = ask === "small" ? ac(Qs) : ask === "big" ? ac(Qb) : ac(Qs) - ac(Qb);
    const q = ask === "small" ? `What is the entrant's average cost if it sells ${Qs.toLocaleString("en-US")} units?` :
      ask === "big" ? `What is the incumbent's average cost at ${Qb.toLocaleString("en-US")} units?` :
      `An entrant expects to sell ${Qs.toLocaleString("en-US")} units and the incumbent sells ${Qb.toLocaleString("en-US")}. How much higher is the entrant's average cost per unit?`;
    return { type: "num", unit: "$", answer: ans, params: { F, c, Qs, Qb, ask },
      stem: `Producing in this market takes a fixed cost of $${F.toLocaleString("en-US")} per year plus $${c} per unit. ${q}`,
      explain: `ATC = TC/Q = F/Q + c. At ${Qs.toLocaleString("en-US")} units: ${F}/${Qs} + ${c} = ${money(ac(Qs))}. At ${Qb.toLocaleString("en-US")} units: ${F}/${Qb} + ${c} = ${money(ac(Qb))}.${ask === "gap" ? ` Gap = ${money(ans)}.` : ""} Spreading the fixed cost over more units is economies of scale, and it is why a small entrant is at a disadvantage.` };
  } });

  M2.gen({ id: "S18-02-g1", los: ["S18-02"], kind: "calc", make(r) {
    const rate = r.pick([0.7, 0.75, 0.8, 0.85, 0.9]), C1 = r.pick([100, 200, 400, 500, 800, 1000, 2000]);
    const start = r.pick([1, 1, 10, 50, 100]), k = r.int(1, 5), n = start * 2 ** k;
    const ans = C1 * rate ** k, steps = [];
    for (let i = 0; i <= k; i++) steps.push((start * 2 ** i).toLocaleString("en-US"));
    return { type: "num", unit: "$", answer: ans, params: { C1, rate, k, start },
      stem: `${start === 1 ? "The first unit" : `Unit number ${start}`} of a product cost $${C1}. The firm is on a ${Math.round(rate * 100)}% learning curve. What does unit number ${n.toLocaleString("en-US")} cost?`,
      explain: `Count doublings: ${steps.join(", ")} is ${k} doubling${k > 1 ? "s" : ""}. Each doubling multiplies cost by ${rate}. ${C1} × ${rate}^${k} = ${C1} × ${fmt(rate ** k, 4)} = ${money(ans)}. A ${Math.round(rate * 100)}% curve means cost falls TO ${Math.round(rate * 100)}% per doubling, a ${Math.round((1 - rate) * 100)}% drop.` };
  } });

  M2.gen({ id: "S18-04-g1", los: ["S18-04", "S18-09"], kind: "calc", make(r) {
    const ask = r.pick(["rev", "profit", "conn", "add"]);
    if (ask === "conn" || ask === "add") {
      const n = r.pick([5, 8, 10, 12, 20, 25, 40, 50, 100]);
      const ans = ask === "conn" ? n * (n - 1) : 2 * n;
      return { type: "num", unit: "connections", answer: ans, params: { n, ask },
        stem: ask === "conn" ? `A two-way network has ${n} users. How many potential connections does it have?` : `A two-way network has ${n} users. How many new connections does user number ${n + 1} add?`,
        explain: ask === "conn" ? `n(n - 1) = ${n} × ${n - 1} = ${ans}. Each user can connect to each of the others, counted in both directions.` : `A new user adds 2n = 2 × ${n} = ${ans}. Check: ${n + 1} × ${n} - ${n} × ${n - 1} = ${(n + 1) * n} - ${n * (n - 1)} = ${ans}. Every existing user gains, which is the network effect.` };
    }
    const users = r.pick([200, 250, 300, 400, 500, 800, 1000, 1500, 2000]);
    const revPer = r.pick([2, 3, 4, 5, 6, 8, 10, 12, 15]), costPer = r.pick([3, 4, 5, 6, 7, 9, 10]);
    const rev = revPer * users, cost = costPer * users;
    const ans = ask === "rev" ? revPer : revPer - costPer;
    return { type: "num", unit: "$", answer: ans, params: { users, rev, cost, ask },
      stem: `A social media company has ${users.toLocaleString("en-US")} million daily active users, $${rev.toLocaleString("en-US")} million of advertising revenue and $${cost.toLocaleString("en-US")} million of operating expense this quarter. What is its ${ask === "rev" ? "ad revenue per user" : "profit per user (negative for a loss)"}?`,
      explain: `Ad revenue per user = ${rev.toLocaleString("en-US")} / ${users.toLocaleString("en-US")} = $${revPer}. ${ask === "profit" ? `Operating expense per user = ${cost.toLocaleString("en-US")} / ${users.toLocaleString("en-US")} = $${costPer}. Profit per user = ${revPer} - ${costPer} = ${money(ans)}.` : ""} Millions divided by millions gives dollars per user. In 2022 Q2 Meta earned $14.29 per user, Twitter $4.52 and Snapchat $3.20.` };
  } });

  const TXT = { deter: "Entry is deterred and the incumbent still earns a profit: limit pricing", noDeter: "Entry is not deterred: the price is above the entrant's average cost", loss: "Entry is deterred, but the price is below the incumbent's own cost", mono: "This is the monopoly price; it does not limit entry" };
  M2.gen({ id: "S18-05-g1", los: ["S18-05", "S18-06"], kind: "apply", make(r) {
    const own = r.pick([10, 15, 20, 25]), ent = own + r.pick([8, 10, 12, 15, 20]), PM = ent + r.pick([10, 15, 20, 30]);
    const which = r.pick(["deter", "noDeter", "loss", "deter"]);
    const P = which === "deter" ? r.int(own + 1, ent - 1) : which === "noDeter" ? r.int(ent + 1, PM - 1) : r.int(Math.max(1, own - 8), own - 1);
    const choices = r.shuffle([TXT.deter, TXT.noDeter, TXT.loss]).concat([TXT.mono]);
    return { type: "mc", choices, answer: choices.indexOf(TXT[which]), params: { own, ent, PM, P },
      stem: `An incumbent's monopoly price is $${PM} and its average cost is $${own}. A potential entrant's lowest possible average cost is $${ent}. The incumbent sets a price of $${P}. What happens?`,
      explain: `Compare the price with both costs. $${P} ${P < ent ? "<" : ">"} entrant's $${ent}, so entry ${P < ent ? "is" : "is not"} unprofitable. $${P} ${P > own ? ">" : "<"} incumbent's $${own}, so the incumbent ${P > own ? "still earns a profit" : "loses money on each unit"}. ${which === "deter" ? "Below the monopoly price, above own cost, aimed at a potential entrant: limit pricing." : which === "loss" ? "Pricing below its own cost costs the incumbent money; a below-cost price aimed at an existing rival would be predatory pricing." : "To deter entry the price has to fall below the entrant's average cost."}` };
  } });
})();


/* ---- S19.js ---- */
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


/* ---- S20.js ---- */
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


/* ---- S21.js ---- */
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


/* ---- S22.js ---- */
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

