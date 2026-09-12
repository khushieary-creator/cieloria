import os, time

# Read cieloria_app.js
with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    full_js = f.read()

# Add defensive guard inside renderApp for blog_detail view
if "mainContent = renderBlogDetailView();" in full_js:
    safe_blog_render = """mainContent = (typeof renderBlogDetailView === 'function') ? renderBlogDetailView() : renderHomepageView();"""
    full_js = full_js.replace("mainContent = renderBlogDetailView();", safe_blog_render)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

os.makedirs('public', exist_ok=True)
with open('public/app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

os.makedirs('dist', exist_ok=True)
with open('dist/app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

with open('style.css', 'r', encoding='utf-8') as f:
    css_code = f.read()

timestamp = str(int(time.time()))

html_template = f"""<!DOCTYPE html>
<!-- BULLETPROOF_BLOG_BUILD_{timestamp}_v58000 -->
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
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
{css_code}
  </style>
</head>
<body class="bg-white text-[#1A1A1A] font-sans antialiased min-h-screen flex flex-col justify-between">
  
  <div id="app"></div>

  <script src="/app.js?v={timestamp}"></script>
  <script>
{full_js}

    function initializeCieloriaApp() {{
      try {{ if (typeof renderApp === 'function') renderApp(); }} catch (e) {{ console.error('Render Step 1 Error:', e); }}
      try {{ cleanTrackingUrl(); }} catch (e) {{}}
      try {{ syncStateFromUrl(); }} catch (e) {{}}
      try {{ syncAccountStorage(); }} catch (e) {{}}
      try {{ if (typeof renderApp === 'function') renderApp(); }} catch (e) {{ console.error('Render Step 3 Error:', e); }}
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

# Also create blog/ static directories so direct blog links never fail
blog_slugs = ['lab-grown-diamonds', 'womens-day-jewellery-guide', 'gold-vs-silver-jewellery']
for slug in blog_slugs:
    blog_dir = os.path.join('blog', slug)
    os.makedirs(blog_dir, exist_ok=True)
    with open(os.path.join(blog_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    dist_blog_dir = os.path.join('dist', 'blog', slug)
    os.makedirs(dist_blog_dir, exist_ok=True)
    with open(os.path.join(dist_blog_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_template)

print('Successfully deployed bulletproof blog rendering & fallback v58000.0.0!')
