import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace BLOG_POSTS with exact screenshot data
new_blog_posts_code = """const BLOG_POSTS = [
  {
    id: "blog-1",
    day: "03",
    month: "MAR",
    title: "Lab-Grown Diamonds: Styling & Care for the Modern Indian Woman",
    image: "/cieloria_hero_rings.jpg",
    excerpt: "If jewellery had a reality check, lab-grown diamonds would be it. Real, pretty, conflict-free, and crafted for everyday elegance.",
    fullContent: `
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Lab-grown diamonds are identical to mined diamonds in optical, chemical, and physical properties. At Cieloria, our demifine solitaire collection features precision-cut lab-grown CZ and diamonds set in 18K gold plating.</p>
      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">Styling Lab-Grown Diamonds</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Stack open-bezel solitaire rings with twisted gold bands for a modern minimalist look that transitions effortlessly from day to night.</p>
    `
  },
  {
    id: "blog-2",
    day: "02",
    month: "MAR",
    title: "The Women's Day Jewellery Guide Nobody Asked For, But Everybody Needed",
    image: "/cieloria_hero_necklaces.jpg",
    excerpt: "Beyoncé told us who runs the world. Legally Blonde proved that a woman can wear gold and dominate the boardroom.",
    fullContent: `
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Celebrate strength, grace, and independence with statement demifine jewelry that empowers every woman to shine on her own terms.</p>
      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">Curated Gift Guide</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Discover waterproof gold pendants, heart-shaped solitaires, and stackable bangles crafted for daily wear.</p>
    `
  },
  {
    id: "blog-3",
    day: "01",
    month: "MAR",
    title: "Gold vs Silver Jewellery: How to Choose What Suits You Best",
    image: "/cieloria_hero_bracelets.jpg",
    excerpt: "The great debate is always on – gold or silver? That's like asking, chai or coffee? Here is how to find your true metallic signature.",
    fullContent: `
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Choosing between gold and silver comes down to skin undertones, personal wardrobe aesthetics, and occasion styling.</p>
      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">Warm Gold vs Cool Silver</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Warm skin undertones shimmer beautifully in 18K champagne gold, while cool undertones glow in 925 fine silver. At Cieloria, we offer both demifine finishes.</p>
    `
  }
];"""

# Replace BLOG_POSTS array block
js = re.sub(r'const BLOG_POSTS = \[.*?\];', new_blog_posts_code, js, flags=re.DOTALL)

# Replace Blog Section HTML with exact screenshot UI
new_blog_section_html = """    <!-- 8.5. BLOGS SECTION (EXACT REFERENCE MATCH) -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-8">
      <div class="text-center">
        <h2 class="font-serif text-xl sm:text-3xl font-bold tracking-widest text-[#1A1A1A] uppercase">BLOGS</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
        ${BLOG_POSTS.map(post => `
          <article onclick="openBlogModal('${post.id}')" class="space-y-4 cursor-pointer group text-left">
            <div class="relative aspect-square sm:aspect-[4/3] rounded-2xl overflow-hidden bg-slate-100 shadow-sm">
              <img src="${post.image}" onerror="this.onerror=null; this.src='/hero_banner.jpg';" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700 ease-out" />
              <!-- Floating Circular Date Badge -->
              <div class="absolute top-4 right-4 w-12 h-12 rounded-full bg-white flex flex-col items-center justify-center shadow-md text-[#1A1A1A] border border-slate-100">
                <span class="text-sm font-bold leading-none">${post.day}</span>
                <span class="text-[9px] font-semibold tracking-wider text-slate-500 uppercase leading-none mt-0.5">${post.month}</span>
              </div>
            </div>
            <div class="space-y-2">
              <h3 class="font-sans text-base sm:text-lg font-bold text-[#1A1A1A] group-hover:text-[#C5A059] transition-colors leading-snug line-clamp-2">${post.title}</h3>
              <p class="text-xs text-slate-500 leading-relaxed line-clamp-2">${post.excerpt}</p>
            </div>
          </article>
        `).join('')}
      </div>
    </section>"""

js = re.sub(r'<!-- 8\.5\. CIELORIA LUXURY JOURNAL.*?<\/section>', new_blog_section_html, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully applied exact BLOGS design with circular date badges & matching content!')
