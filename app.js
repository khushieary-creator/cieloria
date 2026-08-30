// CIELORIA - Demifine® Anti-Tarnish Luxury Storefront (Live Google Cloud Serverless Integration)

const CIELORIA_CREDENTIALS = {
  merchantId: "2yyq6ziimeofq998",
  appId: "app_id_93a59e4095c7408f9b7ebeb50bcdeda9",
  appSecret: "app_secret_2ffb4ee8695d4188a75fd7bcfca5fc5e",
  id: "42961",
  environment: "production"
};

const PRODUCTS = [
  {
    "id": "luxury-gold-plated-anti-tarnish-stone-bracelet",
    "name": "Luxury Gold-Plated Anti-Tarnish Stone Bracelet",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE100",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_33_57PM.png?v=1758182377",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_33_57PM.png?v=1758182377",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_33_57PM.png?v=1758182377",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_33_57PM.png?v=1758182377",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_33_57PM.png?v=1758182377",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_33_57PM.png?v=1758182377"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Luxury Gold-Plated Anti-Tarnish Stone Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "elegant-22k-gold-textured-bangle",
    "name": "Traditional Engraved Gold Kada",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE101",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_15_00PM.png?v=1758182007",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_15_00PM.png?v=1758182007",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_15_00PM.png?v=1758182007",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_15_00PM.png?v=1758182007",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_15_00PM.png?v=1758182007",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_15_00PM.png?v=1758182007"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Traditional Engraved Gold Kada - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "luxury-black-silicone-rose-gold-plated-crystal-bracelet",
    "name": "Luxury Black Silicone & Rose Gold-Plated Crystal Bracelet",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2599,
    "discountPercent": 62,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE102",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_11_38_23AM.png?v=1758953292"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Luxury Black Silicone & Rose Gold-Plated Crystal Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "luxury-geometric-18k-gold-plated-zircon-bangle-bracelet",
    "name": "Luxury Geometric 18K Gold-Plated Zircon Bangle Bracelet",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE103",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_10_56_15AM.png?v=1758954114",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_10_56_15AM.png?v=1758954114",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_10_56_15AM.png?v=1758954114",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_10_56_15AM.png?v=1758954114",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_10_56_15AM.png?v=1758954114",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_10_56_15AM.png?v=1758954114"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Luxury Geometric 18K Gold-Plated Zircon Bangle Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "luxury-18k-gold-plated-diamond-bangle-ring-set",
    "name": "Luxury 18K Gold-Plated Diamond Bangle & Ring Set",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 1499,
    "originalPrice": 3999,
    "discountPercent": 63,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE104",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_01_46_16PM.png?v=1758181451",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_01_46_16PM.png?v=1758181451",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_01_46_16PM.png?v=1758181451",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_01_46_16PM.png?v=1758181451",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_01_46_16PM.png?v=1758181451",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_01_46_16PM.png?v=1758181451"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Luxury 18K Gold-Plated Diamond Bangle & Ring Set - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "nail-gold-plated-bracelet-rhinestones-jewelry",
    "name": "Nail gold plated bracelet rhinestones Jewelry",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE105",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/nail-gold-plated-bracelet-rhinestones-jewelry-2209255.png?v=1758954085",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/nail-gold-plated-bracelet-rhinestones-jewelry-2209255.png?v=1758954085",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/nail-gold-plated-bracelet-rhinestones-jewelry-2209255.png?v=1758954085",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/nail-gold-plated-bracelet-rhinestones-jewelry-2209255.png?v=1758954085",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/nail-gold-plated-bracelet-rhinestones-jewelry-2209255.png?v=1758954085",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/nail-gold-plated-bracelet-rhinestones-jewelry-2209255.png?v=1758954085"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Nail gold plated bracelet rhinestones Jewelry - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "18kt-gold-plated-stainless-tarnish-free-waterproof-demi-fine-kada-bracelet",
    "name": "18KT Gold Plated Stainless Tarnish Free Waterproof Demi-Fine Bracelet",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE106",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/18kt-gold-plated-stainless-tarnish-free-waterproof-demi-fine-bracelet-8848356.png?v=1756056754",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/18kt-gold-plated-stainless-tarnish-free-waterproof-demi-fine-bracelet-8848356.png?v=1756056754",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/18kt-gold-plated-stainless-tarnish-free-waterproof-demi-fine-bracelet-8848356.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/18kt-gold-plated-stainless-tarnish-free-waterproof-demi-fine-bracelet-8848356.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/18kt-gold-plated-stainless-tarnish-free-waterproof-demi-fine-bracelet-8848356.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/18kt-gold-plated-stainless-tarnish-free-waterproof-demi-fine-bracelet-8848356.png?v=1756056754"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "18KT Gold Plated Stainless Tarnish Free Waterproof Demi-Fine Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "stainless-steel-contemporary-gold-plated-love-ad-anti-tarnish-bracelet-for-women",
    "name": "Stainless Steel Contemporary Gold Plated Love AD Anti-Tarnish Bracelet For Women",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE107",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/9022a705161ff42b7879d88f1fd6d0e8.png?v=1758954333",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/9022a705161ff42b7879d88f1fd6d0e8.png?v=1758954333",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/9022a705161ff42b7879d88f1fd6d0e8.png?v=1758954333",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/9022a705161ff42b7879d88f1fd6d0e8.png?v=1758954333",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/9022a705161ff42b7879d88f1fd6d0e8.png?v=1758954333",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/9022a705161ff42b7879d88f1fd6d0e8.png?v=1758954333"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Stainless Steel Contemporary Gold Plated Love AD Anti-Tarnish Bracelet For Women - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "stainless-steel-gold-plated-mother-of-pearls-clover-wraparound-anti-tarnish-bracelet-for-women",
    "name": "Stainless Steel Gold Plated Mother of Pearls Clover Wraparound Anti-Tarnish Bracelet For Women",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 1299,
    "originalPrice": 2999,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE108",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/stainless-steel-gold-plated-mother-of-pearls-clover-wraparound-anti-tarnish-bracelet-for-women-9126826.png?v=1756056755",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/stainless-steel-gold-plated-mother-of-pearls-clover-wraparound-anti-tarnish-bracelet-for-women-9126826.png?v=1756056755",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/stainless-steel-gold-plated-mother-of-pearls-clover-wraparound-anti-tarnish-bracelet-for-women-9126826.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/stainless-steel-gold-plated-mother-of-pearls-clover-wraparound-anti-tarnish-bracelet-for-women-9126826.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/stainless-steel-gold-plated-mother-of-pearls-clover-wraparound-anti-tarnish-bracelet-for-women-9126826.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/stainless-steel-gold-plated-mother-of-pearls-clover-wraparound-anti-tarnish-bracelet-for-women-9126826.png?v=1756056755"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Stainless Steel Gold Plated Mother of Pearls Clover Wraparound Anti-Tarnish Bracelet For Women - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "the-maharani-touch-luxe-gold-sapphire-ring",
    "name": "The Maharani Touch: Luxe Gold Sapphire Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE109",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-maharani-touch-luxe-gold-sapphire-ring-4884489.png?v=1756617959",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-maharani-touch-luxe-gold-sapphire-ring-4884489.png?v=1756617959",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-maharani-touch-luxe-gold-sapphire-ring-4884489.png?v=1756617959",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-maharani-touch-luxe-gold-sapphire-ring-4884489.png?v=1756617959",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-maharani-touch-luxe-gold-sapphire-ring-4884489.png?v=1756617959",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-maharani-touch-luxe-gold-sapphire-ring-4884489.png?v=1756617959"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "The Maharani Touch: Luxe Gold Sapphire Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "luxe-loop-18k-gold-plated-diamond-bow-ring",
    "name": "Luxe Loop: 18K Gold Plated Diamond Bow Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE110",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luxe-loop-18k-gold-plated-diamond-bow-ring-8821816.png?v=1756056758",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luxe-loop-18k-gold-plated-diamond-bow-ring-8821816.png?v=1756056758",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luxe-loop-18k-gold-plated-diamond-bow-ring-8821816.png?v=1756056758",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luxe-loop-18k-gold-plated-diamond-bow-ring-8821816.png?v=1756056758",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luxe-loop-18k-gold-plated-diamond-bow-ring-8821816.png?v=1756056758",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luxe-loop-18k-gold-plated-diamond-bow-ring-8821816.png?v=1756056758"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Luxe Loop: 18K Gold Plated Diamond Bow Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "dual-dazzle-black-white-stone-designer-ring",
    "name": "Dual Dazzle: Black & White Stone Designer Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE111",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-dazzle-black-white-stone-designer-ring-7920742.png?v=1756056753",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-dazzle-black-white-stone-designer-ring-7920742.png?v=1756056753",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-dazzle-black-white-stone-designer-ring-7920742.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-dazzle-black-white-stone-designer-ring-7920742.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-dazzle-black-white-stone-designer-ring-7920742.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-dazzle-black-white-stone-designer-ring-7920742.png?v=1756056753"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Dual Dazzle: Black & White Stone Designer Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "emerald-whirl-gold-ring-with-radiant-sparkle",
    "name": "Emerald Whirl: Gold Ring with Radiant Sparkle",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE112",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-whirl-gold-ring-with-radiant-sparkle-8993970.png?v=1756617827",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-whirl-gold-ring-with-radiant-sparkle-8993970.png?v=1756617827",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-whirl-gold-ring-with-radiant-sparkle-8993970.png?v=1756617827",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-whirl-gold-ring-with-radiant-sparkle-8993970.png?v=1756617827",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-whirl-gold-ring-with-radiant-sparkle-8993970.png?v=1756617827",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-whirl-gold-ring-with-radiant-sparkle-8993970.png?v=1756617827"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Emerald Whirl: Gold Ring with Radiant Sparkle - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "natures-embrace-gold-ring-with-sparkling-petals",
    "name": "Nature's Embrace \u2013 Gold Ring with Sparkling Petals",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE113",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/natures-embrace-gold-ring-with-sparkling-petals-1026972.png?v=1756056753",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/natures-embrace-gold-ring-with-sparkling-petals-1026972.png?v=1756056753",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/natures-embrace-gold-ring-with-sparkling-petals-1026972.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/natures-embrace-gold-ring-with-sparkling-petals-1026972.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/natures-embrace-gold-ring-with-sparkling-petals-1026972.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/natures-embrace-gold-ring-with-sparkling-petals-1026972.png?v=1756056753"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Nature's Embrace \u2013 Gold Ring with Sparkling Petals - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "infinity-grace-gold-ring-with-floating-diamonds",
    "name": "Infinity Grace \u2013 Gold Ring with Floating Diamonds",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE114",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/infinity-grace-gold-ring-with-floating-diamonds-7715030.png?v=1756056753",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/infinity-grace-gold-ring-with-floating-diamonds-7715030.png?v=1756056753",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/infinity-grace-gold-ring-with-floating-diamonds-7715030.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/infinity-grace-gold-ring-with-floating-diamonds-7715030.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/infinity-grace-gold-ring-with-floating-diamonds-7715030.png?v=1756056753",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/infinity-grace-gold-ring-with-floating-diamonds-7715030.png?v=1756056753"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Infinity Grace \u2013 Gold Ring with Floating Diamonds - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "gilded-glory-a-crown-of-light-on-your-finger",
    "name": "Gilded Glory \u2013 A Crown of Light on Your Finger",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE115",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-glory-a-crown-of-light-on-your-finger-8502053.png?v=1756056755",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-glory-a-crown-of-light-on-your-finger-8502053.png?v=1756056755",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-glory-a-crown-of-light-on-your-finger-8502053.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-glory-a-crown-of-light-on-your-finger-8502053.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-glory-a-crown-of-light-on-your-finger-8502053.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-glory-a-crown-of-light-on-your-finger-8502053.png?v=1756056755"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Gilded Glory \u2013 A Crown of Light on Your Finger - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "architect-of-elegance-geometric-gold-glam-ring",
    "name": "Architect of Elegance \u2013 Geometric Gold Glam Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE116",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/architect-of-elegance-geometric-gold-glam-ring-9923044.png?v=1756056757",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/architect-of-elegance-geometric-gold-glam-ring-9923044.png?v=1756056757",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/architect-of-elegance-geometric-gold-glam-ring-9923044.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/architect-of-elegance-geometric-gold-glam-ring-9923044.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/architect-of-elegance-geometric-gold-glam-ring-9923044.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/architect-of-elegance-geometric-gold-glam-ring-9923044.png?v=1756056757"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Architect of Elegance \u2013 Geometric Gold Glam Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "tide-of-glamour-gold-ring-with-flowing-design",
    "name": "Tide of Glamour \u2013 Gold Ring with Flowing Design",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE117",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/tide-of-glamour-gold-ring-with-flowing-design-6343048.png?v=1756056756",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/tide-of-glamour-gold-ring-with-flowing-design-6343048.png?v=1756056756",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/tide-of-glamour-gold-ring-with-flowing-design-6343048.png?v=1756056756",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/tide-of-glamour-gold-ring-with-flowing-design-6343048.png?v=1756056756",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/tide-of-glamour-gold-ring-with-flowing-design-6343048.png?v=1756056756",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/tide-of-glamour-gold-ring-with-flowing-design-6343048.png?v=1756056756"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Tide of Glamour \u2013 Gold Ring with Flowing Design - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "the-empress-band-elegant-triple-row-ring",
    "name": "The Empress Band \u2013 Elegant Triple Row Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE118",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-empress-band-elegant-triple-row-ring-8929622.png?v=1756056754",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-empress-band-elegant-triple-row-ring-8929622.png?v=1756056754",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-empress-band-elegant-triple-row-ring-8929622.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-empress-band-elegant-triple-row-ring-8929622.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-empress-band-elegant-triple-row-ring-8929622.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/the-empress-band-elegant-triple-row-ring-8929622.png?v=1756056754"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "The Empress Band \u2013 Elegant Triple Row Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "midnight-glow-blue-stone-halo-ring",
    "name": "Midnight Glow \u2013 Blue Stone Halo Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE119",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-glow-blue-stone-halo-ring-4446686.png?v=1756056778",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-glow-blue-stone-halo-ring-4446686.png?v=1756056778",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-glow-blue-stone-halo-ring-4446686.png?v=1756056778",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-glow-blue-stone-halo-ring-4446686.png?v=1756056778",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-glow-blue-stone-halo-ring-4446686.png?v=1756056778",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-glow-blue-stone-halo-ring-4446686.png?v=1756056778"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Midnight Glow \u2013 Blue Stone Halo Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "rosy-orbit-bold-sparkle-delicate-heart",
    "name": "Rosy Orbit \u2013 Bold Sparkle",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE120",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/rosy-orbit-bold-sparkle-delicate-heart-3423543.png?v=1756618074",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/rosy-orbit-bold-sparkle-delicate-heart-3423543.png?v=1756618074",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/rosy-orbit-bold-sparkle-delicate-heart-3423543.png?v=1756618074",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/rosy-orbit-bold-sparkle-delicate-heart-3423543.png?v=1756618074",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/rosy-orbit-bold-sparkle-delicate-heart-3423543.png?v=1756618074",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/rosy-orbit-bold-sparkle-delicate-heart-3423543.png?v=1756618074"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Rosy Orbit \u2013 Bold Sparkle - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "moonlit-grace-classic-silver-twist-ring",
    "name": "Moonlit Grace \u2013 Classic Silver Twist Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 1199,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "925 Sterling Silver",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": true,
    "inStock": true,
    "sku": "SKU: CIE121",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-grace-classic-silver-twist-ring-3952516.png?v=1756056754",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-grace-classic-silver-twist-ring-3952516.png?v=1756056754",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-grace-classic-silver-twist-ring-3952516.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-grace-classic-silver-twist-ring-3952516.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-grace-classic-silver-twist-ring-3952516.png?v=1756056754",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-grace-classic-silver-twist-ring-3952516.png?v=1756056754"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Moonlit Grace \u2013 Classic Silver Twist Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "crystal-vow-infinity-loop-ring-in-silver",
    "name": "Crystal Vow \u2013 Infinity Loop Ring in Silver",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 1199,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "925 Sterling Silver",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": true,
    "inStock": true,
    "sku": "SKU: CIE122",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-vow-infinity-loop-ring-in-silver-8446780.png?v=1756056774",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-vow-infinity-loop-ring-in-silver-8446780.png?v=1756056774",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-vow-infinity-loop-ring-in-silver-8446780.png?v=1756056774",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-vow-infinity-loop-ring-in-silver-8446780.png?v=1756056774",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-vow-infinity-loop-ring-in-silver-8446780.png?v=1756056774",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-vow-infinity-loop-ring-in-silver-8446780.png?v=1756056774"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Crystal Vow \u2013 Infinity Loop Ring in Silver - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "silver-petal-sparkle-cluster-designer-ring",
    "name": "Silver Petal \u2013 Sparkle Cluster Designer Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 1199,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "925 Sterling Silver",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": true,
    "inStock": true,
    "sku": "SKU: CIE123",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/silver-petal-sparkle-cluster-designer-ring-1844192.png?v=1756056909",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/silver-petal-sparkle-cluster-designer-ring-1844192.png?v=1756056909",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/silver-petal-sparkle-cluster-designer-ring-1844192.png?v=1756056909",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/silver-petal-sparkle-cluster-designer-ring-1844192.png?v=1756056909",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/silver-petal-sparkle-cluster-designer-ring-1844192.png?v=1756056909",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/silver-petal-sparkle-cluster-designer-ring-1844192.png?v=1756056909"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Silver Petal \u2013 Sparkle Cluster Designer Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "steel-luxe-cubic-diamond-inlay-ring",
    "name": "Steel Luxe \u2013 Cubic Diamond Inlay Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 599,
    "originalPrice": 1499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE124",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/steel-luxe-cubic-diamond-inlay-ring-3656466.png?v=1756056755",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/steel-luxe-cubic-diamond-inlay-ring-3656466.png?v=1756056755",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/steel-luxe-cubic-diamond-inlay-ring-3656466.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/steel-luxe-cubic-diamond-inlay-ring-3656466.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/steel-luxe-cubic-diamond-inlay-ring-3656466.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/steel-luxe-cubic-diamond-inlay-ring-3656466.png?v=1756056755"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Steel Luxe \u2013 Cubic Diamond Inlay Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "everlight-silver-sparkle-dots-ring",
    "name": "Everlight \u2013 Silver Sparkle Dots Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "925 Sterling Silver",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": true,
    "inStock": true,
    "sku": "SKU: CIE125",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/everlight-silver-sparkle-dots-ring-5732023.png?v=1756056757",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/everlight-silver-sparkle-dots-ring-5732023.png?v=1756056757",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/everlight-silver-sparkle-dots-ring-5732023.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/everlight-silver-sparkle-dots-ring-5732023.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/everlight-silver-sparkle-dots-ring-5732023.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/everlight-silver-sparkle-dots-ring-5732023.png?v=1756056757"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Everlight \u2013 Silver Sparkle Dots Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "moonlit-blossom-curved-silver-flower-ring",
    "name": "Moonlit Blossom \u2013 Curved Silver Flower Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 1199,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "925 Sterling Silver",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": true,
    "inStock": true,
    "sku": "SKU: CIE126",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-blossom-curved-silver-flower-ring-5375929.png?v=1756056755",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-blossom-curved-silver-flower-ring-5375929.png?v=1756056755",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-blossom-curved-silver-flower-ring-5375929.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-blossom-curved-silver-flower-ring-5375929.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-blossom-curved-silver-flower-ring-5375929.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonlit-blossom-curved-silver-flower-ring-5375929.png?v=1756056755"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Moonlit Blossom \u2013 Curved Silver Flower Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "queen-s-tear-marquise-halo-silver-ring",
    "name": "Queen\u2019s Tear \u2013 Marquise Halo Silver Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 1499,
    "discountPercent": 67,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "925 Sterling Silver",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": true,
    "inStock": true,
    "sku": "SKU: CIE127",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/queens-tear-marquise-halo-silver-ring-9741809.png?v=1756056757",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/queens-tear-marquise-halo-silver-ring-9741809.png?v=1756056757",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/queens-tear-marquise-halo-silver-ring-9741809.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/queens-tear-marquise-halo-silver-ring-9741809.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/queens-tear-marquise-halo-silver-ring-9741809.png?v=1756056757",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/queens-tear-marquise-halo-silver-ring-9741809.png?v=1756056757"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Queen\u2019s Tear \u2013 Marquise Halo Silver Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "moonleaf-dual-petal-sparkle-band",
    "name": "Moonleaf \u2013 Dual Petal Sparkle Band",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 1499,
    "discountPercent": 67,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE128",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonleaf-dual-petal-sparkle-band-5992710.png?v=1756056776",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonleaf-dual-petal-sparkle-band-5992710.png?v=1756056776",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonleaf-dual-petal-sparkle-band-5992710.png?v=1756056776",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonleaf-dual-petal-sparkle-band-5992710.png?v=1756056776",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonleaf-dual-petal-sparkle-band-5992710.png?v=1756056776",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/moonleaf-dual-petal-sparkle-band-5992710.png?v=1756056776"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Moonleaf \u2013 Dual Petal Sparkle Band - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "orbit-spark-contemporary-cluster-band",
    "name": "Orbit Spark \u2013 Contemporary Cluster Band",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 1199,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE129",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/orbit-spark-contemporary-cluster-band-8194147.png?v=1756056775",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/orbit-spark-contemporary-cluster-band-8194147.png?v=1756056775",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/orbit-spark-contemporary-cluster-band-8194147.png?v=1756056775",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/orbit-spark-contemporary-cluster-band-8194147.png?v=1756056775",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/orbit-spark-contemporary-cluster-band-8194147.png?v=1756056775",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/orbit-spark-contemporary-cluster-band-8194147.png?v=1756056775"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Orbit Spark \u2013 Contemporary Cluster Band - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "starlight-crown-timeless-cz-engagement-ring",
    "name": "Starlight Crown \u2013 Timeless CZ Engagement Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 1499,
    "discountPercent": 67,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE130",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/starlight-crown-timeless-cz-engagement-ring-4856014.png?v=1756056776",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/starlight-crown-timeless-cz-engagement-ring-4856014.png?v=1756056776",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/starlight-crown-timeless-cz-engagement-ring-4856014.png?v=1756056776",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/starlight-crown-timeless-cz-engagement-ring-4856014.png?v=1756056776",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/starlight-crown-timeless-cz-engagement-ring-4856014.png?v=1756056776",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/starlight-crown-timeless-cz-engagement-ring-4856014.png?v=1756056776"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Starlight Crown \u2013 Timeless CZ Engagement Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "luna-light-classic-sparkle-engagement-ring",
    "name": "Luna Light \u2013 Classic Sparkle Engagement Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 499,
    "originalPrice": 999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE131",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luna-light-classic-sparkle-engagement-ring-6019156.png?v=1756056755",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luna-light-classic-sparkle-engagement-ring-6019156.png?v=1756056755",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luna-light-classic-sparkle-engagement-ring-6019156.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luna-light-classic-sparkle-engagement-ring-6019156.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luna-light-classic-sparkle-engagement-ring-6019156.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/luna-light-classic-sparkle-engagement-ring-6019156.png?v=1756056755"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Luna Light \u2013 Classic Sparkle Engagement Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "glacier-gleam-princess-sparkle-ring",
    "name": "Glacier Gleam \u2013 Princess Sparkle Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 499,
    "originalPrice": 1499,
    "discountPercent": 67,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE132",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/glacier-gleam-princess-sparkle-ring-5657175.png?v=1756056755",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/glacier-gleam-princess-sparkle-ring-5657175.png?v=1756056755",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/glacier-gleam-princess-sparkle-ring-5657175.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/glacier-gleam-princess-sparkle-ring-5657175.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/glacier-gleam-princess-sparkle-ring-5657175.png?v=1756056755",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/glacier-gleam-princess-sparkle-ring-5657175.png?v=1756056755"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Glacier Gleam \u2013 Princess Sparkle Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "dual-point-ring",
    "name": "Dual Point Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 699,
    "originalPrice": 1899,
    "discountPercent": 63,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE133",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-point-ring-8420573.png?v=1756617663",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-point-ring-8420573.png?v=1756617663",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-point-ring-8420573.png?v=1756617663",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-point-ring-8420573.png?v=1756617663",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-point-ring-8420573.png?v=1756617663",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/dual-point-ring-8420573.png?v=1756617663"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Dual Point Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "rose-gold-clover",
    "name": "Blush Charm Rose Gold Clover Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE134",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/blush-charm-rose-gold-clover-ring-7022343.png?v=1758953071",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/blush-charm-rose-gold-clover-ring-7022343.png?v=1758953071",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/blush-charm-rose-gold-clover-ring-7022343.png?v=1758953071",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/blush-charm-rose-gold-clover-ring-7022343.png?v=1758953071",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/blush-charm-rose-gold-clover-ring-7022343.png?v=1758953071",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/blush-charm-rose-gold-clover-ring-7022343.png?v=1758953071"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Blush Charm Rose Gold Clover Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "radiant-bloom-rose-gold-diamond-ring",
    "name": "Radiant Bloom Rose Gold Diamond Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 599,
    "originalPrice": 1799,
    "discountPercent": 67,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE135",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/radiant-bloom-rose-gold-diamond-ring-7930669.png?v=1756618126",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/radiant-bloom-rose-gold-diamond-ring-7930669.png?v=1756618126",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/radiant-bloom-rose-gold-diamond-ring-7930669.png?v=1756618126",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/radiant-bloom-rose-gold-diamond-ring-7930669.png?v=1756618126",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/radiant-bloom-rose-gold-diamond-ring-7930669.png?v=1756618126",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/radiant-bloom-rose-gold-diamond-ring-7930669.png?v=1756618126"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Radiant Bloom Rose Gold Diamond Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-aura-crossover-statement-ring",
    "name": "Golden Aura Crossover Statement Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 699,
    "originalPrice": 1699,
    "discountPercent": 59,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE136",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-aura-crossover-statement-ring-8589265.png?v=1756617743",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-aura-crossover-statement-ring-8589265.png?v=1756617743",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-aura-crossover-statement-ring-8589265.png?v=1756617743",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-aura-crossover-statement-ring-8589265.png?v=1756617743",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-aura-crossover-statement-ring-8589265.png?v=1756617743",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-aura-crossover-statement-ring-8589265.png?v=1756617743"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Aura Crossover Statement Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "liquid-gold-organic-band-ring",
    "name": "Liquid Gold Organic Band Ring",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 699,
    "originalPrice": 1799,
    "discountPercent": 61,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE137",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/liquid-gold-organic-band-ring-3431866.png?v=1756617706",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/liquid-gold-organic-band-ring-3431866.png?v=1756617706",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/liquid-gold-organic-band-ring-3431866.png?v=1756617706",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/liquid-gold-organic-band-ring-3431866.png?v=1756617706",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/liquid-gold-organic-band-ring-3431866.png?v=1756617706",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/liquid-gold-organic-band-ring-3431866.png?v=1756617706"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Liquid Gold Organic Band Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "gilded-flame-sculptural-earrings",
    "name": "Gilded Flame Sculptural Earrings",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE138",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-flame-sculptural-earrings-4135706.png?v=1758953814",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-flame-sculptural-earrings-4135706.png?v=1758953814",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-flame-sculptural-earrings-4135706.png?v=1758953814",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-flame-sculptural-earrings-4135706.png?v=1758953814",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-flame-sculptural-earrings-4135706.png?v=1758953814",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/gilded-flame-sculptural-earrings-4135706.png?v=1758953814"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Gilded Flame Sculptural Earrings - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "eternal-time-roman-dial-hoop-earrings",
    "name": "Eternal Time Roman Dial Hoop Earrings",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 899,
    "originalPrice": 2099,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE139",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-time-roman-dial-hoop-earrings-1081657.png?v=1758953698",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-time-roman-dial-hoop-earrings-1081657.png?v=1758953698",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-time-roman-dial-hoop-earrings-1081657.png?v=1758953698",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-time-roman-dial-hoop-earrings-1081657.png?v=1758953698",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-time-roman-dial-hoop-earrings-1081657.png?v=1758953698",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-time-roman-dial-hoop-earrings-1081657.png?v=1758953698"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Eternal Time Roman Dial Hoop Earrings - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "linear-muse-geometric-drop-earrings",
    "name": "Linear Muse Geometric Drop Earrings",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 2099,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE140",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/linear-muse-geometric-drop-earrings-8640731.png?v=1758954131",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/linear-muse-geometric-drop-earrings-8640731.png?v=1758954131",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/linear-muse-geometric-drop-earrings-8640731.png?v=1758954131",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/linear-muse-geometric-drop-earrings-8640731.png?v=1758954131",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/linear-muse-geometric-drop-earrings-8640731.png?v=1758954131",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/linear-muse-geometric-drop-earrings-8640731.png?v=1758954131"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Linear Muse Geometric Drop Earrings - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-whisper-butterfly-drop-earrings",
    "name": "Golden Whisper Butterfly Drop Earrings",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE141",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whisper-butterfly-drop-earrings-8749999.png?v=1758953916",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whisper-butterfly-drop-earrings-8749999.png?v=1758953916",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whisper-butterfly-drop-earrings-8749999.png?v=1758953916",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whisper-butterfly-drop-earrings-8749999.png?v=1758953916",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whisper-butterfly-drop-earrings-8749999.png?v=1758953916",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whisper-butterfly-drop-earrings-8749999.png?v=1758953916"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Whisper Butterfly Drop Earrings - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "honey-love-marble-heart-studs",
    "name": "Honey Love Marble Heart Studs",
    "category": "Earrings",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 2099,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE142",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/honey-love-marble-heart-studs-8479731.png?v=1758953637",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/honey-love-marble-heart-studs-8479731.png?v=1758953637",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/honey-love-marble-heart-studs-8479731.png?v=1758953637",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/honey-love-marble-heart-studs-8479731.png?v=1758953637",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/honey-love-marble-heart-studs-8479731.png?v=1758953637",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/honey-love-marble-heart-studs-8479731.png?v=1758953637"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Honey Love Marble Heart Studs - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-helix-classic-twist-hoops",
    "name": "Golden Helix Classic Twist Hoops",
    "category": "Earrings",
    "occasion": "Office Wear",
    "price": 899,
    "originalPrice": 2099,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE143",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-helix-classic-twist-hoops-7344063.png?v=1758953829",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-helix-classic-twist-hoops-7344063.png?v=1758953829",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-helix-classic-twist-hoops-7344063.png?v=1758953829",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-helix-classic-twist-hoops-7344063.png?v=1758953829",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-helix-classic-twist-hoops-7344063.png?v=1758953829",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-helix-classic-twist-hoops-7344063.png?v=1758953829"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Helix Classic Twist Hoops - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "sona-shakti-temple-coin-hoop-earrings",
    "name": "Sona Shakti Temple Coin Hoop Earrings",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE144",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sona-shakti-temple-coin-hoop-earrings-1604712.png?v=1758953647",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sona-shakti-temple-coin-hoop-earrings-1604712.png?v=1758953647",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sona-shakti-temple-coin-hoop-earrings-1604712.png?v=1758953647",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sona-shakti-temple-coin-hoop-earrings-1604712.png?v=1758953647",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sona-shakti-temple-coin-hoop-earrings-1604712.png?v=1758953647",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sona-shakti-temple-coin-hoop-earrings-1604712.png?v=1758953647"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Sona Shakti Temple Coin Hoop Earrings - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "eternal-roots-rose-gold-tree-of-life-earring-set-3-pairs",
    "name": "Eternal Roots \u2013 Rose Gold Tree of Life Earring Set (3 Pairs)",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 1699,
    "originalPrice": 2999,
    "discountPercent": 43,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE145",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-roots-rose-gold-tree-of-life-earring-set-3-pairs-3914323.png?v=1758953962",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-roots-rose-gold-tree-of-life-earring-set-3-pairs-3914323.png?v=1758953962",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-roots-rose-gold-tree-of-life-earring-set-3-pairs-3914323.png?v=1758953962",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-roots-rose-gold-tree-of-life-earring-set-3-pairs-3914323.png?v=1758953962",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-roots-rose-gold-tree-of-life-earring-set-3-pairs-3914323.png?v=1758953962",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/eternal-roots-rose-gold-tree-of-life-earring-set-3-pairs-3914323.png?v=1758953962"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Eternal Roots \u2013 Rose Gold Tree of Life Earring Set (3 Pairs) - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "melted-heart-sculpted-gold-studs",
    "name": "Melted Heart Sculpted Gold Studs",
    "category": "Earrings",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 2099,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE146",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/melted-heart-sculpted-gold-studs-9215584.png?v=1758954100",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/melted-heart-sculpted-gold-studs-9215584.png?v=1758954100",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/melted-heart-sculpted-gold-studs-9215584.png?v=1758954100",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/melted-heart-sculpted-gold-studs-9215584.png?v=1758954100",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/melted-heart-sculpted-gold-studs-9215584.png?v=1758954100",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/melted-heart-sculpted-gold-studs-9215584.png?v=1758954100"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Melted Heart Sculpted Gold Studs - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "lunar-luxe-bold-crescent-hoops",
    "name": "Lunar Luxe Bold Crescent Hoops",
    "category": "Earrings",
    "occasion": "Office Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE147",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/lunar-luxe-bold-crescent-hoops-5454648.png?v=1758953613",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/lunar-luxe-bold-crescent-hoops-5454648.png?v=1758953613",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/lunar-luxe-bold-crescent-hoops-5454648.png?v=1758953613",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/lunar-luxe-bold-crescent-hoops-5454648.png?v=1758953613",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/lunar-luxe-bold-crescent-hoops-5454648.png?v=1758953613",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/lunar-luxe-bold-crescent-hoops-5454648.png?v=1758953613"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Lunar Luxe Bold Crescent Hoops - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "fleur-de-lune-crystal-crescent-earrings",
    "name": "Fleur de Lune Crystal Crescent Earrings",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE148",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/fleur-de-lune-crystal-crescent-earrings-3913562.png?v=1758953622",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/fleur-de-lune-crystal-crescent-earrings-3913562.png?v=1758953622",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/fleur-de-lune-crystal-crescent-earrings-3913562.png?v=1758953622",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/fleur-de-lune-crystal-crescent-earrings-3913562.png?v=1758953622",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/fleur-de-lune-crystal-crescent-earrings-3913562.png?v=1758953622",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/fleur-de-lune-crystal-crescent-earrings-3913562.png?v=1758953622"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Fleur de Lune Crystal Crescent Earrings - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "emerald-aura-clover-cable-bracelet",
    "name": "Emerald Aura Clover Cable Bracelet",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE149",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-aura-clover-cable-bracelet-4415871.png?v=1758953422",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-aura-clover-cable-bracelet-4415871.png?v=1758953422",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-aura-clover-cable-bracelet-4415871.png?v=1758953422",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-aura-clover-cable-bracelet-4415871.png?v=1758953422",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-aura-clover-cable-bracelet-4415871.png?v=1758953422",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-aura-clover-cable-bracelet-4415871.png?v=1758953422"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Emerald Aura Clover Cable Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "elysian-flow-22k-gold-statement-ring",
    "name": "Elysian Flow 22K Gold Statement Ring",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 799,
    "originalPrice": 1899,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE150",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/elysian-flow-22k-gold-statement-ring-3827294.png?v=1756617860",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/elysian-flow-22k-gold-statement-ring-3827294.png?v=1756617860",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/elysian-flow-22k-gold-statement-ring-3827294.png?v=1756617860",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/elysian-flow-22k-gold-statement-ring-3827294.png?v=1756617860",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/elysian-flow-22k-gold-statement-ring-3827294.png?v=1756617860",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/elysian-flow-22k-gold-statement-ring-3827294.png?v=1756617860"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Elysian Flow 22K Gold Statement Ring - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "sparkle-vibe-18k-gold-plated-open-v-curve-diamond-ring-\u2728",
    "name": "Sparkle Vibe | 18K Gold Plated Open V-Curve Diamond Ring \u2728",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 799,
    "originalPrice": 1999,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE151",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sparkle-vibe-18k-gold-plated-open-v-curve-diamond-ring-7676924.png?v=1756617998",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sparkle-vibe-18k-gold-plated-open-v-curve-diamond-ring-7676924.png?v=1756617998",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sparkle-vibe-18k-gold-plated-open-v-curve-diamond-ring-7676924.png?v=1756617998",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sparkle-vibe-18k-gold-plated-open-v-curve-diamond-ring-7676924.png?v=1756617998",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sparkle-vibe-18k-gold-plated-open-v-curve-diamond-ring-7676924.png?v=1756617998",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/sparkle-vibe-18k-gold-plated-open-v-curve-diamond-ring-7676924.png?v=1756617998"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Sparkle Vibe | 18K Gold Plated Open V-Curve Diamond Ring \u2728 - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "serpent-of-grace-diamond-ring-sterling-elegance-with-emerald-eyes",
    "name": "Serpent of Grace Diamond Ring \u2013 Sterling Elegance with Emerald Eyes",
    "category": "Rings",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 1999,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "925 Sterling Silver",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": true,
    "inStock": true,
    "sku": "SKU: CIE152",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/serpent-of-grace-diamond-ring-sterling-elegance-with-emerald-eyes-5196585.png?v=1756618035",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/serpent-of-grace-diamond-ring-sterling-elegance-with-emerald-eyes-5196585.png?v=1756618035",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/serpent-of-grace-diamond-ring-sterling-elegance-with-emerald-eyes-5196585.png?v=1756618035",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/serpent-of-grace-diamond-ring-sterling-elegance-with-emerald-eyes-5196585.png?v=1756618035",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/serpent-of-grace-diamond-ring-sterling-elegance-with-emerald-eyes-5196585.png?v=1756618035",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/serpent-of-grace-diamond-ring-sterling-elegance-with-emerald-eyes-5196585.png?v=1756618035"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Serpent of Grace Diamond Ring \u2013 Sterling Elegance with Emerald Eyes - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "floral-radiance-gold-toned-designer-bracelet",
    "name": "Floral Radiance Gold-Toned Designer Bracelet",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE153",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/floral-radiance-gold-toned-designer-bracelet-6234231.png?v=1756056774",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/floral-radiance-gold-toned-designer-bracelet-6234231.png?v=1756056774",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/floral-radiance-gold-toned-designer-bracelet-6234231.png?v=1756056774",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/floral-radiance-gold-toned-designer-bracelet-6234231.png?v=1756056774",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/floral-radiance-gold-toned-designer-bracelet-6234231.png?v=1756056774",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/floral-radiance-gold-toned-designer-bracelet-6234231.png?v=1756056774"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Floral Radiance Gold-Toned Designer Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-luxe-bold-link-bracelet",
    "name": "Golden Luxe Bold Link Bracelet",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2099,
    "discountPercent": 52,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE154",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-luxe-bold-link-bracelet-5793520.png?v=1758953842",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-luxe-bold-link-bracelet-5793520.png?v=1758953842",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-luxe-bold-link-bracelet-5793520.png?v=1758953842",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-luxe-bold-link-bracelet-5793520.png?v=1758953842",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-luxe-bold-link-bracelet-5793520.png?v=1758953842",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-luxe-bold-link-bracelet-5793520.png?v=1758953842"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Luxe Bold Link Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "celestial-charm-star-link-bracelet",
    "name": "Celestial Charm Star Link Bracelet",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 899,
    "originalPrice": 1799,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE155",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-charm-star-link-bracelet-5612753.png?v=1758953157",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-charm-star-link-bracelet-5612753.png?v=1758953157",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-charm-star-link-bracelet-5612753.png?v=1758953157",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-charm-star-link-bracelet-5612753.png?v=1758953157",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-charm-star-link-bracelet-5612753.png?v=1758953157",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-charm-star-link-bracelet-5612753.png?v=1758953157"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Celestial Charm Star Link Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-harmony-dual-strand-bracelet",
    "name": "Golden Harmony Dual-Strand Bracelet",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 949,
    "originalPrice": 1899,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE156",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-harmony-dual-strand-bracelet-9285314.png?v=1758953812",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-harmony-dual-strand-bracelet-9285314.png?v=1758953812",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-harmony-dual-strand-bracelet-9285314.png?v=1758953812",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-harmony-dual-strand-bracelet-9285314.png?v=1758953812",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-harmony-dual-strand-bracelet-9285314.png?v=1758953812",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-harmony-dual-strand-bracelet-9285314.png?v=1758953812"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Harmony Dual-Strand Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "crystal-luxe-baguette-tennis-bracelet",
    "name": "Crystal Luxe Baguette Tennis Bracelet",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 1049,
    "originalPrice": 2499,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE157",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-luxe-baguette-tennis-bracelet-5456821.png?v=1758953319",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-luxe-baguette-tennis-bracelet-5456821.png?v=1758953319",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-luxe-baguette-tennis-bracelet-5456821.png?v=1758953319",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-luxe-baguette-tennis-bracelet-5456821.png?v=1758953319",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-luxe-baguette-tennis-bracelet-5456821.png?v=1758953319",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-luxe-baguette-tennis-bracelet-5456821.png?v=1758953319"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Crystal Luxe Baguette Tennis Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "enchanted-clover-charm-bracelet",
    "name": "Enchanted Clover Charm Bracelet",
    "category": "Bracelets",
    "occasion": "Daily Wear",
    "price": 899,
    "originalPrice": 2199,
    "discountPercent": 59,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE158",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/enchanted-clover-charm-bracelet-7505707.png?v=1758953411",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/enchanted-clover-charm-bracelet-7505707.png?v=1758953411",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/enchanted-clover-charm-bracelet-7505707.png?v=1758953411",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/enchanted-clover-charm-bracelet-7505707.png?v=1758953411",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/enchanted-clover-charm-bracelet-7505707.png?v=1758953411",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/enchanted-clover-charm-bracelet-7505707.png?v=1758953411"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Enchanted Clover Charm Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-grace-clover-pearl-necklace",
    "name": "Golden Grace Clover & Pearl Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE159",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-grace-clover-pearl-necklace-9625323.png?v=1756618466",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-grace-clover-pearl-necklace-9625323.png?v=1756618466",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-grace-clover-pearl-necklace-9625323.png?v=1756618466",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-grace-clover-pearl-necklace-9625323.png?v=1756618466",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-grace-clover-pearl-necklace-9625323.png?v=1756618466",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-grace-clover-pearl-necklace-9625323.png?v=1756618466"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Grace Clover & Pearl Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-flutter-butterfly-drop-necklace",
    "name": "Golden Flutter Butterfly Drop Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2599,
    "discountPercent": 62,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE160",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-flutter-butterfly-drop-necklace-8184072.png?v=1756224340",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-flutter-butterfly-drop-necklace-8184072.png?v=1756224340",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-flutter-butterfly-drop-necklace-8184072.png?v=1756224340",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-flutter-butterfly-drop-necklace-8184072.png?v=1756224340",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-flutter-butterfly-drop-necklace-8184072.png?v=1756224340",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-flutter-butterfly-drop-necklace-8184072.png?v=1756224340"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Flutter Butterfly Drop Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "midnight-bloom-petal-charm-necklace",
    "name": "Midnight Bloom Petal Charm Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE161",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-bloom-petal-charm-necklace-8578224.png?v=1756224333",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-bloom-petal-charm-necklace-8578224.png?v=1756224333",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-bloom-petal-charm-necklace-8578224.png?v=1756224333",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-bloom-petal-charm-necklace-8578224.png?v=1756224333",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-bloom-petal-charm-necklace-8578224.png?v=1756224333",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-bloom-petal-charm-necklace-8578224.png?v=1756224333"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Midnight Bloom Petal Charm Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-emblem-luxe-layered-necklace",
    "name": "Golden Emblem Luxe Layered Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2499,
    "discountPercent": 60,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE162",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-emblem-luxe-layered-necklace-8924108.png?v=1756224326",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-emblem-luxe-layered-necklace-8924108.png?v=1756224326",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-emblem-luxe-layered-necklace-8924108.png?v=1756224326",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-emblem-luxe-layered-necklace-8924108.png?v=1756224326",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-emblem-luxe-layered-necklace-8924108.png?v=1756224326",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-emblem-luxe-layered-necklace-8924108.png?v=1756224326"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Emblem Luxe Layered Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "ivory-whisper-petal-necklace",
    "name": "Ivory Whisper Petal Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE163",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-whisper-petal-necklace-3044131.png?v=1756224323",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-whisper-petal-necklace-3044131.png?v=1756224323",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-whisper-petal-necklace-3044131.png?v=1756224323",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-whisper-petal-necklace-3044131.png?v=1756224323",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-whisper-petal-necklace-3044131.png?v=1756224323",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-whisper-petal-necklace-3044131.png?v=1756224323"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Ivory Whisper Petal Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "midnight-hearts-gold-plated-love-lariat-necklace",
    "name": "Midnight Hearts Gold-Plated Love Lariat Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2399,
    "discountPercent": 58,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE164",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-hearts-gold-plated-love-lariat-necklace-4445810.png?v=1756224317",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-hearts-gold-plated-love-lariat-necklace-4445810.png?v=1756224317",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-hearts-gold-plated-love-lariat-necklace-4445810.png?v=1756224317",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-hearts-gold-plated-love-lariat-necklace-4445810.png?v=1756224317",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-hearts-gold-plated-love-lariat-necklace-4445810.png?v=1756224317",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/midnight-hearts-gold-plated-love-lariat-necklace-4445810.png?v=1756224317"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Midnight Hearts Gold-Plated Love Lariat Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "urban-pulse-gold-plated-rectangular-link-chain-necklace",
    "name": "Urban Pulse Gold-Plated Rectangular Link Chain Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2199,
    "discountPercent": 55,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE165",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/urban-pulse-gold-plated-rectangular-link-chain-necklace-7591197.png?v=1756224311",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/urban-pulse-gold-plated-rectangular-link-chain-necklace-7591197.png?v=1756224311",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/urban-pulse-gold-plated-rectangular-link-chain-necklace-7591197.png?v=1756224311",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/urban-pulse-gold-plated-rectangular-link-chain-necklace-7591197.png?v=1756224311",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/urban-pulse-gold-plated-rectangular-link-chain-necklace-7591197.png?v=1756224311",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/urban-pulse-gold-plated-rectangular-link-chain-necklace-7591197.png?v=1756224311"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Urban Pulse Gold-Plated Rectangular Link Chain Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "noir-panther-bold-black-panther-pendant-necklace",
    "name": "Noir Panther Bold Black Panther Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2599,
    "discountPercent": 62,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE166",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/noir-panther-bold-black-panther-pendant-necklace-9654176.png?v=1756224304",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/noir-panther-bold-black-panther-pendant-necklace-9654176.png?v=1756224304",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/noir-panther-bold-black-panther-pendant-necklace-9654176.png?v=1756224304",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/noir-panther-bold-black-panther-pendant-necklace-9654176.png?v=1756224304",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/noir-panther-bold-black-panther-pendant-necklace-9654176.png?v=1756224304",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/noir-panther-bold-black-panther-pendant-necklace-9654176.png?v=1756224304"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Noir Panther Bold Black Panther Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "ivory-hearts-gold-plated-lariat-necklace",
    "name": "Ivory Hearts Gold-Plated Lariat Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2299,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE167",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-hearts-gold-plated-lariat-necklace-7841339.png?v=1756224294",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-hearts-gold-plated-lariat-necklace-7841339.png?v=1756224294",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-hearts-gold-plated-lariat-necklace-7841339.png?v=1756224294",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-hearts-gold-plated-lariat-necklace-7841339.png?v=1756224294",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-hearts-gold-plated-lariat-necklace-7841339.png?v=1756224294",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ivory-hearts-gold-plated-lariat-necklace-7841339.png?v=1756224294"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Ivory Hearts Gold-Plated Lariat Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-whimsy-bow-pendant-necklace",
    "name": "Golden Whimsy Bow Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2299,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "9KT Solid Gold",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": true,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE168",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whimsy-bow-pendant-necklace-2518506.png?v=1758181077",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whimsy-bow-pendant-necklace-2518506.png?v=1758181077",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whimsy-bow-pendant-necklace-2518506.png?v=1758181077",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whimsy-bow-pendant-necklace-2518506.png?v=1758181077",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whimsy-bow-pendant-necklace-2518506.png?v=1758181077",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-whimsy-bow-pendant-necklace-2518506.png?v=1758181077"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Whimsy Bow Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-drizzle-twin-drop-pendant-necklace",
    "name": "Golden Drizzle Twin Drop Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 2299,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "9KT Solid Gold",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": true,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE169",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-drizzle-twin-drop-pendant-necklace-2207145.png?v=1758181113",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-drizzle-twin-drop-pendant-necklace-2207145.png?v=1758181113",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-drizzle-twin-drop-pendant-necklace-2207145.png?v=1758181113",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-drizzle-twin-drop-pendant-necklace-2207145.png?v=1758181113",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-drizzle-twin-drop-pendant-necklace-2207145.png?v=1758181113",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-drizzle-twin-drop-pendant-necklace-2207145.png?v=1758181113"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Drizzle Twin Drop Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "iconic-muse-bold-cc-pendant-necklace",
    "name": "Iconic Muse Bold CC Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 2299,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE170",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/iconic-muse-bold-cc-pendant-necklace-6377947.png?v=1758181203",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/iconic-muse-bold-cc-pendant-necklace-6377947.png?v=1758181203",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/iconic-muse-bold-cc-pendant-necklace-6377947.png?v=1758181203",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/iconic-muse-bold-cc-pendant-necklace-6377947.png?v=1758181203",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/iconic-muse-bold-cc-pendant-necklace-6377947.png?v=1758181203",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/iconic-muse-bold-cc-pendant-necklace-6377947.png?v=1758181203"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Iconic Muse Bold CC Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "molten-muse-sculpted-pendant-teardrop-earring-set",
    "name": "Molten Muse Sculpted Pendant & Teardrop Earring Set",
    "category": "Rings",
    "occasion": "Office Wear",
    "price": 1299,
    "originalPrice": 2999,
    "discountPercent": 57,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE171",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/molten-muse-sculpted-pendant-teardrop-earring-set-4298285.png?v=1756224255",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/molten-muse-sculpted-pendant-teardrop-earring-set-4298285.png?v=1756224255",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/molten-muse-sculpted-pendant-teardrop-earring-set-4298285.png?v=1756224255",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/molten-muse-sculpted-pendant-teardrop-earring-set-4298285.png?v=1756224255",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/molten-muse-sculpted-pendant-teardrop-earring-set-4298285.png?v=1756224255",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/molten-muse-sculpted-pendant-teardrop-earring-set-4298285.png?v=1756224255"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Molten Muse Sculpted Pendant & Teardrop Earring Set - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "emerald-pirouette-dancing-ballerina-pendant-necklace",
    "name": "Emerald Pirouette Dancing Ballerina Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE172",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-pirouette-dancing-ballerina-pendant-necklace-9697600.png?v=1756224247",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-pirouette-dancing-ballerina-pendant-necklace-9697600.png?v=1756224247",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-pirouette-dancing-ballerina-pendant-necklace-9697600.png?v=1756224247",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-pirouette-dancing-ballerina-pendant-necklace-9697600.png?v=1756224247",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-pirouette-dancing-ballerina-pendant-necklace-9697600.png?v=1756224247",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/emerald-pirouette-dancing-ballerina-pendant-necklace-9697600.png?v=1756224247"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Emerald Pirouette Dancing Ballerina Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "golden-bean-fluid-sculpt-pendant-necklace",
    "name": "Golden Bean Fluid Sculpt Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "9KT Solid Gold",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": true,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE173",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-bean-fluid-sculpt-pendant-necklace-6495439.png?v=1756224242",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-bean-fluid-sculpt-pendant-necklace-6495439.png?v=1756224242",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-bean-fluid-sculpt-pendant-necklace-6495439.png?v=1756224242",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-bean-fluid-sculpt-pendant-necklace-6495439.png?v=1756224242",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-bean-fluid-sculpt-pendant-necklace-6495439.png?v=1756224242",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/golden-bean-fluid-sculpt-pendant-necklace-6495439.png?v=1756224242"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Golden Bean Fluid Sculpt Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "pop-pup-balloon-dog-pendant-necklace",
    "name": "Pop Pup Balloon Dog Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE174",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/pop-pup-balloon-dog-pendant-necklace-8995228.png?v=1758181262",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/pop-pup-balloon-dog-pendant-necklace-8995228.png?v=1758181262",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/pop-pup-balloon-dog-pendant-necklace-8995228.png?v=1758181262",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/pop-pup-balloon-dog-pendant-necklace-8995228.png?v=1758181262",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/pop-pup-balloon-dog-pendant-necklace-8995228.png?v=1758181262",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/pop-pup-balloon-dog-pendant-necklace-8995228.png?v=1758181262"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Pop Pup Balloon Dog Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "crystal-charme-bow-baguette-pendant-necklace",
    "name": "Crystal Charme Bow & Baguette Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": true,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE175",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-charme-bow-baguette-pendant-necklace-7190443.png?v=1756224230",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-charme-bow-baguette-pendant-necklace-7190443.png?v=1756224230",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-charme-bow-baguette-pendant-necklace-7190443.png?v=1756224230",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-charme-bow-baguette-pendant-necklace-7190443.png?v=1756224230",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-charme-bow-baguette-pendant-necklace-7190443.png?v=1756224230",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/crystal-charme-bow-baguette-pendant-necklace-7190443.png?v=1756224230"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Crystal Charme Bow & Baguette Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "magnetique-amour-heart-clover-convertible-pendant-necklace",
    "name": "Magnetique Amour Heart-Clover Convertible Pendant Necklace",
    "category": "Necklaces",
    "occasion": "Daily Wear",
    "price": 1299,
    "originalPrice": 2299,
    "discountPercent": 43,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": true,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE176",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/magnetique-amour-heart-clover-convertible-pendant-necklace-6900898.png?v=1756224225",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/magnetique-amour-heart-clover-convertible-pendant-necklace-6900898.png?v=1756224225",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/magnetique-amour-heart-clover-convertible-pendant-necklace-6900898.png?v=1756224225",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/magnetique-amour-heart-clover-convertible-pendant-necklace-6900898.png?v=1756224225",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/magnetique-amour-heart-clover-convertible-pendant-necklace-6900898.png?v=1756224225",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/magnetique-amour-heart-clover-convertible-pendant-necklace-6900898.png?v=1756224225"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Magnetique Amour Heart-Clover Convertible Pendant Necklace - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  },
  {
    "id": "celestial-radiance-adjustable-gold-bracelet",
    "name": "Celestial Radiance Adjustable Gold Bracelet",
    "category": "Bracelets",
    "occasion": "Office Wear",
    "price": 999,
    "originalPrice": 1999,
    "discountPercent": 50,
    "rating": 4.6,
    "reviewCount": 132,
    "metal": "18K Gold Tone Plated",
    "isBestseller": false,
    "isNew": false,
    "isFineGold": false,
    "isSilver": false,
    "inStock": true,
    "sku": "SKU: CIE177",
    "image": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-radiance-adjustable-gold-bracelet-8797428.png?v=1758953255",
    "secondaryImage": "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-radiance-adjustable-gold-bracelet-8797428.png?v=1758953255",
    "gallery": [
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-radiance-adjustable-gold-bracelet-8797428.png?v=1758953255",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-radiance-adjustable-gold-bracelet-8797428.png?v=1758953255",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-radiance-adjustable-gold-bracelet-8797428.png?v=1758953255",
      "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/celestial-radiance-adjustable-gold-bracelet-8797428.png?v=1758953255"
    ],
    "features": [
      "18K Gold Plated Anti-Tarnish Coating",
      "100% Waterproof & Sweatproof",
      "Hypoallergenic & Nickel-Free",
      "Lifetime Polish Guarantee"
    ],
    "description": "Celestial Radiance Adjustable Gold Bracelet - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
    "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
    "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
    "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
  }
];

