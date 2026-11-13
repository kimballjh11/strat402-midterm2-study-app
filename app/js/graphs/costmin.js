// Cost minimization: Cobb-Douglas isoquant plus isocost lines. Tangency where MP_L/w = MP_K/r.
// params: {A, a (exponent on K), b (exponent on L), Q, w, r, L (a trial point)}
(function (M2) {
  const G = M2.G, C = G.C;
  M2.graphs.costmin = function (holder, params) {
    const pr = Object.assign({ A: 2, a: 0.5, b: 0.5, Q: 100, w: 10, r: 25, L: 30 }, params);
    const v = G.controls(holder, [
      { key: "w", label: "Wage w", min: 1, max: 100, step: 0.5, value: pr.w },
      { key: "r", label: "Rental r", min: 1, max: 100, step: 0.5, value: pr.r },
      { key: "Q", label: "Target Q", min: 10, max: 400, step: 5, value: pr.Q },
      { key: "L", label: "Trial L", min: 1, max: 300, step: 1, value: pr.L }], draw);
    const P = G.plot(holder, { h: 380, xlabel: "Labor L", ylabel: "Capital K", title: "Isoquant and isocost lines" });
    const out = G.readout(holder);
    const { A, a, b } = pr;
    const Kof = (L, Q) => Math.pow(Q / (A * Math.pow(L, b)), 1 / a);

    function draw() {
      // Tangency: MP_L/MP_K = (b K)/(a L) = w/r  =>  K = (a w)/(b r) L
      const k = (a * v.w) / (b * v.r);
      const Ls = Math.pow(v.Q / (A * Math.pow(k, a)), 1 / (a + b)), Ks = k * Ls, Cs = v.w * Ls + v.r * Ks;
      const lmax = Math.max(Cs / v.w * 1.15, v.L * 1.2), kmax = Cs / v.r * 1.5;
      P.clear(lmax, kmax, 0);
      P.fn(L => Kof(L, v.Q), C.a, 0.01, lmax);
      P.fn(L => (Cs - v.w * L) / v.r, C.c, 0, Cs / v.w);
      const Kt = Kof(v.L, v.Q), Ct = v.w * v.L + v.r * Kt;
      if (isFinite(Kt)) { P.fn(L => (Ct - v.w * L) / v.r, C.d, 0, Ct / v.w, { "stroke-dasharray": "6 4", "stroke-width": 1.6 }); P.dot(v.L, Kt, C.d, "trial"); }
      P.dot(Ls, Ks, C.c, "cost minimum", 8, -10);
      P.legend([["Isoquant Q = " + G.fmt(v.Q), C.a], ["Isocost at minimum", C.c], ["Isocost through trial point", C.d]]);
      const mpl = L => b * A * Math.pow(Kof(L, v.Q), a) * Math.pow(L, b - 1), mpk = L => a * A * Math.pow(Kof(L, v.Q), a - 1) * Math.pow(L, b);
      const rl = mpl(v.L) / v.w, rk = mpk(v.L) / v.r;
      out.innerHTML = `Q = ${A}K^${a}L^${b}. Isocost: ${G.fmt(v.w)}L + ${G.fmt(v.r)}K = C, slope −w/r = <b>${G.fmt(-v.w / v.r, 3)}</b>. ` +
        `Cost minimum: L* = <b>${G.fmt(Ls)}</b>, K* = <b>${G.fmt(Ks)}</b>, C* = <b>$${G.fmt(Cs)}</b>. ` +
        `At the trial point L = ${G.fmt(v.L)}, K = ${G.fmt(Kt)}: cost $${G.fmt(Ct)}, MP_L/w = ${G.fmt(rl, 3)}, MP_K/r = ${G.fmt(rk, 3)}. ` +
        (Math.abs(rl - rk) < 1e-3 * Math.max(rl, rk) ? "Equal: this is the minimum." : rl > rk ? "Labor gives more output per dollar: use more L, less K." : "Capital gives more output per dollar: use more K, less L.");
    }
    draw();
  };
})(globalThis.M2 = globalThis.M2 || {});
