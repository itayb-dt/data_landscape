document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => {
  document.querySelectorAll('.tab').forEach(x => x.classList.remove('on'));
  t.classList.add('on');
  const f = t.dataset.f;
  document.querySelectorAll('.timeline [data-type], .strip .ev').forEach(el => {
    el.classList.toggle('hidden', f !== 'all' && el.dataset.type !== f);
  });
}));
