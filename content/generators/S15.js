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
