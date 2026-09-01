import os, time

# 1. Update vercel.json with no-cache headers to bust Vercel Edge CDN cache permanently
vercel_config = """{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "no-cache, no-store, must-revalidate, max-age=0, s-maxage=0"
        },
        {
          "key": "Pragma",
          "value": "no-cache"
        },
        {
          "key": "Expires",
          "value": "0"
        }
      ]
    }
  ],
  "routes": [
    { "handle": "filesystem" },
    { "src": "/api/(.*)", "dest": "/api/$1" },
    { "src": "/(.*)", "dest": "/index.html" }
  ]
}
"""

with open('vercel.json', 'w', encoding='utf-8') as f:
    f.write(vercel_config)

# 2. Add unique build timestamp comment to index.html to force Vercel to change ETag
timestamp = str(int(time.time()))

with open('app.js', 'r', encoding='utf-8') as f:
    full_js = f.read()

with open('style.css', 'r', encoding='utf-8') as f:
    css_code = f.read()

html_template = f"""<!DOCTYPE html>
<!-- BUILD_ID_CACHE_BUSTER_{timestamp}_v47000 -->
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate, max-age=0, s-maxage=0">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
  <script>
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
      }}
    }}
  </script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>
  <style>
{css_code}
  </style>
</head>
<body class="bg-white text-[#1A1A1A] font-sans antialiased selection:bg-[#C5A059] selection:text-white min-h-screen flex flex-col justify-between">
  
  <div id="app"></div>

  <script>
{full_js}

    function initializeCieloriaApp() {{
      if (typeof renderApp === 'function') {{
        try {{
          cleanTrackingUrl();
          syncAccountStorage();
          syncStateFromUrl();
          renderApp();
        }} catch (e) {{
          console.error('Render App Execution Error:', e);
        }}
      }}
    }}

    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', initializeCieloriaApp);
    }} else {{
      initializeCieloriaApp();
    }}

    setTimeout(initializeCieloriaApp, 1);
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

os.makedirs('dist', exist_ok=True)
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

print('Successfully applied permanent Vercel Edge CDN cache buster with timestamp:', timestamp)
