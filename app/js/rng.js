// Seeded RNG and the generator registry. Works in the browser and in node (globalThis.M2).
(function (M2) {
  M2.rng = function (seed) {
    let a = (seed >>> 0) || 1;
    const next = () => {                       // mulberry32
      a = (a + 0x6D2B79F5) >>> 0;
      let t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
    const r = {
      next,
      int(lo, hi) { return lo + Math.floor(next() * (hi - lo + 1)); },
      num(lo, hi, step) {
        step = step || 1;
        const n = Math.round((hi - lo) / step);
        return +(lo + step * r.int(0, n)).toFixed(10);
      },
      pick(list) { return list[Math.floor(next() * list.length)]; },
      shuffle(list) {
        const x = list.slice();
        for (let i = x.length - 1; i > 0; i--) { const j = Math.floor(next() * (i + 1)); [x[i], x[j]] = [x[j], x[i]]; }
        return x;
      },
      chance(p) { return next() < p; }
    };
    return r;
  };

  M2.generators = M2.generators || {};
  // M2.gen({id, los, kind, make(r)}) registers a parametric generator.
  M2.gen = function (g) { M2.generators[g.id] = g; };

  // Build a full question object from a generator and seed. Same seed gives the same question.
  M2.makeGen = function (genId, seed) {
    const g = M2.generators[genId];
    if (!g) return null;
    const q = g.make(M2.rng(seed));
    return Object.assign({ type: "num", tol: 0.01, unit: "", diff: 2 }, q, {
      id: genId + "#" + seed, genId, seed, los: g.los, kind: g.kind || "calc",
      source: "generated", verbatim: false
    });
  };

  // Round helper generators use for clean money and quantities.
  M2.round = (x, d) => { const f = Math.pow(10, d == null ? 2 : d); return Math.round(x * f) / f; };
  M2.fmt = (x, d) => {
    if (typeof x !== "number" || !isFinite(x)) return String(x);
    const v = M2.round(x, d == null ? 2 : d);
    return v.toLocaleString("en-US", { maximumFractionDigits: d == null ? 2 : d });
  };
})(globalThis.M2 = globalThis.M2 || {});
