import os

google_favicon_tags = """  <!-- Google Search Engine Favicon Tags -->
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon.png" />
  <link rel="shortcut icon" href="/favicon.ico" />
  <link rel="apple-touch-icon" sizes="192x192" href="/apple-touch-icon.png" />"""

with open('clean_app.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re
# Clean old icon links from clean_app.py
code = re.sub(r'\s*<!-- CIELORIA Luxury Diamond Icon Favicon -->.*?(?=<link rel="preconnect")', '', code, flags=re.DOTALL)

target = '<meta name="google-site-verification" content="wl6j0pA_TmjRllzBhmc--7AGpBvcKpCBQ_eSetJd1-I" />'
replacement = target + '\n' + google_favicon_tags

code = code.replace(target, replacement)

with open('clean_app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully updated Google Search favicon tags in clean_app.py!')
