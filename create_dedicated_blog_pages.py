import os, re

# 1. Update vercel.json with /blog/:slug* rewrite
vercel_config = """{
  "rewrites": [
    {
      "source": "/category/:slug*",
      "destination": "/index.html"
    },
    {
      "source": "/product/:id*",
      "destination": "/index.html"
    },
    {
      "source": "/blog/:slug*",
      "destination": "/index.html"
    },
    {
      "source": "/about",
      "destination": "/index.html"
    },
    {
      "source": "/account",
      "destination": "/index.html"
    },
    {
      "source": "/wishlist",
      "destination": "/index.html"
    },
    {
      "source": "/order-confirmed",
      "destination": "/index.html"
    }
  ]
}
"""

with open('vercel.json', 'w', encoding='utf-8') as f:
    f.write(vercel_config)

# 2. Update cieloria_app.js to add BLOG_POSTS slugs, openBlogPage, syncStateFromUrl, and renderBlogDetailView
with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update BLOG_POSTS array with slugs
new_blog_posts_code = """const BLOG_POSTS = [
  {
    id: "blog-1",
    slug: "lab-grown-diamonds",
    day: "03",
    month: "MAR",
    tag: "DIAMOND CARE",
    title: "Lab-Grown Diamonds: Styling & Care for the Modern Indian Woman",
    image: "/blog_1.jpg",
    excerpt: "If jewellery had a reality check, lab-grown diamonds would be it. Real, pretty, conflict-free, and crafted for everyday elegance.",
    fullContent: `
      <p class="text-base text-slate-700 leading-relaxed">If jewellery had a reality check, lab-grown diamonds would be it. Real, pretty, conflict-free, and crafted for everyday elegance. In a world where luxury often feels distant or delicate, lab-grown diamonds bring brilliant sparkle straight into your daily wardrobe.</p>
      
      <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A] pt-4">What Are Lab-Grown Diamonds?</h3>
      <p class="text-base text-slate-700 leading-relaxed">Lab-grown diamonds are grown using advanced technology that replicates the natural pressure and temperature deep within the earth. They possess the exact same chemical, optical, and physical properties as mined diamonds — with identical hardness, brilliance, and fire.</p>

      <blockquote class="font-serif text-lg text-[#C5A059] italic border-l-4 border-[#C5A059] pl-6 my-6 bg-[#FAF8F5] py-4 rounded-r-xl">
        "Real sparkle shouldn't be locked away in a safe. It's meant to catch the light on your morning coffee run and shine at evening dinners."
      </blockquote>

      <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A] pt-4">Styling Solitaire Diamonds for Everyday Glamour</h3>
      <p class="text-base text-slate-700 leading-relaxed">Pairing a solitaire lab-grown diamond pendant with 18K thick gold plated chains creates a timeless look. You can stack open-bezel rings with twisted gold bands for a subtle yet striking minimalist aesthetic.</p>

      <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A] pt-4">How to Clean & Preserve Your Demifine Solitaires</h3>
      <ul class="list-disc pl-6 text-base text-slate-700 space-y-2">
        <li>Wash gently with lukewarm soapy water and a soft bristle brush once a month.</li>
        <li>Avoid harsh industrial chemicals or bleach.</li>
        <li>Store in your CIELORIA anti-tarnish suede pouch when traveling.</li>
      </ul>
    `
  },
  {
    id: "blog-2",
    slug: "womens-day-jewellery-guide",
    day: "02",
    month: "MAR",
    tag: "WOMEN'S EDITION",
    title: "The Women's Day Jewellery Guide Nobody Asked For, But Everybody Needed",
    image: "/blog_2.jpg",
    excerpt: "Beyoncé told us who runs the world. Legally Blonde proved that a woman can wear gold and dominate the boardroom.",
    fullContent: `
      <p class="text-base text-slate-700 leading-relaxed">Beyoncé told us who runs the world. Legally Blonde proved that a woman can wear gold and dominate the boardroom. Demifine jewelry isn't just an accessory — it's a daily assertion of grace, strength, and individuality.</p>

      <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A] pt-4">Why Self-Gifting Matters</h3>
      <p class="text-base text-slate-700 leading-relaxed">Waiting for a special milestone to buy gold is a thing of the past. Today's modern woman celebrates her own wins — big or small — with lasting demifine pieces that elevate her everyday wardrobe.</p>

      <blockquote class="font-serif text-lg text-[#C5A059] italic border-l-4 border-[#C5A059] pl-6 my-6 bg-[#FAF8F5] py-4 rounded-r-xl">
        "Wear the gold hoop earrings to work. Wear the pendant necklace to coffee. Every day is a occasion worth dressing up for."
      </blockquote>

      <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A] pt-4">Top 3 Pieces Every Woman Needs in Her Capsule Collection</h3>
      <ol class="list-decimal pl-6 text-base text-slate-700 space-y-2">
        <li><strong>Classic Golden Hoop Earrings:</strong> Lightweight, anti-tarnish, and skin-safe for 24/7 wear.</li>
        <li><strong>Layered Chain Pendant:</strong> Adds effortless texture to t-shirts, dresses, and formal blazers.</li>
        <li><strong>Structured Kada Bangle:</strong> A bold symbol of confidence and timeless Indian heritage.</li>
      </ol>
    `
  },
  {
    id: "blog-3",
    slug: "gold-vs-silver-jewellery",
    day: "01",
    month: "MAR",
    tag: "STYLE COMPARISON",
    title: "Gold vs Silver Jewellery: How to Choose What Suits You Best",
    image: "/blog_3.jpg",
    excerpt: "The great debate is always on – gold or silver? That's like asking, chai or coffee? Here is how to find your true metallic signature.",
    fullContent: `
      <p class="text-base text-slate-700 leading-relaxed">The great debate is always on – gold or silver? That's like asking, chai or coffee? Both have their unique charm, but finding your true metallic match will instantly harmonize your wardrobe and complement your skin tones.</p>

      <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A] pt-4">Determining Your Skin Undertone</h3>
      <p class="text-base text-slate-700 leading-relaxed">Look at the veins on your inner wrist under natural light:</p>
      <ul class="list-disc pl-6 text-base text-slate-700 space-y-2">
        <li><strong>Warm Undertones (Greenish veins):</strong> 18K Champagne Gold plating glows against warm skin tones.</li>
        <li><strong>Cool Undertones (Blueish veins):</strong> 925 Sterling Fine Silver provides a crisp, luminous contrast.</li>
        <li><strong>Neutral Undertones (Mix of blue & green):</strong> You hit the jackpot! Both gold and silver look stunning on you.</li>
      </ul>

      <blockquote class="font-serif text-lg text-[#C5A059] italic border-l-4 border-[#C5A059] pl-6 my-6 bg-[#FAF8F5] py-4 rounded-r-xl">
        "Can you mix gold and silver together? Absolutely! Mixed metal styling is one of 2026's boldest fashion trends."
      </blockquote>

      <h3 class="font-serif text-xl sm:text-2xl font-bold text-[#1A1A1A] pt-4">The CIELORIA Waterproof Promise</h3>
      <p class="text-base text-slate-700 leading-relaxed">Whether you choose 18K Gold Demifine or 925 Fine Silver, all CIELORIA pieces are treated with protective anti-tarnish seals, ensuring 100% waterproof resilience against sweat and daily wear.</p>
    `
  }
];"""