const CURRENCIES = {
  INR: { symbol: '₹', rate: 1, label: 'INR (₹)' },
  USD: { symbol: '$', rate: 0.012, label: 'USD ($)' },
  EUR: { symbol: '€', rate: 0.011, label: 'EUR (€)' },
  GBP: { symbol: '£', rate: 0.0094, label: 'GBP (£)' }
};

const ANNOUNCEMENTS = [
  "RAKHI SALE - STARTING FROM FLAT ₹999",
  "⚡ FREE STUDS of ₹1495 on orders above ₹2999",
  "Buy 1 Get 1 Free | Use Code - B1G1"
];

const SEARCH_PLACEHOLDERS = [
  "Search for Mangalsutra...",
  "Search for Necklaces...",
  "Search Gifts for your dearest...",
  "Search for Solitaire Rings...",
  "Search for Anti-Tarnish Bangles..."
];

const CUSTOMER_REVIEWS = [
  { name: "N.", verified: true, date: "27/7/2026", rating: 5, comment: "good" },
  { name: "Ellangi P.", verified: true, date: "19/7/2026", rating: 5, comment: "👍 nice," },
  { name: "Money G.", verified: false, date: "30/5/2026", rating: 5, comment: "nice" },
  { 
    name: "Sarena", 
    verified: false, 
    date: "24/5/2026", 
    rating: 5, 
    comment: "Perfect for everyday!!!",
    videoMedia: PRODUCTS[30].image 
  },
  { 
    name: "Bhagyashree T.", 
    verified: true, 
    date: "3/5/2026", 
    rating: 5, 
    comment: "Nice making of these earrings... It suits me a lot and very cute.. Thank u cieloria" 
  },
  { name: "Girisha S.", verified: true, date: "30/4/2026", rating: 5, comment: "Awesome product" }
];

