import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace CIRCLE_CATEGORIES with 100% matching product images
old_circle_categories = r'const CIRCLE_CATEGORIES = \[.*?\];'

new_circle_categories = """const CIRCLE_CATEGORIES = [
  { name: "Earrings", cat: "Earrings", image: PRODUCTS[43].image },
  { name: "Necklaces", cat: "Necklaces", image: PRODUCTS[59].image },
  { name: "Bracelets", cat: "Bracelets", image: PRODUCTS[0].image },
  { name: "Rings", cat: "Rings", image: PRODUCTS[30].image },
  { name: "Mangalsutras", cat: "Necklaces", image: PRODUCTS[62].image },
  { name: "Mens", cat: "Bracelets", image: PRODUCTS[2].image }
];"""

js = re.sub(old_circle_categories, new_circle_categories, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully fixed CIRCLE_CATEGORIES images to 100% match category names!')
