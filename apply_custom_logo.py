import os

with open('logo_base64.txt', 'r') as f:
    b64_uri = f.read().strip()

header_logo_html = f"""<button onclick="switchViewMode('homepage')" class="flex items-center justify-center focus:outline-none transition-transform hover:scale-[1.02] py-1" title="CIELORIA Home">
              <img src="/cieloria_logo.jpg" onerror="this.onerror=null; this.src='{b64_uri}';" alt="CIELORIA" class="h-10 sm:h-14 lg:h-16 w-auto object-contain mix-blend-multiply my-1" />
            </button>"""

footer_logo_html = f"""<div class="flex items-center justify-center sm:justify-start">
              <img src="/cieloria_logo.jpg" onerror="this.onerror=null; this.src='{b64_uri}';" alt="CIELORIA" class="h-10 sm:h-14 w-auto object-contain filter brightness-0 invert my-1" />
            </div>"""

mobile_logo_html = f"""<img src="/cieloria_logo.jpg" onerror="this.onerror=null; this.src='{b64_uri}';" alt="CIELORIA" class="h-9 w-auto object-contain mix-blend-multiply" />"""

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re

# Replace existing img tag in header
js = re.sub(
    r'<button onclick="switchViewMode\(\'homepage\'\)" class="flex items-center justify-center.*?</button>',
    header_logo_html,
    js,
    flags=re.DOTALL
)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully applied large PALMONAS-style logo sizing to cieloria_app.js!')