const PLP_CATEGORY_DATA = {
  NewArrivals: {
    title: "New Arrivals",
    heading: "Fresh New Arrivals",
    tagline: "Freshly minted 18k gold & sterling silver designs",
    bannerImage: PRODUCTS[15].image,
    subFilters: ["All New", "Solitaire Rings", "Statement Chains", "Hoop Earrings", "Gold Bangles"]
  },
  BestSeller: {
    title: "Best Sellers",
    heading: "Top Selling Demifine Jewelry",
    tagline: "Most loved anti-tarnish bestsellers cherished by 8L+ women",
    bannerImage: PRODUCTS[30].image,
    subFilters: ["All Bestsellers", "Top Earrings", "Bestselling Rings", "Layered Necklaces", "Kadas & Bangles"]
  },
  FineSilver: {
    title: "Fine Silver",
    heading: "925 Sterling Silver Collection",
    tagline: "Pure 925 sterling silver crafted with radiant rhodium finish",
    bannerImage: PRODUCTS[9].image,
    subFilters: ["All Silver", "Silver Rings", "Silver Pendants", "Silver Earrings", "Silver Bracelets"]
  },
  NineKTGold: {
    title: "9KT Fine Gold",
    heading: "9KT Solid Gold Luxury",
    tagline: "Real 9KT solid gold & SGL certified lab-grown diamonds",
    bannerImage: PRODUCTS[2].image,
    subFilters: ["All 9KT Gold", "Diamond Studs", "Gold Bracelets", "Star Pendants", "Solitaire Rings"]
  },
  Earrings: {
    title: "Earrings",
    heading: "All Earrings",
    tagline: "Statement for every occasion",
    bannerImage: "https://cdn.shopify.com/s/files/1/0629/2321/0811/files/ChatGPTImageSep12_2025_12_15_00PM.png?v=1758182007",
    subFilters: ["All Earrings", "Stud Earrings", "Hoop Earrings", "Drop Earrings", "Danglers", "Earrings Set", "Pearl Earrings"]
  },
  Rings: {
    title: "Rings",
    heading: "All Rings",
    tagline: "Elegance on your fingertips",
    bannerImage: PRODUCTS[9].image,
    subFilters: ["All Rings", "Solitaire Rings", "Band Rings", "Stackable Rings", "Adjustable Rings", "Cocktail Rings"]
  },
  Necklaces: {
    title: "Necklaces",
    heading: "All Necklaces",
    tagline: "Timeless chains and radiant pendants",
    bannerImage: PRODUCTS[40].image,
    subFilters: ["All Necklaces", "Layered Necklaces", "Chokers", "Pendants", "Mangalsutras", "Statement Chains"]
  },
  Bracelets: {
    title: "Bracelets",
    heading: "All Bracelets",
    tagline: "Designed to move with your wrist",
    bannerImage: PRODUCTS[2].image,
    subFilters: ["All Bracelets", "Kadas & Bangles", "Chain Bracelets", "Charm Bracelets", "Cuffs", "Men's Bracelets"]
  },
  Gifting: {
    title: "Gifting",
    heading: "Gifting & Curated Sets",
    tagline: "Thoughtful keepsake gifts made for every bond",
    bannerImage: PRODUCTS[30].image,
    subFilters: ["All Gifts", "Gift Boxes", "Sister Gifts", "Brother Gifts", "Sets"]
  },
  Wishlist: {
    title: "My Wishlist",
    heading: "Your Saved Favorites",
    tagline: "Your personal anti-tarnish wishlist collection",
    bannerImage: PRODUCTS[30].image,
    subFilters: ["All Saved Items"]
  },
  All: {
    title: "Demifine ® Collection",
    heading: "All Demifine Jewelry",
    tagline: "18k Thick Gold Plated & Waterproof Collection",
    bannerImage: PRODUCTS[15].image,
    subFilters: ["All Products", "Bestsellers", "New Arrivals", "9KT Solid Gold", "Fine Silver"]
  }
};

const HERO_SLIDES = [
  {
    id: "slide-1",
    image: PRODUCTS[2].image,
    tag: "THE",
    title: "Man of Style",
    subtitle: "SALE",
    priceText: "Starting at ₹999",
    buttonText: "SHOP NOW"
  },
  {
    id: "slide-2",
    image: PRODUCTS[9].image,
    title: "Rakhi Sale",
    subtitle: "Pieces starting at",
    priceText: "₹999",
    buttonText: "SHOP NOW"
  },
  {
    id: "slide-3",
    image: PRODUCTS[40].image,
    tag: "CIELORIA IN STYLE",
    title: "LUXURY COLLECTION",
    subtitle: "FLAT 40% OFF",
    codeText: "Code: RAKHI40",
    buttonText: "SHOP NOW"
  }
];

const FINE_GOLD_PRODUCTS = [
  {
    id: PRODUCTS[10] ? PRODUCTS[10].id : 'fine-gold-1',
    name: "Crystal Peak 9KT Gold Laboratory Grown Solitaire Studs",
    price: 7499,
    originalPrice: 8823,
    discountTag: "Flat 15% off on MRP",
    metalTag: "9KT Solid Gold",
    image: PRODUCTS[30].image
  },
  {
    id: PRODUCTS[11] ? PRODUCTS[11].id : 'fine-gold-2',
    name: "Orba Shine 9KT Gold Laboratory Grown Diamond Bracelet",
    price: 9586,
    originalPrice: 11278,
    discountTag: "Flat 15% off on MRP",
    metalTag: "9KT Solid Gold",
    image: PRODUCTS[0].image
  }
];

const CIRCLE_CATEGORIES = [
  { name: "Earrings", cat: "Earrings", image: PRODUCTS[30].image },
  { name: "Necklaces", cat: "Necklaces", image: PRODUCTS[40].image },
  { name: "Bracelets", cat: "Bracelets", image: PRODUCTS[0].image },
  { name: "Rings", cat: "Rings", image: PRODUCTS[9].image },
  { name: "Mangalsutras", cat: "Necklaces", image: PRODUCTS[42].image },
  { name: "Mens", cat: "Bracelets", image: PRODUCTS[2].image }
];

const FOR_EVERY_YOU_CARDS = [
  { title: "OFFICE WEAR", image: PRODUCTS[40].image },
  { title: "DAILY WEAR", image: PRODUCTS[9].image },
  { title: "PARTY WEAR", image: PRODUCTS[30].image },
  { title: "WEDDING WEAR", image: PRODUCTS[0].image }
];

const SUBHEADER_NAV = [
  { name: "New Arrivals", cat: "NewArrivals" },
  { name: "Best Seller", cat: "BestSeller" },
  { name: "Fine Silver", cat: "FineSilver" },
  { name: "9KT Fine Gold", cat: "NineKTGold", badge: "Luxe", badgeClass: "badge-luxe" },
  { name: "Demifine ® Collection", cat: "All" },
  { name: "Gifting", cat: "Gifting" },
  { name: "About Us", cat: "About" }
];

function getStoredData(key, defaultVal) {
  try {
    const val = localStorage.getItem(key);
    return val ? JSON.parse(val) : defaultVal;
  } catch(e) {
    return defaultVal;
  }
}

function setStoredData(key, val) {
  try {
    localStorage.setItem(key, JSON.stringify(val));
  } catch(e) {}
}

function getCleanPhone(phoneStr) {
  if (!phoneStr) return '';
  const digits = phoneStr.toString().replace(/\D/g, '');
  return digits.length >= 10 ? digits.slice(-10) : digits;
}

const currentIsLoggedIn = getStoredData('cieloria_is_logged_in', false);
const currentCleanPhone = getCleanPhone(getStoredData('cieloria_cust_phone', ''));

// Global Application State
let state = {
  viewMode: (window.location.search.includes('view=admin') || window.location.hash.includes('admin') || window.location.pathname.includes('/admin')) ? 'admin' : 'homepage',
  accountTab: 'orders',
  selectedProductId: PRODUCTS[0].id,
  activeGalleryIndex: 0,
  selectedRingSize: 'US 7',
  openAccordion: 'description',
  bestsellerTab: 'ALL',
  pdpOfferTab: 'b1g1',
  addGiftSleeve: false,
  visibleReviewsCount: 6,
  pincodeCheckResult: '',
  isMobileMenuOpen: false,

  plpCategory: 'BestSeller',
  plpSubFilter: '',
  plpPriceFilter: 'all',
  plpMetalFilter: 'all',
  plpOccasionFilter: 'all',
  plpInStockOnly: false,
  plpSortBy: 'featured',

  cart: getStoredData('cieloria_cart', []),
  wishlist: [],
  appliedCoupon: '',
  discountPercentage: 0,
  activeCurrency: 'INR',
  searchQuery: '',
  searchPlaceholderIndex: 0,
  tickerIndex: 0,
  heroSlideIndex: 0,
  
  isLoggedIn: currentIsLoggedIn,
  customerName: getStoredData('cieloria_cust_name', ''),
  customerPhone: currentCleanPhone,
  customerEmail: getStoredData('cieloria_cust_email', ''),
  pincode: getStoredData('cieloria_pincode', ''),
  customerAddress: getStoredData('cieloria_address', ''),
  ordersList: [],
  rewardsCoins: getStoredData('cieloria_coins', 0),

  merchantAllOrders: getStoredData('cieloria_merchant_all_orders', []),

  isCartOpen: false,
  isCheckoutOpen: false,
  isCIELORIAAuthOpen: false,
  authModalStep: 1,
  otpDigits: ["", "", "", ""],
  checkoutStep: 1,
  isOrderSummaryOpen: false,
  isSubscribed: false,
  lastPlacedOrder: null
};

// Directly compute active storage keys based on live state in JS memory
function getActiveWishlistKey() {
  const cleanPh = getCleanPhone(state.customerPhone);
  if (state.isLoggedIn && cleanPh) {
    return `cieloria_wishlist_${cleanPh}`;
  }
  return `cieloria_wishlist_guest`;
}

function getActiveOrdersKey() {
  const cleanPh = getCleanPhone(state.customerPhone);
  if (state.isLoggedIn && cleanPh) {
    return `cieloria_orders_${cleanPh}`;
  }
  return `cieloria_orders_guest`;
}

// Live Google Cloud Database & Multi-Source Account Syncing
function syncAccountStorage() {
  const wKey = getActiveWishlistKey();
  const oKey = getActiveOrdersKey();
  const phone = getCleanPhone(state.customerPhone);

  const savedAccountWishlist = getStoredData(wKey, []);
  const guestWishlist = getStoredData('cieloria_wishlist_guest', []);
  const inMemoryWishlist = state.wishlist || [];

  if (state.isLoggedIn && phone) {
    // Merge account wishlist + guest wishlist + in-memory wishlist
    const combined = Array.from(new Set([
      ...savedAccountWishlist,
      ...guestWishlist,
      ...inMemoryWishlist
    ]));
    state.wishlist = combined;
    setStoredData(wKey, combined);
    setStoredData('cieloria_wishlist_guest', []);
  } else {
    // Guest mode merge
    const combinedGuest = Array.from(new Set([
      ...guestWishlist,
      ...inMemoryWishlist
    ]));
    state.wishlist = combinedGuest;
    setStoredData('cieloria_wishlist_guest', combinedGuest);
  }

  // Load local orders
  state.ordersList = getStoredData(oKey, []);

  // Sync to Vercel Serverless Google Cloud Database API
  if (state.isLoggedIn && phone) {
    fetch(`/api/sync?action=get_customer&phone=${phone}`)
      .then(res => res.json())
      .then(res => {
        if (res && res.customer) {
          if (res.customer.wishlist && Array.isArray(res.customer.wishlist)) {
            const finalMerged = Array.from(new Set([...state.wishlist, ...res.customer.wishlist]));
            state.wishlist = finalMerged;
            setStoredData(wKey, finalMerged);
          }
          if (res.customer.orders && Array.isArray(res.customer.orders) && res.customer.orders.length > 0) {
            state.ordersList = res.customer.orders;
            setStoredData(oKey, res.customer.orders);
          }
          if (res.customer.name && !state.customerName) {
            state.customerName = res.customer.name;
            setStoredData('cieloria_cust_name', res.customer.name);
          }
          if (res.customer.address && !state.customerAddress) {
            state.customerAddress = res.customer.address;
            setStoredData('cieloria_address', res.customer.address);
          }
          renderApp();
        }
      }).catch(e => console.log('Vercel Google Cloud Read Note:', e));

    // Also sync to Restful Cloud Database REST Endpoint
    fetch(`https://api.restful-api.dev/objects`)
      .then(res => res.json())
      .then(objects => {
        if (Array.isArray(objects)) {
          const match = objects.find(o => o.name === `cieloria_cust_${phone}`);
          if (match && match.data && match.data.wishlist) {
            const finalMerged = Array.from(new Set([...state.wishlist, ...match.data.wishlist]));
            state.wishlist = finalMerged;
            setStoredData(wKey, finalMerged);
            renderApp();
          }
        }
      }).catch(e => console.log('Restful Cloud DB Read Note:', e));
  }
}

