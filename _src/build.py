#!/usr/bin/env python3
"""Builds the static SiteComply site. Run: python3 _src/build.py (from repo root)."""
import os, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://sitecomply.ca"
EMAIL = "matt@sitecomply.ca"
FORM_ACTION = f"https://formsubmit.co/ajax/{EMAIL}"
TODAY = datetime.date.today()
UPDATED = TODAY.strftime("%B %-d, %Y")

CHECK = '<svg class="check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
LOGO = '<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#2fc4a6"/><path d="M9 16.5l4.5 4.5L23 11.5" fill="none" stroke="#052a22" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def icon(path):
    return f'<div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg></div>'
I_SCALE = '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>'
I_PEOPLE = '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'
I_CLOCK = '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'
I_SEARCH = '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/><path d="M8 11h6"/>'
I_WRENCH = '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>'
I_PULSE = '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>'
I_CAP = '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>'
I_BOOK = '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>'
I_LIST = '<path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>'
I_LAYERS = '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>'
I_FILE = '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M9 15l2 2 4-4"/>'
I_MAPLE = '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>'
I_MAIL = '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>'
I_EYE = '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>'

NAV = [("Services","index.html#services","services"),("How it works","index.html#how","how"),("About","about.html","about"),("Resources","resources.html","resources"),("Contact","contact.html","contact")]

def header(active):
    items = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if k==active else ""}>{t}</a></li>' for t,h,k in NAV)
    return f'''<a class="skip" href="#main">Skip to main content</a>
<header class="site-header">
  <nav class="container nav" aria-label="Main">
    <a class="logo" href="index.html" aria-label="SiteComply home">{LOGO}<span>SiteComply</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links"><span class="sr-only">Menu</span><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <ul class="nav-links" id="nav-links">{items}<li class="nav-cta"><a class="btn btn-primary btn-sm" href="index.html#scan">Get a free scan</a></li></ul>
  </nav>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html">{LOGO}<span>SiteComply</span></a>
        <p>Accessibility compliance auditing, remediation and monitoring for Ontario municipalities and public sector organizations.</p>
        <p>Ontario-based · Canadian-owned<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div><h2>Services</h2><ul>
        <li><a href="index.html#services">Accessibility Audits</a></li>
        <li><a href="index.html#services">Remediation Support</a></li>
        <li><a href="index.html#services">Ongoing Monitoring</a></li>
        <li><a href="index.html#services">Staff Training</a></li></ul></div>
      <div><h2>Resources</h2><ul>
        <li><a href="aoda-guide.html">AODA Guide</a></li>
        <li><a href="wcag-overview.html">WCAG Overview</a></li>
        <li><a href="compliance-checklist.html">Compliance Checklist</a></li>
        <li><a href="resources.html">All resources</a></li></ul></div>
      <div><h2>Company</h2><ul>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
        <li><a href="accessibility.html">Accessibility Statement</a></li>
        <li><a href="privacy.html">Privacy Policy</a></li>
        <li><a href="terms.html">Terms of Use</a></li></ul></div>
    </div>
    <div class="foot-bottom">
      <p style="margin:0">© <span data-year>{TODAY.year}</span> SiteComply. All rights reserved. Serving Ontario municipalities and public sector organizations.</p>
      <div class="foot-tags" aria-label="Standards we audit against"><span>AODA</span><span>WCAG 2.0 AA</span><span>WCAG 2.1</span><span>WCAG 2.2</span></div>
    </div>
  </div>
</footer>
<script src="assets/main.js" defer></script>'''

def page(fname, title, desc, active, body, schema=""):
    canon = DOMAIN + ("/" if fname=="index.html" else "/"+fname)
    html = f'''<!doctype html>
<html lang="en-CA" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0b1624">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SiteComply">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{DOMAIN}/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
{schema}
</head>
<body>
{header(active)}
<main id="main" tabindex="-1">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    with open(os.path.join(ROOT, fname), "w") as f: f.write(html)

def scan_form(id_prefix="scan", heading="Request your free scan"):
    return f'''<form class="form" data-sc-form action="{FORM_ACTION}" method="POST" novalidate aria-labelledby="{id_prefix}-h" data-success="Thanks! Your free scan request is in. We'll email your results within one business day.">
  <h3 id="{id_prefix}-h">{heading}</h3>
  <p class="hint">Fields marked <span class="req" aria-hidden="true">*</span><span class="sr-only">with an asterisk</span> are required.</p>
  <input type="hidden" name="_subject" value="New free scan request: SiteComply">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="Request type" value="Free site scan">
  <div class="hp" aria-hidden="true"><label for="{id_prefix}-honey">Leave this empty</label><input id="{id_prefix}-honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
  <div class="row-2">
    <div class="field"><label for="{id_prefix}-name">Your name <span class="req" aria-hidden="true">*</span></label><input id="{id_prefix}-name" name="Name" type="text" autocomplete="name" placeholder="Jane Smith" required aria-describedby="{id_prefix}-name-err"><p class="err" id="{id_prefix}-name-err">Please enter your name.</p></div>
    <div class="field"><label for="{id_prefix}-org">Organization <span class="req" aria-hidden="true">*</span></label><input id="{id_prefix}-org" name="Organization" type="text" autocomplete="organization" placeholder="Town of Oakville" required aria-describedby="{id_prefix}-org-err"><p class="err" id="{id_prefix}-org-err">Please enter your organization.</p></div>
  </div>
  <div class="field"><label for="{id_prefix}-email">Work email <span class="req" aria-hidden="true">*</span></label><input id="{id_prefix}-email" name="email" type="email" autocomplete="email" placeholder="jane@oakville.ca" required aria-describedby="{id_prefix}-email-err"><p class="err" id="{id_prefix}-email-err">Please enter a valid email address.</p></div>
  <div class="field"><label for="{id_prefix}-url">Website URL <span class="req" aria-hidden="true">*</span></label><input id="{id_prefix}-url" name="Website" type="url" inputmode="url" autocomplete="url" placeholder="https://oakville.ca" required aria-describedby="{id_prefix}-url-err"><p class="err" id="{id_prefix}-url-err">Please enter your website address, for example https://oakville.ca.</p></div>
  <button class="btn btn-primary" type="submit">Request free scan</button>
  <div class="form-status" role="status" aria-live="polite" tabindex="-1"></div>
  <p class="form-note">No cost, no commitment. Results within one business day.</p>
