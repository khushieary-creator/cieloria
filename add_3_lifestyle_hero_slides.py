import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update HERO_SLIDES definition with 3 luxury lifestyle slides
new_hero_slides = """const HERO_SLIDES = [
  {
    id: "slide-1",
    image: "/hero_banner.jpg",
    tag: "✦ EXCLUSIVE FESTIVE OFFER ✦",
    title: "LUXURY DEMI-FINE COLLECTION",
    subtitle: "FLAT 40% OFF ON ALL ORDERS",
    codeText: "USE CODE: CIELORIA40",
    giftOffer: "🎁 FREE 18K GOLD STUDS (WORTH ₹1,495) ON ORDERS ABOVE ₹2,999",
    priceText: "100% Waterproof • Anti-Tarnish • 18K Gold Plated",
    buttonText: "EXPLORE OFFERS ➔"
  },
  {
    id: "slide-2",
    image: "/hero_slide2.jpg",
    tag: "✦ SPECIAL RAKHI & GIFTING OFFER ✦",
    title: "SIBLING LOVE KEEPSAKE GIFTS",
    subtitle: "BUY 1 GET 1 FREE + EXTRA 30% OFF",
    codeText: "USE CODE: RAKHI50",
    giftOffer: "🎀 FREE SIGNATURE LUXURY VELVET GIFT BOX INCLUDED",
    priceText: "Skin Safe • 1 Year Anti-Tarnish Warranty",
    buttonText: "SHOP RAKHI GIFTS ➔"
  },
  {
    id: "slide-3",
    image: "/hero_slide3.jpg",
    tag: "✦ DAILY LUXURY ESSENTIALS ✦",
    title: "EVERYDAY 18K GOLD ELEGANCE",
    subtitle: "PIECES STARTING FROM JUST ₹899",
    codeText: "USE CODE: LUXE2026",
    giftOffer: "🚚 FREE EXPRESS BLUEDART DELIVERY ALL OVER INDIA",
    priceText: "PVD 18Kt Gold Plating • Hypoallergenic",
    buttonText: "SHOP BESTSELLERS ➔"
  }
];"""

js = re.sub(r'const HERO_SLIDES = \[.*?\];', new_hero_slides, js, flags=re.DOTALL)

# 2. Update renderHomepageView hero banner section with navigation arrows and indicator dots
old_hero_section = """    <!-- 1. Hero Lifestyle Offer Banner (Single Clean Non-Product Banner) -->
    <section class="relative overflow-hidden w-full bg-[#EAE5D9] min-h-[440px] sm:min-h-[560px] lg:min-h-[640px] flex items-center">
      <div class="absolute inset-0 z-0">
        <img src="${currentHero.image}" onerror="this.onerror=null; this.src='/hero_banner.jpg';" class="w-full h-full object-cover object-center transition-transform duration-1000 scale-105" />
        <div class="absolute inset-0 bg-gradient-to-r from-black/75 via-black/40 to-transparent"></div>
      </div>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full text-left py-12 sm:py-16">
        <div class="max-w-xl space-y-3 sm:space-y-4 text-white">
          ${currentHero.tag ? `<span class="inline-block bg-[#C5A059] text-black text-[10px] sm:text-xs uppercase font-bold tracking-[0.25em] px-3 py-1 rounded-full shadow-sm">${currentHero.tag}</span>` : ''}
          <h1 class="font-serif text-3xl sm:text-5xl lg:text-6xl font-bold leading-tight drop-shadow-md">${currentHero.title}</h1>
          ${currentHero.subtitle ? `<p class="text-xl sm:text-3xl font-light text-amber-200 tracking-wide">${currentHero.subtitle}</p>` : ''}
          
          <div class="flex flex-wrap items-center gap-2 pt-1">
            ${currentHero.codeText ? `<div class="bg-white/20 backdrop-blur-md border border-amber-300/60 px-3.5 py-1.5 rounded-lg text-xs sm:text-sm font-bold uppercase tracking-wider text-amber-300 shadow-sm">${currentHero.codeText}</div>` : ''}
          </div>

          ${currentHero.giftOffer ? `<div class="bg-black/60 backdrop-blur-md border border-white/20 p-3.5 rounded-xl text-xs sm:text-sm text-white font-medium shadow-md leading-relaxed">${currentHero.giftOffer}</div>` : ''}
          
          ${currentHero.priceText ? `<div class="text-xs sm:text-sm font-medium text-slate-300 pt-1 tracking-wider uppercase">${currentHero.priceText}</div>` : ''}

          <div class="pt-4 sm:pt-6">
            <button onclick="openPLPCategory('BestSeller')" class="btn-palmonas-hero text-xs sm:text-sm py-3.5 px-8 shadow-lg hover:scale-105 transition-all">${currentHero.buttonText}</button>
          </div>
        </div>
      </div>
    </section>"""

