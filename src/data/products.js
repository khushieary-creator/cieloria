export const PRODUCTS = [
  {
    id: 'ring-101',
    name: 'Eternal Solitaire Pave Ring',
    category: 'Rings',
    price: 1999,
    originalPrice: 3999,
    discountPercent: 50,
    rating: 4.9,
    reviewCount: 342,
    metal: '18K Gold Plated',
    isBestseller: true,
    isNew: false,
    image: '/ring_1.jpg',
    features: [
      '18K Gold Plated Anti-Tarnish Coating',
      '100% Waterproof & Sweatproof',
      'Hypoallergenic & Nickel-Free',
      'Lifetime Polish Guarantee'
    ],
    description: 'A timeless solitaire ring featuring AAA+ grade cubic zirconia enveloped in a sparkling micro-pave band. Crafted with anti-tarnish 18K yellow gold plating for daily luxury wear without fading.'
  },
  {
    id: 'necklace-201',
    name: 'Lumière Layered Solitaire Pendant',
    category: 'Necklaces',
    price: 2499,
    originalPrice: 4999,
    discountPercent: 50,
    rating: 4.95,
    reviewCount: 518,
    metal: '18K Gold Plated',
    isBestseller: true,
    isNew: true,
    image: '/necklace_1.jpg',
    features: [
      'Dual Layer Chain with Floating Pendant',
      'Waterproof Anti-Tarnish Finish',
      'Adjustable 16" - 18" Length',
      'Free Luxury Gift Packaging'
    ],
    description: 'Effortlessly chic dual-layer pendant necklace handcrafted with 18k gold plating. Resistant to water, perfume, and sweat for worry-free everyday elegance.'
  },
  {
    id: 'hero-301',
    name: 'Aurore Royal Gemstone Drop Set',
    category: 'Earrings',
    price: 2999,
    originalPrice: 5999,
    discountPercent: 50,
    rating: 4.88,
    reviewCount: 219,
    metal: '18K Gold Plated',
    isBestseller: false,
    isNew: true,
    image: '/hero_banner.jpg',
    features: [
      'Royal Sapphire Blue Crystals',
      'Precision Cut Facets for Maximum Sparkle',
      'Anti-Tarnish Stainless Steel Base',
      'Lightweight Comfort Fit'
    ],
    description: 'Statement drop earrings adorned with vivid royal blue stones framed in brilliant 18k yellow gold polish.'
  },
  {
    id: 'bracelet-401',
    name: 'Eternity Crystal Tennis Bracelet',
    category: 'Bracelets',
    price: 2799,
    originalPrice: 5599,
    discountPercent: 50,
    rating: 4.92,
    reviewCount: 412,
    metal: 'Rose Gold',
    isBestseller: true,
    isNew: false,
    image: '/ring_1.jpg',
    features: [
      'Seamless Prong-Set Cubic Zirconia',
      'Secure Double-Latch Clasp',
      'Rose Gold Anti-Fade Plating',
      '100% Shower Safe'
    ],
    description: 'An iconic tennis bracelet designed with continuous radiant stones that capture light from every angle.'
  },
  {
    id: 'ring-102',
    name: 'Sovereign Twisted Gold Band',
    category: 'Rings',
    price: 1499,
    originalPrice: 2999,
    discountPercent: 50,
    rating: 4.85,
    reviewCount: 178,
    metal: '18K Gold Plated',
    isBestseller: false,
    isNew: false,
    image: '/necklace_1.jpg',
    features: [
      'Minimalist Sculpted Rope Texture',
      'Comfort-Fit Curved Interior',
      'Anti-Tarnish Guarantee',
      'Ideal for Stacking'
    ],
    description: 'A sleek twisted gold band perfect for layering or wearing as a subtle statement piece.'
  },
  {
    id: 'earring-501',
    name: 'Celestial Starburst Stud Earrings',
    category: 'Earrings',
    price: 1799,
    originalPrice: 3599,
    discountPercent: 50,
    rating: 4.9,
    reviewCount: 295,
    metal: 'Sterling Silver',
    isBestseller: true,
    isNew: true,
    image: '/ring_1.jpg',
    features: [
      'Rhodium Plated 925 Silver Look',
      'Micro-Pave Starburst Design',
      'Sensitive Ear Friendly',
      'Lifetime Color Guarantee'
    ],
    description: 'Radiant starburst studs with dazzling crystals that shine brightly in any lighting.'
  }
];

export const CATEGORIES = ['All', 'Rings', 'Necklaces', 'Earrings', 'Bracelets'];

export const PINCODES = {
  '400001': { location: 'Mumbai Central, MH', estDays: '2 Days (Express)', cod: true, shiprocketCourier: 'Delhivery Air' },
  '110001': { location: 'Connaught Place, New Delhi', estDays: '2 Days (Express)', cod: true, shiprocketCourier: 'Bluedart Express' },
  '560001': { location: 'MG Road, Bengaluru, KA', estDays: '3 Days', cod: true, shiprocketCourier: 'Xpressbees' },
  '700001': { location: 'Kolkata City, WB', estDays: '3 Days', cod: true, shiprocketCourier: 'Delhivery Surface' },
  '500001': { location: 'Hyderabad, TS', estDays: '2 Days (Express)', cod: true, shiprocketCourier: 'Shiprocket Direct' },
  '380001': { location: 'Ahmedabad, GJ', estDays: '2 Days', cod: true, shiprocketCourier: 'Delhivery Air' }
};