</form>'''

# ---------------- HOME ----------------
_ic = lambda p: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+p+'</svg>'
bld = _ic('<path d="M3 21h18"/><path d="M5 21V8l7-5 7 5v13"/><path d="M9 21v-6h6v6"/>')
sch = _ic('<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>')
hos = _ic('<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M12 8v8M8 12h8"/>')
cap = _ic('<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>')
gov = _ic('<path d="M3 21h18"/><path d="M4 10h16"/><path d="M12 3 3 8h18z"/><path d="M6 10v8M10 10v8M14 10v8M18 10v8"/>')
weeks = [64,58,51,46,40,35,31]
W,H,P = 320,120,14
mx,mn = 70,20
pts = [(P + i*(W-2*P)/6, P + (mx-v)*(H-2*P)/(mx-mn)) for i,v in enumerate(weeks)]
line = " ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
area = f"M{pts[0][0]:.1f},{H-P} L" + " L".join(f"{x:.1f},{y:.1f}" for x,y in pts) + f" L{pts[-1][0]:.1f},{H-P} Z"
dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.5" class="c-dot" stroke-width="2"/>' for x,y in pts)
wk = "".join(f'<text x="{x:.1f}" y="{H+4}" text-anchor="middle" font-size="10" class="c-txt">W{i+1}</text>' for i,(x,y) in enumerate(pts))
chart = f'''<svg viewBox="0 0 {W} {H+10}" role="img" aria-labelledby="chart-t chart-d">
<title id="chart-t">Open issues over 7 weeks</title>
<desc id="chart-d">Open accessibility issues fell each week, from 64 in week 1 to 31 in week 7.</desc>
<defs><linearGradient id="g" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#2fc4a6" stop-opacity=".28"/><stop offset="1" stop-color="#2fc4a6" stop-opacity="0"/></linearGradient></defs>
<line class="c-axis" x1="{P}" x2="{W-P}" y1="{H-P}" y2="{H-P}"/>
<path d="{area}" fill="url(#g)"/>
<polyline class="c-line" points="{line}" fill="none" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
{dots}{wk}
<text x="{pts[0][0]+6:.1f}" y="{pts[0][1]-6:.1f}" font-size="11" font-weight="700" class="c-val">64</text>
<text x="{pts[-1][0]-4:.1f}" y="{pts[-1][1]-9:.1f}" text-anchor="end" font-size="11" font-weight="700" class="c-val end">31</text>
</svg>'''
issues = [("Missing alt text",14),("Low colour contrast",9),("Missing form labels",5),("PDF not tagged",3)]
issue_li = "".join(f'<li><span>{n}</span><b>{c}</b><span class="bar" aria-hidden="true"><i style="width:{c/14*100:.0f}%"></i></span></li>' for n,c in issues)

faq = [
 ("Does AODA apply to my municipality?", "Yes. All Ontario public sector organizations, including municipalities, school boards, hospitals, colleges and provincial agencies, must comply with the Integrated Accessibility Standards Regulation (IASR) under AODA. That includes meeting WCAG 2.0 Level AA on their public websites and web content."),
 ("What is WCAG and which version applies?", "WCAG (Web Content Accessibility Guidelines) is the international standard for web accessibility. Ontario's AODA currently mandates WCAG 2.0 Level AA. SiteComply also evaluates against WCAG 2.1 and 2.2, so your site is ready when the standard is updated and works better for everyone today."),
 ("How long does an audit take?", "A typical audit takes five to ten business days, depending on the size and complexity of your website. You receive a detailed report with prioritized findings and remediation guidance."),
 ("What does the free scan include?", "The free scan is an automated review of your homepage and key pages. It identifies common accessibility barriers and gives you a snapshot of your current compliance status, with no obligation."),
 ("Is an automated scan enough to be compliant?", "No. Automated tools reliably catch only a portion of WCAG issues. Our full audits combine automated scanning with manual testing using a keyboard and screen readers, which is how real residents experience your site."),
 ("Do you check PDFs and other documents?", "Yes. Documents posted on your website are web content under AODA. We review PDFs, Word files and forms for tagging, reading order, alternative text and contrast, and help your team fix or replace them."),
 ("Can you work with our existing web vendor or CMS?", "Yes. We work alongside your internal team or development partners on any platform, including eSolutions, Granicus (govAccess), WordPress, Drupal and custom builds. We provide code-level guidance and verify each fix."),
]
faq_html = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faq)
faq_schema = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join('{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (__import__("json").dumps(q), __import__("json").dumps(a)) for q,a in faq) + ']}</script>'
org_schema = '<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"SiteComply","url":"https://sitecomply.ca","email":"matt@sitecomply.ca","areaServed":{"@type":"State","name":"Ontario"},"description":"Accessibility compliance audits, remediation and monitoring for Ontario municipalities and public sector organizations."}</script>'

home = f'''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow"><span class="dot" aria-hidden="true"></span>Accessibility compliance for governments in Ontario</span>
      <h1>Make your website AODA compliant</h1>
      <p class="lede">SiteComply helps Ontario municipalities and public sector organizations meet their AODA obligations and WCAG standards, with audits, fixes and ongoing monitoring.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="#scan">Get a free site scan</a>
        <a class="btn btn-ghost" href="#how">See how it works</a>
      </div>
      <ul class="hero-meta">
        <li>{CHECK}AODA &amp; WCAG 2.0 AA</li>
        <li>{CHECK}Ontario-based &amp; Canadian-owned</li>
        <li>{CHECK}Free scan in 1 business day</li>
      </ul>
    </div>
    <figure class="report" aria-labelledby="report-cap">
      <div class="report-head">
        <span class="report-title" id="report-cap">Sample compliance report</span>
        <span class="badge">WCAG 2.0 AA · 2.1 · 2.2</span>
      </div>
      <div class="stats">
        <div class="stat"><b>142</b><span>Pages scanned</span></div>
        <div class="stat"><b>31</b><span>Open issues</span></div>
        <div class="stat good"><b>18</b><span>Fixed this month</span></div>
      </div>
      <p class="chart-label">Open issues over 7 weeks</p>
      <div class="chart">{chart}</div>
      <p class="chart-label">Open issues by type</p>
      <ul class="issues">{issue_li}</ul>
    </figure>
  </div>
