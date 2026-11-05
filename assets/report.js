/* SiteComply report renderer: shared by demo.html and report.html.
   Renders a WCAG 2.0 Level AA (AODA) scan result produced by the SiteComply scanner. */
(function () {
  "use strict";
  var STATUS = {
    fail:        { label: "Issues found", cls: "st-fail", icon: "✕", note: "" },
    review:      { label: "Needs human review", cls: "st-review", icon: "?", note: "The automated test couldn't decide. A person needs to check." },
    auto:        { label: "No automated issues", cls: "st-auto", icon: "✓", note: "Passed automated tests. Confirm with manual testing." },
    manual:      { label: "Manual test required", cls: "st-manual", icon: "•", note: "This can't be tested automatically." },
    "none-media":{ label: "No audio or video found", cls: "st-na", icon: "–", note: "No audio or video on the pages tested." },
    "none-forms":{ label: "No forms found", cls: "st-na", icon: "–", note: "No forms on the pages tested." },
    exempt:      { label: "Not required under AODA", cls: "st-na", icon: "–", note: "Exempt for this organization type under O. Reg. 191/11, s. 14(4)." },
    errata:      { label: "Always met for HTML", cls: "st-na", icon: "–", note: "Per W3C's official WCAG 2.0 errata, 4.1.1 is considered always satisfied for HTML content. Related problems are reported under other criteria." }
  };
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&#39;" }[c]; }); }
  function sum(o) { var n = 0; for (var k in o) n += o[k]; return n; }
  function plural(n, one, many) { return n + " " + (n === 1 ? one : many); }
  function fmtDate(d) { try { return new Date(d).toLocaleDateString("en-CA", { year: "numeric", month: "long", day: "numeric", timeZone: "America/Toronto" }); } catch (e) { return d; } }
  function store(k, v) { try { if (v === undefined) return JSON.parse(localStorage.getItem(k) || "null"); localStorage.setItem(k, JSON.stringify(v)); } catch (e) { return null; } }
  var ext = '<span class="sr-only"> (opens in a new tab)</span>';
  function a(href, text) { return '<a href="' + esc(href) + '" target="_blank" rel="noopener">' + text + ext + "</a>"; }

  function crit(r, sc) { for (var i = 0; i < r.criteria.length; i++) if (r.criteria[i].sc === sc) return r.criteria[i]; return { sc: sc, name: "", level: "" }; }

  function groups(r, kind, key) {
    var g = {}, order = [];
    r.pages.forEach(function (p) {
      var m = p[key] || {};
      for (var id in m) {
        var rule = r.rules[id]; if (!rule) continue;
        var gk = rule.t;
        if (!g[gk]) { g[gk] = { t: rule.t, lvl: rule.lvl, who: rule.who, fix: rule.fix, ids: [], sc: [], n: 0, pages: [], ex: [], help: [] }; order.push(gk); }
        var G = g[gk];
        G.n += m[id]; G.lvl = Math.max(G.lvl, rule.lvl);
        if (G.ids.indexOf(id) < 0) {
          G.ids.push(id); G.help.push({ text: rule.help, url: rule.helpUrl });
          rule.sc.forEach(function (s) { if (G.sc.indexOf(s) < 0) G.sc.push(s); });
          rule.ex.forEach(function (e) { if (G.ex.length < 2) G.ex.push(e); });
          if (!G.who && rule.who) G.who = rule.who; if (!G.fix && rule.fix) G.fix = rule.fix;
        }
        var found = null; G.pages.forEach(function (x) { if (x.u === p.u) found = x; });
        if (found) found.n += m[id]; else G.pages.push({ t: p.t, u: p.u, n: m[id] });
      }
    });
    return order.map(function (k) { return g[k]; }).sort(function (x, y) { return (y.lvl * 1000 + y.n) - (x.lvl * 1000 + x.n); });
  }

  function scChips(r, list) {
    return list.sort().map(function (s) { var c = crit(r, s); return '<a class="tag tag-sc" href="' + esc(c.url || "https://www.w3.org/TR/WCAG20/") + '" target="_blank" rel="noopener">WCAG ' + esc(s) + " " + esc(c.name) + " (Level " + esc(c.level) + ")" + ext + "</a>"; }).join("");
  }

  function render(root, r, opts) {
    opts = opts || {};
    var uid = opts.uid || "r";
    var fixedKey = "sc-fixed-" + (opts.storeKey || r.host);
    var fixed = opts.trackFixes ? (store(fixedKey) || {}) : {};
    var fails = groups(r, "fail", "v"), reviews = groups(r, "review", "r");
    var total = r.pages.reduce(function (a, p) { return a + sum(p.v); }, 0);
    var open = fails.reduce(function (a, g) { return a + (fixed[g.t] ? 0 : g.n); }, 0);
    var reviewN = r.pages.reduce(function (a, p) { return a + sum(p.r); }, 0);
    var required = r.criteria.filter(function (c) { return c.status !== "exempt"; });
    var cFail = required.filter(function (c) { return c.status === "fail"; }).length;
    var clean = r.pages.filter(function (p) { return !sum(p.v); }).length;
    var pdfChecked = (r.pdfs && r.pdfs.checked) || [];
    var pdfProblems = pdfChecked.filter(function (p) { return !p.error && (!p.tagged || !p.title || !p.lang); }).length;
    var h = "";

    // Summary
    h += '<div class="demo-bar card"><div><p class="rep-site">' + esc(r.name) + '</p><p class="demo-meta">' + a(r.url, esc(r.host)) + " · " + plural(r.pages.length, "page", "pages") + " tested · " + esc(fmtDate(r.date)) + "</p></div>" +
      '<p class="rep-std"><strong>Standard:</strong> ' + esc(r.standard) + '<br><span class="muted">' + esc(r.law) + "</span></p></div>";
    h += '<div class="demo-stats">' + [
      [open, "Open issues", opts.trackFixes && total ? (total - open) + " marked fixed" : "Found by automated tests"],
      [cFail + " of " + required.length, "WCAG criteria with issues", "Level A and AA criteria that apply"],
      [reviewN, "Items for human review", "The test couldn't decide"],
      [(r.pdfs ? r.pdfs.found : 0), "PDFs linked", pdfChecked.length ? pdfProblems + " of " + pdfChecked.length + " checked have problems" : "From the pages tested"]
    ].map(function (t) { return '<div class="stat card"><p class="stat-n">' + t[0] + '</p><p class="stat-l">' + t[1] + '</p><p class="stat-s">' + t[2] + "</p></div>"; }).join("") + "</div>";

    // Issues + pages
    h += '<div class="demo-grid"><div><h2 class="demo-h2">What to fix first</h2><p class="demo-sub">Grouped by problem and sorted by how much it affects people.' + (opts.trackFixes ? " Tick an item once it's fixed to see how tracking works." : "") + "</p>";
    if (!fails.length) {
      h += '<div class="card demo-empty"><h3>No issues found by automated tests</h3><p>The automated tests didn\'t find problems on the ' + plural(r.pages.length, "page", "pages") + " we tested. That's a strong start. The checklist below shows which WCAG criteria still need a manual check.</p></div>";
    } else {
      h += fails.map(function (g, gi) {
        var id = uid + "-fix-" + gi, done = !!fixed[g.t];
        return '<article class="card issue' + (done ? " is-fixed" : "") + '">' +
          '<div class="issue-head"><h3>' + esc(g.t) + '</h3><span class="issue-n">' + plural(g.n, "instance", "instances") + "</span></div>" +
          '<p class="issue-tags"><span class="tag ' + (g.lvl >= 3 ? "tag-high" : "tag-med") + '">' + (g.lvl >= 3 ? "High impact" : g.lvl === 2 ? "Medium impact" : "Lower impact") + "</span>" + scChips(r, g.sc) + "</p>" +
          (g.who ? "<p><strong>Who it affects:</strong> " + esc(g.who) + "</p>" : "") +
          (g.fix ? "<p><strong>How to fix:</strong> " + esc(g.fix) + "</p>" : "") +
          "<details><summary>Where we found it and technical details</summary>" +
          '<ul class="issue-where">' + g.pages.map(function (p) { return "<li>" + a(p.u, esc(p.t)) + ' <span class="muted">(' + p.n + ")</span></li>"; }).join("") + "</ul>" +
          g.ex.map(function (e) { return '<p class="issue-ex-l">Example from the page code:</p><pre class="issue-ex"><code>' + esc(e.html) + "</code></pre>"; }).join("") +
          '<p class="issue-tech">Technical guide: ' + g.help.map(function (x) { return a(x.url, esc(x.text)); }).join("; ") + "</p></details>" +
          (opts.trackFixes ? '<label class="issue-done" for="' + id + '"><input type="checkbox" id="' + id + '" data-rule="' + esc(g.t) + '"' + (done ? " checked" : "") + "> Mark as fixed</label>" : "") +
          "</article>";
      }).join("");
    }
    if (reviews.length) {
      h += '<h2 class="demo-h2 rep-gap">Needs a human check</h2><p class="demo-sub">The automated test found these but couldn\'t decide whether they pass. For example, text over a background image needs a person to judge the contrast.</p>' +
        '<div class="card rep-review"><ul>' + reviews.map(function (g) {
          return "<li><strong>" + esc(g.t) + "</strong> <span class=\"muted\">(" + plural(g.n, "item", "items") + ", WCAG " + esc(g.sc.sort().join(", ")) + ")</span>" + (g.help[0] ? '<br><span class="issue-tech">' + a(g.help[0].url, "Technical guide") + "</span>" : "") + "</li>";
        }).join("") + "</ul></div>";
    }
    h += '</div><aside aria-labelledby="' + uid + '-pages-h"><h2 class="demo-h2" id="' + uid + '-pages-h">Pages tested</h2><ul class="demo-pages">' +
      r.pages.map(function (p) { var c = sum(p.v); return "<li>" + a(p.u, esc(p.t)) + '<span class="pg-badge ' + (c ? "pg-bad" : "pg-ok") + '">' + (c ? plural(c, "issue", "issues") : "No issues") + "</span></li>"; }).join("") +
      "</ul>" + (r.failed && r.failed.length ? '<p class="demo-sub rep-gap-s">' + plural(r.failed.length, "page", "pages") + " couldn't be loaded and weren't tested.</p>" : "") +
      '<p class="demo-sub rep-gap-s">' + clean + " of " + r.pages.length + " pages had no automated issues.</p></aside></div>";

    // WCAG checklist
    h += '<h2 class="demo-h2 demo-all-h" id="' + uid + '-checklist">WCAG 2.0 Level AA checklist</h2><p class="demo-sub">All 38 Level A and AA success criteria in WCAG 2.0, the standard required by the AODA, and where this website stands on each one based on the pages tested.</p>' +
      '<div class="demo-table-wrap card"><table class="demo-table rep-crit"><caption class="sr-only">WCAG 2.0 Level A and AA success criteria results</caption><thead><tr><th scope="col">Criterion</th><th scope="col">Level</th><th scope="col">What it means</th><th scope="col">Result</th></tr></thead><tbody>' +
      r.criteria.map(function (c) {
        var s = STATUS[c.status] || STATUS.manual;
        return '<tr><th scope="row">' + a(c.url, esc(c.sc) + " " + esc(c.name)) + "</th><td>" + esc(c.level) + "</td><td>" + esc(c.plain) + '</td><td><span class="st ' + s.cls + '"><span aria-hidden="true">' + s.icon + "</span> " + s.label + "</span>" + (s.note ? '<span class="st-note">' + esc(s.note) + "</span>" : "") + "</td></tr>";
      }).join("") + "</tbody></table></div>";

    // PDFs
    if (r.pdfs && r.pdfs.found) {
      var yn = function (v) { return v ? '<span class="st st-auto"><span aria-hidden="true">✓</span> Yes</span>' : '<span class="st st-fail"><span aria-hidden="true">✕</span> No</span>'; };
      h += '<h2 class="demo-h2 demo-all-h">PDF documents</h2><p class="demo-sub">' + plural(r.pdfs.found, "PDF is", "PDFs are") + " linked from the pages tested. PDFs must also meet WCAG 2.0 AA. We checked the basics on " + plural(pdfChecked.length, "file", "files") + ": whether it's tagged (so screen readers can read it in order), has a title, and has its language set. Full PDF accessibility also needs a manual review.</p>" +
        '<div class="demo-table-wrap card"><table class="demo-table"><caption class="sr-only">PDF basic accessibility checks</caption><thead><tr><th scope="col">File</th><th scope="col">Tagged</th><th scope="col">Title</th><th scope="col">Language</th></tr></thead><tbody>' +
        pdfChecked.map(function (p) {
          var nm = decodeURIComponent((p.u.split("?")[0].split("/").pop() || p.u)).slice(0, 70);
          return '<tr><th scope="row">' + a(p.u, esc(nm)) + "</th>" + (p.error ? '<td colspan="3" class="muted">' + esc(p.error) + "</td>" : "<td>" + yn(p.tagged) + "</td><td>" + yn(p.title) + "</td><td>" + yn(p.lang) + "</td>") + "</tr>";
        }).join("") + "</tbody></table></div>";
    }

    // Method
    h += '<div class="card rep-method"><h2 class="demo-h2">About this report</h2><ul>' +
      "<li><strong>Standard:</strong> WCAG 2.0 Level A and AA, as required by " + esc(r.law) + "." + (r.exempt && r.exempt.length ? " Success criteria " + esc(r.exempt.join(" and ")) + " are not required for this type of organization." : "") + "</li>" +
      "<li><strong>What we tested:</strong> " + plural(r.pages.length, "public page", "public pages") + " on " + esc(r.host) + ", chosen from the homepage links and the site map. We only visit public pages, follow the site's robots.txt rules and never log in or submit forms.</li>" +
      "<li><strong>How:</strong> automated tests using " + esc(r.engine) + ", an open-source testing engine widely used across the accessibility industry, limited to the WCAG 2.0 A and AA rules.</li>" +
      "<li><strong>Limits:</strong> automated tests find only some accessibility problems. Many criteria, like keyboard use, focus order and meaningful link text, need a person to check. This report is not a statement of compliance.</li>" +
      "<li><strong>AODA scope:</strong> the AODA applies to web content published after January 1, 2012, and some exceptions apply where meeting the requirement isn't practicable (O. Reg. 191/11, s. 14(5) and (6)).</li></ul></div>";

    root.innerHTML = h;

    if (opts.trackFixes) {
      root.querySelectorAll("input[data-rule]").forEach(function (cb) {
        cb.addEventListener("change", function () {
          var f = store(fixedKey) || {}; if (cb.checked) f[cb.getAttribute("data-rule")] = 1; else delete f[cb.getAttribute("data-rule")];
          store(fixedKey, f); var keep = cb.id; render(root, r, opts); var el = document.getElementById(keep); if (el) el.focus();
        });
      });
    }
  }
  window.SCReport = { render: render, esc: esc, sum: sum, fmtDate: fmtDate, store: store };
})();
