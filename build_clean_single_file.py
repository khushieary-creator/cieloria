import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css_code = f.read()

os.makedirs('public', exist_ok=True)
with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

os.makedirs('dist', exist_ok=True)
with open('dist/app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js_code)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>CIELORIA | Demi-Fine Anti-Tarnish Luxury Jewelry</title>
  <meta name="description" content="Shop 100% waterproof, anti-tarnish 18K gold plated demi-fine jewelry at Cieloria.">
  <link rel="canonical" href="https://www.cieloria.com/" />
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png" />
  <link rel="icon" type="image/png" sizes="192x192" href="/favicon.png" />
  <link rel="shortcut icon" href="/favicon.ico" />
  <link rel="apple-touch-icon" sizes="192x192" href="/apple-touch-icon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
""" + css_code + """
  </style>
</head>
<body class="bg-white text-[#1A1A1A] font-sans antialiased min-h-screen">
  
  <div id="app"></div>

  <script src="/app.js"></script>
  <script>
    function runCieloriaApp() {
      if (typeof renderApp === 'function') {
        try { cleanTrackingUrl(); } catch(e) {}
        try { syncStateFromUrl(); } catch(e) {}
        try { syncAccountStorage(); } catch(e) {}
        try { renderApp(); } catch(e) { console.error(e); }
      }
    }

    if (document.readyState === 'complete' || document.readyState === 'interactive') {
      runCieloriaApp();
    } else {
      document.addEventListener('DOMContentLoaded', runCieloriaApp);
      window.addEventListener('load', runCieloriaApp);
    }
    setTimeout(runCieloriaApp, 10);
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

cat_slugs = ['mangalsutras', 'mens', 'earrings', 'rings', 'necklaces', 'bracelets', 'gifting', 'new-arrivals', 'best-seller', 'fine-silver', '9kt-fine-gold', 'all']
for slug in cat_slugs:
    cat_dir = os.path.join('category', slug)
    os.makedirs(cat_dir, exist_ok=True)
    with open(os.path.join(cat_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    dist_cat_dir = os.path.join('dist', 'category', slug)
    os.makedirs(dist_cat_dir, exist_ok=True)
    with open(os.path.join(dist_cat_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)

print('Successfully created clean index.html with external app.js link v52000.0.0!')