</section>

<div class="trust">
  <div class="container trust-inner">
    <p>Built for Ontario municipalities and public sector organizations</p>
    <ul class="chips">
      <li>{bld}Municipalities</li><li>{sch}School boards</li><li>{hos}Hospitals</li><li>{cap}Colleges &amp; universities</li><li>{gov}Provincial agencies</li>
    </ul>
  </div>
</div>

<section class="section" aria-labelledby="why-h">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Why it matters</span>
      <h2 id="why-h">Why accessibility compliance matters for your municipality</h2>
      <p>Three reasons Ontario public sector organizations can't put this off.</p>
    </div>
    <div class="grid-3">
      <article class="card reveal">{icon(I_SCALE)}<h3>It's the law</h3><p>The Accessibility for Ontarians with Disabilities Act (AODA) requires all Ontario public sector organizations to meet WCAG 2.0 Level AA. Non-compliance can result in significant fines and reputational risk.</p></article>
      <article class="card reveal">{icon(I_PEOPLE)}<h3>It serves your community</h3><p>More than 2.6 million Ontarians live with a disability. An accessible website ensures every resident can access government services, information and programs without barriers.</p></article>
      <article class="card reveal">{icon(I_CLOCK)}<h3>The deadlines have passed</h3><p>The AODA deadline for public sector websites was January 1, 2021. If your site isn't compliant, you're already at risk. SiteComply helps you close the gap quickly and confidently.</p></article>
    </div>
  </div>
</section>

<section class="section alt" id="services" aria-labelledby="svc-h">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">Services</span>
      <h2 id="svc-h">What SiteComply does</h2>
      <p>End-to-end accessibility compliance services tailored to Ontario's public sector, from the first audit to ongoing monitoring.</p>
    </div>
    <div class="grid-2">
      <article class="card reveal"><div class="card-top">{icon(I_SEARCH).replace('class="icon"','class="icon"')}<span class="tag">Core</span></div><h3>Accessibility Audits</h3><p>A thorough review of your website against WCAG 2.0, 2.1 and 2.2 Level AA criteria. You get a prioritized report of issues with clear remediation guidance.</p>
        <ul><li>{CHECK}Automated and manual testing</li><li>{CHECK}Keyboard and screen reader checks</li><li>{CHECK}PDFs and documents included</li></ul></article>
      <article class="card reveal"><div class="card-top">{icon(I_WRENCH).replace('class="icon"','class="icon"')}<span class="tag">Core</span></div><h3>Remediation Support</h3><p>We work alongside your team or development partners to fix identified issues, with code-level guidance, QA review and sign-off on resolved items.</p>
        <ul><li>{CHECK}Works with any CMS or vendor</li><li>{CHECK}Fixes verified before sign-off</li><li>{CHECK}Documentation for your compliance report</li></ul></article>
      <article class="card reveal"><div class="card-top">{icon(I_PULSE).replace('class="icon"','class="icon"')}<span class="tag">Core</span></div><h3>Ongoing Monitoring</h3><p>Continuous automated scanning keeps your site compliant as content changes. Monthly reports flag new issues before they become compliance risks.</p>
        <ul><li>{CHECK}Monthly progress reports</li><li>{CHECK}Alerts on new issues</li><li>{CHECK}Trend tracking over time</li></ul></article>
      <article class="card reveal"><div class="card-top">{icon(I_CAP).replace('class="icon"','class="icon"')}<span class="tag addon">Add-on</span></div><h3>Staff Training</h3><p>Practical workshops for content editors, developers and communications staff on creating and maintaining accessible digital content in line with AODA requirements.</p>
        <ul><li>{CHECK}Role-specific sessions</li><li>{CHECK}Accessible documents and PDFs</li><li>{CHECK}Remote or on-site</li></ul></article>
    </div>
  </div>
</section>

