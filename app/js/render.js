// Markdown subset plus KaTeX. Math delimiters: \( \) inline, \[ \] or $$ $$ display. A single $ is always currency.
(function (M2) {
  const R = {};
  R.esc = s => String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

  const MATH = /(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\))/g;

  function inline(s) {
    return s
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[^*\w])\*([^*\n]+)\*(?!\w)/g, "$1<em>$2</em>");
  }

  // tables: {"0": [[{t,r,c,h}|string, ...], ...]} from imported professor questions
  R.table = function (rows) {
    let h = '<table class="qt">';
    for (const row of rows) {
      h += "<tr>";
      for (const cell of row) {
        const c = typeof cell === "string" ? { t: cell } : cell;
        const tag = c.h ? "th" : "td";
        h += `<${tag}${c.r > 1 ? ` rowspan="${c.r}"` : ""}${c.c > 1 ? ` colspan="${c.c}"` : ""}>${R.esc(c.t)}</${tag}>`;
      }
      h += "</tr>";
    }
    return h + "</table>";
  };

  function pipeTable(lines) {
    const rows = lines.filter(l => !/^\s*\|?\s*:?-{2,}/.test(l)).map(l => l.trim().replace(/^\||\|$/g, "").split("|").map(x => x.trim()));
    let h = '<table class="qt">';
    rows.forEach((r, i) => { h += "<tr>" + r.map(c => i === 0 ? `<th>${inline(c)}</th>` : `<td>${inline(c)}</td>`).join("") + "</tr>"; });
    return h + "</table>";
  }

  R.md = function (text, tables) {
    if (text == null) return "";
    const math = [];
    let s = String(text).replace(MATH, m => { math.push(m); return `\u0000${math.length - 1}\u0000`; });
    s = R.esc(s);
    const blocks = s.split(/\n\s*\n/);
    let out = "";
    for (const b of blocks) {
      const lines = b.split("\n").filter(l => l.trim() !== "");
      if (!lines.length) continue;
      if (lines.every(l => /^\s*[-*] /.test(l))) out += "<ul>" + lines.map(l => "<li>" + inline(l.replace(/^\s*[-*] /, "")) + "</li>").join("") + "</ul>";
      else if (lines.every(l => /^\s*\d+[.)] /.test(l))) out += "<ol>" + lines.map(l => "<li>" + inline(l.replace(/^\s*\d+[.)] /, "")) + "</li>").join("") + "</ol>";
      else if (lines.every(l => /^\s*\|/.test(l))) out += pipeTable(lines);
      else if (/^#{2,4} /.test(lines[0])) out += `<h4>${inline(lines[0].replace(/^#+ /, ""))}</h4>` + (lines.length > 1 ? "<p>" + inline(lines.slice(1).join("<br>")) + "</p>" : "");
      else out += "<p>" + inline(lines.join("<br>")) + "</p>";
    }
    out = out.replace(/\[\[TABLE (\d+)\]\]/g, (m, k) => tables && tables[k] ? "</p>" + R.table(tables[k]) + "<p>" : m).replace(/<p>\s*<\/p>/g, "");
    return out.replace(/\u0000(\d+)\u0000/g, (m, i) => R.esc(math[+i]));
  };

  R.tex = function (tex, display) {
    try { return globalThis.katex.renderToString(tex, { displayMode: !!display, throwOnError: false }); }
    catch (e) { return `<code>${R.esc(tex)}</code>`; }
  };

  R.math = function (el) {
    if (!globalThis.renderMathInElement || !el) return;
    renderMathInElement(el, {
      delimiters: [{ left: "$$", right: "$$", display: true }, { left: "\\[", right: "\\]", display: true }, { left: "\\(", right: "\\)", display: false }],
      throwOnError: false, ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "input"]
    });
  };

  // Small DOM helper: h("div.cls", {attr}, children...)
  R.h = function (sel, attrs, ...kids) {
    const [tag, ...cls] = sel.split(".");
    const el = document.createElement(tag || "div");
    if (cls.length) el.className = cls.join(" ");
    for (const [k, v] of Object.entries(attrs || {})) {
      if (k === "html") el.innerHTML = v;
      else if (k === "text") el.textContent = v;
      else if (k.startsWith("on")) el.addEventListener(k.slice(2), v);
      else if (v !== false && v != null) el.setAttribute(k, v);
    }
    for (const k of kids.flat()) if (k != null) el.append(k.nodeType ? k : document.createTextNode(k));
    return el;
  };

  M2.render = R;
})(globalThis.M2 = globalThis.M2 || {});
