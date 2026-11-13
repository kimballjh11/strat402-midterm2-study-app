// Shared SVG plotting and slider helpers for the graph components. Vanilla SVG, redrawn on every input.
(function (M2) {
  const NS = "http://www.w3.org/2000/svg";
  const G = M2.G = {};
  G.C = { a: "#6ea8fe", b: "#e5c07b", c: "#5fb878", d: "#e06c75", e: "#c678dd", f: "#56b6c2", muted: "#8b93a1", line: "#3a4150", text: "#d7dae0" };
  M2.graphs = M2.graphs || {};

  const el = (tag, attrs) => { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); return e; };
  G.fmt = (x, d) => (x == null || !isFinite(x)) ? "n/a" : (+x.toFixed(d == null ? 2 : d)).toLocaleString("en-US");

  // A plot area. o: {w, h, xmin, xmax, ymin, ymax, xlabel, ylabel, title}
  G.plot = function (holder, o) {
    o = Object.assign({ w: 640, h: 320, xmin: 0, ymin: 0, pad: { l: 56, r: 16, t: 22, b: 40 } }, o);
    const svg = el("svg", { viewBox: `0 0 ${o.w} ${o.h}`, role: "img" });
    holder.append(svg);
    const P = { svg, o };
    const pw = () => o.w - o.pad.l - o.pad.r, ph = () => o.h - o.pad.t - o.pad.b;
    P.X = x => o.pad.l + (x - o.xmin) / (o.xmax - o.xmin) * pw();
    P.Y = y => o.pad.t + ph() - (y - o.ymin) / (o.ymax - o.ymin) * ph();
    P.add = (tag, attrs) => { const e = el(tag, attrs); svg.append(e); return e; };
    P.text = (x, y, s, attrs) => { const t = P.add("text", Object.assign({ x, y, fill: G.C.text, "font-size": 13 }, attrs || {})); t.textContent = s; return t; };
    P.clear = function (xmax, ymax, ymin) {
      if (xmax != null) o.xmax = xmax; if (ymax != null) o.ymax = ymax; if (ymin != null) o.ymin = ymin;
      svg.innerHTML = "";
      const ticks = (lo, hi) => { const span = hi - lo, raw = span / 5, mag = Math.pow(10, Math.floor(Math.log10(raw))); const st = [1, 2, 2.5, 5, 10].map(m => m * mag).find(s => s >= raw); const out = []; for (let v = Math.ceil(lo / st) * st; v <= hi + 1e-9; v += st) out.push(+v.toFixed(10)); return out; };
      for (const t of ticks(o.xmin, o.xmax)) { P.add("line", { x1: P.X(t), x2: P.X(t), y1: P.Y(o.ymin), y2: P.Y(o.ymin) + 4, stroke: G.C.muted }); P.text(P.X(t), P.Y(o.ymin) + 17, G.fmt(t), { "text-anchor": "middle", fill: G.C.muted, "font-size": 11 }); }
      for (const t of ticks(o.ymin, o.ymax)) { P.add("line", { x1: P.X(o.xmin) - 4, x2: P.X(o.xmax), y1: P.Y(t), y2: P.Y(t), stroke: t === 0 ? G.C.muted : "#20252e" }); P.text(P.X(o.xmin) - 7, P.Y(t) + 4, G.fmt(t), { "text-anchor": "end", fill: G.C.muted, "font-size": 11 }); }
      P.add("line", { x1: P.X(o.xmin), x2: P.X(o.xmin), y1: P.Y(o.ymin), y2: P.Y(o.ymax), stroke: G.C.muted });
      P.add("line", { x1: P.X(o.xmin), x2: P.X(o.xmax), y1: P.Y(Math.max(o.ymin, 0)), y2: P.Y(Math.max(o.ymin, 0)), stroke: G.C.muted });
      if (o.xlabel) P.text(o.w - o.pad.r, o.h - 6, o.xlabel, { "text-anchor": "end", fill: G.C.muted });
      if (o.ylabel) P.text(o.pad.l - 50, o.pad.t - 8, o.ylabel, { fill: G.C.muted });
      if (o.title) P.text(o.w / 2, 14, o.title, { "text-anchor": "middle", "font-weight": 600 });
    };
    // Function curve f(x) over [x0, x1]; points outside the y range are clipped.
    P.fn = function (f, color, x0, x1, attrs) {
      x0 = x0 == null ? o.xmin : x0; x1 = x1 == null ? o.xmax : x1;
      let d = "", pen = false;
      for (let i = 0; i <= 240; i++) {
        const x = x0 + (x1 - x0) * i / 240, y = f(x);
        if (!isFinite(y) || y > o.ymax * 1.5 + 1 || y < o.ymin - (o.ymax - o.ymin) * 0.5) { pen = false; continue; }
        const yy = Math.min(Math.max(y, o.ymin - (o.ymax - o.ymin) * 0.02), o.ymax);
        d += (pen ? "L" : "M") + P.X(x).toFixed(1) + " " + P.Y(yy).toFixed(1); pen = true;
      }
      return P.add("path", Object.assign({ d, fill: "none", stroke: color, "stroke-width": 2.2 }, attrs || {}));
    };
    P.poly = (pts, color, attrs) => P.add("path", Object.assign({ d: pts.map((p, i) => (i ? "L" : "M") + P.X(p[0]).toFixed(1) + " " + P.Y(p[1]).toFixed(1)).join(""), fill: "none", stroke: color, "stroke-width": 2.2 }, attrs || {}));
    P.dot = (x, y, color, label, dx, dy) => { if (!isFinite(x) || !isFinite(y)) return; P.add("circle", { cx: P.X(x), cy: P.Y(y), r: 4.5, fill: color }); if (label) P.text(P.X(x) + (dx || 8), P.Y(y) + (dy || -8), label, { fill: color }); };
    P.vline = (x, color, dash, label) => { P.add("line", { x1: P.X(x), x2: P.X(x), y1: P.Y(o.ymin), y2: P.Y(o.ymax), stroke: color, "stroke-dasharray": dash || "4 4" }); if (label) P.text(P.X(x) + 4, P.Y(o.ymax) + 12, label, { fill: color, "font-size": 12 }); };
    P.hline = (y, color, dash, label) => { P.add("line", { x1: P.X(o.xmin), x2: P.X(o.xmax), y1: P.Y(y), y2: P.Y(y), stroke: color, "stroke-dasharray": dash || "4 4" }); if (label) P.text(P.X(o.xmax) - 4, P.Y(y) - 6, label, { fill: color, "font-size": 12, "text-anchor": "end" }); };
    P.band = (x0, x1, color, label) => { P.add("rect", { x: P.X(x0), y: P.Y(o.ymax), width: Math.max(0, P.X(x1) - P.X(x0)), height: P.Y(o.ymin) - P.Y(o.ymax), fill: color, opacity: 0.07 }); if (label) P.text((P.X(x0) + P.X(x1)) / 2, P.Y(o.ymax) + 14, label, { "text-anchor": "middle", fill: G.C.muted, "font-size": 12 }); };
    P.legend = items => items.forEach(([s, c], i) => { P.add("rect", { x: o.pad.l + 10 + i * 150, y: o.h - 14, width: 12, height: 3, fill: c }); P.text(o.pad.l + 26 + i * 150, o.h - 9, s, { fill: G.C.muted, "font-size": 12 }); });
    return P;
  };

  // Sliders with synced number boxes. specs: [{key, label, min, max, step, value} | {key, label, options:[[v,text]], value}]
  G.controls = function (holder, specs, onChange) {
    const box = document.createElement("div"); box.className = "g-controls";
    const vals = {};
    for (const s of specs) {
      vals[s.key] = s.value;
      const row = document.createElement("div"); row.className = "g-ctl";
      const lab = document.createElement("label"); lab.textContent = s.label; row.append(lab);
      if (s.options) {
        const sel = document.createElement("select");
        for (const [v, t] of s.options) { const op = document.createElement("option"); op.value = v; op.textContent = t; if (v === s.value) op.selected = true; sel.append(op); }
        sel.addEventListener("change", () => { vals[s.key] = sel.value; onChange(vals); });
        row.append(sel);
      } else {
        const r = document.createElement("input"); r.type = "range"; r.min = s.min; r.max = s.max; r.step = s.step || "any"; r.value = s.value;
        const n = document.createElement("input"); n.type = "number"; n.step = s.step || "any"; n.value = s.value;
        r.addEventListener("input", () => { vals[s.key] = +r.value; n.value = r.value; onChange(vals); });
        n.addEventListener("input", () => { if (n.value === "" || !isFinite(+n.value)) return; vals[s.key] = +n.value; r.value = n.value; onChange(vals); });
        row.append(r, n);
      }
      box.append(row);
    }
    holder.append(box);
    return vals;
  };

  G.readout = function (holder) { const d = document.createElement("div"); d.className = "g-read"; holder.append(d); return d; };

  // Largest x in [a, b] where f changes sign (bisection over a scan). Used for intersections.
  G.root = function (f, a, b, n) {
    n = n || 400; let prev = f(a), px = a, found = null;
    for (let i = 1; i <= n; i++) {
      const x = a + (b - a) * i / n, y = f(x);
      if (isFinite(prev) && isFinite(y) && (prev === 0 || prev * y < 0)) {
        let lo = px, hi = x;
        for (let k = 0; k < 60; k++) { const m = (lo + hi) / 2; if (f(lo) * f(m) <= 0) hi = m; else lo = m; }
        found = (lo + hi) / 2;
      }
      prev = y; px = x;
    }
    return found;
  };
})(globalThis.M2 = globalThis.M2 || {});