<section class="section" id="how" aria-labelledby="how-h">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">How it works</span>
      <h2 id="how-h">Three steps to a compliant website</h2>
      <p>From your first free scan to a site that stays compliant.</p>
    </div>
    <ol class="steps">
      <li class="reveal"><h3>Request your free scan</h3><p>Submit your website URL and we'll run a preliminary accessibility scan within one business day. No commitment required.</p><span class="when">Day 1</span></li>
      <li class="reveal"><h3>Review your results</h3><p>We walk you through the findings, explain your compliance gaps and recommend a path forward tailored to your organization's needs and timeline.</p><span class="when">Week 1</span></li>
      <li class="reveal"><h3>Get compliant and stay compliant</h3><p>We support your team through remediation and provide ongoing monitoring so your site stays compliant as it evolves.</p><span class="when">Ongoing</span></li>
    </ol>
  </div>
</section>

<section class="section alt" id="faq" aria-labelledby="faq-h">
  <div class="container">
    <div class="section-head reveal">
      <span class="kicker">FAQ</span>
      <h2 id="faq-h">Frequently asked questions</h2>
      <p>Straight answers about AODA, WCAG and how we work.</p>
    </div>
    <div class="faq">{faq_html}</div>
  </div>
</section>

<section class="section" id="scan" aria-labelledby="scan-h">
  <div class="container">
    <div class="cta">
      <div>
        <span class="kicker">Free site scan</span>
        <h2 id="scan-h">Get your free site scan</h2>
        <p class="lede">Find out where your website stands against AODA and WCAG requirements. No cost, no commitment.</p>
        <ul>
          <li>{CHECK}Automated review of your homepage and key pages</li>
          <li>{CHECK}Snapshot of your current compliance status</li>
          <li>{CHECK}Plain-language summary of the top issues</li>
          <li>{CHECK}Results in your inbox within one business day</li>
        </ul>
        <p style="margin-top:24px">Prefer email? Write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      </div>
      {scan_form()}
    </div>
  </div>
</section>
'''
page("index.html", "SiteComply | AODA & WCAG Accessibility Compliance for Ontario", "SiteComply helps Ontario municipalities and public sector organizations meet AODA and WCAG 2.0 AA with accessibility audits, remediation and ongoing monitoring. Get a free site scan.", "home", home, faq_schema + "\n" + org_schema)

# ---------------- ABOUT ----------------
about = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / About</p>
  <h1>Accessible websites for every Ontarian</h1>
  <p>SiteComply is an Ontario-based, Canadian-owned accessibility firm. We help municipalities and public sector organizations meet their AODA obligations and build websites that work for every resident.</p>
</div></section>
<section class="section" style="padding-top:40px"><div class="container split">
  <div class="prose reveal">
    <h2 style="margin-top:0">Our mission</h2>
    <p>Public services are moving online, and residents depend on municipal websites to pay taxes, book programs, find council agendas and get emergency information. When those sites have barriers, people with disabilities are shut out of their own government.</p>
    <p>We exist to close that gap. We make compliance clear, practical and achievable for public sector teams, who are often working with tight budgets, legacy platforms and thousands of pages of content.</p>
    <h2>How we work</h2>
    <ul>
      <li><strong>Standards-based.</strong> Every finding is mapped to a specific WCAG success criterion and the related AODA requirement.</li>
      <li><strong>Human-tested.</strong> We pair automated scanning with manual testing using a keyboard and screen readers such as NVDA, JAWS and VoiceOver.</li>
      <li><strong>Prioritized.</strong> We rank issues by impact on residents and legal risk, so your team fixes what matters most first.</li>
      <li><strong>Collaborative.</strong> We work with your staff and vendors, not around them, and we leave your team more capable than we found it.</li>
    </ul>
  </div>
  <div class="grid-2">
    <div class="card reveal">{icon(I_MAPLE)}<h3>Canadian-owned</h3><p>Ontario-based, with data and reports handled in Canada.</p></div>
    <div class="card reveal">{icon(I_BOOK)}<h3>Public sector focus</h3><p>We know the IASR, council timelines and procurement.</p></div>
    <div class="card reveal">{icon(I_LAYERS)}<h3>WCAG 2.0 to 2.2</h3><p>Compliant today and ready for tomorrow's standard.</p></div>
    <div class="card reveal">{icon(I_EYE)}<h3>Lived experience</h3><p>Testing reflects how residents actually use your site.</p></div>
  </div>
</div></section>
<section class="section alt"><div class="container center">
  <h2>Ready to see where you stand?</h2>
  <p style="font-size:1.1rem;max-width:56ch;margin:0 auto 24px">Start with a free scan of your website. Results arrive in one business day.</p>
  <div class="btn-row"><a class="btn btn-primary" href="index.html#scan">Get a free site scan</a><a class="btn btn-ghost" href="contact.html">Contact us</a></div>
</div></section>
'''
page("about.html", "About SiteComply | Ontario Accessibility Compliance", "SiteComply is an Ontario-based, Canadian-owned accessibility firm helping municipalities and public sector organizations meet AODA and WCAG.", "about", about)

# ---------------- CONTACT ----------------
contact = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Contact</p>
  <h1>Talk to SiteComply</h1>
  <p>Questions about AODA, a request for proposal, or ready to start an audit? Send us a message and we'll reply within one business day.</p>
