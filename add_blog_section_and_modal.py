import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add BLOG_POSTS array right after FOR_EVERY_YOU_CARDS
blog_data_code = """
const BLOG_POSTS = [
  {
    id: "blog-1",
    tag: "STYLE GUIDE",
    title: "How to Layer 18K Gold Necklaces Like a Fashion Stylist",
    date: "Sep 10, 2026",
    readTime: "4 min read",
    image: "/hero_necklaces.jpg",
    excerpt: "Master the art of stacking delicate gold chains, solitaire pendants, and demifine chokers for an effortless everyday luxury look.",
    fullContent: `
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Layering gold necklaces is the single easiest way to elevate any outfit from casual to high-fashion glamour. Whether you're wearing a silk blouse or an effortless linen tee, stacked 18K gold chains add instant texture and luxury.</p>
      
      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">Rule 1: Mix Different Chain Lengths</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Start with a 14-inch choker as your base. Add a 16-inch pendant necklace like our <em>18K Gold Demifine Solitaire Pendant</em>, and complete the stack with an 18-inch to 20-inch chain.</p>

      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">Rule 2: Balance Weights & Textures</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Pair a sleek herringbone snake chain with a dainty stone pendant or paperclip link chain to create eye-catching visual contrast without tangling.</p>

      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">Rule 3: Keep Materials Waterproof</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">All CIELORIA necklaces feature PVD 18K thick gold plating over surgical stainless steel. You can wear your layered stack to the beach, gym, or pool with zero risk of color fading or skin greening.</p>
    `
  },
  {
    id: "blog-2",
    tag: "CARE & MAINTENANCE",
    title: "The Truth About Anti-Tarnish & Waterproof Gold Jewelry",
    date: "Sep 08, 2026",
    readTime: "3 min read",
    image: "/hero_bracelets.jpg",
    excerpt: "Discover how CIELORIA's PVD 18K thick gold plating technology keeps your favorite bangles & rings shining through ocean water & daily showers.",
    fullContent: `
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Many people wonder how demifine jewelry can stay golden and tarnish-free even when exposed to water, sweat, and perfumes. The secret lies in physical vapor deposition (PVD) gold vacuum plating.</p>

      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">What is PVD Gold Plating?</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Unlike traditional electroplating that rubs off in weeks, PVD bonds real 18K gold atom-by-atom to surgical grade 316L stainless steel in a vacuum chamber. This creates a diamond-hard barrier against moisture, sweat, and tarnishing.</p>

      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">Daily Care Tips for Lifetime Sparkle</h4>
      <ul class="list-disc pl-5 text-sm text-slate-700 space-y-1 font-sans">
        <li>Shower, swim, and workout without taking your pieces off.</li>
        <li>Rinse with clean water after sea swimming to remove salt particles.</li>
        <li>Wipe dry with a soft microfiber cloth to preserve high polish mirror shine.</li>
      </ul>
    `
  },
  {
    id: "blog-3",
    tag: "TREND REPORT",
    title: "Demifine Jewelry Trends 2026: Minimalist Solitaires to Statement Kadas",
    date: "Sep 05, 2026",
    readTime: "5 min read",
    image: "/hero_rings.jpg",
    excerpt: "Explore this season's most coveted demifine pieces — from fair-skinned twist hoop earrings to timeless solitaire diamond rings.",
    fullContent: `
      <p class="text-sm text-slate-700 leading-relaxed font-sans">2026 jewelry trends are all about effortless everyday luxury — jewelry that looks solid 18K gold but remains lightweight, comfortable, and skin-safe for all-day wear.</p>

      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">1. Classic Golden Helix Twist Hoops</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Twisted gold hoops are dominating high fashion runways. Their sculptural silhouette catches light from every angle, framing the ear with modern elegance.</p>

      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">2. Modern Engraved Gold Kadas for Him & Her</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Unisex kada bracelets and structured bangles are trending as powerful statement pieces. Stacked with a watch or worn solo, they deliver bold luxury sophistication.</p>

      <h4 class="font-serif text-lg font-bold text-[#1A1A1A] pt-3">3. Minimalist Diamond Solitaires</h4>
      <p class="text-sm text-slate-700 leading-relaxed font-sans">Clean, solitaire bezel rings and delicate pendant chains continue to lead everyday office and brunch wear styling.</p>
    `
  }
];
"""

if "const BLOG_POSTS =" not in js:
    js = js.replace("const FOR_EVERY_YOU_CARDS =", blog_data_code + "\nconst FOR_EVERY_YOU_CARDS =")

