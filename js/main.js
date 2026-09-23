(function () {
  // Header: transparent over hero, solid after scroll
  var header = document.querySelector('.site-header');
  var hero = document.querySelector('.hero');
  function onScroll() {
    if (!header || header.classList.contains('always-solid')) return;
    var y = window.scrollY || window.pageYOffset;
    var limit = hero ? hero.offsetHeight - 80 : 40;
    header.classList.toggle('solid', y > limit);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      header.classList.toggle('menu-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.style.overflow = open ? 'hidden' : '';
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        header.classList.remove('menu-open');
        document.body.style.overflow = '';
      });
    });
  }

  // Scroll reveal
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Lightbox (dress pages)
  var lb = document.querySelector('.lightbox');
  if (lb) {
    var figs = Array.prototype.slice.call(document.querySelectorAll('.dress-gallery figure'));
    var srcs = figs.map(function (f) { return f.querySelector('img').getAttribute('src'); });
    var img = lb.querySelector('img');
    var count = lb.querySelector('.count');
    var idx = 0;
    function show(i) {
      idx = (i + srcs.length) % srcs.length;
      img.src = srcs[idx];
      count.textContent = (idx + 1) + ' / ' + srcs.length;
    }
    function open(i) { show(i); lb.classList.add('open'); document.body.style.overflow = 'hidden'; }
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; }
    figs.forEach(function (f, i) { f.addEventListener('click', function () { open(i); }); });
    lb.querySelector('.close').addEventListener('click', close);
    lb.querySelector('.prev').addEventListener('click', function (e) { e.stopPropagation(); show(idx - 1); });
    lb.querySelector('.next').addEventListener('click', function (e) { e.stopPropagation(); show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
    // swipe
    var sx = null;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (sx === null) return;
      var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 40) show(dx < 0 ? idx + 1 : idx - 1);
      sx = null;
    });
  }

  // Size guide modal
  var modal = document.getElementById('size-guide');
  if (modal) {
    var lastFocus = null;
    function openModal(e) {
      if (e) e.preventDefault();
      lastFocus = document.activeElement;
      modal.hidden = false;
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
      modal.querySelector('.size-close').focus();
    }
    function closeModal() {
      modal.classList.remove('open');
      modal.hidden = true;
      document.body.style.overflow = '';
      if (lastFocus) lastFocus.focus();
    }
    document.querySelectorAll('[data-size-guide]').forEach(function (t) {
      t.addEventListener('click', openModal);
    });
    modal.querySelector('.size-close').addEventListener('click', closeModal);
    modal.addEventListener('click', function (e) { if (e.target === modal) closeModal(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modal.classList.contains('open')) closeModal();
    });
    if (location.hash === '#size-guide') openModal();
  }

  // Size picker -> WhatsApp order message
  var order = document.querySelector('.order');
  if (order) {
    var btn = order.querySelector('.order-btn');
    var dress = order.getAttribute('data-dress');
    var phone = order.getAttribute('data-wa');
    var chosen = null;
    function updateLink() {
      var msg = "Hello! I would like to order '" + dress + "' from the Patraani collection.";
      if (chosen === 'Made to measure') {
        msg += ' I would like it made to my measurements.';
      } else if (chosen) {
        msg += ' Size: ' + chosen + '.';
      }
      btn.href = 'https://wa.me/' + phone + '?text=' + encodeURIComponent(msg);
      btn.textContent = chosen ? 'Order ' + (chosen === 'Made to measure' ? 'made to measure' : 'size ' + chosen) : 'Order on WhatsApp';
    }
    order.querySelectorAll('.size-opt').forEach(function (b) {
      b.addEventListener('click', function () {
        var already = b.classList.contains('selected');
        order.querySelectorAll('.size-opt').forEach(function (o) { o.classList.remove('selected'); });
        if (already) { chosen = null; } else { b.classList.add('selected'); chosen = b.getAttribute('data-size'); }
        updateLink();
      });
    });
  }
})();