</div></section>
<section class="section" style="padding-top:32px"><div class="container split">
  <div class="stack">
    <div class="card">{icon(I_MAIL)}<h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
    <div class="card">{icon(I_CLOCK)}<h3>Response time</h3><p>Within one business day, Monday to Friday, Eastern Time.</p></div>
    <div class="card">{icon(I_MAPLE)}<h3>Service area</h3><p>Serving municipalities and public sector organizations across Ontario, remotely and on-site.</p></div>
  </div>
  <form class="form" data-sc-form action="{FORM_ACTION}" method="POST" novalidate aria-labelledby="contact-h" data-success="Thanks! Your message has been sent. We'll reply within one business day.">
    <h3 id="contact-h">Send us a message</h3>
    <p class="hint">Fields marked <span class="req" aria-hidden="true">*</span><span class="sr-only">with an asterisk</span> are required.</p>
    <input type="hidden" name="_subject" value="New contact message: SiteComply">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="Request type" value="Contact form">
    <div class="hp" aria-hidden="true"><label for="c-honey">Leave this empty</label><input id="c-honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
    <div class="row-2">
      <div class="field"><label for="c-name">Your name <span class="req" aria-hidden="true">*</span></label><input id="c-name" name="Name" type="text" autocomplete="name" required aria-describedby="c-name-err"><p class="err" id="c-name-err">Please enter your name.</p></div>
      <div class="field"><label for="c-org">Organization <span class="req" aria-hidden="true">*</span></label><input id="c-org" name="Organization" type="text" autocomplete="organization" required aria-describedby="c-org-err"><p class="err" id="c-org-err">Please enter your organization.</p></div>
    </div>
    <div class="row-2">
      <div class="field"><label for="c-email">Work email <span class="req" aria-hidden="true">*</span></label><input id="c-email" name="email" type="email" autocomplete="email" required aria-describedby="c-email-err"><p class="err" id="c-email-err">Please enter a valid email address.</p></div>
      <div class="field"><label for="c-phone">Phone</label><input id="c-phone" name="Phone" type="tel" autocomplete="tel"></div>
    </div>
    <div class="field"><label for="c-topic">What can we help with?</label>
      <select id="c-topic" name="Topic"><option>Accessibility audit</option><option>Remediation support</option><option>Ongoing monitoring</option><option>Staff training</option><option>Request for proposal (RFP)</option><option>Something else</option></select></div>
    <div class="field"><label for="c-msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="c-msg" name="Message" required aria-describedby="c-msg-err"></textarea><p class="err" id="c-msg-err">Please enter a message.</p></div>
    <button class="btn btn-primary" type="submit">Send message</button>
    <div class="form-status" role="status" aria-live="polite" tabindex="-1"></div>
  </form>
</div></section>
'''
page("contact.html", "Contact SiteComply | AODA Accessibility Help", f"Contact SiteComply about AODA and WCAG accessibility audits, remediation, monitoring and training. Email {EMAIL}.", "contact", contact)

# ---------------- RESOURCES ----------------
res = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Resources</p>
  <h1>Accessibility resources</h1>
  <p>Plain-language guides to help Ontario public sector teams understand their obligations and keep their websites accessible.</p>
</div></section>
<section class="section" style="padding-top:32px"><div class="container grid-3">
  <a class="card reveal" href="aoda-guide.html" style="text-decoration:none;color:inherit">{icon(I_BOOK)}<h3>AODA Guide</h3><p>Who AODA applies to, what the IASR requires for websites, and the key deadlines.</p><p class="more">Read the guide →</p></a>
  <a class="card reveal" href="wcag-overview.html" style="text-decoration:none;color:inherit">{icon(I_LAYERS)}<h3>WCAG Overview</h3><p>The four principles, conformance levels, and what changed in WCAG 2.1 and 2.2.</p><p class="more">Read the overview →</p></a>
  <a class="card reveal" href="compliance-checklist.html" style="text-decoration:none;color:inherit">{icon(I_LIST)}<h3>Compliance Checklist</h3><p>An interactive checklist your team can work through. Progress saves in your browser.</p><p class="more">Open the checklist →</p></a>
</div></section>
'''
page("resources.html", "Accessibility Resources | SiteComply", "Free AODA and WCAG resources for Ontario public sector teams: AODA guide, WCAG overview and an interactive compliance checklist.", "resources", res)

DISCLAIMER = '<div class="callout"><p><strong>Note:</strong> This guide is general information, not legal advice. Always confirm your obligations against the current text of the AODA and O. Reg. 191/11 on ontario.ca/laws.</p></div>'

aoda = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / AODA Guide</p>
  <h1>AODA website compliance guide</h1>
  <p>What the Accessibility for Ontarians with Disabilities Act requires of public sector websites, in plain language.</p>
