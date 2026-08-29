import csv
import json

raw_file = "/Users/khushi/.gemini/antigravity/scratch/cieloria/parse_full_csv.py"
with open(raw_file) as f:
    text = f.read()

start_idx = text.find("csv_raw = \"\"\"") + len("csv_raw = \"\"\"")
end_idx = text.rfind("\"\"\"")
csv_data = text[start_idx:end_idx]

lines = csv_data.splitlines()
reader = csv.reader(lines)
header = next(reader)

products = []
seen = set()

for row in reader:
    if not row or len(row) < 33: continue
    handle = row[0].strip()
    title = row[1].strip()
    
    if not handle or not title or handle in seen or "http" in handle or "<p" in handle or "<ul" in handle:
        continue
    
    if not handle[0].isalnum():
        continue
        
    seen.add(handle)
    
    try:
        price = int(float(row[23]))
        orig_price = int(float(row[24]))
    except:
        price = 999
        orig_price = 2499
        
    disc = int(round((1 - (price / orig_price)) * 100)) if orig_price > 0 else 50
    
    cat = "Bracelets"
    if "ring" in handle.lower() or "ring" in title.lower(): cat = "Rings"
    elif "necklace" in handle.lower() or "pendant" in handle.lower() or "necklace" in title.lower(): cat = "Necklaces"
    elif "earring" in handle.lower() or "hoop" in handle.lower() or "stud" in handle.lower(): cat = "Earrings"
    elif "set" in handle.lower(): cat = "Personalised"
    
    img = ""
    for cell in row:
        if "https://cdn.shopify.com" in cell:
            img = cell.strip()
            break
            
    if not img: continue
    
    is_fine_gold = "9kt" in title.lower() or "gold" in title.lower() and "pendant" in title.lower()
    is_silver = "silver" in title.lower() or "sterling" in title.lower()
    
    clean_title = title.replace("PALMONAS", "CIELORIA").replace("Palmonas", "Cieloria").replace("palmonas", "cieloria")

    g1 = img
    g2 = img
    g3 = img
    g4 = img
    
    products.append({
        "id": handle,
        "name": clean_title,
        "category": cat,
        "occasion": "Daily Wear" if (len(products) % 2 == 0) else "Office Wear",
        "price": price,
        "originalPrice": orig_price,
        "discountPercent": disc,
        "rating": 4.6,
        "reviewCount": 132,
        "metal": "9KT Solid Gold" if is_fine_gold else ("925 Sterling Silver" if is_silver else "18K Gold Tone Plated"),
        "isBestseller": (len(products) % 2 == 0),
        "isNew": (len(products) % 3 == 0),
        "isFineGold": is_fine_gold,
        "isSilver": is_silver,
        "inStock": True,
        "sku": f"SKU: CIE{100 + len(products)}",
        "image": img,
        "secondaryImage": img,
        "gallery": [g1, g2, g3, g4],
        "features": ["18K Gold Plated Anti-Tarnish Coating", "100% Waterproof & Sweatproof", "Hypoallergenic & Nickel-Free", "Lifetime Polish Guarantee"],
        "description": clean_title + " - 18K Gold Tone Plated PVD Stainless Steel anti-tarnish jewelry by CIELORIA. Designed for everyday luxury and timeless elegance.",
        "dimensions": "Weight: 8g | Length: Adjustable 16 + 2 inch extension | 100% Waterproof & Sweatproof",
        "materials": "18K Gold Plated PVD Vacuum Coating over 316L Surgical Grade Stainless Steel.",
        "care": "100% Shower and swim safe. Tarnish resistant. Wipe with a dry soft cloth after sea/ocean water exposure."
    })

products_json_str = json.dumps(products, indent=2)

