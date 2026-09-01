import os

with open('clean_app.py', 'r', encoding='utf-8') as f:
    py = f.read()

# Add static fallback directory creation in clean_app.py
old_dist_code = """os.makedirs('dist', exist_ok=True)
with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(html)"""

new_dist_code = """os.makedirs('dist', exist_ok=True)
with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Create static fallback directories for every route to ensure 0-fail 200 OK on Vercel
cat_slugs = ['mangalsutras', 'mens', 'earrings', 'rings', 'necklaces', 'bracelets', 'gifting', 'new-arrivals', 'best-seller', 'fine-silver', '9kt-fine-gold', 'all']
for slug in cat_slugs:
    cat_dir = os.path.join('category', slug)
    os.makedirs(cat_dir, exist_ok=True)
    with open(os.path.join(cat_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    
    dist_cat_dir = os.path.join('dist', 'category', slug)
    os.makedirs(dist_cat_dir, exist_ok=True)
    with open(os.path.join(dist_cat_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)"""

py = py.replace(old_dist_code, new_dist_code)

with open('clean_app.py', 'w', encoding='utf-8') as f:
    f.write(py)

print('Successfully added static category fallback directory creation in clean_app.py!')