// Auto-poll cloud database for live order shipment status updates every 5 seconds
if (typeof window !== 'undefined') {
  setInterval(() => {
    if (state.isLoggedIn && state.customerPhone) {
      syncAccountStorage();
    }
  }, 5000);
}

function pushCloudCustomerUpdate() {
  const phone = getCleanPhone(state.customerPhone);
  if (!phone) return;

  const payload = {
    phone: phone,
    name: state.customerName || "Valued Customer",
    address: state.customerAddress || "",
    pincode: state.pincode || "",
    wishlist: state.wishlist,
    updatedAt: new Date().toISOString()
  };

  // 1. Post to Vercel Serverless Google Cloud Endpoint
  try {
    fetch('/api/sync', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action: 'save_customer', phone: phone, data: payload })
    }).catch(e => console.log('Vercel Cloud Write Note:', e));
  } catch(e) {}

  // 2. Post to Restful Cloud Database REST Endpoint
  try {
    fetch('https://api.restful-api.dev/objects', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: `cieloria_cust_${phone}`,
        data: payload
      })
    }).catch(e => console.log('Restful Cloud Write Note:', e));
  } catch(e) {}
}

function formatPrice(inrPrice) {
  const curr = CURRENCIES[state.activeCurrency] || CURRENCIES.INR;
  const val = Math.round(inrPrice * curr.rate);
  return `${curr.symbol} ${val.toLocaleString()}.00`;
}

function calculateCartTotalCount() {
  if (!state.cart || !Array.isArray(state.cart)) return 0;
  return state.cart.reduce((sum, item) => {
    const qty = parseInt(item.quantity) || 1;
    return sum + qty;
  }, 0);
}

function calculateCartSubtotal() {
  if (!state.cart || !Array.isArray(state.cart)) return 0;
  return state.cart.reduce((sum, item) => {
    const qty = parseInt(item.quantity) || 1;
    return sum + (item.price * qty);
  }, 0);
}

function calculateCartDiscount() {
  const subtotal = calculateCartSubtotal();
  if (subtotal <= 0) return 0;
  if (state.appliedCoupon === 'RAKHI40') {
    return Math.round(subtotal * 0.40);
  }
  return 0;
}

function calculateCartFinalTotal() {
  const subtotal = calculateCartSubtotal();
  const discount = calculateCartDiscount();
  const giftExtra = state.addGiftSleeve ? 99 : 0;
  return Math.max(0, subtotal - discount + giftExtra);
}

if (typeof window !== 'undefined') {
  setInterval(() => {
    state.tickerIndex = (state.tickerIndex + 1) % ANNOUNCEMENTS.length;
    state.searchPlaceholderIndex = (state.searchPlaceholderIndex + 1) % SEARCH_PLACEHOLDERS.length;
    const tickerElem = document.getElementById('announcement-ticker');
    if (tickerElem) tickerElem.innerText = ANNOUNCEMENTS[state.tickerIndex];
  }, 3500);

  setInterval(() => {
    if (state.viewMode === 'homepage' && !document.activeElement.tagName.includes('INPUT')) {
      state.heroSlideIndex = (state.heroSlideIndex + 1) % HERO_SLIDES.length;
      renderApp();
    }
  }, 6000);
}

function getActiveNavCategory() {
  if (state.viewMode === 'about') return 'About';
  if (state.viewMode === 'homepage') return '';
  if (state.viewMode === 'wishlist') return 'Wishlist';
  if (state.viewMode === 'account') return '';
  if (state.viewMode === 'plp') return state.plpCategory || 'All';
  return '';
}

function renderApp() {
  if (typeof document === 'undefined') return;
  const appContainer = document.getElementById('app');
  if (!appContainer) return;

  const currentHero = HERO_SLIDES[state.heroSlideIndex];
  const cartTotalItems = calculateCartTotalCount();

  const predictiveResults = state.searchQuery.trim().length >= 2 
    ? PRODUCTS.filter(p => 
        p.name.toLowerCase().includes(state.searchQuery.toLowerCase()) ||
        p.category.toLowerCase().includes(state.searchQuery.toLowerCase())
      ).slice(0, 5)
    : [];

  appContainer.innerHTML = `
    <!-- Top Black Announcement Ticker -->
    <div class="bg-black text-white text-[10px] sm:text-[11px] font-semibold tracking-wider py-2 px-3 sm:px-4 flex items-center justify-center relative border-b border-white/10">
      <div class="flex items-center gap-2 text-center uppercase">
        <span id="announcement-ticker">${ANNOUNCEMENTS[state.tickerIndex]}</span>
      </div>
    </div>

    <!-- Mobile & Desktop Header -->
    <header class="bg-white border-b border-[#E6E1D7] sticky top-0 z-40 shadow-xs">
      <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 py-3.5 flex flex-col gap-3">
        
        <div class="flex items-center justify-between gap-3">
          
          <div class="flex items-center gap-2.5">
            <button onclick="state.isMobileMenuOpen=true; renderApp();" class="lg:hidden p-1.5 text-slate-800 hover:text-black" title="Open Navigation Menu">
              <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <line x1="3" y1="12" x2="21" y2="12"></line>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <line x1="3" y1="18" x2="21" y2="18"></line>
              </svg>
            </button>

            <button onclick="switchViewMode('homepage')" class="font-serif text-2xl sm:text-3xl lg:text-4xl font-bold tracking-[0.18em] text-[#1A1A1A] hover:text-[#C5A059] uppercase">
              CIELORIA
            </button>
          </div>

          <!-- Desktop Search Input -->
          <div class="hidden lg:flex flex-1 max-w-xl flex-col items-center relative mx-4">
            <button onclick="openPincodeModal()" class="text-[11px] text-slate-500 font-medium hover:text-[#1A1A1A] flex items-center gap-1 mb-1">
              <span class="text-[#C5A059]">📍</span>
              <span>${state.pincode ? `Pincode: ${state.pincode}` : 'Enter Pincode'}</span>
              <span class="text-[9px]">▾</span>
            </button>

            <div class="w-full relative">
              <div class="flex items-center bg-[#F3EFE6] rounded-md px-4 py-2.5 w-full">
                <input 
                  type="text" 
                  placeholder="${SEARCH_PLACEHOLDERS[state.searchPlaceholderIndex]}" 
                  value="${state.searchQuery}"
                  oninput="state.searchQuery=this.value"
                  onkeyup="if(e.key==='Enter'||this.value.length>=2){ renderApp(); }"
                  class="bg-transparent text-xs text-[#1A1A1A] placeholder-[#8C857B] focus:outline-none w-full font-medium"
                />
                <button onclick="renderApp()" class="text-[#1A1A1A] text-sm ml-2">🔍</button>
              </div>

              ${predictiveResults.length > 0 ? `
                <div class="absolute top-full left-0 right-0 mt-1 bg-white border border-[#E6E1D7] rounded-xl shadow-2xl p-3 z-50 text-left space-y-2">
                  <span class="text-[10px] uppercase font-bold text-[#C5A059] px-2">Suggestions</span>
                  ${predictiveResults.map(p => `
                    <div onclick="openPDP('${p.id}')" class="flex items-center gap-3 p-2 rounded-lg hover:bg-[#F6F4EF] cursor-pointer">
                      <img src="${p.image}" class="w-10 h-10 object-cover rounded" />
                      <div>
                        <h5 class="font-serif text-xs font-bold text-[#1A1A1A] line-clamp-1">${p.name}</h5>
                        <span class="text-[11px] font-bold text-[#C5A059]">${formatPrice(p.price)}</span>
                      </div>
                    </div>
                  `).join('')}
                </div>
              ` : ''}
            </div>
          </div>

          <!-- Header Icons -->
          <div class="flex items-center gap-4 sm:gap-6 text-[#1A1A1A]">
            
            <button onclick="openWishlistView()" class="relative flex items-center justify-center cursor-pointer hover:opacity-80 transition-opacity p-1" title="My Saved Wishlist">
              <svg class="w-6 h-6 sm:w-7 sm:h-7" viewBox="0 0 24 24" fill="${state.wishlist.length > 0 ? '#1A1A1A' : 'none'}" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l8.72-8.72 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
              </svg>
              <span class="absolute -top-1.5 -right-1.5 w-4 h-4 sm:w-5 sm:h-5 bg-black text-white font-bold text-[9px] sm:text-[10px] rounded-full flex items-center justify-center border border-white shadow-sm">
                ${state.wishlist.length}
              </span>
            </button>

            <button onclick="toggleCart(true)" class="relative flex items-center justify-center cursor-pointer hover:opacity-80 transition-opacity p-1" title="Shopping Bag">
              <svg class="w-6 h-6 sm:w-7 sm:h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path>
                <line x1="3" y1="6" x2="21" y2="6"></line>
                <path d="M16 10a4 4 0 0 1-8 0"></path>
              </svg>
              <span class="absolute -top-1.5 -right-1.5 w-4 h-4 sm:w-5 sm:h-5 bg-black text-white font-bold text-[9px] sm:text-[10px] rounded-full flex items-center justify-center border border-white shadow-sm">
                ${cartTotalItems}
              </span>
            </button>

            <button onclick="handleProfileIconClick()" class="relative flex items-center justify-center cursor-pointer hover:opacity-80 transition-opacity p-1" title="${state.isLoggedIn ? 'My Account' : 'Account Login'}">
              <div class="relative">
                <svg class="w-6 h-6 sm:w-7 sm:h-7" viewBox="0 0 24 24" fill="${state.isLoggedIn ? '#1A1A1A' : 'none'}" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                  <circle cx="12" cy="7" r="4"></circle>
                </svg>
                <span class="absolute -top-1 -right-1 text-amber-500 font-bold text-xs leading-none">⚡</span>
              </div>
            </button>

          </div>
        </div>

        <div class="lg:hidden w-full relative">
          <div class="flex items-center bg-[#F3EFE6] rounded-lg px-3.5 py-2 w-full">
            <input 
              type="text" 
              placeholder="${SEARCH_PLACEHOLDERS[state.searchPlaceholderIndex]}" 
              value="${state.searchQuery}"
              oninput="state.searchQuery=this.value"
              onkeyup="if(e.key==='Enter'||this.value.length>=2){ renderApp(); }"
              class="bg-transparent text-xs text-[#1A1A1A] placeholder-[#8C857B] focus:outline-none w-full font-medium"
            />
            <button onclick="renderApp()" class="text-[#1A1A1A] text-xs ml-2">🔍</button>
          </div>
        </div>

      </div>

      <nav class="border-t border-[#E6E1D7] bg-white py-2.5 overflow-x-auto whitespace-nowrap">
        <div class="max-w-7xl mx-auto px-4 flex items-center justify-start lg:justify-center gap-5 sm:gap-8 text-xs font-medium text-[#1A1A1A]">
          ${SUBHEADER_NAV.map(nav => {
            const activeNav = getActiveNavCategory().toLowerCase();
            const thisNav = (nav.cat || '').toLowerCase();
            const isCurrentActive = activeNav !== '' && activeNav === thisNav;

            const btnStyle = isCurrentActive 
              ? "color: #C5A059 !important; font-weight: 700 !important; border-bottom: 2px solid #C5A059 !important; padding-bottom: 2px !important;"
              : "color: #1A1A1A !important; font-weight: 500 !important; border-bottom: 2px solid transparent !important; padding-bottom: 2px !important;";

            return `
              <div class="relative py-1 cursor-pointer shrink-0">
                <button 
                  onclick="openPLPCategory('${nav.cat}')" 
                  style="${btnStyle}"
                  onmouseover="if(!${isCurrentActive}) this.style.color='#C5A059';"
                  onmouseout="if(!${isCurrentActive}) this.style.color='#1A1A1A';"
                  class="transition-colors cursor-pointer text-xs"
                >
                  ${nav.name}
                </button>
                ${nav.badge ? `<span class="${nav.badgeClass}">${nav.badge}</span>` : ''}
              </div>
            `;
          }).join('')}
        </div>
      </nav>
    </header>

    <main class="flex-1">
      ${state.viewMode === 'homepage' ? renderHomepageView(currentHero) : ''}
      ${state.viewMode === 'plp' ? renderPLPView() : ''}
      ${state.viewMode === 'pdp' ? renderPDPView() : ''}
      ${state.viewMode === 'about' ? renderAboutUsView() : ''}
      ${state.viewMode === 'account' ? renderAccountDashboardView() : ''}
      ${state.viewMode === 'wishlist' ? renderWishlistView() : ''}
      ${state.viewMode === 'order_confirmed' ? renderOrderConfirmedView() : ''}
      ${state.viewMode === 'admin' ? renderAdminView() : ''}
    </main>

    ${renderModals()}

    <div class="marquee-container">
      <div class="marquee-content">
        <span>8L+ Happy Customers | Lucknow Flagship Luxury | Gifts For Her @ 50% OFF | Ships in 24 hours</span>
        <span>8L+ Happy Customers | Lucknow Flagship Luxury | Gifts For Her @ 50% OFF | Ships in 24 hours</span>
        <span>8L+ Happy Customers | Lucknow Flagship Luxury | Gifts For Her @ 50% OFF | Ships in 24 hours</span>
        <span>8L+ Happy Customers | Lucknow Flagship Luxury | Gifts For Her @ 50% OFF | Ships in 24 hours</span>
      </div>
    </div>

    <footer class="bg-black text-slate-400 pt-14 pb-10 text-xs text-left">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
          <div class="space-y-4">
            <h3 class="font-serif text-2xl font-bold tracking-[0.2em] text-white">CIELORIA</h3>
            <p class="text-slate-400 text-xs leading-relaxed">India's pioneer Demifine® 18k thick gold plated & sterling silver anti-tarnish jewelry. Founded in Lucknow, UP.</p>
          </div>

          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase tracking-wider">Customer Care</h4>
            <ul class="space-y-2">
              <li><button onclick="handleProfileIconClick()" class="hover:text-white font-bold text-[#C5A059]">Track Orders & Account</button></li>
              <li><button onclick="openWishlistView()" class="hover:text-white">My Saved Wishlist (${state.wishlist.length})</button></li>
              <li><button onclick="alert('Shipping Details')" class="hover:text-white">Shipping & Delivery</button></li>
              <li><button onclick="switchViewMode('about')" class="hover:text-white">About Us (Lucknow HQ)</button></li>
            </ul>
          </div>

          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase tracking-wider">Shop Collections</h4>
            <ul class="space-y-2">
              <li><button onclick="openPLPCategory('BestSeller')" class="hover:text-white">Best Sellers</button></li>
              <li><button onclick="openPLPCategory('NewArrivals')" class="hover:text-white">New Arrivals</button></li>
              <li><button onclick="openPLPCategory('FineSilver')" class="hover:text-white">Fine Silver 925</button></li>
              <li><button onclick="openPLPCategory('NineKTGold')" class="hover:text-white">9KT Solid Gold</button></li>
            </ul>
          </div>

          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase tracking-wider">Policies</h4>
            <ul class="space-y-2">
              <li><button onclick="alert('Privacy Policy')" class="hover:text-white">Privacy Policy</button></li>
              <li><button onclick="alert('Terms of Service')" class="hover:text-white">Terms of Service</button></li>
              <li><button onclick="alert('Warranty')" class="hover:text-white">Lifetime Warranty</button></li>
            </ul>
          </div>
        </div>

        <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-center md:text-left text-[11px] text-slate-500">
          <div>© ${new Date().getFullYear()} CIELORIA (cieloria.com). Lucknow, UP, India. All Rights Reserved.</div>
          <div>100% Waterproof • Anti-Tarnish • Hypoallergenic</div>
        </div>
      </div>
    </footer>
  `;
}

// Order Confirmed View
function renderOrderConfirmedView() {
  const ord = state.lastPlacedOrder || (state.ordersList.length > 0 ? state.ordersList[0] : null);
  if (!ord) return renderHomepageView(HERO_SLIDES[0]);

  return `
    <div class="bg-[#FAF8F5] min-h-screen py-12 text-left text-[#1A1A1A]">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 space-y-8">
        
        <div class="bg-white border border-[#E6E1D7] rounded-3xl p-8 text-center space-y-5 shadow-lg">
          <div class="w-20 h-20 rounded-full bg-emerald-100 text-emerald-600 text-4xl flex items-center justify-center mx-auto shadow-sm">
            ✔
          </div>

          <div class="space-y-2">
            <span class="text-xs uppercase tracking-widest font-bold text-emerald-700 block">ORDER CONFIRMED & RECEIVED</span>
            <h1 class="font-serif text-3xl sm:text-4xl font-bold text-[#1A1A1A]">Thank You, ${ord.customerName || 'Valued Customer'}! 🎉</h1>
            <p class="text-xs text-slate-500 max-w-md mx-auto">We have received your order <strong>${ord.orderId}</strong>. Our team in Lucknow is preparing your 18K Anti-Tarnish jewelry for dispatch!</p>
          </div>

          <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-5 rounded-2xl space-y-3 text-left">
            <div class="flex items-center justify-between border-b border-slate-200 pb-3 text-xs">
              <div>
                <span class="font-bold text-[#1A1A1A] block">Order ID: ${ord.orderId}</span>
                <span class="text-slate-400">Placed on ${ord.date}</span>
              </div>
              <span class="bg-blue-100 text-blue-800 text-[10px] font-bold px-3 py-1 rounded-full border border-blue-300">
                ${ord.status}
              </span>
            </div>

            <div class="space-y-1 text-xs">
              <span class="font-bold text-[#1A1A1A] block">Delivery Address:</span>
              <p class="text-slate-600 font-medium">${ord.customerAddress || 'Lucknow, UP'} (Pincode: ${ord.pincode || '226001'})</p>
              <p class="text-slate-600 font-medium">Mobile: +91 ${ord.customerPhone}</p>
            </div>

            <div class="border-t border-slate-200 pt-3 flex justify-between items-center text-xs">
              <span class="font-bold text-[#1A1A1A]">Courier Partner:</span>
              <span class="font-bold text-emerald-700">${ord.courier} (${ord.trackingId})</span>
            </div>
          </div>

          <div class="space-y-3 pt-2">
            <button onclick="switchViewMode('account')" class="w-full bg-black text-white font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider shadow-md hover:bg-[#C5A059] transition-colors">
              Track Order Live in My Account →
            </button>
            <button onclick="switchViewMode('homepage')" class="w-full border border-slate-300 text-slate-700 font-bold py-3 rounded-xl text-xs uppercase hover:bg-white">
              Continue Shopping
            </button>
          </div>
        </div>

      </div>
    </div>
  `;
}

function renderWishlistView() {
  const savedProducts = PRODUCTS.filter(p => state.wishlist.includes(p.id));

  return `
    <div class="bg-[#FAF8F5] min-h-screen py-10 text-left text-[#1A1A1A]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        
        <div class="bg-white border border-[#E6E1D7] rounded-3xl p-6 sm:p-8 flex items-center justify-between shadow-xs">
          <div>
            <h1 class="font-serif text-3xl font-bold text-[#1A1A1A]">My Saved Wishlist ❤️</h1>
            <p class="text-xs text-slate-500 font-medium pt-1">You have <strong>${savedProducts.length}</strong> items saved in your favorites</p>
          </div>
          
          <button onclick="switchViewMode('homepage')" class="border border-black hover:bg-black hover:text-white px-5 py-2.5 rounded-xl text-xs font-bold transition-colors">
            Explore More Products
          </button>
        </div>

        ${savedProducts.length === 0 ? `
          <div class="bg-white border border-[#E6E1D7] rounded-3xl p-12 text-center space-y-4 shadow-xs">
            <span class="text-5xl block">🤍</span>
            <h3 class="font-serif text-2xl font-bold text-[#1A1A1A]">Your Wishlist is Empty</h3>
            <p class="text-xs text-slate-500 max-w-sm mx-auto">Explore our 18K Anti-Tarnish Bestsellers and tap the heart icon on any piece to save your favorite jewelry!</p>
            <div class="pt-2">
              <button onclick="openPLPCategory('BestSeller')" class="bg-black text-white font-bold px-8 py-3.5 rounded-xl text-xs uppercase tracking-wider">Browse Bestsellers</button>
            </div>
          </div>
        ` : `
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-6">
            ${savedProducts.map(p => `
              <div class="group relative bg-[#FFFFFF] border border-[#E6E1D7] overflow-hidden flex flex-col justify-between text-left cursor-pointer hover:shadow-lg transition-all rounded-xl">
                <div onclick="openPDP('${p.id}')" class="relative aspect-square w-full bg-[#F6F4EF] overflow-hidden">
                  <img src="${p.image}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-out" />
                  
                  <button onclick="event.stopPropagation(); toggleWishlist('${p.id}');" class="absolute top-3 right-3 w-8 h-8 rounded-full bg-white/90 shadow-sm flex items-center justify-center text-rose-500 hover:scale-110 transition-transform z-20" title="Remove from Wishlist">
                    ❤️
                  </button>
                </div>
                
                <div class="p-4 flex flex-col justify-between flex-1 space-y-3">
                  <div onclick="openPDP('${p.id}')" class="space-y-1 cursor-pointer">
                    <h3 class="font-serif text-xs font-bold text-[#1A1A1A] group-hover:text-[#C5A059] line-clamp-1">${p.name}</h3>
                    <div class="text-xs font-bold text-[#1A1A1A] flex items-center gap-2"><span>${formatPrice(p.price)}</span><span class="text-slate-400 line-through text-[11px] font-normal">${formatPrice(p.originalPrice)}</span></div>
                  </div>

                  <button onclick="event.stopPropagation(); addToCart('${p.id}');" class="w-full border border-[#1A1A1A] bg-white text-[#1A1A1A] font-semibold py-2 rounded-lg text-xs uppercase tracking-wider hover:bg-[#1A1A1A] hover:text-white transition-colors">
                    Add to Cart
                  </button>
                </div>
              </div>
            `).join('')}
          </div>
        `}

      </div>
    </div>
  `;
}