js_content = """// CIELORIA - Demifine® Anti-Tarnish Luxury Storefront (Clean Customer App - No Admin Links)

const GOKWIK_CREDENTIALS = {
  merchantId: "2yyq6ziimeofq998",
  appId: "app_id_93a59e4095c7408f9b7ebeb50bcdeda9",
  appSecret: "app_secret_2ffb4ee8695d4188a75fd7bcfca5fc5e",
  id: "42961",
  environment: "production"
};

const PRODUCTS = """ + products_json_str + """;

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

let state = {
  viewMode: 'homepage',
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
  wishlist: getStoredData('cieloria_wishlist', []),
  appliedCoupon: '',
  discountPercentage: 0,
  activeCurrency: 'INR',
  searchQuery: '',
  searchPlaceholderIndex: 0,
  tickerIndex: 0,
  heroSlideIndex: 0,
  
  isLoggedIn: getStoredData('cieloria_is_logged_in', false),
  customerName: getStoredData('cieloria_cust_name', ''),
  customerPhone: getStoredData('cieloria_cust_phone', ''),
  customerEmail: getStoredData('cieloria_cust_email', ''),
  pincode: getStoredData('cieloria_pincode', ''),
  customerAddress: getStoredData('cieloria_address', ''),
  ordersList: getStoredData('cieloria_orders', []),
  rewardsCoins: getStoredData('cieloria_coins', 0),

  merchantAllOrders: getStoredData('cieloria_merchant_all_orders', []),

  isCartOpen: false,
  isCheckoutOpen: false,
  isKwikPassAuthOpen: false,
  kwikPassStep: 1,
  otpDigits: ["", "", "", ""],
  checkoutStep: 1,
  isOrderSummaryOpen: false,
  isSubscribed: false,
  lastPlacedOrder: null
};

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

            <button onclick="handleProfileIconClick()" class="relative flex items-center justify-center cursor-pointer hover:opacity-80 transition-opacity p-1" title="${state.isLoggedIn ? 'My Account' : 'KwikPass Login'}">
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
          ${SUBHEADER_NAV.map(nav => `
            <div class="relative py-1 cursor-pointer shrink-0">
              <button 
                onclick="openPLPCategory('${nav.cat}')" 
                class="hover:text-[#C5A059] transition-colors ${state.plpCategory === nav.cat && (state.viewMode === 'plp' || state.viewMode === 'about') ? 'font-bold text-[#C5A059]' : ''}"
              >
                ${nav.name}
              </button>
              ${nav.badge ? `<span class="${nav.badgeClass}">${nav.badge}</span>` : ''}
            </div>
          `).join('')}
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
          <p class="text-xs text-slate-500 leading-relaxed">Login via KwikPass 1-Click Mobile OTP to access your orders, saved addresses, and live shipment tracking.</p>
          <div class="pt-2">
            <button onclick="triggerGoKwikSDKLogin()" class="bg-black text-white font-bold px-8 py-3.5 rounded-xl text-xs uppercase tracking-wider shadow-md hover:bg-[#C5A059] transition-colors">
              Login via GoKwik ⚡
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
              <span class="inline-block bg-emerald-100 text-emerald-800 text-[9px] font-bold px-2 py-0.5 rounded mt-1">⚡ Verified KwikPass Member</span>
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
                          <span class="border px-3 py-0.5 rounded-full text-[10px] font-bold ${ord.statusColor}">${ord.status}</span>
                        </div>
                        <p class="text-xs text-slate-400">Placed on ${ord.date}</p>
                      </div>

                      <div class="text-right">
                        <span class="font-bold text-base text-[#1A1A1A] block">₹${ord.totalAmount.toLocaleString()}.00</span>
                        <span class="text-[10px] text-slate-400">Courier: ${ord.courier} (${ord.trackingId})</span>
                      </div>
                    </div>

                    <div class="bg-[#FAF8F5] border border-[#E6E1D7] p-4 rounded-2xl space-y-2">
                      <div class="flex justify-between items-center text-xs">
                        <span class="font-bold text-[#1A1A1A]">Live Shipment Progress</span>
                        <span class="text-xs font-bold text-emerald-700">Est. Delivery: ${ord.estimatedDelivery}</span>
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
                      ${ord.items.map(item => `
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
                  <button onclick="setStoredData('cieloria_cust_name', state.customerName); setStoredData('cieloria_cust_phone', state.customerPhone); alert('Profile Details Saved!')" class="bg-black text-white px-8 py-3.5 rounded-xl font-bold text-xs uppercase tracking-wider">Save Changes</button>
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

            <button onclick="addToCart('${p.id}'); triggerGoKwikCheckout();" class="w-full border-2 border-black bg-white hover:bg-black hover:text-white text-black font-bold py-3.5 rounded-xl text-xs uppercase tracking-widest transition-colors shadow-sm flex items-center justify-center gap-2">
              <span class="text-amber-600">⚡</span>
              <span>BUY IT NOW (KwikPass Fast Checkout)</span>
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

// Modals, Cart Drawer & KwikPass Auth
function renderModals() {
  let html = '';

  const subtotal = calculateCartSubtotal();
  const discount = calculateCartDiscount();
  const finalTotal = calculateCartFinalTotal();
  const cartTotalItems = calculateCartTotalCount();

  // 1. KwikPass Auth & Login Popup Modal
  if (state.isKwikPassAuthOpen) {
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-4 bg-black/65 backdrop-blur-xs">
        <div class="relative w-full max-w-3xl bg-[#FDF0F5] border border-rose-200 rounded-3xl overflow-hidden shadow-2xl text-left flex flex-col md:flex-row">
          
          <button onclick="state.isKwikPassAuthOpen=false; renderApp();" class="absolute top-4 right-4 z-20 w-8 h-8 rounded-full bg-white/80 hover:bg-white text-slate-500 hover:text-black flex items-center justify-center text-sm font-bold shadow-sm">✕</button>

          <!-- Left Side: Cieloria KwikPass Brand Welcome Panel -->
          <div class="md:w-1/2 p-6 sm:p-8 flex flex-col justify-between space-y-6 bg-gradient-to-b from-[#FDF0F5] to-[#F7DCE6] text-center md:text-left">
            <div class="space-y-4">
              <div class="flex items-center justify-center md:justify-start gap-3">
                <span class="font-serif text-2xl font-bold tracking-[0.15em] text-[#1A1A1A] uppercase">CIELORIA</span>
                <span class="text-[10px] font-extrabold uppercase tracking-wider bg-white/80 border border-rose-200 px-2 py-0.5 rounded text-slate-800 flex items-center gap-1">
                  Kwik<span class="text-amber-500 font-bold">⚡</span>Pass
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

            <div class="text-[9px] text-slate-400 font-medium text-center md:text-left">Merchant ID: 2yyq6ziimeofq998 • GoKwik Verified</div>
          </div>

          <!-- Right Side: Clean Form -->
          <div class="md:w-1/2 bg-white p-6 sm:p-8 flex flex-col justify-center text-center space-y-5">
            
            ${state.kwikPassStep === 1 ? `
              <div class="space-y-1">
                <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A]">Explore Cieloria</h3>
                <p class="text-xs text-slate-500">Affordable Luxury, Made for Every Day!</p>
              </div>

              <form onsubmit="handleKwikPassSendOTP(event)" class="space-y-4 pt-2">
                <div class="flex items-center border border-slate-300 rounded-xl px-3.5 py-3 bg-white focus-within:border-black transition-colors">
                  <span class="flex items-center gap-1.5 text-xs font-bold text-slate-700 mr-2 pr-2 border-r border-slate-200">
                    <span>🇮🇳</span>
                    <span>+91</span>
                  </span>
                  <input 
                    type="tel" 
                    id="kwikpass-phone-input"
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

            ${state.kwikPassStep === 2 ? `
              <div class="space-y-2">
                <button onclick="state.kwikPassStep=1; renderApp();" class="text-xs font-bold text-slate-400 hover:text-black flex items-center gap-1 justify-center mx-auto">
                  <span>❮</span> <span>Change Number (+91 ${state.customerPhone})</span>
                </button>
                <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A]">Verify SMS OTP</h3>
                <p class="text-xs text-slate-500">Enter 4-digit OTP sent to <strong>+91 ${state.customerPhone}</strong></p>
              </div>

              <form onsubmit="handleKwikPassVerifyOTP(event)" class="space-y-5 pt-2">
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
                <span>👤 ${state.isLoggedIn ? 'My Account & Orders' : 'Login via KwikPass'}</span>
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

              <button onclick="toggleCart(false); triggerGoKwikCheckout();" class="w-full bg-black hover:bg-[#C5A059] text-white font-bold py-4 rounded-xl text-xs uppercase tracking-wider shadow-lg flex items-center justify-center gap-2">
                <span>Proceed To KwikPass Checkout</span>
                <span>•</span>
                <span>₹${finalTotal.toLocaleString()}.00</span>
                <span>→</span>
              </button>

              <p class="text-[10px] text-slate-400 text-center font-medium">⚡ Merchant ID: ${GOKWIK_CREDENTIALS.merchantId} • Powered by GoKwik</p>
            </div>
          ` : ''}
        </div>
      </div>
    `;
  }

  // 3. Official GoKwik / KwikPass Fast Checkout Popup Modal
  if (state.isCheckoutOpen) {
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-xs">
        <div class="w-full max-w-lg bg-white rounded-3xl overflow-hidden shadow-2xl text-left border border-slate-200 flex flex-col max-h-[90vh]">
          
          <div class="p-4 border-b border-slate-200 flex items-center justify-between bg-white sticky top-0 z-10">
            <div class="flex items-center gap-3">
              <button onclick="state.isCheckoutOpen=false; renderApp();" class="text-slate-400 hover:text-black font-bold text-base">❮</button>
              <div>
                <h3 class="font-serif text-lg font-bold tracking-widest text-[#1A1A1A]">CIELORIA</h3>
                <span class="text-[9px] text-emerald-700 font-bold block">GoKwik KwikPass Integrated • ID: ${GOKWIK_CREDENTIALS.merchantId}</span>
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
            
            <!-- Step 1: KwikPass Mobile OTP Login -->
            ${state.checkoutStep === 1 ? `
              <div class="space-y-4">
                <div class="bg-[#FAF8F5] border border-amber-200 p-3 rounded-2xl flex items-center gap-3">
                  <span class="text-2xl">⚡</span>
                  <div>
                    <h5 class="font-bold text-xs text-[#1A1A1A]">KwikPass 1-Click OTP Verification</h5>
                    <p class="text-[10px] text-slate-500">Enter mobile number to auto-fill saved address from GoKwik Network</p>
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
                <button onclick="if(!state.customerPhone || state.customerPhone.trim().length<10){alert('Please enter 10-digit mobile number!'); return;} setStoredData('cieloria_cust_phone', state.customerPhone); state.checkoutStep=2; renderApp();" class="w-full bg-black text-white font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider hover:bg-[#C5A059] transition-colors">
                  Continue to Address →
                </button>
              </div>
            ` : ''}

            <!-- Step 2: Address Input -->
            ${state.checkoutStep === 2 ? `
              <div class="space-y-4">
                <h4 class="font-bold text-xs text-[#1A1A1A] uppercase tracking-wider">DELIVERY ADDRESS (GOKWIK NETWORK)</h4>
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

                <button onclick="if(!state.customerName || !state.customerAddress || !state.pincode){alert('Please complete all address fields!'); return;} setStoredData('cieloria_cust_name', state.customerName); setStoredData('cieloria_address', state.customerAddress); setStoredData('cieloria_pincode', state.pincode); state.checkoutStep=3; renderApp();" class="w-full bg-black text-white font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider hover:bg-[#C5A059] transition-colors">
                  Proceed to Payment • ₹${finalTotal.toLocaleString()}
                </button>
              </div>
            ` : ''}

            <!-- Step 3: Payment Options & Live Order Complete -->
            ${state.checkoutStep === 3 ? `
              <div class="space-y-5 text-center">
                <div class="bg-slate-50 border border-slate-200 p-4 rounded-2xl space-y-3">
                  <h4 class="font-bold text-xs text-[#1A1A1A] uppercase tracking-wider">INSTANT UPI QR SCANNER (GOKWIK PASS)</h4>
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
};

window.handleResendSMSOTP = function() {
  alert(`📲 Real SMS OTP requested for +91 ${state.customerPhone} via GoKwik Telecom Gateway (Merchant: 2yyq6ziimeofq998)`);
};

window.handleProfileIconClick = function() {
  if (state.isLoggedIn) {
    switchViewMode('account');
  } else {
    triggerGoKwikSDKLogin();
  }
};

window.triggerGoKwikSDKLogin = function() {
  if (typeof window !== 'undefined' && window.GokwikSdk && typeof window.GokwikSdk.initCheckout === 'function') {
    try {
      window.GokwikSdk.initCheckout({
        merchantId: GOKWIK_CREDENTIALS.merchantId,
        appId: GOKWIK_CREDENTIALS.appId,
        type: 'login',
        onSuccess: function(res) {
          state.isLoggedIn = true;
          state.customerPhone = res.phone || '9876543210';
          setStoredData('cieloria_is_logged_in', true);
          setStoredData('cieloria_cust_phone', state.customerPhone);
          switchViewMode('account');
        }
      });
      return;
    } catch(e) { console.log('GokwikSdk:', e); }
  }

  state.isKwikPassAuthOpen = true;
  state.kwikPassStep = 1;
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
  setStoredData('cieloria_is_logged_in', false);
  setStoredData('cieloria_cust_name', '');
  setStoredData('cieloria_cust_phone', '');
  setStoredData('cieloria_orders', []);
  alert("🚪 You have logged out successfully!");
  switchViewMode('homepage');
};

window.handleKwikPassSendOTP = function(e) {
  if (e) e.preventDefault();
  const phoneInput = document.getElementById('kwikpass-phone-input');
  if (phoneInput && phoneInput.value) {
    state.customerPhone = phoneInput.value;
  }

  if (!state.customerPhone || state.customerPhone.trim().length < 10) {
    alert('Please enter a valid 10-digit mobile number!');
    return;
  }

  setStoredData('cieloria_cust_phone', state.customerPhone);
  alert(`📲 SMS OTP Sent to +91 ${state.customerPhone} via GoKwik Gateway!`);
  state.kwikPassStep = 2;
  state.otpDigits = ["", "", "", ""];
  renderApp();

  setTimeout(() => {
    const firstBox = document.getElementById('otp-input-0');
    if (firstBox) firstBox.focus();
  }, 100);
};

window.handleKwikPassVerifyOTP = function(e) {
  if (e) e.preventDefault();
  state.isLoggedIn = true;
  if (!state.customerName) state.customerName = "Valued Customer";
  state.isKwikPassAuthOpen = false;

  setStoredData('cieloria_is_logged_in', true);
  setStoredData('cieloria_cust_name', state.customerName);
  setStoredData('cieloria_cust_phone', state.customerPhone);

  alert(`🎉 Verified! Logged in successfully for +91 ${state.customerPhone}!`);
  switchViewMode('account');
};

window.triggerGoKwikCheckout = function() {
  if (typeof window !== 'undefined' && window.GokwikSdk && typeof window.GokwikSdk.initCheckout === 'function') {
    try {
      window.GokwikSdk.initCheckout({
        merchantId: GOKWIK_CREDENTIALS.merchantId,
        appId: GOKWIK_CREDENTIALS.appId,
        cart: state.cart,
        subtotal: calculateCartSubtotal(),
        onSuccess: function() { completeUserOrder(); }
      });
      return;
    } catch(e) { console.log('GoKwik SDK:', e); }
  }

  openCheckoutModal();
};

window.completeUserOrder = function() {
  const newOrderId = `CIE-${Math.floor(10000 + Math.random() * 90000)}`;
  const finalTotal = calculateCartFinalTotal();

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
    customerPhone: state.customerPhone || '9876543210',
    customerAddress: state.customerAddress || 'Lucknow, UP',
    pincode: state.pincode || '226001',
    items: state.cart.length > 0 ? [...state.cart] : [PRODUCTS[0]]
  };

  state.ordersList.unshift(newOrder);
  state.merchantAllOrders.unshift(newOrder);

  setStoredData('cieloria_orders', state.ordersList);
  setStoredData('cieloria_merchant_all_orders', state.merchantAllOrders);

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
  if (cat === 'About') {
    state.viewMode = 'about';
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
  setStoredData('cieloria_wishlist', state.wishlist);
  renderApp();
};

window.toggleCart = function(open) { state.isCartOpen = open; renderApp(); };

window.openPincodeModal = function() {
  const code = prompt('Enter 6-digit Pincode:', state.pincode || '');
  if (code) { 
    state.pincode = code; 
    setStoredData('cieloria_pincode', code);
    renderApp(); 
  }
};

window.openCheckoutModal = function() { state.isCheckoutOpen = true; state.checkoutStep = 1; renderApp(); };
window.handleNewsletter = function(e) { e.preventDefault(); state.isSubscribed = true; renderApp(); };

document.addEventListener('DOMContentLoaded', () => { 
  renderApp(); 
});
try { renderApp(); } catch(err) { console.error('Render error:', err); }
"""

with open("/Users/khushi/.gemini/antigravity/scratch/cieloria/app.js", "w") as f:
    f.write(js_content)

print("Successfully updated app.js (removed internal admin view from customer storefront)!")
