import os, re

# 1. Update clean_app.py to add Canonical Tag
with open('clean_app.py', 'r', encoding='utf-8') as f:
    clean_code = f.read()

canonical_tag = '  <link rel="canonical" href="https://www.cieloria.com/" />\n'
target = '<meta name="google-site-verification" content="wl6j0pA_TmjRllzBhmc--7AGpBvcKpCBQ_eSetJd1-I" />'

if 'rel="canonical"' not in clean_code:
    clean_code = clean_code.replace(target, canonical_tag + target)
    with open('clean_app.py', 'w', encoding='utf-8') as f:
        f.write(clean_code)

# 2. Add URL cleaner function to cieloria_app.js
clean_url_fn = """
function cleanTrackingUrl() {
  try {
    if (window.location.search && window.location.search.includes('srsltid=')) {
      const url = new URL(window.location.href);
      url.searchParams.delete('srsltid');
      const cleanPath = url.pathname + (url.searchParams.toString() ? '?' + url.searchParams.toString() : '') + url.hash;
      window.history.replaceState({}, document.title, cleanPath);
    }
  } catch (e) {}
}
"""

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    app_js = f.read()

if 'cleanTrackingUrl' not in app_js:
    app_js = clean_url_fn + '\n' + app_js
    app_js = app_js.replace("syncAccountStorage();", "cleanTrackingUrl();\n  syncAccountStorage();")
    with open('cieloria_app.js', 'w', encoding='utf-8') as f:
        f.write(app_js)

print('Successfully added Canonical tag & cleanTrackingUrl function!')