new_hero_section = """    <!-- 1. Hero 3-Slide Lifestyle Offer Carousel (0 Product Closeups) -->
    <section class="relative overflow-hidden w-full bg-[#EAE5D9] min-h-[440px] sm:min-h-[560px] lg:min-h-[640px] flex items-center">
      <div class="absolute inset-0 z-0">
        <img src="${currentHero.image}" onerror="this.onerror=null; this.src='/hero_banner.jpg';" class="w-full h-full object-cover object-center transition-transform duration-1000 scale-105" />
        <div class="absolute inset-0 bg-gradient-to-r from-black/80 via-black/40 to-transparent"></div>
      </div>

      <button onclick="changeHeroSlide(-1)" class="absolute left-2 sm:left-5 top-1/2 -translate-y-1/2 z-20 w-9 h-9 sm:w-12 sm:h-12 rounded-full bg-black/40 backdrop-blur-md border border-white/20 text-white flex items-center justify-center hover:bg-black/80 transition-all text-sm sm:text-lg shadow-lg" title="Previous Offer Slide">❮</button>
      <button onclick="changeHeroSlide(1)" class="absolute right-2 sm:right-5 top-1/2 -translate-y-1/2 z-20 w-9 h-9 sm:w-12 sm:h-12 rounded-full bg-black/40 backdrop-blur-md border border-white/20 text-white flex items-center justify-center hover:bg-black/80 transition-all text-sm sm:text-lg shadow-lg" title="Next Offer Slide">❯</button>

      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 w-full text-left py-12 sm:py-16">
        <div class="max-w-xl space-y-3 sm:space-y-4 text-white">
          ${currentHero.tag ? `<span class="inline-block bg-[#C5A059] text-black text-[10px] sm:text-xs uppercase font-bold tracking-[0.25em] px-3 py-1 rounded-full shadow-sm">${currentHero.tag}</span>` : ''}
          <h1 class="font-serif text-3xl sm:text-5xl lg:text-6xl font-bold leading-tight drop-shadow-md">${currentHero.title}</h1>
          ${currentHero.subtitle ? `<p class="text-xl sm:text-3xl font-light text-amber-200 tracking-wide">${currentHero.subtitle}</p>` : ''}
          
          <div class="flex flex-wrap items-center gap-2 pt-1">
            ${currentHero.codeText ? `<div class="bg-white/20 backdrop-blur-md border border-amber-300/60 px-3.5 py-1.5 rounded-lg text-xs sm:text-sm font-bold uppercase tracking-wider text-amber-300 shadow-sm">${currentHero.codeText}</div>` : ''}
          </div>

          ${currentHero.giftOffer ? `<div class="bg-black/60 backdrop-blur-md border border-white/20 p-3.5 rounded-xl text-xs sm:text-sm text-white font-medium shadow-md leading-relaxed">${currentHero.giftOffer}</div>` : ''}
          
          ${currentHero.priceText ? `<div class="text-xs sm:text-sm font-medium text-slate-300 pt-1 tracking-wider uppercase">${currentHero.priceText}</div>` : ''}

          <div class="pt-4 sm:pt-6">
            <button onclick="openPLPCategory('BestSeller')" class="btn-palmonas-hero text-xs sm:text-sm py-3.5 px-8 shadow-lg hover:scale-105 transition-all">${currentHero.buttonText}</button>
          </div>
        </div>
      </div>

      <!-- Slide Indicator Dots -->
      <div class="absolute bottom-4 left-1/2 -translate-x-1/2 z-20 flex items-center gap-2.5">
        ${HERO_SLIDES.map((slide, idx) => `
          <button onclick="state.heroSlideIndex = ${idx}; renderApp();" class="w-2.5 h-2.5 rounded-full transition-all ${state.heroSlideIndex === idx ? 'bg-amber-300 w-8' : 'bg-white/50 hover:bg-white'}" title="Go to slide ${idx + 1}"></button>
        `).join('')}
      </div>
    </section>"""

js = js.replace(old_hero_section, new_hero_section)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully added 3 luxury lifestyle sliding offer pages to cieloria_app.js!')