</div></section>
<section class="section" style="padding-top:24px"><div class="container prose">
  <h2 style="margin-top:0">What is the AODA?</h2>
  <p>The Accessibility for Ontarians with Disabilities Act, 2005 (AODA) is Ontario's law for removing barriers for people with disabilities. Its stated goal was an accessible Ontario by 2025. Detailed requirements are set out in the Integrated Accessibility Standards Regulation (IASR), Ontario Regulation 191/11.</p>
  <h2>Who has to comply?</h2>
  <ul>
    <li><strong>The Government of Ontario and the Legislative Assembly.</strong></li>
    <li><strong>Designated public sector organizations.</strong> This includes every municipality, school board, college, university, hospital, public transportation organization and the provincial agencies named in the regulation.</li>
    <li><strong>Large organizations.</strong> Private and non-profit organizations with 50 or more employees in Ontario also have website obligations.</li>
  </ul>
  <h2>What the IASR requires for websites</h2>
  <p>Section 14 of the IASR requires designated public sector organizations to make their internet websites and web content conform with WCAG 2.0.</p>
  <div class="table-wrap"><table>
    <thead><tr><th scope="col">Deadline</th><th scope="col">Requirement for designated public sector organizations</th></tr></thead>
    <tbody>
      <tr><td>January 1, 2014</td><td>New internet websites and web content on those sites must conform with WCAG 2.0 Level A.</td></tr>
      <tr><td>January 1, 2021</td><td>All internet websites and web content must conform with WCAG 2.0 Level AA, except live captions (1.2.4) and pre-recorded audio description (1.2.5).</td></tr>
    </tbody>
  </table></div>
  <p>The requirement covers web content published after January 1, 2012. That includes documents such as PDFs posted on your website.</p>
  <h2>Related obligations</h2>
  <ul>
    <li><strong>Accessible formats and communication supports (section 12).</strong> Provide information in an accessible format when someone asks.</li>
    <li><strong>Accessible feedback (section 11).</strong> Your feedback processes, including web forms, must be accessible.</li>
    <li><strong>Training (section 7).</strong> Staff need training on accessibility standards and the Ontario Human Rights Code.</li>
    <li><strong>Multi-year accessibility plan (section 4).</strong> Publish a plan on your website, review it at least every five years, and post an annual status report.</li>
    <li><strong>Compliance reporting.</strong> Designated public sector organizations file accessibility compliance reports with the province on a regular schedule.</li>
  </ul>
  <h2>What happens if you don't comply?</h2>
  <p>The province can inspect organizations and issue compliance orders. The Act allows fines of up to $100,000 per day for corporations, and up to $50,000 per day for individuals and directors. For a municipality, the reputational cost of shutting residents out of services can be just as serious.</p>
  <h2>Where to start</h2>
  <ol>
    <li>Run a <a href="index.html#scan">free scan</a> to get a baseline.</li>
    <li>Commission a full audit covering templates, key journeys and documents.</li>
    <li>Fix the highest-impact issues first, starting with templates that affect every page.</li>
    <li>Train content editors so new content stays accessible.</li>
    <li>Monitor monthly and record progress for your compliance report.</li>
  </ol>
  {DISCLAIMER}
</div></section>
'''
page("aoda-guide.html", "AODA Website Compliance Guide | SiteComply", "A plain-language guide to AODA and IASR website requirements for Ontario municipalities and public sector organizations, including WCAG 2.0 AA deadlines.", "resources", aoda)

wcag = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / WCAG Overview</p>
  <h1>WCAG overview</h1>
  <p>The Web Content Accessibility Guidelines explained: the principles, the levels, and what changed between versions.</p>
</div></section>
<section class="section" style="padding-top:24px"><div class="container prose">
  <h2 style="margin-top:0">What is WCAG?</h2>
  <p>WCAG is the international standard for web accessibility, published by the World Wide Web Consortium (W3C). It is made up of testable success criteria. Ontario's AODA references WCAG 2.0, and many governments worldwide use the same standard.</p>
  <h2>The four principles: POUR</h2>
  <ul>
    <li><strong>Perceivable.</strong> People can see or hear the content. Images have alt text, videos have captions, and text has enough contrast.</li>
    <li><strong>Operable.</strong> Everything works with a keyboard, users have enough time, and nothing flashes in a way that can cause seizures.</li>
    <li><strong>Understandable.</strong> Content is readable, pages behave predictably, and forms help people avoid and fix mistakes.</li>
    <li><strong>Robust.</strong> Code works reliably with assistive technologies such as screen readers.</li>
  </ul>
  <h2>Conformance levels</h2>
  <div class="table-wrap"><table>
    <thead><tr><th scope="col">Level</th><th scope="col">What it means</th></tr></thead>
    <tbody>
      <tr><td>A</td><td>The minimum. Removes the most severe barriers.</td></tr>
      <tr><td>AA</td><td>The legal standard in Ontario and most jurisdictions. Includes everything in Level A.</td></tr>
      <tr><td>AAA</td><td>The highest level. Not required as a whole for entire sites.</td></tr>
    </tbody>
  </table></div>
  <h2>WCAG versions</h2>
  <div class="table-wrap"><table>
    <thead><tr><th scope="col">Version</th><th scope="col">Published</th><th scope="col">Highlights</th></tr></thead>
    <tbody>
      <tr><td>WCAG 2.0</td><td>2008</td><td>The version required by AODA.</td></tr>
      <tr><td>WCAG 2.1</td><td>2018</td><td>Adds criteria for mobile, low vision and cognitive accessibility.</td></tr>
      <tr><td>WCAG 2.2</td><td>2023</td><td>Adds criteria for focus visibility, touch targets and accessible sign-in.</td></tr>
    </tbody>
  </table></div>
  <p>Each version builds on the one before, so a site that meets WCAG 2.2 AA also meets 2.1 AA and 2.0 AA. The one exception is that 2.2 retired criterion 4.1.1 Parsing.</p>
  <h3>Key additions in WCAG 2.1 (Level AA)</h3>
  <ul>
    <li><strong>Reflow (1.4.10).</strong> Content works at 400% zoom without scrolling in two directions.</li>
    <li><strong>Non-text contrast (1.4.11).</strong> Buttons, form borders and icons need 3:1 contrast.</li>
    <li><strong>Text spacing (1.4.12).</strong> Content survives users increasing line and letter spacing.</li>
    <li><strong>Content on hover or focus (1.4.13).</strong> Tooltips and pop-ups can be dismissed and don't vanish unexpectedly.</li>
    <li><strong>Orientation (1.3.4)</strong> and <strong>identify input purpose (1.3.5).</strong> Pages work in portrait and landscape, and personal-data fields support autofill.</li>
    <li><strong>Status messages (4.1.3).</strong> Screen readers announce messages such as "Form submitted".</li>
  </ul>
  <h3>Key additions in WCAG 2.2 (Level AA)</h3>
  <ul>
    <li><strong>Focus not obscured (2.4.11).</strong> Sticky headers and banners can't hide the focused element.</li>
    <li><strong>Dragging movements (2.5.7).</strong> Anything done by dragging can also be done with a single click or tap.</li>
    <li><strong>Target size (2.5.8).</strong> Clickable targets are at least 24 by 24 CSS pixels, or well spaced.</li>
    <li><strong>Consistent help (3.2.6).</strong> Help options appear in the same place across pages.</li>
    <li><strong>Redundant entry (3.3.7).</strong> Users aren't asked to re-enter information they already gave.</li>
    <li><strong>Accessible authentication (3.3.8).</strong> Sign-in doesn't rely on memory or puzzle tests alone.</li>
  </ul>
  <div class="callout"><p>SiteComply audits against WCAG 2.0 AA for AODA compliance and reports 2.1 and 2.2 findings separately, so you can plan ahead without confusing legal requirements with best practice.</p></div>
</div></section>
'''
page("wcag-overview.html", "WCAG Overview: 2.0, 2.1 and 2.2 Explained | SiteComply", "A plain-language overview of WCAG accessibility guidelines: POUR principles, A/AA/AAA levels, and what's new in WCAG 2.1 and 2.2.", "resources", wcag)

