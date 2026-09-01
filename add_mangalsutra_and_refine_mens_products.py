import os, re, json

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add 2 Mangalsutra products to PRODUCTS array if not present
m_prods = """  {
    "id": "luxe-solitaire-diamond-18k-gold-mangalsutra",
    "name": "Luxe Solitaire Diamond 18K Gold Mangalsutra",
    "category": "Mangalsutras",
    "occasion": "Daily Wear",
    "price": 1299,
    "originalPrice": 2999,
    "discountPercent": 56,
    "rating": 4.9,
    "reviewCount": 184,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE-MANG-01",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_05_56PM.png?v=1758180696",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_05_56PM.png?v=1758180696",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_05_56PM.png?v=1758180696"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Black Bead Chain",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Skin Safe",
      "Lifetime Color Guarantee"
    ],
    "description": "Luxe Solitaire Diamond 18K Gold Mangalsutra - Traditional black bead chain with modern solitaire diamond pendant. 100% anti-tarnish demifine jewelry by CIELORIA.",
    "dimensions": "Length: 18 inches + 2 inch extension",
    "materials": "18K Gold Plated PVD Stainless Steel with Black Onyx Beads.",
    "care": "Waterproof and sweatproof. Clean with a dry soft cloth."
  },
  {
    "id": "royal-black-bead-18k-gold-mangalsutra",
    "name": "Royal Black Bead 18K Gold Mangalsutra",
    "category": "Mangalsutras",
    "occasion": "Festive",
    "price": 1499,
    "originalPrice": 3499,
    "discountPercent": 57,
    "rating": 4.8,
    "reviewCount": 96,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE-MANG-02",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292"
    ],
    "features": [
      "Traditional Royal Black Bead Design",
      "18K Gold Plated Anti-Tarnish Finish",
      "100% Waterproof & Sweatproof"
    ],
    "description": "Royal Black Bead 18K Gold Mangalsutra by CIELORIA. Elegant daily wear sacred jewelry.",
    "dimensions": "Length: 18 inches",
    "materials": "18K Gold Plated PVD Stainless Steel.",
    "care": "Waterproof. Wipe dry after bath/ocean water."
  },"""

# Insert Mangalsutras products at top of PRODUCTS array
js = js.replace('const PRODUCTS = [', 'const PRODUCTS = [\n' + m_prods)

# Update renderPLPView filtering logic for Mangalsutras and Mens
old_filter_logic = r'if \(state\.plpCategory === \'Mangalsutras\'\).*?if \(state\.plpCategory === \'Mens\'\).*?;'

new_filter_logic = """if (state.plpCategory === 'Mangalsutras') return p.category === 'Mangalsutras' || p.name.toLowerCase().includes('mangalsutra');
    if (state.plpCategory === 'Mens') return p.category === 'Mens' || p.id === 'traditional-engraved-gold-kada' || p.id === 'luxury-black-silicone-rose-gold-plated-crystal-bracelet' || p.name.toLowerCase().includes('kada') || (p.name.toLowerCase().includes('men') && !p.name.toLowerCase().includes('demifine'));"""

js = re.sub(old_filter_logic, new_filter_logic, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully added Mangalsutra products and fixed Mens filtering!')
