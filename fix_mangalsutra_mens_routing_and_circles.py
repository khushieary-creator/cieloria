import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update CIRCLE_CATEGORIES to have exact cat targets & high quality non-broken images
old_circle = r'const CIRCLE_CATEGORIES = \[.*?\];'

new_circle = """const CIRCLE_CATEGORIES = [
  { name: "Earrings", cat: "Earrings", image: PRODUCTS[45].image },
  { name: "Necklaces", cat: "Necklaces", image: PRODUCTS[61].image },
  { name: "Bracelets", cat: "Bracelets", image: PRODUCTS[2].image },
  { name: "Rings", cat: "Rings", image: PRODUCTS[32].image },
  { name: "Mangalsutras", cat: "Mangalsutras", image: PRODUCTS[0].image },
  { name: "Mens", cat: "Mens", image: PRODUCTS[3].image }
];"""

js = re.sub(old_circle, new_circle, js, flags=re.DOTALL)

# 2. Update topStylesProducts filter logic in homepage view
old_top_filter = r'const topStylesProducts = PRODUCTS\.filter\(p => \{\s*if \(selectedTabCategory === \'ALL\'\) return true;\s*return p\.category\.toUpperCase\(\) === selectedTabCategory\.toUpperCase\(\);\s*\}\);'

new_top_filter = """const topStylesProducts = PRODUCTS.filter(p => {
    if (selectedTabCategory === 'ALL') return true;
    if (selectedTabCategory === 'MANGALSUTRA') return p.category === 'Mangalsutras' || p.name.toLowerCase().includes('mangalsutra');
    if (selectedTabCategory === 'MENS') return p.category === 'Mens' || p.id === 'traditional-engraved-gold-kada' || p.id === 'luxury-black-silicone-rose-gold-plated-crystal-bracelet';
    return p.category.toUpperCase() === selectedTabCategory.toUpperCase();
  });"""

js = re.sub(old_top_filter, new_top_filter, js)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully fixed CIRCLE_CATEGORIES routing & TOP STYLES filtering!')