groups = [
 ("Governance", ["A multi-year accessibility plan is published on your website","An accessibility statement explains how to report barriers and request alternate formats","Staff who publish content have received accessibility training","A process exists to respond to accessible format requests"]),
 ("Structure & navigation", ["Every page has a unique, descriptive title","Headings follow a logical order (one H1, then H2, H3)","A skip-to-content link is the first focusable item","All functionality works with a keyboard alone","The keyboard focus indicator is always clearly visible","Link text makes sense out of context (no \"click here\")"]),
 ("Visual design", ["Body text has at least 4.5:1 contrast with its background","Large text and UI components have at least 3:1 contrast","Colour is never the only way information is conveyed","Pages work at 200% zoom and reflow at 400% without horizontal scrolling"]),
 ("Images & media", ["Informative images have meaningful alt text","Decorative images have empty alt text","Pre-recorded videos have accurate captions","Audio-only content has a transcript","Nothing auto-plays for more than 5 seconds without a pause control"]),
 ("Forms", ["Every form field has a visible, programmatic label","Required fields are clearly indicated","Error messages explain what went wrong and how to fix it","Success and error messages are announced to screen readers"]),
 ("Documents", ["PDFs are tagged with a correct reading order","Documents have titles, headings and alt text","Scanned image-only PDFs are replaced with accessible versions","An accessible alternative is offered for complex documents such as maps"]),
 ("Testing", ["Key pages have been tested with a screen reader (NVDA, JAWS or VoiceOver)","Automated scans run regularly and new issues are tracked","Third-party tools (payments, bookings, maps) have been checked for accessibility"]),
]
cl = ""; n = 0
for g, items in groups:
    cl += f"<h2>{g}</h2><ul class=\"checklist\">"
    for it in items:
        n += 1
        cl += f'<li><input type="checkbox" id="c{n}"><label for="c{n}">{it}</label></li>'
    cl += "</ul>"
checklist = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / <a href="resources.html">Resources</a> / Compliance Checklist</p>
  <h1>Website accessibility compliance checklist</h1>
  <p>A practical checklist for Ontario public sector websites, based on AODA and WCAG 2.0 AA with selected 2.1 and 2.2 best practices. Tick items off as you go. Your progress is saved in this browser.</p>
</div></section>
<section class="section" style="padding-top:24px"><div class="container prose" data-checklist>
  <div class="progress" aria-live="polite"><strong data-progress-text>0 complete</strong><div class="progress-bar" aria-hidden="true"><i data-progress-bar></i></div></div>
  <p class="btn-row"><button class="btn btn-ghost btn-sm" type="button" data-print>Print checklist</button><button class="btn btn-ghost btn-sm" type="button" data-checklist-reset>Reset progress</button></p>
  {cl}
  <div class="callout"><p><strong>A checklist is a starting point.</strong> Many WCAG criteria need expert manual testing to verify. <a href="index.html#scan">Request a free scan</a> to see how your site measures up.</p></div>
</div></section>
'''
page("compliance-checklist.html", "Website Accessibility Compliance Checklist | SiteComply", "An interactive AODA and WCAG accessibility checklist for Ontario municipalities and public sector websites.", "resources", checklist)

# ---------------- LEGAL ----------------
a11y = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Accessibility Statement</p>
  <h1>Accessibility statement</h1>
  <p class="updated">Last updated {UPDATED}</p>
</div></section>
<section class="section" style="padding-top:24px"><div class="container prose">
  <h2 style="margin-top:0">Our commitment</h2>
  <p>SiteComply is committed to making this website accessible to everyone, including people with disabilities. We aim to conform with WCAG 2.2 Level AA, which exceeds the WCAG 2.0 Level AA standard required under AODA.</p>
  <h2>What we've done</h2>
  <ul>
    <li>Semantic HTML with a logical heading structure and landmarks</li>
    <li>A skip-to-content link and full keyboard support</li>
    <li>A clearly visible focus indicator on every interactive element</li>
    <li>Colour contrast that meets or exceeds AA ratios</li>
    <li>Labelled form fields with clear, announced error and success messages</li>
    <li>Layouts that reflow on small screens and at high zoom levels</li>
    <li>Respect for your device's reduced-motion setting</li>
  </ul>
  <h2>Feedback and alternate formats</h2>
  <p>If you encounter a barrier on this website, or need any content in an alternate format, please email <a href="mailto:{EMAIL}">{EMAIL}</a>. We will respond within two business days and provide accessible formats or communication supports at no cost.</p>
  <h2>Known limitations</h2>
  <p>We test this site regularly. If we find an issue we can't fix right away, we will list it here with a planned resolution date.</p>
</div></section>
'''
page("accessibility.html", "Accessibility Statement | SiteComply", "SiteComply's commitment to an accessible website, how to report barriers, and how to request alternate formats.", "", a11y)