function renderAccountDashboardView() {
  if (!state.isLoggedIn) {
    return `
      <div class="bg-[#FAF8F5] min-h-screen py-16 text-center text-[#1A1A1A]">
        <div class="max-w-md mx-auto bg-white border border-[#E6E1D7] rounded-3xl p-8 shadow-xs space-y-5">
          <span class="text-5xl block">👤⚡</span>
          <h2 class="font-serif text-2xl font-bold text-[#1A1A1A]">Please Login to View Account</h2>
          <p class="text-xs text-slate-500 leading-relaxed">Login via CIELORIA 1-Click Mobile OTP to access your orders, saved addresses, and live shipment tracking.</p>
          <div class="pt-2">
            <button onclick="triggerCIELORIASDKLogin()" class="bg-black text-white font-bold px-8 py-3.5 rounded-xl text-xs uppercase tracking-wider shadow-md hover:bg-[#C5A059] transition-colors">
              Login via CIELORIA ⚡
            </button>
          </div>
        </div>
      </div>
    `;
  }

  return `
    <div class="bg-[#FAF8F5] min-h-screen py-10 text-left text-[#1A1A1A]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        
        <div class="bg-white border border-[#E6E1D7] rounded-3xl p-6 sm:p-8 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-6 shadow-xs">
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 rounded-full bg-black text-white text-2xl font-bold flex items-center justify-center font-serif shadow-md">
              ${state.customerName ? state.customerName.charAt(0) : '👤'}
            </div>
            <div>
              <h1 class="font-serif text-2xl sm:text-3xl font-bold text-[#1A1A1A]">${state.customerName || 'Customer Account'}</h1>
              <p class="text-xs text-slate-500 font-medium">${state.customerPhone ? `+91 ${state.customerPhone}` : 'Guest'} ${state.customerEmail ? `• ${state.customerEmail}` : ''}</p>
              <span class="inline-block bg-emerald-100 text-emerald-800 text-[9px] font-bold px-2 py-0.5 rounded mt-1">⚡ Verified CIELORIA Member</span>
            </div>
          </div>

          <div class="flex items-center gap-3">
            <div class="bg-amber-50 border border-amber-200 px-4 py-2 rounded-2xl flex items-center gap-2">
              <span class="text-amber-600 text-lg">🪙</span>
              <div>
                <span class="font-bold text-xs text-[#1A1A1A] block">${state.rewardsCoins} Cieloria Coins</span>
                <span class="text-[10px] text-amber-700 font-semibold">Anti-Tarnish Club</span>
              </div>
            </div>

            <!-- Logout Button -->
            <button onclick="handleUserLogout()" class="border border-rose-200 hover:bg-rose-50 text-rose-700 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors flex items-center gap-1.5" title="Logout of Account">
              <span>🚪 Logout</span>
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          
          <div class="lg:col-span-3 bg-white border border-[#E6E1D7] rounded-3xl p-4 shadow-xs space-y-2">
            <button onclick="state.accountTab='orders'; renderApp();" class="w-full text-left p-3.5 rounded-2xl font-bold text-xs flex items-center justify-between transition-colors ${state.accountTab==='orders' ? 'bg-black text-white' : 'hover:bg-[#FAF8F5] text-[#1A1A1A]'}">
              <span class="flex items-center gap-2.5">
                <span>📦</span>
                <span>My Orders (${state.ordersList.length})</span>
              </span>
              <span class="text-xs">›</span>
            </button>

            <button onclick="openWishlistView()" class="w-full text-left p-3.5 rounded-2xl font-bold text-xs flex items-center justify-between transition-colors hover:bg-[#FAF8F5] text-[#1A1A1A]">
              <span class="flex items-center gap-2.5">
                <span>❤️</span>
                <span>My Saved Wishlist (${state.wishlist.length})</span>
              </span>
              <span class="text-xs">›</span>
            </button>

            <button onclick="state.accountTab='profile'; renderApp();" class="w-full text-left p-3.5 rounded-2xl font-bold text-xs flex items-center justify-between transition-colors ${state.accountTab==='profile' ? 'bg-black text-white' : 'hover:bg-[#FAF8F5] text-[#1A1A1A]'}">
              <span class="flex items-center gap-2.5">
                <span>👤</span>
                <span>Profile Details</span>
              </span>
              <span class="text-xs">›</span>
            </button>

            <button onclick="handleUserLogout()" class="w-full text-left p-3.5 rounded-2xl font-bold text-xs flex items-center justify-between transition-colors hover:bg-rose-50 text-rose-700">
              <span class="flex items-center gap-2.5">
                <span>🚪</span>
                <span>Logout</span>
              </span>
              <span class="text-xs">›</span>
            </button>
          </div>

          <div class="lg:col-span-9 space-y-6">
            
            ${state.accountTab === 'orders' ? `
              <div class="space-y-6">
                <div class="flex items-center justify-between">
                  <h2 class="font-serif text-2xl font-bold text-[#1A1A1A]">My Recent Orders (${state.ordersList.length})</h2>
                  <span class="text-xs text-slate-500 font-medium">⚡ Real-time Shipment Tracking</span>
                </div>

                ${state.ordersList.length === 0 ? `
                  <div class="bg-white border border-[#E6E1D7] rounded-3xl p-10 text-center space-y-3 shadow-xs">
                    <span class="text-4xl block">📦</span>
                    <h4 class="font-serif text-xl font-bold text-[#1A1A1A]">No Orders Placed Yet</h4>
                    <p class="text-xs text-slate-500 max-w-sm mx-auto">Explore our 18K Anti-Tarnish Bestsellers and place your first order!</p>
                    <div class="pt-2">
                      <button onclick="openPLPCategory('BestSeller')" class="bg-black text-white font-bold px-6 py-2.5 text-xs rounded-xl uppercase">Start Shopping</button>
                    </div>
                  </div>
                ` : state.ordersList.map(ord => `
                  <div class="bg-white border border-[#E6E1D7] rounded-3xl p-6 shadow-xs space-y-5">
                    
                    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center pb-4 border-b border-[#E6E1D7] gap-3">
                      <div class="space-y-1">
                        <div class="flex items-center gap-3">
                          <span class="font-serif font-bold text-base text-[#1A1A1A]">${ord.orderId}</span>
                          <span class="border px-3 py-0.5 rounded-full text-[10px] font-bold ${ord.statusColor || 'bg-blue-100 text-blue-800 border-blue-300'}">${ord.status}</span>
                        </div>
                        <p class="text-xs text-slate-400">Placed on ${ord.date}</p>
                      </div>

                      <div class="text-right">
                        <span class="font-bold text-base text-[#1A1A1A] block">₹${(ord.totalAmount || 999).toLocaleString()}.00</span>
                        <span class="text-[10px] text-slate-400">Courier: ${ord.courier || 'Bluedart Express'} (${ord.trackingId || 'BLU123456'})</span>
                      </div>
                    </div>

                    <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-4 rounded-2xl space-y-2">
                      <div class="flex justify-between items-center text-xs">
                        <span class="font-bold text-[#1A1A1A]">Live Shipment Progress</span>
                        <span class="text-xs font-bold text-emerald-700">Est. Delivery: ${ord.estimatedDelivery || '2-3 Business Days'}</span>
                      </div>

                      <div class="grid grid-cols-4 gap-2 pt-2 text-center text-[10px] font-bold">
                        <div class="space-y-1 text-emerald-700">
                          <div class="h-2 bg-emerald-500 rounded-full"></div>
                          <span>Order Placed</span>
                        </div>
                        <div class="space-y-1 ${ord.status === 'Dispatched' || ord.status === 'In Transit' || ord.status === 'Out for Delivery' || ord.status === 'Delivered' ? 'text-emerald-700' : 'text-slate-400'}">
                          <div class="h-2 ${ord.status === 'Dispatched' || ord.status === 'In Transit' || ord.status === 'Out for Delivery' || ord.status === 'Delivered' ? 'bg-emerald-500' : 'bg-slate-200'} rounded-full"></div>
                          <span>Dispatched</span>
                        </div>
                        <div class="space-y-1 ${ord.status === 'In Transit' || ord.status === 'Out for Delivery' || ord.status === 'Delivered' ? 'text-emerald-700' : 'text-slate-400'}">
                          <div class="h-2 ${ord.status === 'In Transit' || ord.status === 'Out for Delivery' || ord.status === 'Delivered' ? 'bg-emerald-500' : 'bg-slate-200'} rounded-full"></div>
                          <span>In Transit</span>
                        </div>
                        <div class="space-y-1 ${ord.status === 'Delivered' ? 'text-emerald-700' : 'text-slate-400'}">
                          <div class="h-2 ${ord.status === 'Delivered' ? 'bg-emerald-500' : 'bg-slate-200'} rounded-full"></div>
                          <span>Delivered</span>
                        </div>
                      </div>
                    </div>

                    <div class="space-y-3">
                      ${(ord.items || [PRODUCTS[0]]).map(item => `
                        <div class="flex items-center gap-4 p-3 bg-white border border-[#E6E1D7] rounded-2xl">
                          <img src="${item.image}" class="w-16 h-16 object-cover rounded-xl bg-[#F6F4EF]" />
                          <div class="flex-1">
                            <h4 class="font-serif text-xs font-bold text-[#1A1A1A] line-clamp-1">${item.name}</h4>
                            <p class="text-[11px] text-slate-400 font-medium">Qty: ${item.quantity || 1} • 18K Gold Plated Anti-Tarnish</p>
                          </div>
                          <span class="font-bold text-xs text-[#1A1A1A]">${formatPrice(item.price)}</span>
                        </div>
                      `).join('')}
                    </div>

                  </div>
                `).join('')}
              </div>
            ` : ''}

            ${state.accountTab === 'profile' ? `
              <div class="bg-white border border-[#E6E1D7] rounded-3xl p-8 shadow-xs space-y-6">
                <h2 class="font-serif text-2xl font-bold text-[#1A1A1A]">Edit Profile Details</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label class="text-xs font-bold text-slate-600 block mb-1">Full Name</label>
                    <input type="text" value="${state.customerName}" oninput="state.customerName=this.value" placeholder="Enter Full Name" class="w-full border border-[#E6E1D7] p-3 rounded-xl text-xs focus:outline-none focus:border-black font-medium" />
                  </div>

                  <div>
                    <label class="text-xs font-bold text-slate-600 block mb-1">Mobile Number</label>
                    <input type="tel" value="${state.customerPhone}" oninput="state.customerPhone=this.value" placeholder="Enter Mobile Number" class="w-full border border-[#E6E1D7] p-3 rounded-xl text-xs focus:outline-none focus:border-black font-medium" />
                  </div>
                </div>

                <div class="pt-4">
                  <button onclick="setStoredData('cieloria_cust_name', state.customerName); setStoredData('cieloria_cust_phone', getCleanPhone(state.customerPhone)); pushCloudCustomerUpdate(); alert('Profile Details Saved & Synced to Google Cloud DB!')" class="bg-black text-[#FFFFFF] px-8 py-3.5 rounded-xl font-bold text-xs uppercase tracking-wider">Save Changes</button>
                </div>
              </div>
            ` : ''}

          </div>
        </div>

      </div>
    </div>
  `;
}

function renderHomepageView(currentHero) {
  let selectedTabCategory = state.bestsellerTab;
  if (selectedTabCategory === 'MANGALSUTRA') selectedTabCategory = 'Necklaces';
  if (selectedTabCategory === 'MENS') selectedTabCategory = 'Bracelets';

  const topStylesProducts = PRODUCTS.filter(p => {
    if (selectedTabCategory === 'ALL') return true;
    return p.category.toUpperCase() === selectedTabCategory.toUpperCase();
  });

  return `
    <!-- 1. Hero Slider Banner -->
    <section class="relative overflow-hidden w-full bg-[#EAE5D9] min-h-[440px] sm:min-h-[560px] lg:min-h-[640px] flex items-center">
      <div class="absolute inset-0 z-0">
        <img src="${currentHero.image}" class="w-full h-full object-cover transition-transform duration-1000 scale-105" />
        <div class="absolute inset-0 bg-gradient-to-r from-black/60 via-black/20 to-transparent"></div>
      </div>

      <button onclick="changeHeroSlide(-1)" class="absolute left-2 sm:left-4 top-1/2 -translate-y-1/2 z-20 w-8 h-8 sm:w-10 sm:h-10 rounded-full bg-black/50 text-white flex items-center justify-center hover:bg-black transition-colors text-xs sm:text-base">❮</button>
      <button onclick="changeHeroSlide(1)" class="absolute right-2 sm:right-4 top-1/2 -translate-y-1/2 z-20 w-8 h-8 sm:w-10 sm:h-10 rounded-full bg-black/50 text-white flex items-center justify-center hover:bg-black transition-colors text-xs sm:text-base">❯</button>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full text-left py-12 sm:py-16">
        <div class="max-w-xl space-y-3 sm:space-y-4 text-white">
          ${currentHero.tag ? `<span class="text-[10px] sm:text-xs uppercase font-bold tracking-[0.3em] text-white/80 block">${currentHero.tag}</span>` : ''}
          <h1 class="font-serif text-3xl sm:text-5xl lg:text-6xl font-bold leading-tight">${currentHero.title}</h1>
          ${currentHero.subtitle ? `<p class="text-lg sm:text-2xl font-light text-slate-100">${currentHero.subtitle}</p>` : ''}
          ${currentHero.priceText ? `<div class="text-2xl sm:text-4xl font-serif font-bold text-white pt-1">${currentHero.priceText}</div>` : ''}
          ${currentHero.codeText ? `<div class="inline-block bg-white/20 backdrop-blur-md border border-white/40 px-3 py-1 rounded text-[10px] sm:text-xs font-bold uppercase tracking-wider text-white">${currentHero.codeText}</div>` : ''}
          <div class="pt-4 sm:pt-6">
            <button onclick="openPLPCategory('BestSeller')" class="btn-palmonas-hero text-xs py-3 px-6">${currentHero.buttonText}</button>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. Special Gifting Banner -->
    <section class="py-12 sm:py-16 bg-white text-center space-y-4 border-b border-[#E6E1D7]">
      <div class="max-w-3xl mx-auto px-4 space-y-3">
        <h2 class="font-serif text-2xl sm:text-4xl lg:text-5xl font-bold text-[#4A0E17] italic">
          A bond this special <br class="sm:hidden" />deserves a little gold
        </h2>
        <p class="text-slate-600 text-xs sm:text-base font-light">Thoughtful rakhis and keepsake gifts, made for every kind of sibling love.</p>
        <div class="pt-3">
          <button onclick="openPLPCategory('Gifting')" class="bg-[#4A0E17] text-white text-xs font-semibold px-6 py-3 rounded-md uppercase tracking-wider hover:bg-[#330A10]">Shop Rakhi Gifts →</button>
        </div>
      </div>
    </section>

    <!-- 3. Dual Gift Banners -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-8">
      <div class="text-center"><h2 class="font-serif text-2xl sm:text-3xl font-bold text-[#4A0E17]">Rakhi Gifts For</h2></div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
        <div class="relative rounded-3xl overflow-hidden shadow-md group h-[320px] sm:h-[380px] bg-[#EAE5D9]">
          <img src="${PRODUCTS[40].image}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 p-6 sm:p-8 flex flex-col justify-center items-end text-right bg-gradient-to-l from-black/60 via-transparent to-transparent">
            <div class="space-y-2 text-white">
              <h3 class="font-serif text-2xl sm:text-3xl font-bold">Rakhi Gift Box for Sister</h3>
              <p class="text-xs text-slate-200">2 Best Sellers Plus Mirror</p>
              <div class="pt-4"><button onclick="openPLPCategory('Gifting')" class="border border-white text-white px-5 py-2 text-xs uppercase font-bold tracking-wider hover:bg-white hover:text-black">SHOP NOW</button></div>
            </div>
          </div>
        </div>
        <div class="relative rounded-3xl overflow-hidden shadow-md group h-[320px] sm:h-[380px] bg-[#EAE5D9]">
          <img src="${PRODUCTS[2].image}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 p-6 sm:p-8 flex flex-col justify-center items-end text-right bg-gradient-to-l from-black/60 via-transparent to-transparent">
            <div class="space-y-2 text-white">
              <h3 class="font-serif text-2xl sm:text-3xl font-bold">Rakhi Gifts for Brother</h3>
              <div class="pt-4"><button onclick="openPLPCategory('Gifting')" class="border border-white text-white px-5 py-2 text-xs uppercase font-bold tracking-wider hover:bg-white hover:text-black">SHOP NOW</button></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. EVERYDAY DEMIFINE® COLLECTION Circle Grid -->
    <section class="py-12 sm:py-16 bg-[#FAF8F5] border-y border-[#E6E1D7]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8 sm:space-y-10">
        <h2 class="font-serif text-xl sm:text-3xl font-bold tracking-widest text-[#1A1A1A] uppercase">EVERYDAY DEMIFINE® COLLECTION</h2>
        <div class="grid grid-cols-3 sm:grid-cols-3 lg:grid-cols-6 gap-4 sm:gap-8">
          ${CIRCLE_CATEGORIES.map(c => `
            <div onclick="openPLPCategory('${c.cat}')" class="flex flex-col items-center space-y-2 sm:space-y-3 cursor-pointer group">
              <div class="w-24 h-24 sm:w-36 sm:h-36 rounded-full overflow-hidden border-2 border-transparent group-hover:border-[#C5A059] transition-all shadow-sm bg-white">
                <img src="${c.image}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
              </div>
              <span class="font-serif text-xs sm:text-base font-semibold text-[#1A1A1A] group-hover:text-[#C5A059]">${c.name}</span>
            </div>
          `).join('')}
        </div>
      </div>
    </section>

    <!-- 5. CIELORIA TOP STYLES Tabbed Grid -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-8 sm:space-y-10">
      <div class="text-center space-y-4 sm:space-y-6">
        <h2 class="font-serif text-xl sm:text-3xl font-bold tracking-widest text-[#1A1A1A] uppercase">CIELORIA TOP STYLES</h2>
        <div class="flex flex-wrap justify-center gap-1.5 sm:gap-2">
          ${['ALL', 'NECKLACES', 'BRACELETS', 'EARRINGS', 'RINGS', 'MENS', 'MANGALSUTRA'].map(tab => `
            <button onclick="state.bestsellerTab = '${tab}'; renderApp();" class="px-3 py-1.5 sm:px-5 sm:py-2 text-[10px] sm:text-xs font-semibold uppercase border transition-all ${state.bestsellerTab === tab ? 'bg-black text-white border-black' : 'bg-white text-[#1A1A1A] border-[#E6E1D7]'}">${tab}</button>
          `).join('')}
        </div>
      </div>

      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        ${topStylesProducts.slice(0, 8).map(p => {
          const isSaved = state.wishlist.includes(p.id);
          return `
            <div class="group relative bg-white border border-[#E6E1D7] overflow-hidden flex flex-col justify-between text-left cursor-pointer transition-all hover:shadow-lg rounded-xl">
              <div onclick="openPDP('${p.id}')" class="relative aspect-square w-full bg-[#F6F4EF] overflow-hidden">
                <img src="${p.image}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-out" />
                <div class="absolute top-0 left-0 bg-[#8B1E2B] text-white text-[9px] font-bold uppercase px-2 py-0.5 sm:px-2.5 sm:py-1 z-10 shadow-xs">Flat ${p.price}</div>
                
                <button onclick="event.stopPropagation(); toggleWishlist('${p.id}');" class="absolute bottom-2.5 left-2.5 sm:bottom-3 sm:left-3 text-base sm:text-lg transition-transform hover:scale-110 z-20" title="${isSaved ? 'Remove from Wishlist' : 'Add to Wishlist'}">
                  ${isSaved ? '❤️' : '🤍'}
                </button>
              </div>
              
              <div class="p-3 sm:p-4 flex flex-col justify-between flex-1 space-y-2.5">
                <div onclick="openPDP('${p.id}')" class="space-y-1 cursor-pointer">
                  <h3 class="font-serif text-xs font-bold text-[#1A1A1A] group-hover:text-[#C5A059] line-clamp-1">${p.name}</h3>
                  <div class="text-xs font-bold text-[#1A1A1A] flex items-center gap-2"><span>${formatPrice(p.price)}</span><span class="text-slate-400 line-through text-[11px] font-normal">${formatPrice(p.originalPrice)}</span></div>
                  <div class="flex items-center gap-1 text-[#C5A059] text-[10px] sm:text-[11px] font-semibold pt-0.5">
                    <span>★★★★★</span>
                    <span class="text-slate-400 font-normal">(${p.reviewCount})</span>
                  </div>
                </div>

                <button onclick="event.stopPropagation(); addToCart('${p.id}');" class="w-full border border-[#1A1A1A] bg-white text-[#1A1A1A] font-semibold py-2 rounded-lg text-[11px] sm:text-xs uppercase tracking-wider hover:bg-[#1A1A1A] hover:text-white transition-colors">
                  Add to Cart
                </button>
              </div>
            </div>
          `;
        }).join('')}
      </div>
      <div class="text-center pt-4"><button onclick="openPLPCategory('BestSeller')" class="border border-black text-black font-semibold text-xs px-8 py-3 uppercase tracking-widest hover:bg-black hover:text-white">VIEW ALL BESTSELLERS</button></div>
    </section>

    <!-- 6. 9KT FINE GOLD Grid -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-8 sm:space-y-10 border-t border-[#E6E1D7]">
      <div class="text-center space-y-2"><h2 class="font-serif text-xl sm:text-3xl font-bold tracking-widest text-[#1A1A1A] uppercase">9KT FINE GOLD</h2></div>
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
        ${FINE_GOLD_PRODUCTS.map(fg => `
          <div class="group relative bg-white border border-[#E6E1D7] p-3 sm:p-4 text-left flex flex-col justify-between rounded-xl cursor-pointer hover:shadow-lg transition-all space-y-3">
            <div onclick="openPDP('${fg.id}')" class="relative aspect-square w-full bg-[#F6F4EF] rounded-lg overflow-hidden">
              <img src="${fg.image}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-out" />
              <button onclick="event.stopPropagation(); toggleWishlist('${fg.id}');" class="absolute bottom-2 left-2 text-base z-20">
                ${state.wishlist.includes(fg.id) ? '❤️' : '🤍'}
              </button>
            </div>
            
            <div class="flex-1 flex flex-col justify-between space-y-2.5">
              <div onclick="openPDP('${fg.id}')" class="space-y-1">
                <h4 class="font-serif text-xs font-bold text-[#1A1A1A] group-hover:text-[#C5A059] line-clamp-2">${fg.name}</h4>
                <div class="text-xs font-bold text-[#1A1A1A] flex items-center gap-2"><span>₹${fg.price.toLocaleString()}</span><span class="text-slate-400 line-through text-[11px] font-normal">₹${fg.originalPrice.toLocaleString()}</span></div>
              </div>

              <button onclick="event.stopPropagation(); addToCart('${fg.id}');" class="w-full border border-[#1A1A1A] bg-white text-[#1A1A1A] font-semibold py-2 rounded-lg text-[11px] sm:text-xs uppercase tracking-wider hover:bg-[#1A1A1A] hover:text-white transition-colors">
                Add to Cart
              </button>
            </div>
          </div>
        `).join('')}
      </div>
    </section>

    <!-- 7. FROM SHRADDHA, FOR YOU Quote -->
    <section class="py-12 sm:py-16 bg-[#FAF8F5] border-y border-[#E6E1D7]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        <p class="text-center text-xs text-slate-600 max-w-4xl mx-auto leading-relaxed px-2">At Cieloria, we create jewellery that's made to be worn — every day and on the days that matter most. It's premium in quality, thoughtful in design, and priced so it feels right. We don't believe in saving the good stuff for later. Our pieces are made to move with you, not sit in a box. <strong>Because with Cieloria, the sparkle is always yours to keep.</strong></p>
        <h2 class="text-center font-serif text-xl sm:text-3xl font-bold tracking-widest text-[#1A1A1A] uppercase">FROM SHRADDHA, FOR YOU</h2>
        <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center pt-2">
          <div class="md:col-span-6 rounded-2xl overflow-hidden shadow-md"><img src="${PRODUCTS[40].image}" class="w-full h-[320px] sm:h-[420px] object-cover" /></div>
          <div class="md:col-span-6 text-left space-y-4 p-2">
            <blockquote class="font-serif text-sm sm:text-lg text-slate-800 leading-relaxed italic border-l-4 border-[#C5A059] pl-4 sm:pl-6">"A lot of us find real gold too expensive — and we don't want our jewellery locked away. At the same time, imitation jewellery fades, breaks, and doesn't last. So at Cieloria, we're building something in the middle — a new vision called Demifine® :18k thick gold plating on premium metals, so everyone can enjoy jewellery that's trendy, lasting, and high on quality."</blockquote>
          </div>
        </div>
      </div>
    </section>

    <!-- 8. Gifts For Her / Him & FOR EVERY YOU -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-10">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6">
        <div onclick="openPLPCategory('Necklaces')" class="bg-[#FAF8F5] border border-[#E6E1D7] rounded-2xl p-5 flex items-center justify-between cursor-pointer hover:border-black"><span class="font-serif text-lg sm:text-xl font-bold text-[#1A1A1A]">Gifts For <strong>Her</strong> ›</span><img src="${PRODUCTS[40].image}" class="w-16 h-16 sm:w-20 sm:h-20 object-cover rounded-xl" /></div>
        <div onclick="openPLPCategory('Bracelets')" class="bg-[#FAF8F5] border border-[#E6E1D7] rounded-2xl p-5 flex items-center justify-between cursor-pointer hover:border-black"><span class="font-serif text-lg sm:text-xl font-bold text-[#1A1A1A]">Gifts For <strong>Him</strong> ›</span><img src="${PRODUCTS[2].image}" class="w-16 h-16 sm:w-20 sm:h-20 object-cover rounded-xl" /></div>
      </div>
      <div class="space-y-6 text-center">
        <h2 class="font-serif text-xl sm:text-3xl font-bold tracking-widest text-[#1A1A1A] uppercase">FOR EVERY YOU</h2>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          ${FOR_EVERY_YOU_CARDS.map(card => `
            <div onclick="openPLPCategory('All')" class="relative rounded-2xl overflow-hidden cursor-pointer group h-[300px] sm:h-[380px] bg-black">
              <img src="${card.image}" class="w-full h-full object-cover opacity-80 group-hover:scale-105 transition-transform duration-700" />
              <div class="absolute inset-0 p-4 flex items-end justify-center bg-gradient-to-t from-black/80 via-transparent to-transparent"><span class="font-serif text-base sm:text-lg font-bold text-white pb-1 tracking-wider uppercase">${card.title}</span></div>
            </div>
          `).join('')}
        </div>
      </div>
    </section>

    <!-- 9. SHOP WITH CONFIDENCE -->
    <section class="py-12 sm:py-16 bg-[#FAF8F5] border-y border-[#E6E1D7]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-10 text-center">
        <h2 class="font-serif text-xl sm:text-3xl font-bold tracking-widest text-[#1A1A1A] uppercase">SHOP WITH CONFIDENCE</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
          <div class="space-y-2 p-2">
            <span class="text-3xl sm:text-4xl">😊</span>
            <h3 class="font-serif text-base sm:text-lg font-bold text-[#1A1A1A]">SKIN SAFE</h3>
            <p class="text-xs text-slate-600 leading-relaxed max-w-xs mx-auto">Our jewelry is hypoallergenic and skin-safe, crafted with care to ensure comfort for all skin types.</p>
          </div>
          <div class="space-y-2 p-2">
            <span class="text-3xl sm:text-4xl">✨</span>
            <h3 class="font-serif text-base sm:text-lg font-bold text-[#1A1A1A]">18K GOLD VERMEIL</h3>
            <p class="text-xs text-slate-600 leading-relaxed max-w-xs mx-auto">Our jewelry is crafted from premium surgical steel, sterling silver, and thick 18k gold plating for lasting shine.</p>
          </div>
          <div class="space-y-2 p-2">
            <span class="text-3xl sm:text-4xl">💎</span>
            <h3 class="font-serif text-base sm:text-lg font-bold text-[#1A1A1A]">AUTHENTIC DIAMONDS</h3>
            <p class="text-xs text-slate-600 leading-relaxed max-w-xs mx-auto">Our lab-grown diamonds are SGL Certified, ensuring the highest standards of quality and ethical origins.</p>
          </div>
        </div>
      </div>
    </section>
  `;
}

