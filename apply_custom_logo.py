import os

with open('logo_base64.txt', 'r') as f:
    b64_uri = f.read().strip()

header_logo_html = f"""<button onclick="switchViewMode('homepage')" class="flex items-center justify-center focus:outline-none transition-transform hover:scale-[1.02] py-1" title="CIELORIA Home">
              <img src="/cieloria_logo.jpg" onerror="this.onerror=null; this.src='{b64_uri}';" alt="CIELORIA" class="h-7 sm:h-9 lg:h-11 w-auto object-contain mix-blend-multiply" />
            </button>"""

footer_logo_html = f"""<div class="flex items-center justify-center sm:justify-start">
              <img src="/cieloria_logo.jpg" onerror="this.onerror=null; this.src='{b64_uri}';" alt="CIELORIA" class="h-8 sm:h-10 w-auto object-contain filter brightness-0 invert" />
            </div>"""

mobile_logo_html = f"""<img src="/cieloria_logo.jpg" onerror="this.onerror=null; this.src='{b64_uri}';" alt="CIELORIA" class="h-7 w-auto object-contain mix-blend-multiply" />"""

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace Header Logo
old_header_target = """<button onclick="switchViewMode('homepage')" class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold tracking-[0.18em] text-[#1A1A1A] hover:text-[#C5A059] uppercase">
              CIELORIA
            </button>"""

js = js.replace(old_header_target, header_logo_html)

# Replace Footer Logo
old_footer_target = """<h3 class="font-serif text-2xl font-bold tracking-[0.2em] text-white">CIELORIA</h3>"""

js = js.replace(old_footer_target, footer_logo_html)

# Replace Mobile Menu Logo
old_mobile_target = """<span class="font-serif text-2xl font-bold tracking-[0.15em] text-[#1A1A1A] uppercase">CIELORIA</span>"""

js = js.replace(old_mobile_target, mobile_logo_html)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully applied custom logo across Header, Footer, and Mobile Menu!')