# 2. Add Blog Section HTML right above SHOP WITH CONFIDENCE section
blog_section_html = """
    <!-- 8.5. CIELORIA LUXURY JOURNAL (BLOG SECTION) -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 sm:py-16 space-y-10">
      <div class="text-center space-y-2">
        <span class="text-xs uppercase font-bold text-[#C5A059] tracking-[0.25em]">OUR JOURNAL</span>
        <h2 class="font-serif text-2xl sm:text-4xl font-bold tracking-widest text-[#1A1A1A] uppercase">CIELORIA EDITORIAL & STYLING BLOGS</h2>
        <p class="text-xs sm:text-sm text-slate-500 max-w-xl mx-auto font-medium">Expert styling guides, jewelry care secrets, and daily demifine luxury trends.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 sm:gap-8">
        ${BLOG_POSTS.map(post => `
          <article onclick="openBlogModal('${post.id}')" class="bg-[#FAF8F5] border border-[#E6E1D7] rounded-3xl overflow-hidden shadow-sm hover:shadow-xl hover:border-[#C5A059] transition-all duration-500 group cursor-pointer flex flex-col justify-between text-left">
            <div>
              <div class="relative h-48 sm:h-56 overflow-hidden">
                <img src="${post.image}" onerror="this.onerror=null; this.src='/hero_banner.jpg';" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700 ease-out" />
                <span class="absolute top-3 left-3 bg-[#C5A059] text-white text-[9px] font-bold uppercase tracking-widest px-3 py-1 rounded-full shadow-sm">${post.tag}</span>
              </div>
              <div class="p-6 space-y-3 text-left">
                <div class="flex items-center justify-between text-[11px] text-slate-400 font-medium">
                  <span>📅 ${post.date}</span>
                  <span>⏱️ ${post.readTime}</span>
                </div>
                <h3 class="font-serif text-lg sm:text-xl font-bold text-[#1A1A1A] group-hover:text-[#C5A059] transition-colors leading-snug line-clamp-2">${post.title}</h3>
                <p class="text-xs text-slate-600 leading-relaxed line-clamp-3">${post.excerpt}</p>
              </div>
            </div>
            <div class="p-6 pt-0 text-left">
              <span class="text-xs font-bold text-[#C5A059] group-hover:translate-x-1 inline-block transition-transform">Read Full Article →</span>
            </div>
          </article>
        `).join('')}
      </div>
    </section>
"""

if "<!-- 8.5. CIELORIA LUXURY JOURNAL" not in js:
    js = js.replace("<!-- 9. SHOP WITH CONFIDENCE -->", blog_section_html + "\n    <!-- 9. SHOP WITH CONFIDENCE -->")

# 3. Add openBlogModal handler to state and window
if "activeBlogId" not in js:
    js = js.replace("isMobileMenuOpen: false,", "isMobileMenuOpen: false,\n  activeBlogId: null,")

blog_modal_code = """
window.openBlogModal = function(id) {
  state.activeBlogId = id;
  renderApp();
};

window.closeBlogModal = function() {
  state.activeBlogId = null;
  renderApp();
};
"""

if "window.openBlogModal =" not in js:
    js = js.replace("window.switchViewMode = function", blog_modal_code + "\nwindow.switchViewMode = function")

# 4. Inject blog modal HTML inside renderModals()
blog_modal_view = """
      <!-- Blog Modal -->
      ${state.activeBlogId ? (() => {
        const post = BLOG_POSTS.find(b => b.id === state.activeBlogId) || BLOG_POSTS[0];
        return `
          <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm animate-fade-in text-left">
            <div class="bg-white border border-[#E6E1D7] rounded-3xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl p-6 sm:p-8 space-y-6 relative">
              <button onclick="closeBlogModal()" class="absolute top-4 right-4 text-slate-400 hover:text-black text-xl font-bold p-2">✕</button>

              <div class="space-y-3">
                <span class="bg-[#C5A059] text-white text-[9px] font-bold uppercase tracking-widest px-3 py-1 rounded-full shadow-sm">${post.tag}</span>
                <h2 class="font-serif text-2xl sm:text-3xl font-bold text-[#1A1A1A] leading-tight">${post.title}</h2>
                <div class="flex items-center gap-4 text-xs text-slate-400 font-medium">
                  <span>📅 ${post.date}</span>
                  <span>⏱️ ${post.readTime}</span>
                  <span>✍️ By CIELORIA Editorial</span>
                </div>
              </div>

              <div class="h-64 sm:h-80 rounded-2xl overflow-hidden">
                <img src="${post.image}" onerror="this.onerror=null; this.src='/hero_banner.jpg';" class="w-full h-full object-cover" />
              </div>

              <div class="prose max-w-none space-y-4 pt-2">
                ${post.fullContent}
              </div>

              <div class="pt-4 border-t border-[#E6E1D7] flex items-center justify-between">
                <button onclick="openPLPCategory('All'); closeBlogModal();" class="bg-[#1A1A1A] hover:bg-[#C5A059] text-white font-bold px-6 py-3 rounded-xl text-xs uppercase tracking-wider transition-colors">
                  Explore Demifine Collection →
                </button>
                <button onclick="closeBlogModal()" class="text-xs font-bold text-slate-500 hover:text-black">
                  Close Article
                </button>
              </div>
            </div>
          </div>
        `;
      })() : ''}
"""

if "<!-- Blog Modal -->" not in js:
    js = js.replace("return `\n      <!-- Pincode Modal -->", blog_modal_view + "\n      <!-- Pincode Modal -->")

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully added 3 Blog Posts Section & Interactive Blog Modal above SHOP WITH CONFIDENCE!')
