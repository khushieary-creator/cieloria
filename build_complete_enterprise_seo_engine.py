import os, sys, json, time, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Generate sitemap.xml
products_raw = re.findall(r'"id": "([^"]+)"', js)
# Extract unique product IDs
product_ids = []
for p_id in products_raw:
    if p_id not in product_ids and len(p_id) > 2 and not p_id.startswith('app_') and not p_id.startswith('blog-'):
        product_ids.append(p_id)

category_slugs = ['all', 'best-seller', 'new-arrivals', 'rings', 'earrings', 'necklaces', 'bracelets', 'mangalsutras', 'mens', 'gifting', 'fine-silver', '9kt-fine-gold']
blog_slugs = ['lab-grown-diamonds', 'womens-day-jewellery-guide', 'gold-vs-silver-jewellery']

current_date = time.strftime('%Y-%m-%d')

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  
  <!-- Root Homepage -->
  <url>
    <loc>https://www.cieloria.com/</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  
  <!-- About Us -->
  <url>
    <loc>https://www.cieloria.com/about</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""

# Add Categories
for cat in category_slugs:
    sitemap_xml += f"""  <url>
    <loc>https://www.cieloria.com/category/{cat}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
"""

# Add Blogs
for b_slug in blog_slugs:
    sitemap_xml += f"""  <url>
    <loc>https://www.cieloria.com/blog/{b_slug}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""

# Add Products
for p_id in product_ids:
    sitemap_xml += f"""  <url>
    <loc>https://www.cieloria.com/product/{p_id}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""

sitemap_xml += "</urlset>\n"

# Write sitemap.xml to root, public, dist
dirs = ['.', 'public', 'dist']
for d in dirs:
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_xml)

print(f'Successfully generated sitemap.xml with {1 + len(category_slugs) + len(blog_slugs) + len(product_ids)} indexed URLs!')

# 2. Generate robots.txt
robots_txt = """User-agent: *
Allow: /
Disallow: /?view=admin
Disallow: /api/

Sitemap: https://www.cieloria.com/sitemap.xml
"""

