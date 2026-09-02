import os, time

with open('app.js', 'r', encoding='utf-8') as f:
    full_js = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    custom_css = f.read()

os.makedirs('public', exist_ok=True)
with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

os.makedirs('dist', exist_ok=True)
with open('dist/app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

timestamp = str(int(time.time()))

# Complete Tailwind Utility Core CSS
tailwind_core_css = """
/* FULL TAILWIND UTILITY CORE FALLBACK FOR SAFARI & MOBILE */
*, ::before, ::after { box-sizing: border-box; border-width: 0; border-style: solid; border-color: #e5e7eb; }
html { line-height: 1.5; -webkit-text-size-adjust: 100%; -moz-tab-size: 4; tab-size: 4; font-family: 'Inter', 'Montserrat', system-ui, -apple-system, sans-serif; }
body { margin: 0; line-height: inherit; background-color: #ffffff; color: #1A1A1A; min-height: 100vh; display: flex; flex-direction: column; }
#app { width: 100%; min-height: 100vh; display: flex; flex-direction: column; flex: 1 1 0%; }

/* Layout & Flexbox */
.flex { display: flex !important; }
.inline-flex { display: inline-flex !important; }
.grid { display: grid !important; }
.block { display: block !important; }
.inline-block { display: inline-block !important; }
.hidden { display: none !important; }

.flex-col { flex-direction: column !important; }
.flex-row { flex-direction: row !important; }
.flex-wrap { flex-wrap: wrap !important; }
.flex-1 { flex: 1 1 0% !important; }
.shrink-0 { flex-shrink: 0 !important; }

.items-center { align-items: center !important; }
.items-start { align-items: flex-start !important; }
.items-end { align-items: flex-end !important; }
.justify-center { justify-content: center !important; }
.justify-between { justify-content: space-between !important; }
.justify-start { justify-content: flex-start !important; }
.justify-end { justify-content: flex-end !important; }

.gap-1 { gap: 0.25rem !important; }
.gap-2 { gap: 0.5rem !important; }
.gap-3 { gap: 0.75rem !important; }
.gap-4 { gap: 1rem !important; }
.gap-5 { gap: 1.25rem !important; }
.gap-6 { gap: 1.5rem !important; }
.gap-8 { gap: 2rem !important; }

/* Width & Height */
.w-full { width: 100% !important; }
.h-full { height: 100% !important; }
.w-screen { width: 100vw !important; }
.min-h-screen { min-height: 100vh !important; }
.max-w-7xl { max-width: 80rem !important; }
.max-w-xl { max-width: 36rem !important; }
.max-w-md { max-width: 28rem !important; }
.mx-auto { margin-left: auto !important; margin-right: auto !important; }

/* Spacing */
.p-1 { padding: 0.25rem !important; }
.p-2 { padding: 0.5rem !important; }
.p-3 { padding: 0.75rem !important; }
.p-4 { padding: 1rem !important; }
.p-6 { padding: 1.5rem !important; }
.p-8 { padding: 2rem !important; }

.px-2 { padding-left: 0.5rem !important; padding-right: 0.5rem !important; }
.px-3 { padding-left: 0.75rem !important; padding-right: 0.75rem !important; }
.px-4 { padding-left: 1rem !important; padding-right: 1rem !important; }
.px-6 { padding-left: 1.5rem !important; padding-right: 1.5rem !important; }

.py-1 { padding-top: 0.25rem !important; padding-bottom: 0.25rem !important; }
.py-2 { padding-top: 0.5rem !important; padding-bottom: 0.5rem !important; }
.py-3 { padding-top: 0.75rem !important; padding-bottom: 0.75rem !important; }
.py-4 { padding-top: 1rem !important; padding-bottom: 1rem !important; }

/* Colors & Backgrounds */
.bg-white { background-color: #ffffff !important; }
.bg-black { background-color: #000000 !important; }
.bg-[#FAF8F5] { background-color: #FAF8F5 !important; }
.bg-[#F3EFE6] { background-color: #F3EFE6 !important; }
.bg-[#EAE5D9] { background-color: #EAE5D9 !important; }
.bg-[#C5A059] { background-color: #C5A059 !important; }

.text-white { color: #ffffff !important; }
.text-black { color: #000000 !important; }
.text-[#1A1A1A] { color: #1A1A1A !important; }
.text-[#C5A059] { color: #C5A059 !important; }
.text-slate-400 { color: #94a3b8 !important; }
.text-slate-500 { color: #64748b !important; }
.text-amber-200 { color: #fde68a !important; }
.text-amber-500 { color: #f59e0b !important; }

/* Typography */
.font-sans { font-family: 'Inter', 'Montserrat', sans-serif !important; }
.font-serif { font-family: 'Cormorant Garamond', 'Playfair Display', serif !important; }
.font-bold { font-weight: 700 !important; }
.font-semibold { font-weight: 600 !important; }
.font-medium { font-weight: 500 !important; }
.font-light { font-weight: 300 !important; }

.text-xs { font-size: 0.75rem !important; line-height: 1rem !important; }
.text-sm { font-size: 0.875rem !important; line-height: 1.25rem !important; }
.text-base { font-size: 1rem !important; line-height: 1.5rem !important; }
.text-lg { font-size: 1.125rem !important; line-height: 1.75rem !important; }
.text-xl { font-size: 1.25rem !important; line-height: 1.75rem !important; }
.text-2xl { font-size: 1.5rem !important; line-height: 2rem !important; }
.text-3xl { font-size: 1.875rem !important; line-height: 2.25rem !important; }
.text-4xl { font-size: 2.25rem !important; line-height: 2.5rem !important; }
.text-5xl { font-size: 3rem !important; line-height: 1 !important; }

.uppercase { text-transform: uppercase !important; }
.tracking-wider { letter-spacing: 0.05em !important; }
.tracking-widest { letter-spacing: 0.1em !important; }
.text-center { text-align: center !important; }
.text-left { text-align: left !important; }

/* Positioning & Borders */
.relative { position: relative !important; }
.absolute { position: absolute !important; }
.sticky { position: sticky !important; }
.top-0 { top: 0 !important; }
.inset-0 { top: 0; right: 0; bottom: 0; left: 0; position: absolute !important; }
.z-10 { z-index: 10 !important; }
.z-20 { z-index: 20 !important; }
.z-40 { z-index: 40 !important; }
.z-50 { z-index: 50 !important; }

.border { border-width: 1px !important; }
.border-b { border-bottom-width: 1px !important; }
.border-t { border-top-width: 1px !important; }
.border-[#E6E1D7] { border-color: #E6E1D7 !important; }
.rounded-full { border-radius: 9999px !important; }
.rounded-xl { border-radius: 0.75rem !important; }
.rounded-2xl { border-radius: 1rem !important; }
.rounded-3xl { border-radius: 1.5rem !important; }

.object-cover { object-fit: cover !important; }
.object-contain { object-fit: contain !important; }
.overflow-hidden { overflow: hidden !important; }
.cursor-pointer { cursor: pointer !important; }

/* Responsive Media Queries */
@media (min-width: 640px) {
  .sm\\:flex { display: flex !important; }
  .sm\\:grid { display: grid !important; }
  .sm\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
  .sm\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; }
  .sm\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }
  .sm\\:px-6 { padding-left: 1.5rem !important; padding-right: 1.5rem !important; }
  .sm\\:text-3xl { font-size: 1.875rem !important; line-height: 2.25rem !important; }
  .sm\\:text-5xl { font-size: 3rem !important; line-height: 1 !important; }
}

@media (min-width: 1024px) {
  .lg\\:flex { display: flex !important; }
  .lg\\:hidden { display: none !important; }
  .lg\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }
  .lg\\:grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)) !important; }
  .lg\\:px-8 { padding-left: 2rem !important; padding-right: 2rem !important; }
  .lg\\:text-6xl { font-size: 3.75rem !important; line-height: 1 !important; }
}
""" + custom_css

html_template = f"""<!DOCTYPE html>
<!-- TAILWIND_EMBEDDED_BUILD_{timestamp}_v51000 -->
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate, max-age=0, s-maxage=0">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>CIELORIA | Demi-Fine Anti-Tarnish Luxury Jewelry</title>
  <meta name="description" content="Shop 100% waterproof, anti-tarnish 18K gold plated demi-fine jewelry at Cieloria. Warm Nude & Champagne Gold luxury collection.">
  <link rel="canonical" href="https://www.cieloria.com/" />
  <meta name="google-site-verification" content="wl6j0pA_TmjRllzBhmc--7AGpBvcKpCBQ_eSetJd1-I" />
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon.png" />
  <link rel="shortcut icon" href="/favicon.ico" />
  <link rel="apple-touch-icon" sizes="192x192" href="/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
{tailwind_core_css}
  </style>
  <script defer src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-white text-[#1A1A1A] font-sans antialiased selection:bg-[#C5A059] selection:text-white min-h-screen flex flex-col justify-between">
  
  <div id="app"></div>

  <script>
{full_js}

    function safeLaunchApp() {{
      try {{
        if (typeof renderApp === 'function') {{
          renderApp();
        }}
      }} catch(err) {{
        console.error('Safe Launch Error:', err);
      }}
    }}

    function initializeCieloriaApp() {{
      safeLaunchApp();
      try {{ cleanTrackingUrl(); }} catch (e) {{}}
      try {{ syncStateFromUrl(); }} catch (e) {{}}
      try {{ syncAccountStorage(); }} catch (e) {{}}
      safeLaunchApp();
    }}

    if (document.readyState === 'complete' || document.readyState === 'interactive') {{
      initializeCieloriaApp();
    }} else {{
      document.addEventListener('DOMContentLoaded', initializeCieloriaApp);
      window.addEventListener('load', initializeCieloriaApp);
    }}

    setTimeout(initializeCieloriaApp, 0);
    setTimeout(initializeCieloriaApp, 20);
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

cat_slugs = ['mangalsutras', 'mens', 'earrings', 'rings', 'necklaces', 'bracelets', 'gifting', 'new-arrivals', 'best-seller', 'fine-silver', '9kt-fine-gold', 'all']
for slug in cat_slugs:
    cat_dir = os.path.join('category', slug)
    os.makedirs(cat_dir, exist_ok=True)
    with open(os.path.join(cat_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    dist_cat_dir = os.path.join('dist', 'category', slug)
    os.makedirs(dist_cat_dir, exist_ok=True)
    with open(os.path.join(dist_cat_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_template)

print('Successfully embedded complete Tailwind core utility CSS v51000.0.0!')