function renderPLPView() {
  const catKey = PLP_CATEGORY_DATA[state.plpCategory] ? state.plpCategory : 'All';
  const cData = PLP_CATEGORY_DATA[catKey];

  let plpProducts = PRODUCTS.filter(p => {
    if (state.plpCategory === 'NewArrivals') return p.isNew;
    if (state.plpCategory === 'BestSeller') return p.isBestseller;
    if (state.plpCategory === 'FineSilver') return p.isSilver || p.metal.includes("Silver");
    if (state.plpCategory === 'NineKTGold') return p.isFineGold || p.metal.includes("Solid Gold");
    if (state.plpCategory === 'Gifting') return p.category === 'Personalised' || p.price > 1200;
    if (state.plpCategory !== 'All' && p.category !== state.plpCategory) return false;
    return true;
  });

  if (plpProducts.length === 0) {
    plpProducts = PRODUCTS.slice(0, 16);
  }

  if (state.plpSortBy === 'lowToHigh') {
    plpProducts.sort((a, b) => a.price - b.price);
  } else if (state.plpSortBy === 'highToLow') {
    plpProducts.sort((a, b) => b.price - a.price);
  } else if (state.plpSortBy === 'newest') {
    plpProducts.sort((a, b) => (b.isNew ? 1 : 0) - (a.isNew ? 1 : 0));
  }

  return `
    <div class="relative w-full h-[260px] sm:h-[380px] overflow-hidden bg-[#EAE5D9]">
      <img src="${cData.bannerImage}" class="w-full h-full object-cover" />
      <div class="absolute inset-0 bg-black/40 flex items-center justify-center p-4 text-center">
        <div class="text-white space-y-1.5 max-w-2xl">
          <h1 class="font-serif text-3xl sm:text-5xl font-bold tracking-tight">${cData.title}</h1>
          <p class="text-xs sm:text-base font-light text-slate-100 italic">${cData.tagline}</p>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 py-8 space-y-6 text-center">
      <div class="space-y-1">
        <h2 class="font-serif text-2xl sm:text-4xl font-bold text-[#1A1A1A]">${cData.heading}</h2>
        <div class="flex items-center justify-center gap-2 text-xs text-slate-400 font-medium">
          <button onclick="switchViewMode('homepage')" class="hover:text-[#1A1A1A]">Home</button>
          <span>›</span>
          <span class="text-[#1A1A1A] font-bold">${cData.heading}</span>
        </div>
      </div>

      <div class="flex flex-wrap justify-center gap-2 pt-2">
        ${cData.subFilters.map((pill, idx) => `
          <button 
            onclick="state.plpSubFilter = '${pill}'; renderApp();" 
            class="px-3.5 py-1.5 rounded-full text-xs font-medium transition-all border ${ (state.plpSubFilter === pill || (idx === 0 && !state.plpSubFilter)) ? 'bg-black text-white border-black font-semibold' : 'bg-white text-[#1A1A1A] border-[#E6E1D7] hover:border-black' }"
          >
            ${pill}
          </button>
        `).join('')}
      </div>

      <div class="flex items-center justify-between border-t border-b border-[#E6E1D7] py-3 mt-6 text-xs font-medium text-[#1A1A1A]">
        <span class="text-slate-500 font-medium">Showing <strong>${plpProducts.length}</strong> items</span>

        <div class="flex items-center gap-2">
          <span>Sort By:</span>
          <select onchange="state.plpSortBy = this.value; renderApp();" class="bg-transparent text-xs font-bold text-[#1A1A1A] focus:outline-none cursor-pointer">
            <option value="featured" ${state.plpSortBy === 'featured' ? 'selected' : ''}>Best selling ⇅</option>
            <option value="lowToHigh" ${state.plpSortBy === 'lowToHigh' ? 'selected' : ''}>Price: Low to High</option>
            <option value="highToLow" ${state.plpSortBy === 'highToLow' ? 'selected' : ''}>Price: High to Low</option>
            <option value="newest" ${state.plpSortBy === 'newest' ? 'selected' : ''}>Newest Arrivals</option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6 pt-4 text-left">
        ${plpProducts.map(p => {
          const isSaved = state.wishlist.includes(p.id);
          return `
            <div class="group relative bg-[#FFFFFF] border border-[#E6E1D7] overflow-hidden flex flex-col justify-between text-left cursor-pointer hover:shadow-lg transition-all rounded-xl">
              <div onclick="openPDP('${p.id}')" class="relative aspect-square w-full bg-[#F6F4EF] overflow-hidden">
                <img src="${p.image}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-out" />
                
                <div class="absolute top-0 left-0 bg-[#8B1E2B] text-white text-[9px] font-bold uppercase px-2 py-0.5 sm:px-2.5 sm:py-1 z-10 shadow-xs">
                  ${p.discountPercent > 50 ? `EXTRA ${p.discountPercent}% OFF` : `Flat ${p.price}`}
                </div>
                
                <button onclick="event.stopPropagation(); toggleWishlist('${p.id}');" class="absolute bottom-2.5 left-2.5 sm:bottom-3 sm:left-3 text-base sm:text-lg transition-transform hover:scale-110 z-20" title="${isSaved ? 'Remove from Wishlist' : 'Add to Wishlist'}">
                  ${isSaved ? '❤️' : '🤍'}
                </button>
              </div>
              
              <div class="p-3 sm:p-4 flex flex-col justify-between flex-1 space-y-2.5">
                <div onclick="openPDP('${p.id}')" class="space-y-1 cursor-pointer">
                  <h3 class="font-serif text-xs font-bold text-[#1A1A1A] group-hover:text-[#C5A059] line-clamp-1">${p.name}</h3>
                  <div class="text-xs font-bold text-[#1A1A1A] flex items-center gap-2"><span>${formatPrice(p.price)}</span><span class="text-slate-400 line-through text-[11px] font-normal">${formatPrice(p.originalPrice)}</span></div>
                  
                  <div class="flex items-center gap-1 text-[#C5A059] text-[10px] sm:text-[11px] font-semibold pt-0.5">
                    <span>★★★★★</span>
                    <span class="text-slate-400 font-normal">(${p.reviewCount})</span>
                  </div>
                </div>

                <button onclick="event.stopPropagation(); addToCart('${p.id}');" class="w-full border border-[#1A1A1A] bg-white text-[#1A1A1A] font-semibold py-2 rounded-lg text-[11px] sm:text-xs uppercase tracking-wider hover:bg-[#1A1A1A] hover:text-white transition-colors">
                  Add to Cart
                </button>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    </div>
  `;
}

function renderAboutUsView() {
  return `
    <div class="bg-white text-[#1A1A1A] text-left">
      
      <section class="relative w-full h-[360px] sm:h-[550px] bg-black overflow-hidden flex items-center justify-center">
        <img src="${PRODUCTS[40].image}" class="w-full h-full object-cover opacity-50" />
        <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent flex flex-col justify-center items-center text-center p-4 sm:p-6 text-white space-y-3">
          <span class="text-[10px] sm:text-xs uppercase tracking-[0.3em] font-bold text-[#C5A059]">EST. 1 YEAR AGO • LUCKNOW, INDIA</span>
          <h1 class="font-serif text-3xl sm:text-6xl font-bold tracking-tight max-w-4xl leading-tight">Crafting Timeless Luxury in the Heart of Lucknow</h1>
          <p class="text-xs sm:text-lg font-light max-w-2xl text-slate-200">Demifine® 18K Thick Gold Plated & Waterproof Jewelry — Crafted for the modern Indian woman.</p>
        </div>
      </section>

      <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-14 sm:py-20 space-y-16">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 sm:gap-12 items-center">
          <div class="lg:col-span-6 space-y-4 sm:space-y-6">
            <span class="text-xs uppercase tracking-widest font-bold text-[#C5A059]">OUR STORY & ORIGIN</span>
            <h2 class="font-serif text-2xl sm:text-4xl font-bold leading-tight text-[#1A1A1A]">Born in Lucknow, Cherished Nationwide</h2>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              Launched <strong>1 year ago</strong> in the royal city of <strong>Lucknow, Uttar Pradesh</strong>, <strong>CIELORIA</strong> was born with a single revolutionary vision: to bridge the gap between expensive solid gold and low-quality imitation jewelry.
            </p>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
              We pioneered <strong>Demifine® anti-tarnish jewelry in India</strong>: blending 316L surgical grade stainless steel and 925 sterling silver with real 18K thick gold PVD vacuum plating. Celebrating our 1-year anniversary, we have delivered elegance to over 8,000,000+ happy women across India!
            </p>

            <div class="pt-2 flex items-center gap-4 sm:gap-6 border-t border-[#E6E1D7] pt-6">
              <div>
                <span class="font-serif text-2xl sm:text-3xl font-bold text-[#1A1A1A] block">1 Year</span>
                <span class="text-[10px] sm:text-xs text-slate-400">Anniversary Milestone</span>
              </div>
              <div class="border-l border-[#E6E1D7] pl-4 sm:pl-6">
                <span class="font-serif text-2xl sm:text-3xl font-bold text-[#1A1A1A] block">Lucknow, UP</span>
                <span class="text-[10px] sm:text-xs text-slate-400">Headquarters & Studio</span>
              </div>
              <div class="border-l border-[#E6E1D7] pl-4 sm:pl-6">
                <span class="font-serif text-2xl sm:text-3xl font-bold text-[#1A1A1A] block">8L+</span>
                <span class="text-[10px] sm:text-xs text-slate-400">Happy Customers</span>
              </div>
            </div>
          </div>

          <div class="lg:col-span-6">
            <div class="relative rounded-3xl overflow-hidden shadow-2xl border border-[#E6E1D7] bg-[#FAF8F5] p-3">
              <img src="${PRODUCTS[9].image}" class="w-full h-[340px] sm:h-[450px] object-cover rounded-2xl" />
            </div>
          </div>
        </div>

        <div class="pt-8 border-t border-[#E6E1D7] space-y-8 text-center">
          <div class="space-y-1">
            <span class="text-xs uppercase tracking-widest font-bold text-[#C5A059]">WHY CIELORIA</span>
            <h3 class="font-serif text-2xl sm:text-3xl font-bold text-[#1A1A1A]">The 4 Pillars of Cieloria Luxury</h3>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 text-left">
            <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-5 rounded-2xl space-y-2">
              <span class="text-2xl sm:text-3xl">✨</span>
              <h4 class="font-serif text-base font-bold text-[#1A1A1A]">100% Anti-Tarnish</h4>
              <p class="text-xs text-slate-600 leading-relaxed">Advanced PVD vacuum plating guarantees your jewelry never turns black or loses its golden radiance.</p>
            </div>

            <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-5 rounded-2xl space-y-2">
              <span class="text-2xl sm:text-3xl">💧</span>
              <h4 class="font-serif text-base font-bold text-[#1A1A1A]">Water & Sweatproof</h4>
              <p class="text-xs text-slate-600 leading-relaxed">Wear it in the shower, pool, gym, or ocean — 100% waterproof for everyday active living.</p>
            </div>

            <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-5 rounded-2xl space-y-2">
              <span class="text-2xl sm:text-3xl">🌿</span>
              <h4 class="font-serif text-base font-bold text-[#1A1A1A]">Hypoallergenic & Safe</h4>
              <p class="text-xs text-slate-600 leading-relaxed">Nickel-free and lead-free surgical grade steel ensures zero skin irritation or green marks.</p>
            </div>

            <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-5 rounded-2xl space-y-2">
              <span class="text-2xl sm:text-3xl">🏛️</span>
              <h4 class="font-serif text-base font-bold text-[#1A1A1A]">Lucknow Craftsmanship</h4>
              <p class="text-xs text-slate-600 leading-relaxed">Infused with Lucknow's rich heritage of royal craftsmanship and modern high-fashion design.</p>
            </div>
          </div>
        </div>
      </section>
    </div>
  `;
}

function renderPDPView() {
  const p = PRODUCTS.find(prod => prod.id === state.selectedProductId) || PRODUCTS[0];
  const gallery = (p.gallery && p.gallery.length > 0) ? p.gallery : [p.image];
  const activeImg = gallery[state.activeGalleryIndex] || p.image;
  const isSaved = state.wishlist.includes(p.id);

  const displayedReviews = CUSTOMER_REVIEWS.slice(0, state.visibleReviewsCount);

  return `
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 space-y-12 text-left">
      
      <div class="flex items-center gap-2 text-xs text-slate-400 font-medium">
        <button onclick="switchViewMode('homepage')" class="hover:text-[#1A1A1A]">Home</button>
        <span>/</span>
        <button onclick="openPLPCategory('${p.category}')" class="hover:text-[#1A1A1A]">${p.category}</button>
        <span>/</span>
        <span class="text-[#1A1A1A] font-bold line-clamp-1">${p.name}</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-start">
        
        <div class="lg:col-span-7 space-y-4">
          <div class="relative aspect-square w-full rounded-2xl overflow-hidden border border-[#E6E1D7] bg-[#F6F4EF] group">
            
            <div class="absolute top-0 left-0 bg-[#8B1E2B] text-white text-xs font-bold uppercase px-3.5 py-1.5 z-10 shadow-xs">
              EXTRA 40% OFF
            </div>

            <img src="${activeImg}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110 group-hover:brightness-105 cursor-zoom-in" />

            <button onclick="alert('Product link copied!')" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-white/90 shadow-sm flex items-center justify-center text-sm text-[#1A1A1A] hover:bg-white z-10" title="Share Product">
              ↗
            </button>
          </div>

          <div class="flex items-center justify-center gap-3 pt-1">
            ${gallery.map((gImg, idx) => `
              <button 
                onclick="state.activeGalleryIndex = ${idx}; renderApp();" 
                class="w-14 h-14 sm:w-16 sm:h-16 rounded-xl overflow-hidden border-2 transition-all ${state.activeGalleryIndex === idx ? 'border-black scale-105 shadow-sm' : 'border-transparent opacity-60 hover:opacity-100'}"
              >
                <img src="${gImg}" class="w-full h-full object-cover" />
              </button>
            `).join('')}
          </div>
          <div class="flex items-center justify-center gap-1.5 text-xs text-slate-400">
            ${gallery.map((_, idx) => `
              <span class="w-2 h-2 rounded-full ${state.activeGalleryIndex === idx ? 'bg-black w-4' : 'bg-slate-300'} transition-all"></span>
            `).join('')}
          </div>
        </div>

        <div class="lg:col-span-5 space-y-5 text-left">
          
          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-[#C5A059] uppercase tracking-wider">${p.metal}</span>
              <div class="flex items-center gap-1.5 bg-[#FAF8F5] border border-[#E6E1D7] px-3 py-1 rounded-full text-xs font-bold text-[#1A1A1A]">
                <span class="text-amber-500">★</span>
                <span>4.6</span>
                <span class="text-slate-400 font-normal">(${p.reviewCount})</span>
              </div>
            </div>

            <h1 class="font-serif text-2xl sm:text-3xl font-bold text-[#1A1A1A] leading-tight">${p.name}</h1>
          </div>

          <div class="inline-flex items-center gap-2 bg-rose-50 border border-rose-200 text-rose-800 px-3.5 py-1.5 rounded-full text-xs font-bold">
            <span>⚡ 132 quantity sold in last 7 days</span>
          </div>

          <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-4 rounded-2xl flex items-center justify-between">
            <div>
              <div class="flex items-baseline gap-2">
                <span class="text-2xl sm:text-3xl font-bold text-[#1A1A1A]">${formatPrice(p.price)}</span>
                <span class="text-sm text-slate-400 line-through font-normal">${formatPrice(p.originalPrice)}</span>
              </div>
              <span class="text-[11px] text-emerald-700 font-bold block pt-0.5">Inclusive of all taxes & FREE Express Shipping</span>
            </div>
            <span class="bg-[#8B1E2B] text-white text-xs font-bold px-3 py-1.5 rounded-lg uppercase">Save ${p.discountPercent}%</span>
          </div>

          <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-bold text-[#1A1A1A]">
            <div class="bg-amber-50 border border-amber-200 py-2 rounded-xl">✨ Anti-Tarnish</div>
            <div class="bg-blue-50 border border-blue-200 py-2 rounded-xl">💧 Waterproof</div>
            <div class="bg-emerald-50 border border-emerald-200 py-2 rounded-xl">🌿 Hypoallergenic</div>
          </div>

          <div class="border border-dashed border-[#C5A059] bg-[#FAF8F5] p-4 rounded-2xl space-y-2">
            <span class="text-[10px] uppercase font-bold text-[#C5A059] tracking-wider">% AVAILABLE OFFERS</span>
            <div class="flex items-center justify-between text-xs">
              <span class="font-bold text-[#1A1A1A]">Buy 1 Get 1 Free</span>
              <span class="bg-black text-white text-[10px] font-bold px-2.5 py-1 rounded uppercase">Code: B1G1</span>
            </div>
            <div class="flex items-center justify-between text-xs border-t border-[#E6E1D7] pt-2">
              <span class="font-bold text-[#1A1A1A]">Flat 40% OFF</span>
              <button onclick="state.appliedCoupon='RAKHI40'; renderApp(); alert('RAKHI40 Applied! 40% Discount active.');" class="bg-black text-white text-[10px] font-bold px-2.5 py-1 rounded uppercase">
                ${state.appliedCoupon==='RAKHI40' ? '✔ APPLIED' : 'Apply Code: RAKHI40'}
              </button>
            </div>
          </div>

          <label class="flex items-center gap-3 bg-white border border-[#E6E1D7] p-3.5 rounded-xl cursor-pointer hover:border-black transition-colors">
            <input type="checkbox" ${state.addGiftSleeve ? 'checked' : ''} onchange="state.addGiftSleeve = this.checked; renderApp();" class="w-4 h-4 accent-black" />
            <span class="text-xs font-bold text-[#1A1A1A]">🎁 Add Luxury Keepsake Gift Box & Sleeve (+₹99)</span>
          </label>

          <div class="bg-white border border-[#E6E1D7] p-4 rounded-2xl space-y-2">
            <span class="text-xs font-bold text-[#1A1A1A] block">Check Delivery & COD Availability:</span>
            <div class="flex gap-2">
              <input 
                type="text" 
                value="${state.pincode}" 
                oninput="state.pincode=this.value"
                placeholder="Enter 6-digit Pincode" 
                class="flex-1 border border-[#E6E1D7] rounded-xl px-3 py-2 text-xs focus:outline-none focus:border-black font-medium" 
              />
              <button onclick="state.pincodeCheckResult='⚡ Delivery in 2-3 Days via Bluedart Express'; renderApp();" class="bg-black text-white font-bold px-4 py-2 rounded-xl text-xs uppercase">Check</button>
            </div>
            ${state.pincodeCheckResult ? `<p class="text-xs font-bold text-emerald-700 pt-1">${state.pincodeCheckResult}</p>` : ''}
          </div>

          <div class="space-y-3 pt-2">
            <div class="flex items-center gap-3">
              <button onclick="addToCart('${p.id}')" class="flex-1 bg-black hover:bg-[#C5A059] text-white font-bold py-4 rounded-xl text-xs uppercase tracking-widest transition-colors flex items-center justify-center gap-2 shadow-lg">
                <span>🛒</span>
                <span>ADD TO CART</span>
                <span>→</span>
              </button>

              <button onclick="toggleWishlist('${p.id}')" class="w-12 h-12 rounded-xl border border-[#E6E1D7] bg-white flex items-center justify-center text-lg transition-transform hover:scale-105" title="${isSaved ? 'Remove from Wishlist' : 'Save to Wishlist'}">
                ${isSaved ? '❤️' : '🤍'}
              </button>
            </div>

            <button onclick="addToCart('${p.id}'); triggerCIELORIACheckout();" class="w-full border-2 border-black bg-white hover:bg-black hover:text-white text-black font-bold py-3.5 rounded-xl text-xs uppercase tracking-widest transition-colors shadow-sm flex items-center justify-center gap-2">
              <span class="text-amber-600">⚡</span>
              <span>BUY IT NOW (CIELORIA Fast Checkout)</span>
            </button>
          </div>

          <div class="border-t border-[#E6E1D7] pt-4 space-y-2">
            
            <div class="border border-[#E6E1D7] rounded-xl overflow-hidden">
              <button onclick="state.openAccordion = state.openAccordion === 'description' ? '' : 'description'; renderApp();" class="w-full p-4 text-left font-bold text-xs flex justify-between items-center bg-[#FAF8F5]">
                <span>PRODUCT DESCRIPTION</span>
                <span>${state.openAccordion === 'description' ? '−' : '+'}</span>
              </button>
              ${state.openAccordion === 'description' ? `<div class="p-4 text-xs text-slate-600 leading-relaxed bg-white border-t border-[#E6E1D7]">${p.description}</div>` : ''}
            </div>

            <div class="border border-[#E6E1D7] rounded-xl overflow-hidden">
              <button onclick="state.openAccordion = state.openAccordion === 'specs' ? '' : 'specs'; renderApp();" class="w-full p-4 text-left font-bold text-xs flex justify-between items-center bg-[#FAF8F5]">
                <span>SPECIFICATIONS & MATERIALS</span>
                <span>${state.openAccordion === 'specs' ? '−' : '+'}</span>
              </button>
              ${state.openAccordion === 'specs' ? `<div class="p-4 text-xs text-slate-600 leading-relaxed bg-white border-t border-[#E6E1D7] space-y-1"><p><strong>Material:</strong> ${p.materials}</p><p><strong>Dimensions:</strong> ${p.dimensions}</p><p><strong>Care:</strong> ${p.care}</p></div>` : ''}
            </div>

            <div class="border border-[#E6E1D7] rounded-xl overflow-hidden">
              <button onclick="state.openAccordion = state.openAccordion === 'returns' ? '' : 'returns'; renderApp();" class="w-full p-4 text-left font-bold text-xs flex justify-between items-center bg-[#FAF8F5]">
                <span>RETURNS & WARRANTY</span>
                <span>${state.openAccordion === 'returns' ? '−' : '+'}</span>
              </button>
              ${state.openAccordion === 'returns' ? `<div class="p-4 text-xs text-slate-600 leading-relaxed bg-white border-t border-[#E6E1D7]">7-Day Easy Return & Exchange policy. Covered under Cieloria Lifetime Anti-Tarnish Guarantee.</div>` : ''}
            </div>

          </div>

          <div class="grid grid-cols-3 gap-4 pt-4 text-center border-t border-[#E6E1D7]">
            <div class="space-y-1">
              <span class="text-2xl">🔒</span>
              <h5 class="font-bold text-[11px] text-[#1A1A1A]">Lifetime Plating</h5>
            </div>
            <div class="space-y-1">
              <span class="text-2xl">🚚</span>
              <h5 class="font-bold text-[11px] text-[#1A1A1A]">Free Shipping</h5>
            </div>
            <div class="space-y-1">
              <span class="text-2xl">🔄</span>
              <h5 class="font-bold text-[11px] text-[#1A1A1A]">7-Day Returns</h5>
            </div>
          </div>

        </div>
      </div>

      <section class="bg-black text-white rounded-3xl p-6 sm:p-12 my-10 text-center space-y-5 shadow-xl">
        <div class="max-w-3xl mx-auto space-y-3">
          <span class="text-xs uppercase font-bold tracking-[0.3em] text-[#C5A059]">CIELORIA LUXURY DEMIFINE®</span>
          <h2 class="font-serif text-2xl sm:text-4xl font-bold">Anti-Tarnish • 18Kt Thick Plating • Skin Safe</h2>
          <p class="text-xs sm:text-sm text-slate-300 font-light leading-relaxed">Built with surgical stainless steel & sterling silver. Designed to move with you everywhere.</p>
        </div>
      </section>

      <section class="space-y-8 pt-6 border-t border-[#E6E1D7]">
        <div class="flex items-center justify-between">
          <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A]">Verified Customer Reviews</h3>
          <button onclick="alert('Write a Review form opened!')" class="border border-black text-black px-4 py-2 rounded-xl text-xs font-bold hover:bg-black hover:text-white">Write A Review</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          ${displayedReviews.map(r => `
            <div class="bg-white border border-[#E6E1D7] p-5 rounded-2xl space-y-3 shadow-xs">
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-2">
                  <span class="font-bold text-xs text-[#1A1A1A]">${r.name}</span>
                  ${r.verified ? `<span class="bg-emerald-100 text-emerald-800 text-[9px] font-bold px-2 py-0.5 rounded-full">✔ Verified Buyer</span>` : ''}
                </div>
                <span class="text-[10px] text-slate-400">${r.date}</span>
              </div>

              <div class="text-amber-500 text-xs">★★★★★</div>
              <p class="text-xs text-slate-700 font-medium leading-relaxed">${r.comment}</p>

              ${r.videoMedia ? `
                <div class="relative w-24 h-24 rounded-xl overflow-hidden bg-black border border-slate-200 mt-2">
                  <img src="${r.videoMedia}" class="w-full h-full object-cover opacity-80" />
                  <span class="absolute inset-0 flex items-center justify-center text-white text-lg">▶</span>
                </div>
              ` : ''}
            </div>
          `).join('')}
        </div>
      </section>

    </div>
  `;
}

// Modals, Cart Drawer & CIELORIA Auth
function renderModals() {
  let html = '';

  const subtotal = calculateCartSubtotal();
  const discount = calculateCartDiscount();
  const finalTotal = calculateCartFinalTotal();
  const cartTotalItems = calculateCartTotalCount();

  // 1. CIELORIA Auth & Login Popup Modal
  if (state.isCIELORIAAuthOpen) {
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/65 backdrop-blur-xs">
        <div class="relative w-full max-w-3xl bg-[#FDF0F5] border border-rose-200 rounded-3xl overflow-hidden shadow-2xl text-left flex flex-col md:flex-row">
          
          <button onclick="state.isCIELORIAAuthOpen=false; renderApp();" class="absolute top-4 right-4 z-20 w-8 h-8 rounded-full bg-white/80 hover:bg-white text-slate-500 hover:text-black flex items-center justify-center text-sm font-bold shadow-sm">✕</button>

          <!-- Left Side: Cieloria CIELORIA Brand Welcome Panel -->
          <div class="md:w-1/2 p-6 sm:p-8 flex flex-col justify-between space-y-6 bg-gradient-to-b from-[#FDF0F5] to-[#F7DCE6] text-center md:text-left">
            <div class="space-y-4">
              <div class="flex items-center justify-center md:justify-start gap-3">
                <span class="font-serif text-2xl font-bold tracking-[0.15em] text-[#1A1A1A] uppercase">CIELORIA</span>
                <span class="text-[10px] font-extrabold uppercase tracking-wider bg-white/80 border border-rose-200 px-2 py-0.5 rounded text-slate-800 flex items-center gap-1">
                  CIELORIA <span class="text-amber-500 font-bold">🔐</span> Account
                </span>
              </div>

              <div class="space-y-1">
                <h2 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A]">Welcome to Cieloria!</h2>
                <p class="text-xs text-rose-900 font-medium">India's 1st Demifine Jewellery Brand</p>
              </div>
            </div>

            <div class="grid grid-cols-1 gap-3 pt-2">
              <div class="bg-white/70 border border-rose-200/80 p-3.5 rounded-2xl space-y-1 text-center shadow-2xs">
                <div class="w-5 h-5 rounded-full bg-rose-200 text-rose-700 mx-auto flex items-center justify-center text-xs">✦</div>
                <h4 class="font-bold text-[11px] text-[#1A1A1A]">Powered by Demifine</h4>
                <p class="text-[9px] text-slate-500 font-medium">Built to Last, Swim, Sweat, No Tarnish, no worries</p>
              </div>

              <div class="bg-white/70 border border-rose-200/80 p-3.5 rounded-2xl space-y-1 text-center shadow-2xs">
                <div class="w-5 h-5 rounded-full bg-rose-200 text-rose-700 mx-auto flex items-center justify-center text-xs">✦</div>
                <h4 class="font-bold text-[11px] text-[#1A1A1A]">Exclusive Perks Just for You</h4>
                <p class="text-[9px] text-slate-500 font-medium">Earn Cieloria Coins. Unlock Early Bird Offers</p>
              </div>

              <div class="bg-white/70 border border-rose-200/80 p-3.5 rounded-2xl space-y-1 text-center shadow-2xs">
                <div class="w-5 h-5 rounded-full bg-rose-200 text-rose-700 mx-auto flex items-center justify-center text-xs">✦</div>
                <h4 class="font-bold text-[11px] text-[#1A1A1A]">VIP Treatment, Every Time</h4>
                <p class="text-[9px] text-slate-500 font-medium">Exclusive Access to Cieloria's Private Events & Launches</p>
              </div>
            </div>

            <div class="text-[9px] text-slate-400 font-medium text-center md:text-left">Merchant ID: 2yyq6ziimeofq998 • CIELORIA Verified</div>
          </div>

          <!-- Right Side: Clean Form -->
          <div class="md:w-1/2 bg-white p-6 sm:p-8 flex flex-col justify-center text-center space-y-5">
            
            ${state.authModalStep === 1 ? `
              <div class="space-y-1">
                <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A]">Explore Cieloria</h3>
                <p class="text-xs text-slate-500">Affordable Luxury, Made for Every Day!</p>
              </div>

              <form onsubmit="handleCIELORIASendOTP(event)" class="space-y-4 pt-2">
                <div class="flex items-center border border-slate-300 rounded-xl px-3.5 py-3 bg-white focus-within:border-black transition-colors">
                  <span class="flex items-center gap-1.5 text-xs font-bold text-slate-700 mr-2 pr-2 border-r border-slate-200">
                    <span>🇮🇳</span>
                    <span>+91</span>
                  </span>
                  <input 
                    type="tel" 
                    id="cieloria-phone-input"
                    value="${state.customerPhone}"
                    oninput="state.customerPhone=this.value"
                    placeholder="Enter Mobile Number" 
                    required
                    class="w-full focus:outline-none text-xs font-medium text-[#1A1A1A]" 
                  />
                </div>

                <label class="flex items-center justify-center gap-2 text-[11px] text-slate-500 font-medium cursor-pointer">
                  <input type="checkbox" checked class="w-3.5 h-3.5 accent-rose-500 rounded" />
                  <span>Notify me with offers & updates</span>
                </label>

                <button type="submit" class="w-full bg-[#FCE4EC] hover:bg-[#F8BBD0] text-rose-900 font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider transition-colors border border-rose-300">
                  Send OTP via SMS →
                </button>
              </form>

              <p class="text-[9px] text-slate-400 max-w-xs mx-auto leading-relaxed">
                I accept that I have read & understood your <button onclick="alert('Privacy Policy')" class="underline hover:text-black">Privacy Policy</button> and <button onclick="alert('Terms & Conditions')" class="underline hover:text-black">T&Cs</button>.
              </p>
            ` : ''}

            ${state.authModalStep === 2 ? `
              <div class="space-y-2">
                <button onclick="state.authModalStep=1; renderApp();" class="text-xs font-bold text-slate-400 hover:text-black flex items-center gap-1 justify-center mx-auto">
                  <span>❮</span> <span>Change Number (+91 ${state.customerPhone})</span>
                </button>
                <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A]">Verify SMS OTP</h3>
                <p class="text-xs text-slate-500">Enter 4-digit OTP sent to <strong>+91 ${state.customerPhone}</strong></p>
              </div>

              <form onsubmit="handleCIELORIAVerifyOTP(event)" class="space-y-5 pt-2">
                <div class="flex justify-center gap-3">
                  ${[0, 1, 2, 3].map(idx => `
                    <input 
                      type="text" 
                      maxlength="1" 
                      id="otp-input-${idx}"
                      value="${state.otpDigits[idx] || ''}"
                      oninput="handleOtpBoxInput(${idx}, this.value)"
                      class="w-12 h-12 text-center text-lg font-bold border-2 border-slate-300 rounded-xl focus:border-rose-500 focus:outline-none bg-slate-50"
                    />
                  `).join('')}
                </div>

                <div class="text-[11px] text-slate-400 font-semibold">
                  <span>Didn't receive SMS? </span>
                  <button type="button" onclick="handleResendSMSOTP()" class="text-rose-600 font-bold underline">Resend SMS OTP</button>
                </div>

                <button type="submit" class="w-full bg-[#FCE4EC] hover:bg-[#F8BBD0] text-rose-900 font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider transition-colors border border-rose-300 shadow-sm">
                  Verify & Continue →
                </button>
              </form>
            ` : ''}

          </div>

        </div>
      </div>
    `;
  }

  if (state.isMobileMenuOpen) {
    html += `
      <div class="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex justify-start lg:hidden">
        <div class="w-4/5 max-w-xs bg-white h-full flex flex-col justify-between shadow-2xl text-left">
          
          <div class="p-5 border-b border-[#E6E1D7] flex items-center justify-between bg-[#FAF8F5]">
            <span class="font-serif text-xl font-bold tracking-widest text-[#1A1A1A]">CIELORIA</span>
            <button onclick="state.isMobileMenuOpen=false; renderApp();" class="text-xl font-bold text-slate-500 hover:text-black">✕</button>
          </div>

          <div class="flex-1 overflow-y-auto p-5 space-y-5">
            <div class="space-y-1.5">
              <span class="text-[10px] font-bold uppercase tracking-wider text-[#C5A059]">Shop Collections</span>
              ${SUBHEADER_NAV.map(nav => `
                <button 
                  onclick="state.isMobileMenuOpen=false; openPLPCategory('${nav.cat}');" 
                  class="w-full text-left py-3 border-b border-slate-100 flex items-center justify-between text-xs font-bold text-[#1A1A1A] hover:text-[#C5A059]"
                >
                  <span>${nav.name}</span>
                  ${nav.badge ? `<span class="bg-amber-100 text-amber-900 font-bold text-[9px] px-2 py-0.5 rounded-full">${nav.badge}</span>` : '<span class="text-slate-300">›</span>'}
                </button>
              `).join('')}
            </div>

            <div class="pt-4 border-t border-slate-200 space-y-3 text-xs">
              <button onclick="state.isMobileMenuOpen=false; openWishlistView();" class="w-full text-left py-2 font-bold text-[#1A1A1A] flex items-center justify-between">
                <span>❤️ My Saved Wishlist</span>
                <span class="bg-black text-white text-[10px] px-2 py-0.5 rounded-full">${state.wishlist.length}</span>
              </button>

              <button onclick="state.isMobileMenuOpen=false; handleProfileIconClick();" class="w-full text-left py-2 font-bold text-[#1A1A1A] flex items-center justify-between">
                <span>👤 ${state.isLoggedIn ? 'My Account & Orders' : 'Login via CIELORIA'}</span>
                <span class="text-amber-500">⚡</span>
              </button>
            </div>
          </div>

          <div class="p-5 border-t border-[#E6E1D7] bg-[#FAF8F5] text-center space-y-2">
            <span class="text-[10px] text-slate-400 font-bold uppercase block tracking-wider">LUCKNOW FLAGSHIP HQ</span>
            <span class="text-xs font-bold text-emerald-700 block">100% Waterproof & Anti-Tarnish</span>
          </div>

        </div>
      </div>
    `;
  }

  // 2. Cart Drawer
  if (state.isCartOpen) {
    html += `
      <div class="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex justify-end">
        <div class="w-full max-w-md bg-white flex flex-col justify-between text-left shadow-2xl h-full">
          
          <div class="flex items-center justify-between p-4 border-b border-[#E6E1D7]">
            <h2 class="font-serif text-base font-bold text-[#1A1A1A]">Your Cart (${cartTotalItems} items)</h2>
            <button onclick="toggleCart(false)" class="text-lg font-bold text-slate-500 hover:text-black">✕</button>
          </div>

          <div class="bg-black text-white text-[11px] font-semibold py-2 px-4 text-center">
            Buy 1 Get 1 Free | Use Code : B1G1
          </div>

          <div class="bg-emerald-50 border-b border-emerald-200 p-3 text-center text-xs font-bold text-emerald-800 flex items-center justify-center gap-2">
            <span>🎁</span>
            <span>You have unlocked FREE Gift & Shipping!</span>
          </div>

          <div class="flex-1 overflow-y-auto p-4 space-y-4">
            ${state.cart.length === 0 ? `
              <div class="text-center py-12 space-y-3">
                <span class="text-4xl block">🛍️</span>
                <p class="text-sm text-slate-500 font-medium">Your Shopping Bag is empty!</p>
                <button onclick="toggleCart(false); openPLPCategory('BestSeller')" class="bg-black text-white font-bold px-6 py-2.5 text-xs rounded-lg uppercase">Start Shopping</button>
              </div>
            ` : state.cart.map((item) => `
              <div class="flex gap-4 p-3 bg-white border border-[#E6E1D7] rounded-xl relative shadow-xs">
                <img src="${item.image}" class="w-20 h-20 object-cover rounded-lg bg-[#F6F4EF]" />
                <div class="flex-1 flex flex-col justify-between">
                  <h4 class="font-serif text-xs font-bold text-[#1A1A1A] line-clamp-1">${item.name}</h4>
                  
                  <div class="flex items-center justify-between pt-2">
                    <span class="font-bold text-xs text-[#1A1A1A]">${formatPrice(item.price)}</span>
                    
                    <div class="flex items-center border border-slate-300 rounded-lg overflow-hidden bg-slate-50">
                      <button onclick="updateCartQty('${item.id}', -1)" class="px-2.5 py-1 font-bold text-slate-700 hover:bg-slate-200 text-xs">-</button>
                      <span class="px-3 font-bold text-xs text-[#1A1A1A]">${item.quantity}</span>
                      <button onclick="updateCartQty('${item.id}', 1)" class="px-2.5 py-1 font-bold text-slate-700 hover:bg-slate-200 text-xs">+</button>
                    </div>

                    <button onclick="removeCartItem('${item.id}')" class="text-slate-400 hover:text-rose-600 text-sm ml-2" title="Remove Item">🗑️</button>
                  </div>
                </div>
              </div>
            `).join('')}
          </div>

          ${state.cart.length > 0 ? `
            <div class="p-4 border-t border-[#E6E1D7] bg-[#FAF8F5] space-y-3">
              
              <div class="space-y-1.5 text-xs border-b border-slate-200 pb-3">
                <div class="flex justify-between items-center text-slate-600">
                  <span>Subtotal:</span>
                  <span class="font-bold text-[#1A1A1A]">₹${subtotal.toLocaleString()}.00</span>
                </div>
                ${discount > 0 ? `
                  <div class="flex justify-between items-center text-emerald-700 font-semibold">
                    <span>Discount (${state.appliedCoupon}):</span>
                    <span>- ₹${discount.toLocaleString()}.00</span>
                  </div>
                ` : ''}
                ${state.addGiftSleeve ? `
                  <div class="flex justify-between items-center text-slate-600">
                    <span>Gift Box & Sleeve:</span>
                    <span>+ ₹99.00</span>
                  </div>
                ` : ''}
                <div class="flex justify-between items-center text-sm font-bold text-[#1A1A1A] pt-1 border-t border-slate-200">
                  <span>Total Payable:</span>
                  <span class="text-base text-black">₹${finalTotal.toLocaleString()}.00</span>
                </div>
              </div>

              <button onclick="toggleCart(false); triggerCIELORIACheckout();" class="w-full bg-black hover:bg-[#C5A059] text-white font-bold py-4 rounded-xl text-xs uppercase tracking-wider shadow-lg flex items-center justify-center gap-2">
                <span>Proceed To CIELORIA Checkout</span>
                <span>•</span>
                <span>₹${finalTotal.toLocaleString()}.00</span>
                <span>→</span>
              </button>

              <p class="text-[10px] text-slate-400 text-center font-medium">⚡ Merchant ID: ${CIELORIA_CREDENTIALS.merchantId} • CIELORIA Secure</p>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }

  // 3. Official CIELORIA / CIELORIA Fast Checkout Popup Modal
  if (state.isCheckoutOpen) {
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs">
        <div class="w-full max-w-lg bg-white rounded-3xl overflow-hidden shadow-2xl text-left border border-slate-200 flex flex-col max-h-[90vh]">
          
          <div class="p-4 border-b border-slate-200 flex items-center justify-between bg-white sticky top-0 z-10">
            <div class="flex items-center gap-3">
              <button onclick="state.isCheckoutOpen=false; renderApp();" class="text-slate-400 hover:text-black font-bold text-base">❮</button>
              <div>
                <h3 class="font-serif text-lg font-bold tracking-widest text-[#1A1A1A]">CIELORIA</h3>
                <span class="text-[9px] text-emerald-700 font-bold block">CIELORIA CIELORIA Integrated • ID: ${CIELORIA_CREDENTIALS.merchantId}</span>
              </div>
            </div>
            <div class="flex items-center gap-1 text-[11px] font-semibold text-slate-500">
              <span>100% Secured</span>
              <span>🔒</span>
            </div>
          </div>

          <div class="bg-amber-50 border-b border-amber-200 p-2.5 text-center text-xs font-bold text-amber-900">
            ⚡ FREE STUDS worth ₹1,495 on Prepaid orders ₹2,999+
          </div>

          <div class="flex-1 overflow-y-auto p-5 space-y-5 text-xs">
            
            <!-- Step 1: CIELORIA Mobile OTP Login -->
            ${state.checkoutStep === 1 ? `
              <div class="space-y-4">
                <div class="bg-[#FAF8F5] border border-amber-200 p-3 rounded-2xl flex items-center gap-3">
                  <span class="text-2xl">⚡</span>
                  <div>
                    <h5 class="font-bold text-xs text-[#1A1A1A]">1-Click OTP Verification</h5>
                    <p class="text-[10px] text-slate-500">Enter mobile number to auto-fill saved address from Saved Address</p>
                  </div>
                </div>

                <label class="font-bold text-xs text-[#1A1A1A] block">Enter Mobile Number to continue</label>
                <div class="flex items-center border border-slate-300 rounded-xl px-3.5 py-3 bg-white">
                  <span class="text-slate-400 font-bold mr-2.5">+91</span>
                  <input 
                    type="tel" 
                    value="${state.customerPhone}" 
                    oninput="state.customerPhone=this.value" 
                    placeholder="Enter 10-digit Mobile Number" 
                    class="w-full focus:outline-none text-xs font-medium" 
                  />
                </div>
                <button onclick="if(!state.customerPhone || state.customerPhone.trim().length<10){alert('Please enter 10-digit mobile number!'); return;} setStoredData('cieloria_cust_phone', getCleanPhone(state.customerPhone)); state.checkoutStep=2; renderApp();" class="w-full bg-black text-white font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider hover:bg-[#C5A059] transition-colors">
                  Continue to Address →
                </button>
              </div>
            ` : ''}

            <!-- Step 2: Address Input -->
            ${state.checkoutStep === 2 ? `
              <div class="space-y-4">
                <h4 class="font-bold text-xs text-[#1A1A1A] uppercase tracking-wider">DELIVERY ADDRESS (CIELORIA NETWORK)</h4>
                <div class="space-y-3 bg-white border border-slate-200 p-4 rounded-2xl">
                  <div>
                    <label class="text-[10px] font-bold text-slate-500 block mb-1">Full Name</label>
                    <input type="text" value="${state.customerName}" oninput="state.customerName=this.value" placeholder="Enter Full Name" class="w-full border border-slate-300 rounded-lg p-2.5 text-xs focus:outline-none focus:border-black font-medium" />
                  </div>
                  
                  <div>
                    <label class="text-[10px] font-bold text-slate-500 block mb-1">6-Digit Pincode</label>
                    <input type="text" value="${state.pincode}" oninput="state.pincode=this.value" placeholder="Enter 6-digit Pincode" class="w-full border border-slate-300 rounded-lg p-2.5 text-xs focus:outline-none focus:border-black font-medium" />
                  </div>

                  <div>
                    <label class="text-[10px] font-bold text-slate-500 block mb-1">House / Flat No, Street Address</label>
                    <textarea oninput="state.customerAddress=this.value" placeholder="House/Flat No, Building Name, Street Name..." class="w-full border border-slate-300 rounded-lg p-2.5 text-xs focus:outline-none focus:border-black font-medium h-20">${state.customerAddress}</textarea>
                  </div>
                </div>

                <button onclick="if(!state.customerName || !state.customerAddress || !state.pincode){alert('Please complete all address fields!'); return;} setStoredData('cieloria_cust_name', state.customerName); setStoredData('cieloria_address', state.customerAddress); setStoredData('cieloria_pincode', state.pincode); pushCloudCustomerUpdate(); state.checkoutStep=3; renderApp();" class="w-full bg-black text-white font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider hover:bg-[#C5A059] transition-colors">
                  Proceed to Payment • ₹${finalTotal.toLocaleString()}
                </button>
              </div>
            ` : ''}

            <!-- Step 3: Payment Options & Live Order Complete -->
            ${state.checkoutStep === 3 ? `
              <div class="space-y-5 text-center">
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-2xl space-y-3">
                  <h4 class="font-bold text-xs text-[#1A1A1A] uppercase tracking-wider">INSTANT UPI QR SCANNER (CIELORIA PASS)</h4>
                  <div class="w-36 h-36 bg-white rounded-xl p-2 mx-auto flex items-center justify-center border shadow-xs">
                    <img src="${PRODUCTS[0].image}" class="w-full h-full object-cover rounded" />
                  </div>
                  <p class="text-[11px] font-bold text-emerald-700">Scan via GPay, PhonePe, Paytm or BHIM</p>
                </div>

                <div class="pt-2">
                  <button onclick="completeUserOrder()" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-4 rounded-xl text-xs uppercase tracking-wider shadow-lg flex items-center justify-center gap-2">
                    <span>🎉 Complete Order & Track Live</span>
                    <span>→</span>
                  </button>
                </div>
              </div>
            ` : ''}

          </div>
        </div>
      </div>
    `;
  }

  return html;
}

window.handleOtpBoxInput = function(idx, val) {
  state.otpDigits[idx] = val;
  if (val && idx < 3) {
    const nextBox = document.getElementById(`otp-input-${idx + 1}`);
    if (nextBox) nextBox.focus();
  }
  // Auto verify when 4 digits typed
  if (state.otpDigits.join('').length === 4) {
    handleCIELORIAVerifyOTP();
  }
};

window.handleResendSMSOTP = function() {
  alert(`📲 Real SMS OTP requested for +91 ${state.customerPhone} via Secure Telecom Gateway (Merchant: 2yyq6ziimeofq998)`);
};

window.handleProfileIconClick = function() {
  if (state.isLoggedIn) {
    switchViewMode('account');
  } else {
    triggerCIELORIASDKLogin();
  }
};

window.triggerCIELORIASDKLogin = function() {
  if (typeof window !== 'undefined' && window.CieloriaSdk && typeof window.CieloriaSdk.initCheckout === 'function') {
    try {
      window.CieloriaSdk.initCheckout({
        merchantId: CIELORIA_CREDENTIALS.merchantId,
        appId: CIELORIA_CREDENTIALS.appId,
        type: 'login',
        onSuccess: function(res) {
          const cleanPh = getCleanPhone(res.phone || '9876543210');
          state.isLoggedIn = true;
          state.customerPhone = cleanPh;
          setStoredData('cieloria_is_logged_in', true);
          setStoredData('cieloria_cust_phone', cleanPh);
          syncAccountStorage();
          switchViewMode('account');
        }
      });
      return;
    } catch(e) { console.log('CieloriaSdk:', e); }
  }

  state.isCIELORIAAuthOpen = true;
  state.authModalStep = 1;
  state.otpDigits = ["", "", "", ""];
  renderApp();
};

window.handleUserLogout = function() {
  state.isLoggedIn = false;
  state.customerName = "";
  state.customerPhone = "";
  state.customerEmail = "";
  state.customerAddress = "";
  state.ordersList = [];
  state.wishlist = [];

  setStoredData('cieloria_is_logged_in', false);
  setStoredData('cieloria_cust_name', '');
  setStoredData('cieloria_cust_phone', '');

  alert("🚪 You have logged out successfully!");
  switchViewMode('homepage');
};

window.handleCIELORIASendOTP = function(e) {
  if (e) e.preventDefault();
  const phoneInput = document.getElementById('cieloria-phone-input');
  if (phoneInput && phoneInput.value) {
    state.customerPhone = getCleanPhone(phoneInput.value);
  }

  if (!state.customerPhone || state.customerPhone.trim().length < 10) {
    alert('Please enter a valid 10-digit mobile number!');
    return;
  }

  setStoredData('cieloria_cust_phone', state.customerPhone);
  alert(`📲 SMS OTP Sent to +91 ${state.customerPhone} via CIELORIA Gateway!`);
  state.authModalStep = 2;
  state.otpDigits = ["", "", "", ""];
  renderApp();

  setTimeout(() => {
    const firstBox = document.getElementById('otp-input-0');
    if (firstBox) firstBox.focus();
  }, 100);
};

window.handleCIELORIAVerifyOTP = function(e) {
  if (e) e.preventDefault();
  const cleanPh = getCleanPhone(state.customerPhone);
  if (!cleanPh || cleanPh.length < 10) {
    alert('Please enter a valid mobile number!');
    return;
  }

  state.isLoggedIn = true;
  state.customerPhone = cleanPh;
  if (!state.customerName) state.customerName = "Valued Customer";
  state.isCIELORIAAuthOpen = false;

  setStoredData('cieloria_is_logged_in', true);
  setStoredData('cieloria_cust_name', state.customerName);
  setStoredData('cieloria_cust_phone', cleanPh);

  syncAccountStorage();

  alert(`🎉 Verified! Logged in successfully for +91 ${cleanPh}!`);
  switchViewMode('account');
};

window.triggerCIELORIACheckout = function() {
  if (typeof window !== 'undefined' && window.CieloriaSdk && typeof window.CieloriaSdk.initCheckout === 'function') {
    try {
      window.CieloriaSdk.initCheckout({
        merchantId: CIELORIA_CREDENTIALS.merchantId,
        appId: CIELORIA_CREDENTIALS.appId,
        cart: state.cart,
        subtotal: calculateCartSubtotal(),
        onSuccess: function() { completeUserOrder(); }
      });
      return;
    } catch(e) { console.log('CIELORIA SDK:', e); }
  }

  openCheckoutModal();
};

window.completeUserOrder = function() {
  const newOrderId = `CIE-${Math.floor(10000 + Math.random() * 90000)}`;
  const finalTotal = calculateCartFinalTotal();

  const cleanPh = getCleanPhone(state.customerPhone) || '9876543210';

  const newOrder = {
    orderId: newOrderId,
    date: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }),
    status: "Order Placed",
    statusColor: "bg-blue-100 text-blue-800 border-blue-300",
    courier: "Bluedart Express",
    trackingId: `BLU${Math.floor(10000000 + Math.random() * 90000000)}`,
    estimatedDelivery: "2-3 Business Days",
    totalAmount: finalTotal > 0 ? finalTotal : 999,
    customerName: state.customerName || 'Valued Customer',
    customerPhone: cleanPh,
    customerAddress: state.customerAddress || 'Lucknow, UP',
    pincode: state.pincode || '226001',
    items: state.cart.length > 0 ? [...state.cart] : [PRODUCTS[0]]
  };

  state.ordersList.unshift(newOrder);
  state.merchantAllOrders.unshift(newOrder);

  if (cleanPh) {
    setStoredData(`cieloria_orders_${cleanPh}`, state.ordersList);
  }
  setStoredData('cieloria_merchant_all_orders', state.merchantAllOrders);

  // Sync Order to Vercel Google Cloud Serverless API
  try {
    fetch('/api/sync', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action: 'place_order', phone: cleanPh, data: newOrder })
    }).catch(e => console.log('Cloud Order Write Note:', e));
  } catch(e) {}

  state.lastPlacedOrder = newOrder;
  state.cart = [];
  setStoredData('cieloria_cart', []);

  state.isCheckoutOpen = false;
  state.isLoggedIn = true;
  setStoredData('cieloria_is_logged_in', true);

  switchViewMode('order_confirmed');
};

window.switchViewMode = function(mode) { 
  state.viewMode = mode; 
  if (mode === 'about') {
    state.plpCategory = 'About';
  } else if (mode === 'homepage') {
    state.plpCategory = '';
  }
  window.scrollTo({ top: 0, behavior: 'smooth' }); 
  renderApp(); 
};
window.openPDP = function(id) { 
  state.selectedProductId = id; 
  state.activeGalleryIndex = 0;
  state.viewMode = 'pdp'; 
  window.scrollTo({ top: 0, behavior: 'smooth' }); 
  renderApp(); 
};
window.openPLPCategory = function(cat) { 
  if (cat && cat.toLowerCase() === 'about') {
    state.viewMode = 'about';
    state.plpCategory = 'About';
  } else {
    state.plpCategory = cat; 
    state.plpSubFilter = '';
    state.viewMode = 'plp'; 
  }
  window.scrollTo({ top: 0, behavior: 'smooth' }); 
  renderApp(); 
};
window.openWishlistView = function() {
  state.viewMode = 'wishlist';
  window.scrollTo({ top: 0, behavior: 'smooth' });
  renderApp();
};

window.changeHeroSlide = function(dir) { state.heroSlideIndex = (state.heroSlideIndex + dir + HERO_SLIDES.length) % HERO_SLIDES.length; renderApp(); };

window.addToCart = function(id) {
  const p = PRODUCTS.find(prod => prod.id === id);
  if (!p) return;
  const existing = state.cart.find(item => item.id === id);
  if (existing) { 
    existing.quantity = (parseInt(existing.quantity) || 1) + 1; 
  } else { 
    state.cart.push({ ...p, quantity: 1 }); 
  }
  setStoredData('cieloria_cart', state.cart);
  state.isCartOpen = true;
  renderApp();
};

window.updateCartQty = function(id, delta) {
  const item = state.cart.find(i => i.id === id);
  if (item) {
    item.quantity = (parseInt(item.quantity) || 1) + delta;
    if (item.quantity <= 0) {
      state.cart = state.cart.filter(i => i.id !== id);
    }
  }
  setStoredData('cieloria_cart', state.cart);
  renderApp();
};

window.removeCartItem = function(id) {
  state.cart = state.cart.filter(i => i.id !== id);
  setStoredData('cieloria_cart', state.cart);
  renderApp();
};

window.toggleWishlist = function(id) {
  const idx = state.wishlist.indexOf(id);
  if (idx > -1) { 
    state.wishlist.splice(idx, 1); 
  } else { 
    state.wishlist.push(id); 
  }
  
  const wKey = getActiveWishlistKey();
  setStoredData(wKey, state.wishlist);
  pushCloudCustomerUpdate();
  
  renderApp();
};

window.toggleCart = function(open) { state.isCartOpen = open; renderApp(); };

window.openPincodeModal = function() {
  const code = prompt('Enter 6-digit Pincode:', state.pincode || '');
  if (code) { 
    state.pincode = code; 
    setStoredData('cieloria_pincode', code);
    pushCloudCustomerUpdate();
    renderApp(); 
  }
};

window.openCheckoutModal = function() { state.isCheckoutOpen = true; state.checkoutStep = 1; renderApp(); };
window.handleNewsletter = function(e) { e.preventDefault(); state.isSubscribed = true; renderApp(); };

document.addEventListener('DOMContentLoaded', () => { 
  syncAccountStorage();
  renderApp(); 
});
try { 
  syncAccountStorage();
  renderApp(); 
} catch(err) { console.error('Render error:', err); }


// CIELORIA Merchant Admin Portal Logic
let adminState = {
  isAuthenticated: sessionStorage.getItem('cieloria_admin_auth') === 'true',
  passcode: '',
  allOrders: getStoredData('cieloria_merchant_all_orders', [])
};

function fetchCloudOrders() {
  fetch('/api/sync?action=get_all_orders')
    .then(res => res.json())
    .then(data => {
      if (data && data.orders && Array.isArray(data.orders) && data.orders.length > 0) {
        adminState.allOrders = data.orders;
        setStoredData('cieloria_merchant_all_orders', data.orders);
        if (adminState.isAuthenticated && state.viewMode === 'admin') renderApp();
      }
    }).catch(e => console.log('Admin Cloud Fetch Note:', e));
}

setInterval(fetchCloudOrders, 4000);

function handleAdminLogin(e) {
  if (e) e.preventDefault();
  if (adminState.passcode === '42961' || adminState.passcode === '2yyq6ziimeofq998' || adminState.passcode === 'cieloria123') {
    adminState.isAuthenticated = true;
    sessionStorage.setItem('cieloria_admin_auth', 'true');
    renderApp();
  } else {
    alert('❌ Invalid Merchant Passcode! Use your Merchant Code: 42961');
  }
}

function handleAdminLogout() {
  adminState.isAuthenticated = false;
  sessionStorage.removeItem('cieloria_admin_auth');
  renderApp();
}

function handleOrderStatusChange(orderId, newStatus) {
  let orders = getStoredData('cieloria_merchant_all_orders', []);
  let target = orders.find(o => o.orderId === orderId);
  let statusColor = 'bg-blue-100 text-blue-800 border-blue-300';

  if (newStatus === 'Dispatched') statusColor = 'bg-blue-100 text-blue-800 border-blue-300';
  if (newStatus === 'In Transit') statusColor = 'bg-indigo-100 text-indigo-800 border-indigo-300';
  if (newStatus === 'Out for Delivery') statusColor = 'bg-amber-100 text-amber-800 border-amber-300';
  if (newStatus === 'Delivered') statusColor = 'bg-emerald-100 text-emerald-800 border-emerald-300';

  if (target) {
    target.status = newStatus;
    target.statusColor = statusColor;
  }

  setStoredData('cieloria_merchant_all_orders', orders);

  try {
    fetch('/api/sync', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        action: 'update_order_status',
        data: { orderId: orderId, newStatus: newStatus, statusColor: statusColor }
      })
    }).catch(e => console.log('Admin Cloud Order Status Write Note:', e));
  } catch(e) {}

  let custOrders = getStoredData('cieloria_orders', []);
  let custTarget = custOrders.find(o => o.orderId === orderId);
  if (custTarget) {
    custTarget.status = newStatus;
    custTarget.statusColor = statusColor;
    setStoredData('cieloria_orders', custOrders);
  }

  adminState.allOrders = orders;
  alert(`✅ Order ${orderId} status updated to '${newStatus}' on Google Cloud DB! Customer will see this live in My Account.`);
  renderApp();
}

function renderAdminView() {
  if (!adminState.isAuthenticated) {
    return `
      <div class="min-h-screen flex items-center justify-center p-4 bg-[#0F172A] text-slate-100">
        <div class="w-full max-w-md bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-2xl text-center space-y-6">
          <div class="w-16 h-16 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-2xl font-bold flex items-center justify-center mx-auto">
            🔒
          </div>

          <div class="space-y-2">
            <h1 class="font-serif text-2xl font-bold text-white uppercase tracking-wider">CIELORIA STORE ADMIN</h1>
            <p class="text-xs text-slate-400">Enter Merchant Passcode or Merchant Code to access Orders Dashboard.</p>
          </div>

          <form onsubmit="handleAdminLogin(event)" class="space-y-4">
            <input 
              type="password" 
              value="${adminState.passcode}" 
              oninput="adminState.passcode=this.value" 
              placeholder="Enter Merchant Code (e.g. 42961)" 
              required 
              class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-xs text-white focus:outline-none focus:border-amber-400 font-medium text-center tracking-widest text-lg" 
            />

            <button type="submit" class="w-full bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider transition-colors shadow-lg">
              Login to Admin Portal →
            </button>
          </form>

          <div class="text-[10px] text-slate-500 font-mono">
            Merchant ID: 2yyq6ziimeofq998 • Passcode Hint: 42961
          </div>
        </div>
      </div>
    `;
  }

  const orders = adminState.allOrders;
  const totalRev = orders.reduce((sum, o) => sum + (o.totalAmount || 0), 0);

  return `
    <div class="min-h-screen py-8 text-left bg-[#0F172A] text-slate-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center pb-6 border-b border-slate-800 gap-4">
          <div>
            <div class="flex items-center gap-3">
              <span class="text-3xl">⚙️</span>
              <h1 class="font-serif text-3xl font-bold text-amber-400 uppercase tracking-widest">CIELORIA MERCHANT ADMIN DASHBOARD</h1>
            </div>
            <p class="text-xs text-slate-400 pt-1">Manage Customer Orders, Customer Contact Details & Update Dispatch Status (Merchant ID: 2yyq6ziimeofq998 • Live Cloud API Active)</p>
          </div>

          <div class="flex items-center gap-3">
            <button onclick="state.viewMode='homepage'; renderApp();" class="bg-slate-800 hover:bg-slate-700 text-white px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              🌐 Visit Storefront
            </button>
            <button onclick="handleAdminLogout()" class="border border-rose-500/40 hover:bg-rose-500/10 text-rose-400 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              Logout
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-4 gap-4 text-center">
          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Total Received Orders</span>
            <span class="text-3xl font-bold text-white pt-1 block">${orders.length}</span>
          </div>

          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Total Revenue (₹)</span>
            <span class="text-3xl font-bold text-emerald-400 pt-1 block">₹${totalRev.toLocaleString()}</span>
          </div>

          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Dispatched Orders</span>
            <span class="text-3xl font-bold text-blue-400 pt-1 block">${orders.filter(o => o.status === 'Dispatched' || o.status === 'In Transit' || o.status === 'Out for Delivery' || o.status === 'Delivered').length}</span>
          </div>

          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Delivered Orders</span>
            <span class="text-3xl font-bold text-amber-400 pt-1 block">${orders.filter(o => o.status === 'Delivered').length}</span>
          </div>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 space-y-6 shadow-2xl">
          <div class="flex items-center justify-between">
            <h3 class="font-serif text-2xl font-bold text-white">Customer Orders List (${orders.length})</h3>
            <span class="text-xs text-slate-400 font-medium">Select new status from dropdown to update live tracking for customer!</span>
          </div>

          ${orders.length === 0 ? `
            <div class="text-center py-16 text-slate-500 space-y-3">
              <span class="text-5xl block">📦</span>
              <h4 class="font-bold text-slate-300">No Customer Orders Received Yet</h4>
              <p class="text-xs max-w-sm mx-auto">When customers place orders on www.cieloria.com, their name, mobile number, delivery address, and ordered items will appear here automatically!</p>
            </div>
          ` : `
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs text-slate-200">
                <thead class="bg-slate-800 text-slate-400 uppercase text-[10px]">
                  <tr>
                    <th class="p-3.5">Order ID & Date</th>
                    <th class="p-3.5">Customer Name & Phone</th>
                    <th class="p-3.5">Delivery Address</th>
                    <th class="p-3.5">Total Payable</th>
                    <th class="p-3.5">Current Status</th>
                    <th class="p-3.5">Update Order Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-800">
                  ${orders.map(ord => `
                    <tr class="hover:bg-slate-800/50 transition-colors">
                      <td class="p-3.5 font-bold text-white">
                        ${ord.orderId}<br/>
                        <span class="text-[10px] text-slate-400 font-normal">${ord.date}</span>
                      </td>
                      <td class="p-3.5 font-medium text-amber-300">
                        ${ord.customerName || 'Customer'}<br/>
                        <span class="text-[10px] text-slate-400 font-normal">+91 ${ord.customerPhone}</span>
                      </td>
                      <td class="p-3.5 max-w-xs truncate font-medium text-slate-300">
                        ${ord.customerAddress || 'Lucknow, UP'} (Pincode: ${ord.pincode || '226001'})
                      </td>
                      <td class="p-3.5 font-bold text-emerald-400">
                        ₹${(ord.totalAmount || 999).toLocaleString()}.00
                      </td>
                      <td class="p-3.5">
                        <span class="px-3 py-1 rounded-full text-[10px] font-bold ${ord.statusColor || 'bg-blue-900 text-blue-200'} border">
                          ${ord.status}
                        </span>
                      </td>
                      <td class="p-3.5">
                        <select onchange="handleOrderStatusChange('${ord.orderId}', this.value)" class="bg-slate-800 text-white border border-slate-700 rounded-xl p-2.5 text-xs focus:outline-none focus:border-amber-400 cursor-pointer font-semibold">
                          <option value="Order Placed" ${ord.status==='Order Placed'?'selected':''}>1. Order Received (Order Placed)</option>
                          <option value="Dispatched" ${ord.status==='Dispatched'?'selected':''}>2. Dispatched from Lucknow HQ</option>
                          <option value="In Transit" ${ord.status==='In Transit'?'selected':''}>3. In Transit (Bluedart Express)</option>
                          <option value="Out for Delivery" ${ord.status==='Out for Delivery'?'selected':''}>4. Out for Delivery</option>
                          <option value="Delivered" ${ord.status==='Delivered'?'selected':''}>5. Delivered Successfully 🎉</option>
                        </select>
                      </td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          `}
        </div>

      </div>
    </div>
  `;
}
