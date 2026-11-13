// Progress model, saved in localStorage key m2.progress.v1. Export and import as a JSON file.
(function (M2) {
  const KEY = "m2.progress.v1";
  const blank = () => ({ v: 1, q: {}, lo: {}, queue: [], served: 0, sinceQueue: 0, mock: null, mockHistory: [], settings: {} });

  let mem = null;                    // fallback when localStorage is blocked
  function load() {
    try {
      const raw = globalThis.localStorage && localStorage.getItem(KEY);
      if (raw) return Object.assign(blank(), JSON.parse(raw));
    } catch (e) { /* storage blocked or corrupt */ }
    return mem || blank();
  }
  function save(p) {
    mem = p;
    try { globalThis.localStorage && localStorage.setItem(KEY, JSON.stringify(p)); } catch (e) { /* ignore */ }
  }

  M2.store = {
    KEY, blank, load, save,
    p: null,
    get() { if (!this.p) this.p = load(); return this.p; },
    commit() { save(this.p); },
    reset(p) { this.p = p || blank(); save(this.p); },

    exportFile() {
      const blob = new Blob([JSON.stringify(this.get(), null, 1)], { type: "application/json" });
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "m2-progress-" + new Date().toISOString().slice(0, 10) + ".json";
      document.body.appendChild(a); a.click(); a.remove();
    },
    importFile(file, done) {
      const fr = new FileReader();
      fr.onload = () => {
        try {
          const p = JSON.parse(fr.result);
          if (!p || p.v !== 1 || typeof p.q !== "object") throw new Error("not a progress file");
          this.reset(Object.assign(blank(), p));
          done(null);
        } catch (e) { done(e); }
      };
      fr.readAsText(file);
    }
  };
})(globalThis.M2 = globalThis.M2 || {});
