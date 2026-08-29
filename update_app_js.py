import json

with open("/Users/khushi/.gemini/antigravity/scratch/cieloria/products_output.json") as f:
    products = json.load(f)

products_js_str = json.dumps(products, indent=2)

app_js_content = f"""// Cieloria Application - Restored Phase 4 Storefront with Complete 78 Shopify CSV Products

const CURRENCIES = {{
  INR: {{ symbol: '₹', rate: 1, label: 'INR (₹)' }},
  USD: {{ symbol: '$', rate: 0.012, label: 'USD ($)' }},
  EUR: {{ symbol: '€', rate: 0.011, label: 'EUR (€)' }},
  GBP: {{ symbol: '£', rate: 0.0094, label: 'GBP (£)' }}
}};

const ANNOUNCEMENTS = [
  "✨ 100% Anti-Tarnish & Water Resistant | Lifetime Polish Guarantee",
  "🚚 Free Express Delivery on Orders Above ₹999 via Shiprocket",
  "🎁 Use Code CIELORIA10 for Extra 10% OFF First Order",
  "⚡ Extra 5% Instant Discount on Razorpay & UPI Payments"
];

// Task 3.1 Hero Slides
const HERO_SLIDES = [
  {{
    id: 'slide-1',
    image: '{products[0]["image"]}',
    tag: '✨ DEMIFINE JEWELLERY FOR EVERYDAY LUXURY',
    title: 'Demifine Jewellery For Everyday Luxury',
    highlight: 'Anti-Tarnish & Waterproof',
    subtitle: 'Crafted in 18K Gold Plated PVD Stainless Steel for non-stop everyday elegance.'
  }},
  {{
    id: 'slide-2',
    image: '{products[1]["image"]}',
    tag: '👑 LUMIÈRE ROYAL COLLECTION 2026',
    title: 'Waterproof 18K Gold & Gemstones',
    highlight: 'Shower & Swim Safe',
    subtitle: 'Wear your favorite Solitaire pieces in the shower, pool, or gym without fading.'
  }},
  {{
    id: 'slide-3',
    image: '{products[2]["image"]}',
    tag: '💎 ANTI-TARNISH SOLITAIRE RINGS & NECKLACES',
    title: 'Timeless Everyday Polish',
    highlight: 'Lifetime Warranty Included',
    subtitle: 'Nickel-free, hypoallergenic solitaire rings backed by our lifetime color guarantee.'
  }}
];

// Task 3.3 Visual Category Grid
const CATEGORY_CARDS = [
  {{ id: 'bracelets', name: 'Bracelets', image: '{products[0]["image"]}', count: '24 Designs' }},
  {{ id: 'rings', name: 'Rings', image: '{products[9]["image"]}', count: '32 Designs' }},
  {{ id: 'necklaces', name: 'Necklaces', image: '{products[49]["image"]}', count: '28 Designs' }},
  {{ id: 'earrings', name: 'Earrings', image: '{products[38]["image"]}', count: '18 Designs' }},
  {{ id: 'mens', name: 'Men’s', image: '{products[2]["image"]}', count: '12 Designs' }},
  {{ id: 'gifting', name: 'Gifting', image: '{products[4]["image"]}', count: '20 Gift Sets' }}
];

// Task 3.7 Influencer Shoppable Reels
const REELS_DATA = [
  {{
    id: 'reel-1',
    author: '@radhika_styles',
    views: '124K',
    title: 'Waterproof test with Cieloria gold necklace in pool! 💦✨',
    productTagged: '{products[49]["name"]}',
    productId: '{products[49]["id"]}',
    image: '{products[49]["image"]}'
  }},
  {{
    id: 'reel-2',
    author: '@ananya_vogue',
    views: '98K',
    title: 'Unboxing my 18K anti-tarnish stone bracelet 💍🔥',
    productTagged: '{products[0]["name"]}',
    productId: '{products[0]["id"]}',
    image: '{products[0]["image"]}'
  }},
  {{
    id: 'reel-3',
    author: '@tanya_fashion',
    views: '156K',
    title: 'Maharani sapphire ring unboxing ✨',
    productTagged: '{products[9]["name"]}',
    productId: '{products[9]["id"]}',
    image: '{products[9]["image"]}'
  }}
];

// Task 3.8 Customer Reviews
const REVIEWS_DATA = [
  {{
    id: 'rev-1',
    author: 'Priya Malhotra',
    location: 'Mumbai, MH',
    rating: 5,
    title: 'Wore it in the ocean & shower – ZERO tarnishing!',
    review: 'I was skeptical about waterproof claims, but Cieloria 18K gold pendant survived my Bali beach vacation without losing any polish. Amazing quality!',
    date: 'Verified 2 Days Ago',
    avatar: '👩🏻',
    photo: '{products[0]["image"]}'
  }},
  {{
    id: 'rev-2',
    author: 'Simran Kaur',
    location: 'New Delhi, DL',
    rating: 5,
    title: 'Sensitive skin friendly! No green marks.',
    review: 'Cheap artificial jewelry always gave me skin allergies. Cieloria hypoallergenic surgical steel base is a lifesaver. Feels so luxurious!',
    date: 'Verified 1 Week Ago',
    avatar: '👱‍♀️',
    photo: '{products[9]["image"]}'
  }},
  {{
    id: 'rev-3',
    author: 'Rohan Verma',
    location: 'Bengaluru, KA',
    rating: 5,
    title: 'Bought signet ring for myself & gift set for girlfriend',
    review: 'Shiprocket delivery was super fast (2 days to Bangalore). COD OTP verification was smooth. Best demi-fine jewelry brand!',
    date: 'Verified 2 Weeks Ago',
    avatar: '👨🏻',
    photo: '{products[49]["image"]}'
  }}
];

// Complete Real Cieloria Shopify Product Catalog (All 78 CSV Products)
const PRODUCTS = {products_js_str};

const CATEGORIES = ['All', 'Rings', 'Necklaces', 'Earrings', 'Bracelets', 'Men’s', 'Personalised'];
const OCCASIONS = ['Daily Wear', 'Office Wear', '18K Gold Plated', 'Anti-Tarnish Demi-Fine', 'Gifts'];

const PINCODES = {{
  '400001': {{ location: 'Mumbai Central, MH', estDays: 'Tuesday, Sep 2 (Express Air)', cod: true, shiprocketCourier: 'Delhivery Air' }},
  '110001': {{ location: 'Connaught Place, New Delhi', estDays: 'Tuesday, Sep 2 (Express Air)', cod: true, shiprocketCourier: 'Bluedart Express' }},
  '560001': {{ location: 'MG Road, Bengaluru, KA', estDays: 'Wednesday, Sep 3', cod: true, shiprocketCourier: 'Xpressbees' }}
}};

// Global State
let state = {{
  viewMode: 'homepage', // 'homepage', 'plp', 'pdp'
  selectedProductId: '{products[0]["id"]}',
  activeGalleryIndex: 0,
  selectedRingSize: 'US 7',
  openAccordion: 'details',
  bestsellerTab: 'All',

  // PLP Filter State
  plpCategory: 'All',
  plpPriceFilter: 'all',
  plpMetalFilter: 'all',
  plpOccasionFilter: 'all',
  plpInStockOnly: false,
  plpSortBy: 'featured',

  cart: [{{ ...PRODUCTS[0], quantity: 1 }}],
  wishlist: ['{products[0]["id"]}'],
  activeCurrency: 'INR',
  searchQuery: '',
  tickerIndex: 0,
  heroSlideIndex: 0,
  pincode: '',
  pincodeResult: null,
  quickViewProduct: null,
  isCartOpen: false,
  isCheckoutOpen: false,
  isTrackerOpen: false,
  isAccountOpen: false,
  isGuaranteeOpen: false,
  isSizeGuideOpen: false,
  activePolicy: null,
  isSubscribed: false
}};

function formatPrice(inrPrice) {{
  const curr = CURRENCIES[state.activeCurrency] || CURRENCIES.INR;
  const val = Math.round(inrPrice * curr.rate);
  return `${{curr.symbol}}${{val.toLocaleString()}}`;
}}

// Auto Timers
setInterval(() => {{
  state.tickerIndex = (state.tickerIndex + 1) % ANNOUNCEMENTS.length;
  renderApp();
}}, 3500);

setInterval(() => {{
  if (state.viewMode === 'homepage') {{
    state.heroSlideIndex = (state.heroSlideIndex + 1) % HERO_SLIDES.length;
    renderApp();
  }}
}}, 4500);

// Main App Renderer
function renderApp() {{
  const appContainer = document.getElementById('app');
  if (!appContainer) return;

  const currentHero = HERO_SLIDES[state.heroSlideIndex];
  const cartTotalItems = state.cart.reduce((sum, item) => sum + item.quantity, 0);

  const predictiveResults = state.searchQuery.trim().length >= 2 
    ? PRODUCTS.filter(p => 
        p.name.toLowerCase().includes(state.searchQuery.toLowerCase()) ||
        p.category.toLowerCase().includes(state.searchQuery.toLowerCase())
      ).slice(0, 5)
    : [];

  appContainer.innerHTML = `
    <!-- Header (Task 2.1) -->
    <header class="sticky top-0 z-40 w-full border-b border-[#EBE5DF] bg-[#FAF8F5]/95 backdrop-blur-md shadow-sm">
      <div class="bg-[#1A1A1A] text-xs py-2 px-4 text-[#E6CA65] flex items-center justify-between relative overflow-hidden">
        <button onclick="changeTicker(-1)" class="text-slate-400 hover:text-white px-2">❮</button>
        <div class="w-full text-center font-medium text-white tracking-wide flex items-center justify-center gap-2">
          <span>✨ \${{ANNOUNCEMENTS[state.tickerIndex]}}</span>
        </div>
        <button onclick="changeTicker(1)" class="text-slate-400 hover:text-white px-2">❯</button>
      </div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-[#C5A059] to-[#F4E4BA] flex items-center justify-center text-white font-serif font-bold text-xl shadow-md">
            C
          </div>
          <div>
            <button onclick="switchViewMode('homepage')" class="font-serif text-2xl md:text-3xl font-bold tracking-widest text-[#1A1A1A] hover:text-[#C5A059] text-left">
              CIELORIA
            </button>
            <span class="block text-[9px] tracking-[0.3em] text-[#C5A059] font-semibold uppercase -mt-1">
              Demi-Fine Luxury
            </span>
          </div>
        </div>

        <nav class="hidden lg:flex items-center gap-8 text-xs font-semibold uppercase tracking-wider text-[#1A1A1A]">
          <button onclick="switchViewMode('homepage')" class="hover:text-[#C5A059] \${{state.viewMode === 'homepage' ? 'text-[#C5A059] font-bold' : ''}}">Storefront</button>
          
          <div class="relative group py-6">
            <button class="flex items-center gap-1 hover:text-[#C5A059]">
              <span>Categories ▾</span>
            </button>
            <div class="mega-menu-dropdown absolute top-full left-0 w-80 bg-white border border-[#EBE5DF] rounded-2xl shadow-xl p-4 text-left grid grid-cols-2 gap-2 text-xs">
              \${{CATEGORIES.filter(c => c !== 'All').map(cat => `
                <button onclick="openPLPCategory('\${{cat}}')" class="p-2.5 rounded-xl hover:bg-[#FAF8F5] text-left font-medium hover:text-[#C5A059]">
                  \${{cat}}
                </button>
              `).join('')}}
            </div>
          </div>

          <button onclick="switchViewMode('plp')" class="hover:text-[#C5A059] \${{state.viewMode === 'plp' ? 'text-[#C5A059] font-bold' : ''}}">Shop Catalog (\${{PRODUCTS.length}} Items)</button>
          <button onclick="openPDP('\${{state.selectedProductId}}')" class="hover:text-[#C5A059] \${{state.viewMode === 'pdp' ? 'text-[#C5A059] font-bold' : ''}}">Featured PDP</button>
          <button onclick="openGuaranteeModal()" class="hover:text-[#C5A059]">Anti-Tarnish Science</button>
        </nav>

        <div class="flex items-center gap-3">
          <select onchange="changeCurrency(this.value)" class="bg-white border border-[#EBE5DF] text-xs font-bold text-[#1A1A1A] rounded-full px-3 py-1.5 focus:outline-none cursor-pointer shadow-sm">
            \${{Object.keys(CURRENCIES).map(curr => `
              <option value="\${{curr}}" \${{state.activeCurrency === curr ? 'selected' : ''}}>\${{CURRENCIES[curr].label}}</option>
            `).join('')}}
          </select>

          <div class="relative">
            <div class="flex items-center bg-white border border-[#EBE5DF] rounded-full px-3 py-1.5 w-44 sm:w-60 shadow-sm">
              <span class="text-[#C5A059] mr-2">🔍</span>
              <input 
                type="text" 
                placeholder="Search \${{PRODUCTS.length}} products..." 
                value="\${{state.searchQuery}}"
                oninput="handleSearchInput(this.value)"
                class="bg-transparent text-xs text-[#1A1A1A] placeholder-slate-400 focus:outline-none w-full"
              />
            </div>

            \${{predictiveResults.length > 0 ? `
              <div class="absolute top-full right-0 mt-2 w-72 sm:w-80 bg-white border border-[#EBE5DF] rounded-2xl shadow-2xl p-3 z-50 text-left space-y-2">
                <span class="text-[10px] uppercase font-bold text-[#C5A059] px-2">Auto Suggestions</span>
                \${{predictiveResults.map(p => `
                  <div onclick="openPDP('\${{p.id}}')" class="flex items-center gap-3 p-2 rounded-xl hover:bg-[#FAF8F5] cursor-pointer">
                    <img src="\${{p.image}}" class="w-10 h-10 object-cover rounded-lg" />
                    <div>
                      <h5 class="font-serif text-xs font-bold text-[#1A1A1A] line-clamp-1">\${{p.name}}</h5>
                      <span class="text-[11px] font-bold text-[#C5A059]">\${{formatPrice(p.price)}}</span>
                    </div>
                  </div>
                `).join('')}}
              </div>
            ` : ''}}
          </div>

          <button onclick="openAccountModal()" class="p-2 text-[#1A1A1A] hover:text-[#C5A059]" title="VIP Account">👤</button>

          <button class="relative p-2 text-[#1A1A1A]" title="Wishlist">
            ❤️
            <span class="absolute top-0 right-0 w-4 h-4 bg-rose-500 text-white font-bold text-[10px] rounded-full flex items-center justify-center">
              \${{state.wishlist.length}}
            </span>
          </button>

          <button onclick="toggleCart(true)" class="p-2.5 bg-[#C5A059] hover:bg-[#D4AF37] text-white rounded-full font-bold shadow-md flex items-center gap-2 px-4">
            🛍️ <span class="hidden sm:inline text-xs font-semibold">Bag</span>
            <span class="w-5 h-5 bg-white text-[#C5A059] rounded-full text-[11px] flex items-center justify-center font-bold">
              \${{cartTotalItems}}
            </span>
          </button>
        </div>
      </div>
    </header>

    <!-- Main View Switcher -->
    <main class="flex-1">
      \${{state.viewMode === 'homepage' ? renderHomepageView(currentHero) : ''}}
      \${{state.viewMode === 'plp' ? renderPLPView() : ''}}
      \${{state.viewMode === 'pdp' ? renderPDPView() : ''}}
    </main>

    <!-- Modals -->
    \${{renderModals()}}

    <!-- Task 2.2: 5-Column Footer -->
    <footer class="bg-[#1A1A1A] text-slate-400 pt-16 pb-8 text-xs text-left">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8">
          <div class="space-y-4">
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-[#C5A059] to-[#F4E4BA] flex items-center justify-center text-white font-serif font-bold text-base">C</div>
              <span class="font-serif text-2xl font-bold tracking-widest text-white">CIELORIA</span>
            </div>
            <p class="text-slate-400 text-xs">India's premier demi-fine anti-tarnish jewelry brand. 100% waterproof 18K gold plated luxury.</p>
          </div>

          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase">Customer Care</h4>
            <ul class="space-y-2">
              <li><button onclick="openTrackerModal()" class="hover:text-[#C5A059]">Track Order (Shiprocket)</button></li>
              <li><button onclick="openPolicyModal('refund')" class="hover:text-[#C5A059]">Shipping & Delivery</button></li>
              <li><button onclick="openPolicyModal('refund')" class="hover:text-[#C5A059]">Return & Exchange</button></li>
              <li><button onclick="openPolicyModal('faqs')" class="hover:text-[#C5A059]">FAQs</button></li>
              <li><button onclick="openPolicyModal('contact')" class="hover:text-[#C5A059]">Contact Us</button></li>
            </ul>
          </div>

          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase">Shop Quick Links</h4>
            <ul class="space-y-2">
              \${{CATEGORIES.filter(c => c !== 'All').map(c => `
                <li><button onclick="openPLPCategory('\${{c}}')" class="hover:text-[#C5A059]">18K \${{c}}</button></li>
              `).join('')}}
            </ul>
          </div>

          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase">Policies</h4>
            <ul class="space-y-2">
              <li><button onclick="openPolicyModal('privacy')" class="hover:text-[#C5A059]">Privacy Policy</button></li>
              <li><button onclick="openPolicyModal('terms')" class="hover:text-[#C5A059]">Terms of Service</button></li>
              <li><button onclick="openPolicyModal('refund')" class="hover:text-[#C5A059]">Refund Policy</button></li>
              <li><button onclick="openPolicyModal('warranty')" class="hover:text-[#C5A059]">Warranty & Anti-Tarnish</button></li>
            </ul>
          </div>

          <div class="space-y-3">
            <h4 class="font-serif text-sm font-bold text-white uppercase">Cieloria VIP Club</h4>
            <p class="text-slate-400 text-xs">Get 10% off your first order.</p>
            \${{!state.isSubscribed ? `
              <form onsubmit="handleNewsletter(event)" class="space-y-2">
                <input type="email" placeholder="Enter email..." required class="w-full bg-[#2C2C2C] text-white text-xs border border-white/10 rounded-xl px-3 py-2.5 focus:outline-none" />
                <button type="submit" class="w-full bg-[#C5A059] text-white font-bold py-2.5 rounded-xl text-xs">Subscribe & Save 10%</button>
              </form>
            ` : `
              <div class="bg-[#C5A059]/20 text-[#E6CA65] p-3 rounded-xl border border-[#C5A059]/40 text-xs">
                🎉 Subscribed! Use Code <strong class="text-white">CIELORIA10</strong> for 10% OFF!
              </div>
            `}}
          </div>
        </div>

        <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-center md:text-left">
          <div class="flex flex-wrap items-center justify-center gap-2 text-[11px]">
            <span class="text-slate-500 font-semibold mr-1">Accepted Payments:</span>
            <span class="bg-[#2C2C2C] text-[#E6CA65] font-bold px-2.5 py-1 rounded">Razorpay</span>
            <span class="bg-[#2C2C2C] text-slate-200 font-bold px-2.5 py-1 rounded">Stripe</span>
            <span class="bg-[#2C2C2C] text-emerald-400 font-bold px-2.5 py-1 rounded">UPI / GPay</span>
            <span class="bg-[#2C2C2C] text-slate-200 font-bold px-2.5 py-1 rounded">Cash on Delivery</span>
          </div>

          <div class="text-slate-500 text-[11px]">
            © ${{new Date().getFullYear()}} CIELORIA (cieloria.com). All Rights Reserved. \${{PRODUCTS.length}} Products Loaded.
          </div>
        </div>
      </div>
    </footer>
  `;
}}

// Render Homepage View
function renderHomepageView(currentHero) {{
  const bestsellersTabProducts = PRODUCTS.filter(p => {{
    const matchesTab = state.bestsellerTab === 'All' || p.category === state.bestsellerTab;
    return matchesTab && p.isBestseller;
  }});

  return `
    <section class="relative overflow-hidden w-full bg-[#1A1A1A] min-h-[520px] lg:min-h-[600px] flex items-center">
      <div class="absolute inset-0 z-0">
        <img src="\${{currentHero.image}}" class="w-full h-full object-cover opacity-60 transition-all duration-1000 scale-105" />
        <div class="absolute inset-0 bg-gradient-to-r from-[#1A1A1A] via-[#1A1A1A]/70 to-transparent"></div>
      </div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full text-left py-16">
        <div class="max-w-2xl space-y-6">
          <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-[#E6CA65] text-xs font-bold uppercase tracking-widest">
            <span>\${{currentHero.tag}}</span>
          </div>

          <h1 class="font-serif text-4xl sm:text-5xl lg:text-6xl font-bold text-white leading-[1.12]">
            Demifine Jewellery For Everyday Luxury <br />
            <span class="gold-gradient-text">\${{currentHero.highlight}}</span>
          </h1>

          <p class="text-slate-300 text-base sm:text-lg font-light leading-relaxed">
            \${{currentHero.subtitle}}
          </p>

          <div class="flex flex-wrap items-center gap-4 pt-4">
            <button onclick="scrollToSection('bestsellers-section')" class="btn-gold shadow-2xl">
              <span>Shop Bestsellers →</span>
            </button>
            <button onclick="switchViewMode('plp')" class="btn-outline-white">
              <span>Explore All \${{PRODUCTS.length}} Products</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Task 3.2 USPs Strip -->
    <section class="py-8 bg-white border-y border-[#EBE5DF]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
          <div class="flex flex-col items-center space-y-2 p-3">
            <span class="w-12 h-12 rounded-full bg-[#C5A059]/15 text-[#C5A059] flex items-center justify-center text-xl font-bold">✨</span>
            <h4 class="font-serif text-sm font-bold text-[#1A1A1A]">Anti-Tarnish Guarantee</h4>
            <p class="text-[11px] text-[#6B655F]">Lifetime Color Polish Warranty</p>
          </div>
          <div class="flex flex-col items-center space-y-2 p-3">
            <span class="w-12 h-12 rounded-full bg-[#C5A059]/15 text-[#C5A059] flex items-center justify-center text-xl font-bold">🌿</span>
            <h4 class="font-serif text-sm font-bold text-[#1A1A1A]">Hypoallergenic & Safe</h4>
            <p class="text-[11px] text-[#6B655F]">316L Surgical Steel Base</p>
          </div>
          <div class="flex flex-col items-center space-y-2 p-3">
            <span class="w-12 h-12 rounded-full bg-[#C5A059]/15 text-[#C5A059] flex items-center justify-center text-xl font-bold">💦</span>
            <h4 class="font-serif text-sm font-bold text-[#1A1A1A]">Water & Sweat Resistant</h4>
            <p class="text-[11px] text-[#6B655F]">100% Shower & Swim Safe</p>
          </div>
          <div class="flex flex-col items-center space-y-2 p-3">
            <span class="w-12 h-12 rounded-full bg-[#C5A059]/15 text-[#C5A059] flex items-center justify-center text-xl font-bold">🔄</span>
            <h4 class="font-serif text-sm font-bold text-[#1A1A1A]">Easy 7-Day Returns</h4>
            <p class="text-[11px] text-[#6B655F]">Hassle-Free Doorstep Pickups</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Task 3.3 Visual Category Grid -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-8">
      <div class="text-center space-y-2">
        <span class="text-xs uppercase tracking-widest text-[#C5A059] font-bold">Explore Collections</span>
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#1A1A1A]">Curated Jewelry Categories</h2>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6">
        \${{CATEGORY_CARDS.map(c => `
          <div onclick="openPLPCategory('\${{c.name}}')" class="arch-card bg-white border border-[#EBE5DF] cursor-pointer text-center group shadow-sm">
            <img src="\${{c.image}}" class="w-full h-44 object-cover transition-transform duration-700 group-hover:scale-110" />
            <div class="p-3 bg-white space-y-0.5">
              <h4 class="font-serif text-base font-bold text-[#1A1A1A] group-hover:text-[#C5A059]">\${{c.name}}</h4>
              <span class="text-[10px] text-[#6B655F] block font-medium">\${{c.count}}</span>
            </div>
          </div>
        `).join('')}}
      </div>
    </section>

    <!-- Task 3.4: Bestsellers Carousel / Tabbed Collection -->
    <section id="bestsellers-section" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-8 bg-white border-y border-[#EBE5DF] rounded-3xl">
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-[#EBE5DF] pb-6 text-left">
        <div>
          <span class="text-xs uppercase tracking-widest text-[#C5A059] font-bold">🔥 Most Loved Jewels</span>
          <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#1A1A1A] mt-1">Cieloria Bestsellers</h2>
        </div>

        <div class="flex flex-wrap gap-2">
          \${{['All', 'Rings', 'Necklaces', 'Earrings', 'Bracelets'].map(tab => `
            <button 
              onclick="state.bestsellerTab = '\${{tab}}'; renderApp();" 
              class="px-4 py-2 rounded-full text-xs font-semibold \${{state.bestsellerTab === tab ? 'bg-[#C5A059] text-white shadow-md' : 'bg-[#FAF8F5] text-[#1A1A1A] border border-[#EBE5DF]'}}"
            >
              \${{tab === 'All' ? 'All Bestsellers' : tab}}
            </button>
          `).join('')}}
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        \${{bestsellersTabProducts.slice(0, 12).map(p => `
          <div class="group relative bg-[#FAF8F5] rounded-2xl border border-[#EBE5DF] card-elevation overflow-hidden shadow-sm flex flex-col justify-between">
            <div class="relative aspect-square w-full bg-white overflow-hidden">
              <img src="\${{p.image}}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
              <div class="absolute top-3 left-3 bg-[#1A1A1A] text-white text-[10px] font-bold uppercase px-2 py-0.5 rounded shadow">
                \${{p.discountPercent}}% OFF
              </div>
              <div class="absolute inset-0 bg-gradient-to-t from-[#1A1A1A]/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end justify-center p-4 gap-2">
                <button onclick="openPDP('\${{p.id}}')" class="flex-1 bg-white text-[#1A1A1A] text-xs font-semibold py-2.5 rounded-xl border">View PDP</button>
                <button onclick="addToCart('\${{p.id}}')" class="bg-[#C5A059] text-white text-xs font-bold px-3 py-2.5 rounded-xl">Add</button>
              </div>
            </div>

            <div class="p-4 space-y-2 text-left">
              <div class="flex items-center justify-between text-xs text-[#6B655F]">
                <div class="flex items-center gap-1 text-[#C5A059]">
                  <span>★</span> <span class="font-bold text-[#1A1A1A]">\${{p.rating}}</span> <span>(\${{p.reviewCount}})</span>
                </div>
                <span class="text-[10px] text-emerald-700 font-semibold bg-emerald-50 px-2 py-0.5 rounded">COD Verified</span>
              </div>
              <h3 onclick="openPDP('\${{p.id}}')" class="font-serif text-base font-bold text-[#1A1A1A] hover:text-[#C5A059] cursor-pointer line-clamp-1">\${{p.name}}</h3>
              <div class="pt-2 border-t border-[#EBE5DF] flex items-center justify-between">
                <div>
                  <span class="text-xs text-slate-400 line-through mr-1">\${{formatPrice(p.originalPrice)}}</span>
                  <span class="font-bold text-base text-[#1A1A1A]">\${{formatPrice(p.price)}}</span>
                </div>
                <button onclick="addToCart('\${{p.id}}')" class="text-xs text-[#C5A059] font-bold uppercase">+ Add</button>
              </div>
            </div>
          </div>
        `).join('')}}
      </div>
    </section>

    <!-- Task 3.5: Comparison Banner -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="bg-white rounded-3xl border border-[#EBE5DF] overflow-hidden shadow-xl grid grid-cols-1 lg:grid-cols-12">
        <div class="lg:col-span-6 relative min-h-[380px] bg-[#1A1A1A]">
          <img src="\${{products[0]["image"]}}" class="w-full h-full object-cover opacity-80" />
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent flex items-end p-8 text-left">
            <div class="space-y-2">
              <span class="bg-[#C5A059] text-white text-xs font-bold px-3 py-1 rounded-full uppercase">100% Shower & Swim Safe</span>
              <h3 class="font-serif text-3xl font-bold text-white">Waterproof Science in Motion</h3>
            </div>
          </div>
        </div>

        <div class="lg:col-span-6 p-8 sm:p-12 space-y-6 text-left flex flex-col justify-between">
          <div>
            <span class="text-xs uppercase tracking-widest text-[#C5A059] font-bold">The Demi-Fine Revolution</span>
            <h3 class="font-serif text-3xl font-bold text-[#1A1A1A] mt-1">Cheap Imitation vs. Cieloria Demi-Fine</h3>
          </div>

          <div class="space-y-3 text-xs">
            <div class="grid grid-cols-3 p-3 bg-[#FAF8F5] rounded-xl font-bold border border-[#EBE5DF] text-[#1A1A1A]">
              <span>Feature</span>
              <span class="text-slate-400">Cheap Brass Jewelry</span>
              <span class="text-[#C5A059]">✨ Cieloria 18K</span>
            </div>
            <div class="grid grid-cols-3 p-3 border-b border-[#EBE5DF]">
              <span class="font-semibold">Waterproof</span>
              <span class="text-rose-500">❌ Rusts in water</span>
              <span class="text-emerald-700 font-bold">✓ 100% Swim Safe</span>
            </div>
            <div class="grid grid-cols-3 p-3 border-b border-[#EBE5DF]">
              <span class="font-semibold">Skin Reaction</span>
              <span class="text-rose-500">❌ Turns skin green</span>
              <span class="text-emerald-700 font-bold">✓ Hypoallergenic</span>
            </div>
            <div class="grid grid-cols-3 p-3 border-b border-[#EBE5DF]">
              <span class="font-semibold">Plating Tech</span>
              <span class="text-slate-400">Flash electroplate</span>
              <span class="text-[#C5A059] font-bold">PVD 18K Vacuum Gold</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Task 3.6: Shop by Look -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-8">
      <div class="text-center space-y-2">
        <span class="text-xs uppercase tracking-widest text-[#C5A059] font-bold">Curated Styling</span>
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#1A1A1A]">Shop By Look</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="relative rounded-3xl overflow-hidden shadow-xl group h-96 bg-[#1A1A1A]">
          <img src="\${{products[9]["image"]}}" class="w-full h-full object-cover opacity-70 group-hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 p-8 flex flex-col justify-end text-left bg-gradient-to-t from-black/80 via-transparent to-transparent">
            <span class="text-xs uppercase font-bold text-[#E6CA65] tracking-widest">Edit #01</span>
            <h3 class="font-serif text-3xl font-bold text-white">Stack Your Look</h3>
            <button onclick="switchViewMode('plp')" class="btn-gold mt-4 text-xs font-bold inline-flex w-40">Shop The Edit →</button>
          </div>
        </div>

        <div class="relative rounded-3xl overflow-hidden shadow-xl group h-96 bg-[#1A1A1A]">
          <img src="\${{products[49]["image"]}}" class="w-full h-full object-cover opacity-70 group-hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 p-8 flex flex-col justify-end text-left bg-gradient-to-t from-black/80 via-transparent to-transparent">
            <span class="text-xs uppercase font-bold text-[#E6CA65] tracking-widest">Edit #02</span>
            <h3 class="font-serif text-3xl font-bold text-white">Minimal Office Edit</h3>
            <button onclick="switchViewMode('plp')" class="btn-gold mt-4 text-xs font-bold inline-flex w-40">Shop The Edit →</button>
          </div>
        </div>
      </div>
    </section>

    <!-- Task 3.7: Influencer Video Reels -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-8 bg-white border-y border-[#EBE5DF] rounded-3xl">
      <div class="text-center space-y-2">
        <span class="text-xs uppercase tracking-widest text-[#C5A059] font-bold">As Seen On Instagram</span>
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#1A1A1A]">Influencer Shoppable Reels</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        \${{REELS_DATA.map(reel => `
          <div class="relative rounded-2xl overflow-hidden shadow-lg group bg-[#1A1A1A] h-96 text-left flex flex-col justify-between p-6">
            <img src="\${{reel.image}}" class="absolute inset-0 w-full h-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" />
            <div class="relative z-10 flex justify-between items-center text-xs text-white">
              <span class="bg-black/60 backdrop-blur-md px-3 py-1 rounded-full font-bold">\${{reel.author}}</span>
              <span class="bg-[#C5A059] px-2.5 py-1 rounded-full font-bold">👁️ \${{reel.views}}</span>
            </div>

            <div class="relative z-10 space-y-3 bg-gradient-to-t from-black/90 via-black/50 to-transparent p-4 -mx-6 -mb-6 rounded-b-2xl">
              <p class="text-xs text-white font-medium">\${{reel.title}}</p>
              <div class="bg-white/90 backdrop-blur-md p-2.5 rounded-xl flex items-center justify-between text-xs">
                <span class="font-bold text-[#1A1A1A] line-clamp-1">\${{reel.productTagged}}</span>
                <button onclick="openPDP('\${{reel.productId}}')" class="bg-[#C5A059] text-white font-bold px-3 py-1 rounded-lg text-[10px]">Shop</button>
              </div>
            </div>
          </div>
        `).join('')}}
      </div>
    </section>

    <!-- Task 3.8 Customer Reviews -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-8">
      <div class="text-center space-y-2">
        <span class="text-xs uppercase tracking-widest text-[#C5A059] font-bold">50,000+ Happy Customers</span>
        <h2 class="font-serif text-3xl sm:text-4xl font-bold text-[#1A1A1A]">Real Customer Reviews</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        \${{REVIEWS_DATA.map(rev => `
          <div class="bg-white p-6 rounded-2xl border border-[#EBE5DF] space-y-4 text-left shadow-sm">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="text-2xl">\${{rev.avatar}}</span>
                <div>
                  <h4 class="font-serif text-base font-bold text-[#1A1A1A]">\${{rev.author}}</h4>
                  <span class="text-[10px] text-slate-400 block">\${{rev.location}}</span>
                </div>
              </div>
              <span class="bg-emerald-50 text-emerald-700 text-[10px] font-bold px-2 py-0.5 rounded border border-emerald-200">✓ Verified Buyer</span>
            </div>

            <div class="text-[#C5A059] text-xs font-bold">★★★★★</div>
            <h5 class="font-bold text-sm text-[#1A1A1A]">\${{rev.title}}</h5>
            <p class="text-xs text-[#6B655F] leading-relaxed">\${{rev.review}}</p>
            <span class="text-[10px] text-slate-400 block pt-2 border-t border-[#EBE5DF]">\${{rev.date}}</span>
          </div>
        `).join('')}}
      </div>
    </section>

    <!-- Task 3.9 Press Mentions -->
    <section class="py-12 bg-white border-y border-[#EBE5DF]">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
        <span class="text-xs uppercase tracking-widest text-slate-400 font-bold">As Featured In</span>
        <div class="flex flex-wrap items-center justify-center gap-8 md:gap-16 font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A]/40 tracking-wider">
          <span>VOGUE</span>
          <span>ELLE</span>
          <span>HARPER'S BAZAAR</span>
          <span>GRAZIA</span>
          <span>GQ INDIA</span>
        </div>
      </div>
    </section>
  `;
}}

// Task 4.1: Collection & Category Pages (PLP)
function renderPLPView() {{
  let plpProducts = PRODUCTS.filter(p => {{
    if (state.plpCategory !== 'All' && p.category !== state.plpCategory) return false;
    if (state.plpPriceFilter === 'under2000' && p.price >= 2000) return false;
    if (state.plpPriceFilter === '2000to3000' && (p.price < 2000 || p.price > 3000)) return false;
    if (state.plpPriceFilter === 'above3000' && p.price <= 3000) return false;
    if (state.plpMetalFilter !== 'all' && p.metal !== state.plpMetalFilter) return false;
    if (state.plpOccasionFilter !== 'all' && p.occasion !== state.plpOccasionFilter) return false;
    if (state.plpInStockOnly && !p.inStock) return false;
    return true;
  }});

  if (state.plpSortBy === 'bestselling') plpProducts.sort((a, b) => (b.isBestseller ? 1 : 0) - (a.isBestseller ? 1 : 0));
  if (state.plpSortBy === 'priceAsc') plpProducts.sort((a, b) => a.price - b.price);
  if (state.plpSortBy === 'priceDesc') plpProducts.sort((a, b) => b.price - a.price);

  return `
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 text-left">
      <div class="flex items-center gap-2 text-xs text-slate-400">
        <button onclick="switchViewMode('homepage')" class="hover:text-[#1A1A1A]">Home</button>
        <span>/</span>
        <span class="text-[#1A1A1A] font-bold">\${{state.plpCategory === 'All' ? 'Jewelry Catalog' : state.plpCategory}}</span>
      </div>

      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between border-b border-[#EBE5DF] pb-6 gap-4">
        <div>
          <span class="text-xs uppercase tracking-widest text-[#C5A059] font-bold">Category Collection</span>
          <h1 class="font-serif text-3xl sm:text-4xl font-bold text-[#1A1A1A] mt-1">
            \${{state.plpCategory === 'All' ? '18K Anti-Tarnish Jewelry' : `\${{state.plpCategory}} Collection`}} (\${{plpProducts.length}} Items)
          </h1>
        </div>

        <div class="flex items-center gap-3">
          <span class="text-xs font-semibold text-slate-500">Sort By:</span>
          <select 
            onchange="state.plpSortBy = this.value; renderApp();"
            class="bg-white border border-[#EBE5DF] text-xs font-bold text-[#1A1A1A] rounded-xl px-3 py-2 shadow-sm focus:outline-none"
          >
            <option value="featured" \${{state.plpSortBy === 'featured' ? 'selected' : ''}}>Featured</option>
            <option value="bestselling" \${{state.plpSortBy === 'bestselling' ? 'selected' : ''}}>Best Selling</option>
            <option value="priceAsc" \${{state.plpSortBy === 'priceAsc' ? 'selected' : ''}}>Price: Low to High</option>
            <option value="priceDesc" \${{state.plpSortBy === 'priceDesc' ? 'selected' : ''}}>Price: High to Low</option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        <aside class="lg:col-span-3 space-y-6 bg-white p-6 rounded-3xl border border-[#EBE5DF] shadow-sm">
          <div class="flex items-center justify-between border-b pb-3">
            <h3 class="font-serif text-lg font-bold">Filters</h3>
            <button onclick="resetPLPFilters()" class="text-xs text-[#C5A059] font-bold">Reset All</button>
          </div>

          <div class="space-y-2">
            <h4 class="text-xs font-bold uppercase text-[#1A1A1A]">Price Range</h4>
            <div class="space-y-1.5 text-xs text-[#6B655F]">
              <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="p" value="all" \${{state.plpPriceFilter === 'all' ? 'checked' : ''}} onchange="state.plpPriceFilter='all'; renderApp();" /> All Prices</label>
              <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="p" value="under2000" \${{state.plpPriceFilter === 'under2000' ? 'checked' : ''}} onchange="state.plpPriceFilter='under2000'; renderApp();" /> Under ₹2,000</label>
              <label class="flex items-center gap-2 cursor-pointer"><input type="radio" name="p" value="2000to3000" \${{state.plpPriceFilter === '2000to3000' ? 'checked' : ''}} onchange="state.plpPriceFilter='2000to3000'; renderApp();" /> ₹2,000 - ₹3,000</label>
            </div>
          </div>
        </aside>

        <!-- Task 4.1 Grid: 2-column mobile, 4-column desktop -->
        <main class="lg:col-span-9">
          <div class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
            \${{plpProducts.map(p => `
              <div class="group relative bg-white rounded-2xl border border-[#EBE5DF] card-elevation overflow-hidden shadow-sm flex flex-col justify-between">
                <div class="relative aspect-square w-full bg-[#FAF8F5]">
                  <img src="\${{p.image}}" class="w-full h-full object-cover" />
                  <div class="p-3 flex justify-between absolute top-0 left-0 right-0">
                    \${{p.isBestseller ? '<span class="bg-[#1A1A1A] text-white text-[9px] font-bold uppercase px-2 py-0.5 rounded">BESTSELLER</span>' : '<span></span>'}}
                    <button onclick="toggleWishlist('\${{p.id}}')" class="p-1.5 rounded-full bg-white/80 text-rose-500">❤️</button>
                  </div>
                </div>

                <div class="p-4 space-y-2 text-left">
                  <span class="text-[10px] text-[#C5A059] font-bold uppercase">\${{p.metal}}</span>
                  <h3 onclick="openPDP('\${{p.id}}')" class="font-serif text-sm font-bold text-[#1A1A1A] hover:text-[#C5A059] cursor-pointer line-clamp-1">\${{p.name}}</h3>
                  <div class="flex items-center justify-between pt-2 border-t border-[#EBE5DF]">
                    <span class="font-bold text-sm text-[#1A1A1A]">\${{formatPrice(p.price)}}</span>
                    <button onclick="addToCart('\${{p.id}}')" class="bg-[#C5A059] text-white text-xs font-bold px-3 py-1.5 rounded-xl">+ Add</button>
                  </div>
                </div>
              </div>
            `).join('')}}
          </div>
        </main>
      </div>
    </div>
  `;
}}

// Task 4.2: High-Converting Product Detail Page (PDP)
function renderPDPView() {{
  const p = PRODUCTS.find(prod => prod.id === state.selectedProductId) || PRODUCTS[0];
  const gallery = p.gallery || [p.image];
  const currentImage = gallery[state.activeGalleryIndex] || p.image;

  return `
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-12 text-left">
      <div class="flex items-center gap-2 text-xs text-slate-400">
        <button onclick="switchViewMode('homepage')" class="hover:text-[#1A1A1A]">Home</button>
        <span>/</span>
        <button onclick="openPLPCategory('\${{p.category}}')" class="hover:text-[#1A1A1A]">\${{p.category}}</button>
        <span>/</span>
        <span class="text-[#1A1A1A] font-bold">\${{p.name}}</span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
        <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-12 gap-4">
          <div class="sm:col-span-3 flex sm:flex-col gap-3 overflow-x-auto sm:overflow-y-auto max-h-[500px]">
            \${{gallery.map((img, idx) => `
              <img 
                src="\${{img}}" 
                onclick="state.activeGalleryIndex = \${{idx}}; renderApp();"
                class="w-20 h-20 object-cover rounded-2xl border-2 cursor-pointer \${{state.activeGalleryIndex === idx ? 'border-[#C5A059]' : 'border-[#EBE5DF]'}}"
              />
            `).join('')}}
          </div>

          <div class="sm:col-span-9 relative rounded-3xl overflow-hidden border border-[#EBE5DF] bg-[#FAF8F5] group">
            <img src="\${{currentImage}}" class="w-full h-[480px] object-cover transition-transform duration-500 group-hover:scale-125" />
            <div class="absolute bottom-4 left-4 bg-white/90 backdrop-blur-md px-3 py-1.5 rounded-full text-[11px] font-bold text-[#1A1A1A]">
              🔍 Hover to Zoom | 360° Preview Active
            </div>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-6 flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex flex-wrap gap-2">
              <span class="bg-[#1A1A1A] text-white text-[10px] font-bold px-2.5 py-1 rounded-full uppercase">✨ 100% Anti-Tarnish</span>
              <span class="bg-[#C5A059] text-white text-[10px] font-bold px-2.5 py-1 rounded-full uppercase">🔥 Bestseller</span>
              <span class="bg-cyan-600 text-white text-[10px] font-bold px-2.5 py-1 rounded-full uppercase">💦 Waterproof</span>
            </div>

            <h1 class="font-serif text-3xl font-bold text-[#1A1A1A]">\${{p.name}}</h1>

            <div class="flex items-baseline gap-3">
              <span class="text-3xl font-bold text-[#1A1A1A]">\${{formatPrice(p.price)}}</span>
              <span class="text-sm text-slate-400 line-through">\${{formatPrice(p.originalPrice)}}</span>
              <span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded">\${{p.discountPercent}}% OFF</span>
            </div>

            <div class="bg-[#FAF8F5] p-3.5 rounded-2xl border border-[#EBE5DF] text-xs flex items-center justify-between">
              <div>
                <span class="font-bold text-[#1A1A1A]">3 Interest-Free EMIs of \${{formatPrice(Math.round(p.price / 3))}}/mo</span>
                <span class="block text-[10px] text-slate-500">Powered by Snapmint / ShopFlo</span>
              </div>
              <span class="bg-[#C5A059]/20 text-[#C5A059] font-bold px-2 py-1 rounded text-[10px]">No Cost EMI</span>
            </div>

            \${{p.category === 'Rings' ? `
              <div class="space-y-2">
                <div class="flex justify-between items-center text-xs">
                  <span class="font-bold text-[#1A1A1A]">Select Ring Size:</span>
                  <button onclick="openSizeGuideModal()" class="text-[#C5A059] font-bold underline">📏 Ring Size Guide</button>
                </div>
                <div class="flex gap-2">
                  \${{['US 6', 'US 7', 'US 8', 'US 9'].map(size => `
                    <button 
                      onclick="state.selectedRingSize = '\${{size}}'; renderApp();"
                      class="px-4 py-2 rounded-xl text-xs font-bold border \${{state.selectedRingSize === size ? 'bg-[#C5A059] text-white border-[#C5A059]' : 'bg-white border-[#EBE5DF] text-[#1A1A1A]'}}"
                    >
                      \${{size}}
                    </button>
                  `).join('')}}
                </div>
              </div>
            ` : ''}}

            <div class="space-y-2 border-t pt-4">
              <label class="block text-xs font-bold text-[#1A1A1A]">Check Delivery & COD Eligibility:</label>
              <form onsubmit="handlePincodeSubmit(event)" class="flex gap-2">
                <input 
                  type="text" 
                  placeholder="Enter 6-digit Pincode" 
                  value="\${{state.pincode}}"
                  oninput="state.pincode = this.value"
                  maxlength="6"
                  class="flex-1 bg-[#FAF8F5] border border-[#EBE5DF] rounded-xl px-3 py-2 text-xs focus:outline-none"
                />
                <button type="submit" class="bg-[#1A1A1A] text-white text-xs font-bold px-4 py-2 rounded-xl">Check</button>
              </form>
              \${{state.pincodeResult ? `
                <div class="p-2.5 bg-emerald-50 text-emerald-800 rounded-xl text-xs font-semibold border border-emerald-200">
                  🚚 \${{state.pincodeResult.estDays}} via \${{state.pincodeResult.shiprocketCourier}} | COD Available
                </div>
              ` : ''}}
            </div>

            <div class="flex gap-3 pt-4">
              <button onclick="addToCart('\${{p.id}}')" class="flex-1 bg-[#FAF8F5] border-2 border-[#C5A059] text-[#1A1A1A] font-bold py-3.5 rounded-2xl text-xs flex items-center justify-center gap-2">
                🛍️ Add to Bag
              </button>
              <button onclick="addToCart('\${{p.id}}'); openCheckoutModal();" class="flex-1 btn-gold py-3.5 rounded-2xl text-xs font-bold justify-center">
                ⚡ Buy Now
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Task 4.2 Accordions -->
      <div class="bg-white rounded-3xl border border-[#EBE5DF] p-6 sm:p-8 space-y-4 shadow-sm">
        <h3 class="font-serif text-2xl font-bold text-[#1A1A1A]">Product Specifications & Guarantee</h3>

        <div class="border-b pb-3">
          <button onclick="toggleAccordion('details')" class="w-full flex justify-between items-center text-sm font-bold text-[#1A1A1A] py-2">
            <span>📐 Product Details & Dimensions</span>
            <span>\${{state.openAccordion === 'details' ? '▲' : '▼'}}</span>
          </button>
          \${{state.openAccordion === 'details' ? `<p class="text-xs text-[#6B655F] pt-2 leading-relaxed">\${{p.dimensions}}</p>` : ''}}
        </div>

        <div class="border-b pb-3">
          <button onclick="toggleAccordion('care')" class="w-full flex justify-between items-center text-sm font-bold text-[#1A1A1A] py-2">
            <span>✨ Anti-Tarnish & Care Instructions</span>
            <span>\${{state.openAccordion === 'care' ? '▲' : '▼'}}</span>
          </button>
          \${{state.openAccordion === 'care' ? `<p class="text-xs text-[#6B655F] pt-2 leading-relaxed">\${{p.care}}</p>` : ''}}
        </div>

        <div class="border-b pb-3">
          <button onclick="toggleAccordion('materials')" class="w-full flex justify-between items-center text-sm font-bold text-[#1A1A1A] py-2">
            <span>👑 Premium Materials</span>
            <span>\${{state.openAccordion === 'materials' ? '▲' : '▼'}}</span>
          </button>
          \${{state.openAccordion === 'materials' ? `<p class="text-xs text-[#6B655F] pt-2 leading-relaxed">\${{p.materials}}</p>` : ''}}
        </div>
      </div>
    </div>
  `;
}}

// Modals Renderer
function renderModals() {{
  let html = '';

  if (state.isSizeGuideOpen) {{
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="relative w-full max-w-lg bg-white border border-[#EBE5DF] rounded-3xl p-6 shadow-2xl text-left space-y-4">
          <button onclick="state.isSizeGuideOpen = false; renderApp();" class="absolute top-4 right-4 text-slate-400 font-bold">✕</button>
          <h3 class="font-serif text-2xl font-bold text-[#1A1A1A]">📏 Ring Size Guide</h3>
          <div class="bg-[#FAF8F5] p-4 rounded-2xl border border-[#EBE5DF] text-xs space-y-2">
            <div class="grid grid-cols-3 font-bold border-b pb-2"><span>US Size</span><span>Inner Diameter</span><span>Circumference</span></div>
            <div class="grid grid-cols-3"><span>US 6</span><span>16.5 mm</span><span>51.8 mm</span></div>
            <div class="grid grid-cols-3"><span>US 7</span><span>17.3 mm</span><span>54.4 mm</span></div>
            <div class="grid grid-cols-3"><span>US 8</span><span>18.1 mm</span><span>56.9 mm</span></div>
            <div class="grid grid-cols-3"><span>US 9</span><span>18.9 mm</span><span>59.5 mm</span></div>
          </div>
          <button onclick="state.isSizeGuideOpen = false; renderApp();" class="btn-gold w-full justify-center py-2.5 text-xs">Got It</button>
        </div>
      </div>
    `;
  }}

  if (state.isCartOpen) {{
    html += `
      <div class="fixed inset-0 z-50 overflow-hidden bg-black/50 backdrop-blur-sm">
        <div class="absolute inset-y-0 right-0 max-w-full flex pl-10">
          <div class="w-screen max-w-md bg-white border-l border-[#EBE5DF] p-6 flex flex-col justify-between text-left">
            <div class="flex justify-between border-b pb-4">
              <h2 class="font-serif text-xl font-bold">Your Jewelry Bag</h2>
              <button onclick="toggleCart(false)">✕</button>
            </div>
            <div class="flex-1 overflow-y-auto py-4 space-y-3">
              \${{state.cart.map(item => `
                <div class="flex gap-3 p-3 bg-[#FAF8F5] rounded-2xl border">
                  <img src="\${{item.image}}" class="w-14 h-14 object-cover rounded-xl" />
                  <div class="flex-1">
                    <h4 class="font-serif text-sm font-bold">\${{item.name}}</h4>
                    <span class="font-bold text-xs">\${{formatPrice(item.price * item.quantity)}}</span>
                  </div>
                </div>
              `).join('')}}
            </div>
            <button onclick="toggleCart(false); openCheckoutModal();" class="btn-gold w-full justify-center py-3 font-bold">Proceed to Checkout</button>
          </div>
        </div>
      </div>
    `;
  }}

  if (state.isCheckoutOpen) {{
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="relative w-full max-w-md bg-white border border-[#EBE5DF] rounded-3xl p-6 shadow-2xl text-left space-y-4">
          <div class="flex justify-between border-b pb-3"><h2 class="font-serif text-xl font-bold">Razorpay & COD Checkout</h2><button onclick="closeCheckoutModal()">✕</button></div>
          <button onclick="confirmOrder()" class="btn-gold w-full justify-center py-3 font-bold">Confirm & Pay Order</button>
        </div>
      </div>
    `;
  }}

  if (state.isTrackerOpen) {{
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="relative w-full max-w-md bg-white border border-[#EBE5DF] rounded-3xl p-6 shadow-2xl text-left space-y-4">
          <div class="flex justify-between border-b pb-3"><h3 class="font-serif text-lg font-bold">Shiprocket Tracking</h3><button onclick="closeTrackerModal()">✕</button></div>
          <p class="text-xs text-emerald-700 font-semibold">✓ Order CL-84920 In-Transit via Delhivery Air</p>
        </div>
      </div>
    `;
  }}

  if (state.isAccountOpen) {{
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="relative w-full max-w-md bg-white border border-[#EBE5DF] rounded-3xl p-6 shadow-2xl text-left space-y-4">
          <button onclick="closeAccountModal()" class="absolute top-4 right-4">✕</button>
          <h3 class="font-serif text-2xl font-bold text-center">Cieloria VIP Login</h3>
          <input type="text" placeholder="+91 Mobile Number" class="w-full bg-[#FAF8F5] border rounded-xl p-3 text-xs" />
          <button onclick="closeAccountModal()" class="btn-gold w-full justify-center py-3 font-bold text-xs">Send OTP</button>
        </div>
      </div>
    `;
  }}

  if (state.activePolicy) {{
    html += `
      <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
        <div class="relative w-full max-w-md bg-white border border-[#EBE5DF] rounded-3xl p-6 shadow-2xl text-left space-y-4">
          <button onclick="closePolicyModal()" class="absolute top-4 right-4">✕</button>
          <h3 class="font-serif text-2xl font-bold">\${{state.activePolicy.toUpperCase()}} Policy</h3>
          <p class="text-xs text-[#6B655F]">Cieloria guarantees 100% authentic anti-tarnish 18K gold jewelry with 7-day returns & lifetime replacement cards.</p>
          <button onclick="closePolicyModal()" class="btn-gold w-full justify-center py-2">Close</button>
        </div>
      </div>
    `;
  }}

  return html;
}}

// Global Actions
window.switchViewMode = function(mode) {{
  state.viewMode = mode;
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
  renderApp();
}};

window.openPDP = function(id) {{
  state.selectedProductId = id;
  state.viewMode = 'pdp';
  state.activeGalleryIndex = 0;
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
  renderApp();
}};

window.openPLPCategory = function(cat) {{
  state.plpCategory = cat;
  state.viewMode = 'plp';
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
  renderApp();
}};

window.resetPLPFilters = function() {{
  state.plpPriceFilter = 'all';
  state.plpMetalFilter = 'all';
  state.plpOccasionFilter = 'all';
  state.plpInStockOnly = false;
  state.plpSortBy = 'featured';
  renderApp();
}};

window.toggleAccordion = function(acc) {{
  state.openAccordion = state.openAccordion === acc ? '' : acc;
  renderApp();
}};

window.openSizeGuideModal = function() {{
  state.isSizeGuideOpen = true;
  renderApp();
}};

window.scrollToSection = function(id) {{
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({{ behavior: 'smooth' }});
}};

window.changeCurrency = function(curr) {{
  state.activeCurrency = curr;
  renderApp();
}};

window.changeTicker = function(dir) {{
  state.tickerIndex = (state.tickerIndex + dir + ANNOUNCEMENTS.length) % ANNOUNCEMENTS.length;
  renderApp();
}};

window.handleSearchInput = function(val) {{
  state.searchQuery = val;
  renderApp();
}};

window.addToCart = function(id) {{
  const p = PRODUCTS.find(prod => prod.id === id);
  if (!p) return;
  const existing = state.cart.find(item => item.id === id);
  if (existing) {{
    existing.quantity += 1;
  }} else {{
    state.cart.push({{ ...p, quantity: 1 }});
  }}
  state.isCartOpen = true;
  renderApp();
}};

window.toggleCart = function(open) {{
  state.isCartOpen = open;
  renderApp();
}};

window.openCheckoutModal = function() {{
  state.isCheckoutOpen = true;
  renderApp();
}};

window.closeCheckoutModal = function() {{
  state.isCheckoutOpen = false;
  renderApp();
}};

window.confirmOrder = function() {{
  alert('Order Confirmed! ID: CL-84920');
  state.cart = [];
  state.isCheckoutOpen = false;
  renderApp();
}};

window.openTrackerModal = function() {{
  state.isTrackerOpen = true;
  renderApp();
}};

window.closeTrackerModal = function() {{
  state.isTrackerOpen = false;
  renderApp();
}};

window.openAccountModal = function() {{
  state.isAccountOpen = true;
  renderApp();
}};

window.closeAccountModal = function() {{
  state.isAccountOpen = false;
  renderApp();
}};

window.openGuaranteeModal = function() {{
  state.activePolicy = 'warranty';
  renderApp();
}};

window.openPolicyModal = function(pol) {{
  state.activePolicy = pol;
  renderApp();
}};

window.closePolicyModal = function() {{
  state.activePolicy = null;
  renderApp();
}};

window.handlePincodeSubmit = function(e) {{
  e.preventDefault();
  const res = PINCODES[state.pincode.trim()];
  if (res) {{
    state.pincodeResult = res;
  }} else {{
    state.pincodeResult = {{ location: 'Pan India Delivery', estDays: 'Tuesday, Sep 2 (Express Air)', shiprocketCourier: 'Shiprocket Air' }};
  }}
  renderApp();
}};

window.handleNewsletter = function(e) {{
  e.preventDefault();
  state.isSubscribed = true;
  if (window.confetti) window.confetti({{ particleCount: 60 }});
  renderApp();
}};

document.addEventListener('DOMContentLoaded', () => {{
  renderApp();
}});
renderApp();
"""

with open("/Users/khushi/.gemini/antigravity/scratch/cieloria/app.js", "w") as out_js:
    out_js.write(app_js_content)

print("Successfully wrote full app.js with ALL 78 products!")
