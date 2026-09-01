import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update Gifting Banners Section to use Product Images (PRODUCTS[40].image for Her, PRODUCTS[2].image for Him)
old_dual_section = r'<!-- 3\. Dual Luxury Gifting Banners -->.*?<!-- 4\. EVERYDAY DEMIFINE® COLLECTION Circle Grid -->'

new_dual_section = """<!-- 3. Dual Luxury Gifting Banners (Product Images) -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-8">
      <div class="text-center"><h2 class="font-serif text-2xl sm:text-3xl font-bold text-[#4A0E17]">CURATED LUXURY GIFTS FOR</h2></div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
        <div class="relative rounded-3xl overflow-hidden shadow-md group h-[320px] sm:h-[380px] bg-[#EAE5D9]">
          <img src="${PRODUCTS[40].image}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
          <div class="absolute inset-0 p-6 sm:p-8 flex flex-col justify-center items-end text-right bg-gradient-to-l from-black/75 via-black/30 to-transparent">
            <div class="space-y-2 text-white max-w-xs">
              <span class="text-[10px] uppercase font-bold tracking-[0.2em] text-amber-300 block">FOR HER</span>
              <h3 class="font-serif text-2xl sm:text-3xl font-bold">Luxe Keepsakes For Her</h3>
              <p class="text-xs text-slate-200">Curated Anti-Tarnish Jewelry & Gift Box</p>
              <div class="pt-4"><button onclick="openPLPCategory('Gifting')" class="border border-white text-white px-5 py-2.5 text-xs uppercase font-bold tracking-wider hover:bg-white hover:text-black transition-colors rounded-lg">SHOP GIFTS FOR HER</button></div>
            </div>
          </div>
        </div>
        <div class="relative rounded-3xl overflow-hidden shadow-md group h-[320px] sm:h-[380px] bg-[#EAE5D9]">
          <img src="${PRODUCTS[2].image}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" />
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

js = re.sub(old_dual_section, new_dual_section, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated Gifting cards to use PRODUCT IMAGES!')