js = re.sub(r'const BLOG_POSTS = \[.*?\];', new_blog_posts_code, js, flags=re.DOTALL)

# Update BLOGS section to openBlogPage(post.slug)
js = js.replace("openBlogModal('${post.id}')", "openBlogPage('${post.slug}')")
js = js.replace('openBlogModal("${post.id}")', 'openBlogPage("${post.slug}")')

# Add window.openBlogPage and renderBlogDetailView
blog_page_functions = """
window.openBlogPage = function(slug, skipPush = false) {
  state.selectedBlogSlug = slug;
  state.viewMode = 'blog_detail';
  updateBrowserUrl('/blog/' + slug, skipPush);
  window.scrollTo({ top: 0, behavior: 'smooth' });
  renderApp();
};

function renderBlogDetailView() {
  const post = BLOG_POSTS.find(b => b.slug === state.selectedBlogSlug) || BLOG_POSTS[0];
  const otherPosts = BLOG_POSTS.filter(b => b.slug !== post.slug);

  return `
    <div class="bg-white min-h-screen pb-20 animate-fade-in text-left">
      <!-- Breadcrumb Bar -->
      <nav class="bg-[#FAF8F5] border-b border-[#E6E1D7] py-4">
        <div class="max-w-4xl mx-auto px-4 text-xs text-slate-500 flex items-center gap-2">
          <button onclick="switchViewMode('homepage')" class="hover:text-black font-semibold">Home</button>
          <span>›</span>
          <button onclick="switchViewMode('homepage')" class="hover:text-black font-semibold">Blogs</button>
          <span>›</span>
          <span class="text-[#1A1A1A] font-bold truncate">${post.title}</span>
        </div>
      </nav>

      <!-- Article Header -->
      <header class="max-w-4xl mx-auto px-4 pt-10 pb-6 space-y-4">
        <div class="flex items-center gap-3">
          <span class="bg-[#C5A059] text-white text-[10px] font-bold uppercase tracking-widest px-3 py-1 rounded-full shadow-sm">${post.tag}</span>
          <span class="text-xs text-slate-400 font-medium">📅 ${post.day} ${post.month} 2026</span>
          <span class="text-xs text-slate-400 font-medium">⏱️ 4 min read</span>
        </div>

        <h1 class="font-serif text-3xl sm:text-5xl font-bold text-[#1A1A1A] leading-tight">${post.title}</h1>
        
        <p class="text-base sm:text-lg text-slate-600 font-serif italic">${post.excerpt}</p>
      </header>

      <!-- Featured Image -->
      <div class="max-w-4xl mx-auto px-4 mb-10">
        <div class="aspect-video sm:aspect-[16/9] rounded-3xl overflow-hidden shadow-lg border border-[#E6E1D7] bg-slate-100">
          <img src="${post.image}" onerror="this.onerror=null; this.src='/hero_banner.jpg';" class="w-full h-full object-cover" />
        </div>
      </div>

      <!-- Article Main Content -->
      <article class="max-w-3xl mx-auto px-4 space-y-6 text-slate-800 leading-relaxed text-base font-sans border-b border-[#E6E1D7] pb-12 mb-16">
        ${post.fullContent}

        <div class="pt-8 flex items-center justify-between border-t border-[#E6E1D7] mt-10">
          <button onclick="switchViewMode('homepage')" class="border border-black text-black hover:bg-black hover:text-white px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-wider transition-colors">
            ← Back to All Blogs
          </button>

          <button onclick="openPLPCategory('All')" class="bg-[#C5A059] hover:bg-[#A38038] text-white px-6 py-3 rounded-xl text-xs font-bold uppercase tracking-wider transition-colors shadow-md">
            Shop Demifine Jewelry →
          </button>
        </div>
      </article>

      <!-- More Articles Section -->
      <section class="max-w-4xl mx-auto px-4 space-y-6">
        <h3 class="font-serif text-2xl font-bold text-[#1A1A1A] tracking-wider uppercase text-center sm:text-left">More Articles You Might Love</h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          ${otherPosts.map(other => `
            <div onclick="openBlogPage('${other.slug}')" class="flex gap-4 p-4 rounded-2xl bg-[#FAF8F5] border border-[#E6E1D7] cursor-pointer hover:border-[#C5A059] transition-all group">
              <img src="${other.image}" class="w-24 h-24 object-cover rounded-xl shrink-0 group-hover:scale-105 transition-transform" />
              <div class="space-y-1 my-auto">
                <span class="text-[9px] font-bold text-[#C5A059] uppercase tracking-wider">${other.tag}</span>
                <h4 class="font-serif text-base font-bold text-[#1A1A1A] line-clamp-2 leading-snug group-hover:text-[#C5A059]">${other.title}</h4>
                <span class="text-[10px] text-slate-400 font-medium">Read Article →</span>
              </div>
            </div>
          `).join('')}
        </div>
      </section>
    </div>
  `;
}
"""

if "window.openBlogPage =" not in js:
    js = js.replace("window.switchViewMode = function", blog_page_functions + "\nwindow.switchViewMode = function")

# Update syncStateFromUrl to handle /blog/
if "path.startsWith('/blog/')" not in js:
    sync_blog_code = """    } else if (path.startsWith('/blog/')) {
      const blogSlug = path.replace('/blog/', '').toLowerCase();
      state.selectedBlogSlug = blogSlug;
      state.viewMode = 'blog_detail';
    }"""
    js = js.replace("} else if (path.startsWith('/product/')) {", sync_blog_code + "\n    } else if (path.startsWith('/product/')) {")

# Update renderApp to handle viewMode === 'blog_detail'
if "state.viewMode === 'blog_detail'" not in js:
    js = js.replace("} else if (state.viewMode === 'pdp') {", "} else if (state.viewMode === 'blog_detail') {\n    mainContent = renderBlogDetailView();\n  } else if (state.viewMode === 'pdp') {")

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully added Dedicated Full-Page Blog Article Routes /blog/<slug>!')
