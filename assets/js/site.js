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
