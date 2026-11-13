// Isoquants for linear, Leontief and Cobb-Douglas production, with MRTS at a chosen L.
// params: {form: "linear"|"leontief"|"cd", a, b (coefficients or exponents on K and L), A (CD scale), Q, L}
(function (M2) {
  const G = M2.G, C = G.C;
  M2.graphs.isoquant = function (holder, params) {
    const pr = Object.assign({ form: "cd", a: 0.5, b: 0.5, A: 2, Q: 100, L: 50 }, params);
    const v = G.controls(holder, [
      { key: "form", label: "Function", value: pr.form, options: [["linear", "Linear Q = aK + bL"], ["leontief", "Leontief Q = min(aK, bL)"], ["cd", "Cobb-Douglas Q = A K^a L^b"]] },
      { key: "Q", label: "Output Q", min: 10, max: 400, step: 5, value: pr.Q },
      { key: "a", label: "a (on K)", min: 0.1, max: 5, step: 0.05, value: pr.a },
      { key: "b", label: "b (on L)", min: 0.1, max: 5, step: 0.05, value: pr.b },
      { key: "L", label: "Point at L", min: 1, max: 200, step: 1, value: pr.L }], draw);
    const P = G.plot(holder, { h: 360, xlabel: "Labor L", ylabel: "Capital K", title: "Isoquants" });
    const out = G.readout(holder);
    const A = pr.A;

    function Kof(L, Q) {
      if (v.form === "linear") return (Q - v.b * L) / v.a;
      if (v.form === "leontief") return v.b * L >= Q ? Q / v.a : Infinity;
      return Math.pow(Q / (A * Math.pow(L, v.b)), 1 / v.a);
    }
    function draw() {
      let lmax, kmax;
      if (v.form === "linear") { lmax = 2 * v.Q / v.b; kmax = 2 * v.Q / v.a; }
      else if (v.form === "leontief") { lmax = 3 * v.Q / v.b; kmax = 3 * v.Q / v.a; }
      else { lmax = Math.max(200, v.L * 1.5); kmax = Math.min(Kof(lmax * 0.12, v.Q), Kof(v.L, v.Q) * 4); }
      P.clear(lmax, kmax, 0);
      const levels = [[v.Q, C.a], [1.5 * v.Q, C.f], [2 * v.Q, C.e]];
      for (const [q, col] of levels) {
        if (v.form === "leontief") {
          const L0 = q / v.b, K0 = q / v.a;
          P.poly([[L0, kmax], [L0, K0], [lmax, K0]], col, { opacity: q === v.Q ? 1 : 0.5 });
          if (q === v.Q) P.dot(L0, K0, col, "corner");
        } else P.fn(L => Kof(L, q), col, 0.01, lmax, { opacity: q === v.Q ? 1 : 0.5 });
      }
      P.legend([["Q = " + G.fmt(v.Q), C.a], ["Q = " + G.fmt(1.5 * v.Q), C.f], ["Q = " + G.fmt(2 * v.Q), C.e]]);
      const L = v.L, K = Kof(L, v.Q);
      let mrts, note;
      if (v.form === "linear") { mrts = v.b / v.a; note = "MRTS = MP_L / MP_K = b / a, constant: the inputs are perfect substitutes."; }
      else if (v.form === "leontief") { mrts = null; note = "No substitution: inputs are used in fixed proportions. MRTS is undefined at the corner (0 on the flat part, infinite on the vertical part)."; }
      else { mrts = (v.b * K) / (v.a * L); note = "MRTS = MP_L / MP_K = (b K) / (a L). It falls as L rises: diminishing MRTS."; }
      if (isFinite(K) && K >= 0 && v.form !== "leontief") {
        P.dot(L, K, C.b, `(${G.fmt(L)}, ${G.fmt(K)})`);
        if (mrts != null) P.fn(x => K - mrts * (x - L), C.b, Math.max(0, L - lmax * 0.2), Math.min(lmax, L + lmax * 0.2), { "stroke-dasharray": "5 4", "stroke-width": 1.5 });
      }
      out.innerHTML = (isFinite(K) && K >= 0 ? `At L = ${G.fmt(L)}, staying on Q = ${G.fmt(v.Q)} needs K = <b>${G.fmt(K)}</b>. ` : `L = ${G.fmt(L)} cannot reach Q = ${G.fmt(v.Q)} on this isoquant. `) +
        (mrts != null ? `MRTS = <b>${G.fmt(mrts, 3)}</b>. ` : "") + note;
    }
    draw();
  };
})(globalThis.M2 = globalThis.M2 || {});
