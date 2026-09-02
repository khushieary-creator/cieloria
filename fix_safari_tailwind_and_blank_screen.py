import os, time

with open('app.js', 'r', encoding='utf-8') as f:
    full_js = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css_code = f.read()

os.makedirs('public', exist_ok=True)
with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

os.makedirs('dist', exist_ok=True)
with open('dist/app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

timestamp = str(int(time.time()))

# Standard standalone fallback CSS rules so website works 100% even if CDN is blocked
standalone_css = """
/* Standalone Safari Fallback CSS */
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Inter', 'Montserrat', -apple-system, BlinkMacSystemFont, sans-serif; background-color: #ffffff; color: #1A1A1A; line-height: 1.5; webkit-font-smoothing: antialiased; }
#app { width: 100%; min-height: 100vh; display: flex; flex-direction: column; }
.hidden { display: none !important; }
@media (min-width: 1024px) { .lg\\:hidden { display: none !important; } .lg\\:flex { display: flex !important; } .lg\\:grid { display: grid !important; } }
@media (max-width: 1023px) { .hidden-mobile { display: none !important; } }
""" + css_code

html_template = f"""<!DOCTYPE html>
<!-- SAFARI_SAFEPATH_BUILD_{timestamp}_v50000 -->
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
{standalone_css}
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    try {{
      if (window.tailwind) {{
        tailwind.config = {{
          theme: {{
            extend: {{
              colors: {{
                nude: {{ 50: '#FAF8F5', 100: '#F7F4F0', 200: '#EBE5DF', 300: '#D9D0C7', 900: '#1A1A1A' }},
                champagne: {{ 300: '#F4E4BA', 400: '#E6CA65', 500: '#C5A059', 600: '#A38038' }}
              }},
              fontFamily: {{
                serif: ['"Cormorant Garamond"', '"Playfair Display"', 'serif'],
                sans: ['"Inter"', '"Montserrat"', 'sans-serif']
              }}
            }}
          }}
        }};
      }}
    }} catch(e) {{}}
  </script>
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

    // Safari & Mobile Chrome execution triggers
    if (document.readyState === 'complete' || document.readyState === 'interactive') {{
      initializeCieloriaApp();
    }} else {{
      document.addEventListener('DOMContentLoaded', initializeCieloriaApp);
      window.addEventListener('load', initializeCieloriaApp);
    }}

    setTimeout(initializeCieloriaApp, 0);
    setTimeout(initializeCieloriaApp, 50);
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

print('Successfully applied Safari Safe-Path Fix v50000.0.0!')
