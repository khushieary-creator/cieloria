import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update syncStateFromUrl in cieloria_app.js
old_sync_func = r'function syncStateFromUrl\(\) \{.*?\n\}'

new_sync_func = """function syncStateFromUrl() {
  try {
    const path = window.location.pathname || '/';
    if (path === '/about') {
      state.viewMode = 'about';
      state.plpCategory = 'About';
    } else if (path === '/account') {
      state.viewMode = 'account';
    } else if (path === '/wishlist') {
      state.viewMode = 'wishlist';
    } else if (path === '/order-confirmed') {
      state.viewMode = 'order_confirmed';
    } else if (path.startsWith('/product/')) {
      const prodId = path.replace('/product/', '');
      if (prodId) {
        state.selectedProductId = prodId;
        state.viewMode = 'pdp';
      }
    } else if (path.startsWith('/category/')) {
      const rawSlug = path.replace('/category/', '').toLowerCase();
      const categoryMap = {
        'new-arrivals': 'NewArrivals',
        'best-seller': 'BestSeller',
        'bestseller': 'BestSeller',
        'fine-silver': 'FineSilver',
        '9kt-fine-gold': 'NineKTGold',
        'anti-tarnish': 'Anti-Tarnish',
        'waterproof': 'Waterproof',
        'rings': 'Rings',
        'earrings': 'Earrings',
        'necklaces': 'Necklaces',
        'bracelets': 'Bracelets',
        'mangalsutras': 'Mangalsutras',
        'mangalsutra': 'Mangalsutras',
        'mens': 'Mens',
        'men': 'Mens',
        'gifting': 'Gifting'
      };
      if (categoryMap[rawSlug]) {
        state.plpCategory = categoryMap[rawSlug];
      } else {
        const matchedKey = Object.keys(PLP_CATEGORY_DATA).find(k => k.toLowerCase() === rawSlug || k.toLowerCase() === rawSlug.replace(/-/g, ''));
        state.plpCategory = matchedKey || 'All';
      }
      state.viewMode = 'plp';
    }
  } catch(e) {}
}"""

js = re.sub(old_sync_func, new_sync_func, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated syncStateFromUrl with Mangalsutras & Mens mappings!')
