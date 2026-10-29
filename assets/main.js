(function () {
  document.documentElement.classList.remove('no-js');

  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var links = document.getElementById('nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.closest('a')) { links.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && links.classList.contains('open')) {
        links.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus();
      }
    });
  }

  // Header border on scroll
  var header = document.querySelector('.site-header');
  var onScroll = function () { if (header) header.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // Forms -> FormSubmit -> matt@sitecomply.ca
  document.querySelectorAll('form[data-sc-form]').forEach(function (form) {
    var status = form.querySelector('.form-status');
    var submit = form.querySelector('button[type="submit"]');
    function validate() {
      var first = null;
      form.querySelectorAll('[required]').forEach(function (f) {
        var ok = f.checkValidity();
        f.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok && !first) first = f;
      });
      return first;
    }
    form.querySelectorAll('input,textarea').forEach(function (f) {
      f.addEventListener('blur', function () { if (f.required && f.value) f.setAttribute('aria-invalid', f.checkValidity() ? 'false' : 'true'); });
      f.addEventListener('input', function () { if (f.getAttribute('aria-invalid') === 'true' && f.checkValidity()) f.setAttribute('aria-invalid', 'false'); });
    });
    // Normalise URLs typed without https://
    var url = form.querySelector('input[type="url"]');
    if (url) url.addEventListener('blur', function () {
      var v = url.value.trim();
      if (v && !/^https?:\/\//i.test(v)) url.value = 'https://' + v;
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      status.className = 'form-status'; status.textContent = '';
      var bad = validate();
      if (bad) { bad.focus(); status.className = 'form-status bad'; status.textContent = 'Please fill in the highlighted fields.'; return; }
      var data = new FormData(form);
      if (data.get('_honey')) return;
      submit.disabled = true; var label = submit.textContent; submit.textContent = 'Sending…';
      fetch(form.action, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
        .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { if (!r.ok || j.success === 'false' || j.success === false) throw new Error(j.message || 'Request failed'); }); })
        .then(function () {
          form.reset();
          status.className = 'form-status ok';
          status.textContent = form.getAttribute('data-success') || 'Thanks! We received your request and will be in touch within one business day.';
          status.focus();
        })
        .catch(function () {
          status.className = 'form-status bad';
          var lines = [];
          data.forEach(function (v, k) { if (k.charAt(0) !== '_' && v) lines.push(k + ': ' + v); });
          var href = 'mailto:matt@sitecomply.ca?subject=' + encodeURIComponent(data.get('_subject') || 'SiteComply enquiry') + '&body=' + encodeURIComponent(lines.join('\n'));
          status.innerHTML = 'We couldn\u2019t send your request just now. <a href="' + href + '">Send it by email instead</a> and your details will be filled in for you.';
          status.focus();
        })
        .finally(function () { submit.disabled = false; submit.textContent = label; });
    });
  });

  // Interactive checklist with saved progress
  var list = document.querySelector('[data-checklist]');
  if (list) {
    var key = 'sc-checklist-v1', saved = {};
    try { saved = JSON.parse(localStorage.getItem(key) || '{}'); } catch (e) {}
    var boxes = list.querySelectorAll('input[type="checkbox"]');
    var out = document.querySelector('[data-progress-text]'), bar = document.querySelector('[data-progress-bar]');
    function update() {
      var n = 0; boxes.forEach(function (b) { if (b.checked) n++; });
      if (out) out.textContent = n + ' of ' + boxes.length + ' complete';
      if (bar) bar.style.width = (100 * n / boxes.length) + '%';
    }
    boxes.forEach(function (b) {
      b.checked = !!saved[b.id];
      b.addEventListener('change', function () {
        saved[b.id] = b.checked; try { localStorage.setItem(key, JSON.stringify(saved)); } catch (e) {} update();
      });
    });
    var reset = document.querySelector('[data-checklist-reset]');
    if (reset) reset.addEventListener('click', function () { boxes.forEach(function (b) { b.checked = false; }); saved = {}; try { localStorage.removeItem(key); } catch (e) {} update(); });
    var print = document.querySelector('[data-print]');
    if (print) print.addEventListener('click', function () { window.print(); });
    update();
  }

  var y = document.querySelectorAll('[data-year]'); y.forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
