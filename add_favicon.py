import os

with open('favicon_base64.txt', 'r') as f:
    b64_uri = f.read().strip()

favicon_tags = f"""  <!-- CIELORIA Luxury Diamond Icon Favicon -->
  <link rel="icon" type="image/jpeg" href="/favicon.jpg" />
  <link rel="icon" type="image/jpeg" href="{b64_uri}" />
  <link rel="shortcut icon" type="image/jpeg" href="/favicon.jpg" />
  <link rel="apple-touch-icon" href="/favicon.jpg" />
"""

# Update clean_app.py
with open('clean_app.py', 'r', encoding='utf-8') as f:
    code = f.read()

target = '<meta name="google-site-verification" content="wl6j0pA_TmjRllzBhmc--7AGpBvcKpCBQ_eSetJd1-I" />'
replacement = target + '\n' + favicon_tags

if 'link rel="icon"' not in code:
    code = code.replace(target, replacement)
    with open('clean_app.py', 'w', encoding='utf-8') as f:
        f.write(code)

print('Successfully added Favicon tags to clean_app.py!')
