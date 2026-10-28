/* Jakob Kohlbrenner – Skript: Menü, Bild-Platzhalter, Projektfilter, Lightbox */
(function () {
  // Kopfhöhe als CSS-Variable
  var kopf = document.querySelector('.kopf');
  function setKopf() { if (kopf) document.documentElement.style.setProperty('--kopf', kopf.offsetHeight + 'px'); }
  setKopf(); window.addEventListener('resize', setKopf);

  // Fortschrittslinie beim Scrollen
  var bar = document.querySelector('.progress span'), ticking = false;
  function progress() {
    var h = document.documentElement.scrollHeight - innerHeight;
    if (bar) bar.style.transform = 'scaleX(' + (h > 0 ? Math.min(1, scrollY / h) : 0) + ')';
    ticking = false;
  }
  addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(progress); } }, { passive: true });
  progress();

  // Menü am Handy
  var btn = document.querySelector('.menu-btn'), nav = document.querySelector('.nav');
  if (btn && nav) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
    btn.textContent = open ? 'Schließen' : 'Menü';
  });

  // Fehlende Bilder zeigen einen beschrifteten Platzhalter
  function markMissing(img) {
    var fig = img.closest('.ph');
    if (fig) { fig.classList.add('is-missing'); fig.dataset.label = img.getAttribute('alt') || 'Bild folgt'; }
  }
  document.querySelectorAll('.ph img').forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) markMissing(img);
    img.addEventListener('error', function () { markMissing(img); });
  });

  // Projektfilter
  var fbox = document.getElementById('filters'), grid = document.getElementById('gallery');
  if (fbox && grid) {
    var tiles = [].slice.call(grid.querySelectorAll('.tile'));
    var cats = ['Alle'];
    tiles.forEach(function (t) { (t.dataset.cats || '').split('|').forEach(function (c) { if (c && cats.indexOf(c) < 0) cats.push(c); }); });
    cats.forEach(function (c, i) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = c;
      b.setAttribute('aria-pressed', i === 0);
      b.addEventListener('click', function () {
        [].forEach.call(fbox.children, function (x) { x.setAttribute('aria-pressed', x === b); });
        tiles.forEach(function (t) { t.hidden = !(c === 'Alle' || (t.dataset.cats || '').split('|').indexOf(c) > -1); });
      });
      fbox.appendChild(b);
    });
  }

  // Lightbox für Bildergalerien
  var lb = document.createElement('div'); lb.className = 'lb'; lb.innerHTML = '<img alt="">';
  document.body.appendChild(lb);
  lb.addEventListener('click', function () { lb.classList.remove('open'); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') lb.classList.remove('open'); });
  document.querySelectorAll('.masonry .ph').forEach(function (fig) {
    fig.addEventListener('click', function () {
      var img = fig.querySelector('img'); if (!img || fig.classList.contains('is-missing')) return;
      lb.firstChild.src = img.currentSrc || img.src; lb.firstChild.alt = img.alt; lb.classList.add('open');
    });
  });

  // Keine einzelnen Wörter am Zeilenende: geschütztes Leerzeichen vor dem letzten Wort
  document.querySelectorAll('.prose p, .lead, .card p, .step p, .tile p, .quote p').forEach(function (p) {
    if (p.children.length) return;
    p.textContent = p.textContent.replace(/\s+(\S+)\s*$/, ' $1');
  });
})();
