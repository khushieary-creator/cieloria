import os, re

router_js = """
// CIELORIA Clean URL Router Engine
function getUrlSlug(str) {
  return (str || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

function updateBrowserUrl(path, skipPush) {
  try {
    if (!skipPush && window.location.pathname !== path) {
      window.history.pushState({ path }, document.title, path);
    }
  } catch (e) {}
}

window.switchViewMode = function(mode, skipPush = false) { 
  state.viewMode = mode; 
  if (mode === 'about') {
    state.plpCategory = 'About';
    updateBrowserUrl('/about', skipPush);
  } else if (mode === 'homepage') {
    state.plpCategory = '';
    updateBrowserUrl('/', skipPush);
  } else if (mode === 'account') {
    updateBrowserUrl('/account', skipPush);
  } else if (mode === 'wishlist') {
    updateBrowserUrl('/wishlist', skipPush);
  } else if (mode === 'order_confirmed') {
    updateBrowserUrl('/order-confirmed', skipPush);
  }
  window.scrollTo({ top: 0, behavior: 'smooth' }); 
  renderApp(); 
};

window.openPDP = function(id, skipPush = false) { 
  state.selectedProductId = id; 
  state.activeGalleryIndex = 0;
  state.viewMode = 'pdp'; 
  updateBrowserUrl('/product/' + id, skipPush);
  window.scrollTo({ top: 0, behavior: 'smooth' }); 
  renderApp(); 
};

window.openPLPCategory = function(cat, skipPush = false) { 
  if (cat && cat.toLowerCase() === 'about') {
    state.viewMode = 'about';
    state.plpCategory = 'About';
    updateBrowserUrl('/about', skipPush);
  } else {
    state.plpCategory = cat; 
    state.plpSubFilter = '';
    state.viewMode = 'plp'; 
    const slug = getUrlSlug(cat || 'all');
    updateBrowserUrl('/category/' + (slug || 'all'), skipPush);
  }
  window.scrollTo({ top: 0, behavior: 'smooth' }); 
  renderApp(); 
};

window.openWishlistView = function() {
  state.viewMode = 'wishlist';
  updateBrowserUrl('/wishlist', false);
  window.scrollTo({ top: 0, behavior: 'smooth' });
  renderApp();
};

function syncStateFromUrl() {
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
      const slug = path.replace('/category/', '');
      const categoryMap = {
        'new-arrivals': 'New Arrivals',
        'anti-tarnish': 'Anti-Tarnish',
        'waterproof': 'Waterproof',
        'rings': 'Rings',
        'earrings': 'Earrings',
        'necklaces': 'Necklaces',
        'bracelets': 'Bracelets',
        'gifting': 'Gifting',
        'bestsellers': 'Bestsellers'
      };
      state.plpCategory = categoryMap[slug] || (slug ? slug.replace(/-/g, ' ').toUpperCase() : 'All');
      state.viewMode = 'plp';
    }
  } catch(e) {}
}

window.addEventListener('popstate', () => {
  syncStateFromUrl();
  renderApp();
});
"""

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace existing navigation functions
target_pattern = r'window\.switchViewMode = function\(mode\).*?window\.openWishlistView = function\(\) \{.*?\};'
js = re.sub(target_pattern, router_js, js, flags=re.DOTALL)

# Insert syncStateFromUrl call before renderApp on page load
js = js.replace("syncAccountStorage();", "syncAccountStorage();\n  syncStateFromUrl();")

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully integrated Clean URL Router into cieloria_app.js!')
