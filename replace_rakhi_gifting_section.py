import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Replace Rakhi code text in slide 2
js = js.replace('tag: "✦ SPECIAL RAKHI & GIFTING OFFER ✦"', 'tag: "✦ SPECIAL LUXURY GIFTING OFFER ✦"')
js = js.replace('title: "SIBLING LOVE KEEPSAKE GIFTS"', 'title: "CURATED LUXURY GIFT SETS"')
js = js.replace('buttonText: "SHOP RAKHI GIFTS ➔"', 'buttonText: "SHOP LUXURY GIFTS ➔"')

# 2. Replace section 2 & section 3 Rakhi banners
old_gifting_pattern = r'<!-- 2\. Special Gifting Banner -->.*?<!-- 4\. EVERYDAY DEMIFINE® COLLECTION Circle Grid -->'

new_gifting_html = """<!-- 2. Special Luxury Gifting Banner -->
    <section class="py-12 sm:py-16 bg-white text-center space-y-4 border-b border-[#E6E1D7]">
      <div class="max-w-3xl mx-auto px-4 space-y-3">
        <h2 class="font-serif text-2xl sm:text-4xl lg:text-5xl font-bold text-[#4A0E17] italic">
          Moments this timeless <br class="sm:hidden" />deserve everlasting 18K gold
        </h2>
        <p class="text-slate-600 text-xs sm:text-base font-light">Thoughtful luxury keepsakes, anti-tarnish jewelry, and signature velvet gift sets for loved ones.</p>
        <div class="pt-3">
          <button onclick="openPLPCategory('Gifting')" class="bg-[#4A0E17] text-white text-xs font-semibold px-6 py-3 rounded-md uppercase tracking-wider hover:bg-[#330A10]">EXPLORE LUXURY GIFTING →</button>
        </div>
      </div>
    </section>

    <!-- 3. Dual Luxury Gifting Banners -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-8">
      <div class="text-center"><h2 class="font-serif text-2xl sm:text-3xl font-bold text-[#4A0E17]">CURATED LUXURY GIFTS FOR</h2></div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
        <div class="relative rounded-3xl overflow-hidden shadow-md group h-[320px] sm:h-[380px] bg-[#EAE5D9]">
          <img src="/gifting_her.jpg" onerror="this.onerror=null; this.src='/hero_banner.jpg';" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 p-6 sm:p-8 flex flex-col justify-center items-end text-right bg-gradient-to-l from-black/75 via-black/30 to-transparent">
            <div class="space-y-2 text-white max-w-xs">
              <span class="text-[10px] uppercase font-bold tracking-[0.2em] text-amber-300 block">FOR HER</span>
              <h3 class="font-serif text-2xl sm:text-3xl font-bold">Luxe Keepsakes For Her</h3>
              <p class="text-xs text-slate-200">Curated Anti-Tarnish Jewelry & Velvet Box</p>
              <div class="pt-4"><button onclick="openPLPCategory('Gifting')" class="border border-white text-white px-5 py-2.5 text-xs uppercase font-bold tracking-wider hover:bg-white hover:text-black transition-colors rounded-lg">SHOP GIFTS FOR HER</button></div>
            </div>
          </div>
        </div>
        <div class="relative rounded-3xl overflow-hidden shadow-md group h-[320px] sm:h-[380px] bg-[#EAE5D9]">
          <img src="/gifting_him.jpg" onerror="this.onerror=null; this.src='/hero_slide3.jpg';" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 p-6 sm:p-8 flex flex-col justify-center items-end text-right bg-gradient-to-l from-black/75 via-black/30 to-transparent">
            <div class="space-y-2 text-white max-w-xs">
              <span class="text-[10px] uppercase font-bold tracking-[0.2em] text-amber-300 block">FOR HIM</span>
              <h3 class="font-serif text-2xl sm:text-3xl font-bold">Modern Elegance For Him</h3>
              <p class="text-xs text-slate-200">Men's 18K Gold Plated Kadas & Bracelets</p>
              <div class="pt-4"><button onclick="openPLPCategory('Gifting')" class="border border-white text-white px-5 py-2.5 text-xs uppercase font-bold tracking-wider hover:bg-white hover:text-black transition-colors rounded-lg">SHOP GIFTS FOR HIM</button></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. EVERYDAY DEMIFINE® COLLECTION Circle Grid -->"""

js = re.sub(old_gifting_pattern, new_gifting_html, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully replaced Rakhi section with Curated Luxury Gifting For Her & Him!')
