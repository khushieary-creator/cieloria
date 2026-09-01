import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Copy hero_mangalsutras.jpg as mangalsutra_product.jpg and mangalsutra_product2.jpg
import shutil
shutil.copy('hero_mangalsutras.jpg', 'mangalsutra_product.jpg')
shutil.copy('hero_mangalsutras.jpg', 'public/mangalsutra_product.jpg')
shutil.copy('hero_mangalsutras.jpg', 'dist/mangalsutra_product.jpg')

# 2. Update CIRCLE_CATEGORIES to use bulletproof local high-res category images
old_circle = r'const CIRCLE_CATEGORIES = \[.*?\];'

new_circle = """const CIRCLE_CATEGORIES = [
  { name: "Earrings", cat: "Earrings", image: "/hero_earrings.jpg" },
  { name: "Necklaces", cat: "Necklaces", image: "/hero_necklaces.jpg" },
  { name: "Bracelets", cat: "Bracelets", image: "/hero_bracelets.jpg" },
  { name: "Rings", cat: "Rings", image: "/hero_rings.jpg" },
  { name: "Mangalsutras", cat: "Mangalsutras", image: "/hero_mangalsutras.jpg" },
  { name: "Mens", cat: "Mens", image: "/hero_mens.jpg" }
];"""

js = re.sub(old_circle, new_circle, js, flags=re.DOTALL)

# 3. Update Mangalsutra product images in PRODUCTS array
js = js.replace('"image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_05_56PM.png?v=1758180696",\n    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_05_56PM.png?v=1758180696",', '"image": "/mangalsutra_product.jpg",\n    "secondaryImage": "/hero_mangalsutras.jpg",')
js = js.replace('"image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",\n    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",', '"image": "/hero_mangalsutras.jpg",\n    "secondaryImage": "/mangalsutra_product.jpg",', 1)

# 4. Add universal image fallback to ALL circle category and product grid images
js = js.replace('<img src="${c.image}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />', '<img src="${c.image}" onerror="this.onerror=null; this.src=\'/hero_banner.jpg\';" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />')
js = js.replace('<img src="${p.image}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-out" />', '<img src="${p.image}" onerror="this.onerror=null; this.src=\'/hero_banner.jpg\';" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-out" />')

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated CIRCLE_CATEGORIES to use bulletproof local images and updated Mangalsutra product images!')
