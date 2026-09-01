import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update PLP_CATEGORY_DATA with sharp images & new Mangalsutras & Mens categories
old_plp_data = r'const PLP_CATEGORY_DATA = \{.*?\n\};'

new_plp_data = """const PLP_CATEGORY_DATA = {
  NewArrivals: {
    title: "New Arrivals",
    heading: "Fresh Luxury Additions",
    tagline: "Explore our latest 18K Gold Plated anti-tarnish releases",
    bannerImage: "/hero_banner.jpg",
    subFilters: ["All New", "Earrings", "Necklaces", "Bracelets", "Rings"]
  },
  BestSeller: {
    title: "Best Sellers",
    heading: "Most Loved Luxury Pieces",
    tagline: "Top-rated anti-tarnish jewelry chosen by thousands",
    bannerImage: "/hero_slide2.jpg",
    subFilters: ["All Best Sellers", "Statement Earrings", "Solitaire Rings", "Chic Bracelets"]
  },
  FineSilver: {
    title: "Fine Silver",
    heading: "Pure 925 Sterling Silver",
    tagline: "Certified 925 Sterling Silver with anti-tarnish rhodium finish",
    bannerImage: "/hero_slide3.jpg",
    subFilters: ["All Silver", "Silver Rings", "Silver Earrings", "Silver Pendants"]
  },
  NineKTGold: {
    title: "9KT Fine Gold",
    heading: "9KT Solid Gold Luxury",
    tagline: "Real 9KT solid gold & SGL certified lab-grown diamonds",
    bannerImage: "/hero_banner.jpg",
    subFilters: ["All 9KT Gold", "Diamond Studs", "Gold Bracelets", "Star Pendants", "Solitaire Rings"]
  },
  Earrings: {
    title: "Earrings",
    heading: "All Earrings",
    tagline: "Elegantly styled on her ear • 100% Anti-Tarnish & Hypoallergenic",
    bannerImage: "/hero_earrings.jpg",
    subFilters: ["All Earrings", "Stud Earrings", "Hoop Earrings", "Drop Earrings", "Danglers", "Earrings Set", "Pearl Earrings"]
  },
  Rings: {
    title: "Rings",
    heading: "All Rings",
    tagline: "Elegance on your fingertips • 18K Gold & Certified CZ Stones",
    bannerImage: "/hero_rings.jpg",
    subFilters: ["All Rings", "Solitaire Rings", "Band Rings", "Stackable Rings", "Adjustable Rings", "Cocktail Rings"]
  },
  Necklaces: {
    title: "Necklaces",
    heading: "All Necklaces",
    tagline: "Timeless chains and radiant 18K gold pendants",
    bannerImage: "/hero_necklaces.jpg",
    subFilters: ["All Necklaces", "Layered Necklaces", "Chokers", "Pendants", "Mangalsutras", "Statement Chains"]
  },
  Bracelets: {
    title: "Bracelets",
    heading: "All Bracelets",
    tagline: "Designed to move with your wrist • Waterproof & Sweatproof",
    bannerImage: "/hero_bracelets.jpg",
    subFilters: ["All Bracelets", "Kadas & Bangles", "Chain Bracelets", "Charm Bracelets", "Cuffs", "Men's Bracelets"]
  },
  Mangalsutras: {
    title: "Mangalsutras",
    heading: "Sacred & Modern Mangalsutras",
    tagline: "Timeless 18K Gold & Black Bead Sacred Keepsakes",
    bannerImage: "/hero_mangalsutras.jpg",
    subFilters: ["All Mangalsutras", "Solitaire Mangalsutras", "Modern Mangalsutras"]
  },
  Mens: {
    title: "Men's Collection",
    heading: "Men's Luxury Kadas & Bracelets",
    tagline: "Bold 18K Gold Plated & PVD Steel Jewelry For Men",
    bannerImage: "/hero_mens.jpg",
    subFilters: ["All Men's", "Gold Kadas", "Leather Bracelets", "Rings"]
  },
  Gifting: {
    title: "Gifting",
    heading: "Gifting & Curated Sets",
    tagline: "Thoughtful keepsake gifts made for every bond",
    bannerImage: "/gifting_her.jpg",
    subFilters: ["All Gifts", "Gift Boxes", "Sister Gifts", "Brother Gifts", "Sets"]
  },
  Wishlist: {
    title: "My Wishlist",
    heading: "Your Saved Favorites",
    tagline: "Your personal anti-tarnish wishlist collection",
    bannerImage: "/hero_banner.jpg",
    subFilters: ["All Saved Items"]
  },
  All: {
    title: "Demifine ® Collection",
    heading: "All Demifine Jewelry",
    tagline: "18k Thick Gold Plated & Waterproof Collection",
    bannerImage: "/hero_banner.jpg",
    subFilters: ["All Products", "Bestsellers", "New Arrivals", "9KT Solid Gold", "Fine Silver"]
  }
};"""

js = re.sub(old_plp_data, new_plp_data, js, flags=re.DOTALL)

# 2. Update renderPLPView filtering logic for Mangalsutras and Mens
old_filter_logic = r'if \(state\.plpCategory === \'Gifting\'\) return p\.category === \'Personalised\' \|\| p\.price > 1200;'

new_filter_logic = """if (state.plpCategory === 'Gifting') return p.category === 'Personalised' || p.price > 1200;
    if (state.plpCategory === 'Mangalsutras') return p.name.toLowerCase().includes('mangalsutra') || p.category === 'Mangalsutras' || p.description.toLowerCase().includes('mangalsutra');
    if (state.plpCategory === 'Mens') return p.name.toLowerCase().includes('kada') || p.name.toLowerCase().includes('men') || p.category === 'Mens' || p.sku === 'SKU: CIE102' || p.id === 'traditional-engraved-gold-kada';"""

js = re.sub(old_filter_logic, new_filter_logic, js)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully fixed PLP categories, sharp hero banners, and Mangalsutras/Mens product filter glitch!')
