document.querySelectorAll('#tabs .tab').forEach(t => t.addEventListener('click', () => {
  document.querySelectorAll('#tabs .tab').forEach(x => x.classList.remove('on'));
  t.classList.add('on');
  const f = t.dataset.f;
  document.querySelectorAll('.timeline [data-type], .compact [data-type], .strip .ev').forEach(el => {
    el.classList.toggle('hidden', f !== 'all' && el.dataset.type !== f);
  });
}));

function setView(v) {
  document.body.classList.toggle('view-compact', v === 'compact');
  document.querySelectorAll('#views .tab').forEach(x => x.classList.toggle('on', x.dataset.v === v));
  try { localStorage.setItem('view', v); } catch (e) {}
}
document.querySelectorAll('#views .tab').forEach(t => t.addEventListener('click', () => setView(t.dataset.v)));
if (document.getElementById('views')) {
  let v = 'detailed';
  try { v = localStorage.getItem('view') || v; } catch (e) {}
  setView(v);
}

// Search: loads search.json on first focus, all typed words must match (title, company names or text).
(function () {
  const q = document.getElementById('q'), box = document.getElementById('results');
  if (!q || !box) return;
  let docs = null, loading = null, sel = -1, shown = [];
  const clean = s => s.replace(/\{\{[^}]*\}\}|\{%[^%]*%\}/g, ' ').replace(/\]\([^)]*\)/g, ']').replace(/[*_#`>|\[\]]/g, ' ').replace(/\s+/g, ' ').trim();
  const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  function load() {
    if (!loading) loading = fetch(q.dataset.index).then(r => r.json()).then(d => {
      docs = d.map(x => ({ t: x.t, u: x.u, c: x.c || '', n: x.n || '', x: clean(x.x || '') }));
      docs.forEach(d => { d.tl = d.t.toLowerCase(); d.nl = d.n.toLowerCase(); d.xl = d.x.toLowerCase(); });
    }).catch(() => { loading = null; });
    return loading;
  }
  function count(h, w) { let i = 0, n = 0; while ((i = h.indexOf(w, i)) !== -1 && n < 20) { n++; i += w.length; } return n; }
  function run() {
    const words = q.value.toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length || !docs) { box.hidden = true; return; }
    shown = docs.map(d => {
      let s = 0;
      for (const w of words) {
        const inT = d.tl.includes(w), inN = d.nl.includes(w), nx = count(d.xl, w);
        if (!inT && !inN && !nx) return null;
        s += (inT ? 20 : 0) + (inN ? 12 : 0) + Math.min(nx, 10);
      }
      return { d, s };
    }).filter(Boolean).sort((a, b) => b.s - a.s).slice(0, 8);
    sel = shown.length ? 0 : -1;
    box.innerHTML = shown.length ? shown.map((r, i) => {
      const d = r.d, w = words[0], at = d.xl.indexOf(w);
      const snip = at >= 0 ? (at > 40 ? '…' : '') + d.x.slice(Math.max(0, at - 40), at + 90) + '…' : '';
      return '<a href="' + esc(d.u) + '" class="' + (i === 0 ? 'sel' : '') + '"><div class="rt"><span class="rc">' + esc(d.c) + '</span>' + esc(d.t) + '</div>' + (snip ? '<div class="rm">' + esc(snip) + '</div>' : '') + '</a>';
    }).join('') : '<div class="none">No articles match.</div>';
    box.hidden = false;
  }
  function move(d) {
    const items = box.querySelectorAll('a'); if (!items.length) return;
    sel = (sel + d + items.length) % items.length;
    items.forEach((a, i) => a.classList.toggle('sel', i === sel));
    items[sel].scrollIntoView({ block: 'nearest' });
  }
  q.addEventListener('focus', () => { load().then(run); });
  q.addEventListener('input', () => { load().then(run); });
  q.addEventListener('keydown', e => {
    if (e.key === 'Escape') { box.hidden = true; q.blur(); }
    else if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter' && shown[sel]) { window.location = shown[sel].d.u; }
  });
  document.addEventListener('click', e => { if (!e.target.closest('.search')) box.hidden = true; });
  document.addEventListener('keydown', e => {
    if (e.key === '/' && document.activeElement !== q && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); q.focus(); }
  });
})();