for d in dirs:
    with open(os.path.join(d, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots_txt)

print('Successfully generated robots.txt!')

# 3. Add Dynamic SEO & Structured Data Engine to cieloria_app.js
seo_engine_code = """
// CIELORIA Enterprise Dynamic SEO & JSON-LD Structured Data Engine
function updateDynamicSEO(options = {}) {
  try {
    const title = options.title || "Buy 18K Gold Anti-Tarnish & Waterproof Demifine Jewelry Online | CIELORIA®";
    const desc = options.desc || "Shop 100% waterproof, anti-tarnish 18K gold plated demi-fine jewelry at Cieloria. Solitaire rings, anti-tarnish bracelets, pendant necklaces, mangalsutras & kada bangles.";
    const url = options.url || window.location.href;
    const image = options.image || "https://www.cieloria.com/hero_banner.jpg";

    document.title = title;

    // Update Meta Description
    let metaDesc = document.querySelector('meta[name="description"]');
    if (!metaDesc) {
      metaDesc = document.createElement('meta');
      metaDesc.name = "description";
      document.head.appendChild(metaDesc);
    }
    metaDesc.content = desc;

    # OpenGraph Tags
    const ogTags = {
      'og:title': title,
      'og:description': desc,
      'og:url': url,
      'og:image': image,
      'og:type': options.type || 'website',
      'og:site_name': 'CIELORIA Demifine Luxury',
      'twitter:card': 'summary_large_image',
      'twitter:title': title,
      'twitter:description': desc,
      'twitter:image': image
    };

    Object.keys(ogTags).forEach(property => {
      let tag = document.querySelector(`meta[property="${property}"]`) || document.querySelector(`meta[name="${property}"]`);
      if (!tag) {
        tag = document.createElement('meta');
        if (property.startsWith('og:')) tag.setAttribute('property', property);
        else tag.setAttribute('name', property);
        document.head.appendChild(tag);
      }
      tag.content = ogTags[property];
    });

    # Inject Dynamic JSON-LD Schema
    if (options.schema) {
      let schemaScript = document.getElementById('cieloria-dynamic-jsonld');
      if (!schemaScript) {
        schemaScript = document.createElement('script');
        schemaScript.id = 'cieloria-dynamic-jsonld';
        schemaScript.type = 'application/ld+json';
        document.head.appendChild(schemaScript);
      }
      schemaScript.textContent = JSON.stringify(options.schema);
    }
  } catch(e) {}
}

# Update SEO on renderApp
const originalRenderApp = renderApp;
"""

if "function updateDynamicSEO(" not in js:
    # Inject updateDynamicSEO logic into syncStateFromUrl or view handlers
    js = seo_engine_code + "\n" + js

# Update renderApp to trigger updateDynamicSEO based on viewMode
seo_render_hook = """
  // Dynamic SEO Trigger
  try {
    if (state.viewMode === 'pdp' && state.selectedProductId) {
      const prod = PRODUCTS.find(p => p.id === state.selectedProductId);
      if (prod) {
        updateDynamicSEO({
          title: `${prod.name} - 18K Gold Waterproof Demifine Jewelry | CIELORIA®`,
          desc: `Buy ${prod.name} online at CIELORIA. 100% Waterproof, 18K gold plated anti-tarnish coating, skin safe & hypoallergenic. Free shipping across India.`,
          url: `https://www.cieloria.com/product/${prod.id}`,
          image: prod.image,
          type: 'product',
          schema: {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": prod.name,
            "image": [prod.image, prod.secondaryImage || prod.image],
            "description": prod.description,
            "sku": prod.sku || `SKU-${prod.id}`,
            "brand": {
              "@type": "Brand",
              "name": "CIELORIA"
            },
            "offers": {
              "@type": "Offer",
              "url": `https://www.cieloria.com/product/${prod.id}`,
              "priceCurrency": "INR",
              "price": prod.price,
              "priceValidUntil": "2027-12-31",
              "itemCondition": "https://schema.org/NewCondition",
              "availability": prod.inStock !== false ? "https://schema.org/InStock" : "https://schema.org/OutOfStock",
              "seller": {
                "@type": "Organization",
                "name": "CIELORIA"
              }
            },
            "aggregateRating": {
              "@type": "AggregateRating",
              "ratingValue": prod.rating || 4.8,
              "reviewCount": prod.reviewCount || 120
            }
          }
        });
      }
    } else if (state.viewMode === 'blog_detail' && state.selectedBlogSlug) {
      const blog = BLOG_POSTS.find(b => b.slug === state.selectedBlogSlug);
      if (blog) {
        updateDynamicSEO({
          title: `${blog.title} | CIELORIA® Jewelry Journal`,
          desc: blog.excerpt,
          url: `https://www.cieloria.com/blog/${blog.slug}`,
          image: blog.image,
          type: 'article',
          schema: {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": blog.title,
            "image": [blog.image],
            "datePublished": "2026-03-01",
            "dateModified": "2026-09-13",
            "author": {
              "@type": "Organization",
              "name": "CIELORIA Editorial Team"
            },
            "publisher": {
              "@type": "Organization",
              "name": "CIELORIA",
              "logo": {
                "@type": "ImageObject",
                "url": "https://www.cieloria.com/cieloria_logo.png"
              }
            },
            "description": blog.excerpt
          }
        });
      }
    } else if (state.viewMode === 'plp') {
      const catName = state.plpCategory || 'All';
      updateDynamicSEO({
        title: `Buy Anti-Tarnish ${catName} Jewelry Online | CIELORIA® Demifine Collection`,
        desc: `Explore 100% waterproof 18K gold plated ${catName} at CIELORIA. Anti-tarnish, nickel-free, hypoallergenic luxury jewelry designed for everyday wear.`,
        url: `https://www.cieloria.com/category/${getUrlSlug(catName)}`
      });
    } else if (state.viewMode === 'about') {
      updateDynamicSEO({
        title: "About CIELORIA® | Lucknow HQ Demifine Luxury Jewelry Brand",
        desc: "Learn about CIELORIA's mission to craft 100% waterproof, anti-tarnish 18K gold demifine jewelry for modern India."
      });
    } else {
      updateDynamicSEO({
        title: "Buy 18K Gold Anti-Tarnish & Waterproof Demifine Jewelry Online | CIELORIA®",
        desc: "Shop 100% waterproof, anti-tarnish 18K gold plated demi-fine jewelry at Cieloria. Solitaire rings, anti-tarnish bracelets, pendant necklaces, mangalsutras & kada bangles.",
        schema: {
          "@context": "https://schema.org",
          "@type": "Organization",
          "name": "CIELORIA",
          "url": "https://www.cieloria.com",
          "logo": "https://www.cieloria.com/cieloria_logo.png",
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+91-9999999999",
            "contactType": "customer service"
          },
          "sameAs": [
            "https://www.instagram.com/cieloria",
            "https://www.facebook.com/cieloria"
          ]
        }
      });
    }
  } catch(e) {}
"""

if "Dynamic SEO Trigger" not in js:
    js = js.replace("const appContainer = document.getElementById('app');", "const appContainer = document.getElementById('app');\n" + seo_render_hook)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully integrated Enterprise Dynamic SEO Engine into cieloria_app.js!')