privacy = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Privacy Policy</p>
  <h1>Privacy policy</h1>
  <p class="updated">Last updated {UPDATED}</p>
</div></section>
<section class="section" style="padding-top:24px"><div class="container prose">
  <p style="margin-top:0">SiteComply respects your privacy. This policy explains what information we collect through this website and how we use it, consistent with Canada's Personal Information Protection and Electronic Documents Act (PIPEDA).</p>
  <h2>What we collect</h2>
  <p>We only collect information you choose to give us through our forms: your name, organization, work email, website address, and optionally your phone number and message.</p>
  <h2>How we use it</h2>
  <ul>
    <li>To run the free scan you requested and send you the results</li>
    <li>To respond to your questions and provide services you ask for</li>
  </ul>
  <p>We do not sell, rent or trade your information. We do not add you to a mailing list without your consent.</p>
  <h2>Cookies and analytics</h2>
  <p>This website does not use advertising cookies or tracking analytics. The compliance checklist saves your progress in your own browser's local storage. That information never leaves your device.</p>
  <h2>Service providers</h2>
  <p>Form submissions are delivered to our inbox through FormSubmit, a form-processing service. Our website is hosted on GitHub Pages and fonts are served by Google Fonts. These providers may process technical data such as your IP address to deliver their services.</p>
  <h2>Retention and your rights</h2>
  <p>We keep your information only as long as needed for the purpose you provided it. You can ask to see, correct or delete your information at any time by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>Contact</h2>
  <p>Questions about this policy? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>
'''
page("privacy.html", "Privacy Policy | SiteComply", "How SiteComply collects, uses and protects information submitted through sitecomply.ca.", "", privacy)

terms = f'''
<section class="page-hero"><div class="container">
  <p class="crumbs"><a href="index.html">Home</a> / Terms of Use</p>
  <h1>Terms of use</h1>
  <p class="updated">Last updated {UPDATED}</p>
</div></section>
<section class="section" style="padding-top:24px"><div class="container prose">
  <p style="margin-top:0">By using sitecomply.ca you agree to these terms.</p>
  <h2>Information only</h2>
  <p>The guides, checklists and other content on this website are general information. They are not legal advice. Confirm your specific obligations with the current legislation or a qualified advisor.</p>
  <h2>Free scans</h2>
  <p>The free scan is an automated, preliminary review. It does not identify every accessibility issue and does not certify compliance with AODA or WCAG. Only request a scan of a website you are authorized to act for.</p>
  <h2>Intellectual property</h2>
  <p>Content on this website belongs to SiteComply unless otherwise noted. You may share and print our resources for internal, non-commercial use with attribution.</p>
  <h2>Limitation of liability</h2>
  <p>This website is provided "as is". To the extent permitted by law, SiteComply is not liable for any loss arising from your use of this website or reliance on its content.</p>
  <h2>Governing law</h2>
  <p>These terms are governed by the laws of the Province of Ontario and the federal laws of Canada that apply there.</p>
  <h2>Contact</h2>
  <p>Questions? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div></section>
'''
page("terms.html", "Terms of Use | SiteComply", "Terms of use for the SiteComply website and free accessibility scan.", "", terms)

nf = '''
<section class="page-hero" style="padding:120px 0"><div class="container" style="text-align:center">
  <p class="kicker">Error 404</p>
  <h1>We couldn't find that page</h1>
  <p style="margin:0 auto 28px">The page may have moved. Try the homepage or our resources.</p>
  <div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="/">Go to homepage</a><a class="btn btn-ghost" href="/resources.html">Browse resources</a></div>
</div></section>
'''
page("404.html", "Page not found | SiteComply", "The page you were looking for could not be found.", "", nf.replace('href="index.html', 'href="/index.html'))
# 404 is served from any path, so make its asset links absolute
p = os.path.join(ROOT,"404.html"); s = open(p).read()
s = s.replace('href="assets/','href="/assets/').replace('src="assets/','src="/assets/').replace('href="index.html','href="/index.html').replace('href="about.html','href="/about.html').replace('href="resources.html','href="/resources.html').replace('href="contact.html','href="/contact.html').replace('href="aoda-guide.html','href="/aoda-guide.html').replace('href="wcag-overview.html','href="/wcag-overview.html').replace('href="compliance-checklist.html','href="/compliance-checklist.html').replace('href="accessibility.html','href="/accessibility.html').replace('href="privacy.html','href="/privacy.html').replace('href="terms.html','href="/terms.html')
open(p,"w").write(s)

pages = ["","about.html","contact.html","resources.html","aoda-guide.html","wcag-overview.html","compliance-checklist.html","accessibility.html","privacy.html","terms.html"]
open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}/{p}</loc><lastmod>{TODAY.isoformat()}</lastmod></url>\n" for p in pages) + "</urlset>\n")
open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
open(os.path.join(ROOT,"CNAME"),"w").write("sitecomply.ca\n")
print("built", len(pages)+1, "pages")
