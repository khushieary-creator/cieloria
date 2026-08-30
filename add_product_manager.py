import os

with open('clean_app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Enhance adminState to include newProduct draft
old_admin_state = """let adminState = {
  isAuthenticated: sessionStorage.getItem('cieloria_admin_auth') === 'true',
  passcode: '',
  allOrders: getStoredData('cieloria_merchant_all_orders', [])
};"""

new_admin_state = """let adminState = {
  isAuthenticated: sessionStorage.getItem('cieloria_admin_auth') === 'true',
  passcode: '',
  allOrders: getStoredData('cieloria_merchant_all_orders', []),
  showAddProductForm: false,
  newProd: {
    title: '',
    price: '',
    mrp: '',
    category: 'BestSeller',
    type: 'Necklaces',
    image: '',
    description: ''
  }
};

// Merge Custom Merchant Added Products into Store Catalog
(function mergeMerchantProducts() {
  try {
    const custom = getStoredData('cieloria_custom_merchant_products', []);
    if (custom && custom.length > 0) {
      custom.forEach(cp => {
        if (!PRODUCTS.find(p => p.id === cp.id)) {
          PRODUCTS.unshift(cp);
        }
      });
    }
  } catch(e) {}
})();

function handleAddNewProductSubmit(e) {
  if (e) e.preventDefault();
  const np = adminState.newProd;
  if (!np.title || !np.price) {
    alert('⚠️ Please enter Product Title and Price!');
    return;
  }

  const priceNum = parseInt(np.price) || 999;
  const mrpNum = parseInt(np.mrp) || Math.round(priceNum * 1.8);
  const prodId = 'prod_custom_' + Date.now();

  const newProductObj = {
    id: prodId,
    title: np.title,
    price: priceNum,
    mrp: mrpNum,
    rating: 4.9,
    reviewsCount: 12,
    tag: 'NEW LAUNCH ✦',
    tagBg: 'bg-[#C5A059] text-white',
    category: np.category || 'BestSeller',
    type: np.type || 'Jewelry',
    material: '18K Gold Plated Anti-Tarnish',
    warranty: 'Lifetime Anti-Tarnish Guarantee',
    images: [
      np.image || 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&q=80&w=800',
      'https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&q=80&w=800'
    ],
    image: np.image || 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&q=80&w=800',
    description: np.description || 'Handcrafted 100% anti-tarnish 18K gold plated demi-fine luxury piece.',
    highlights: [
      '100% Anti-Tarnish Guarantee',
      'Waterproof 18K Gold Plating',
      'Hypoallergenic & Skin Friendly',
      'Ships in 24 Hours from Lucknow'
    ]
  };

  PRODUCTS.unshift(newProductObj);
  const customList = getStoredData('cieloria_custom_merchant_products', []);
  customList.unshift(newProductObj);
  setStoredData('cieloria_custom_merchant_products', customList);

  alert(`🎉 SUCCESS! '${newProductObj.title}' is NOW LIVE on CIELORIA Storefront!`);
  adminState.showAddProductForm = false;
  adminState.newProd = { title: '', price: '', mrp: '', category: 'BestSeller', type: 'Necklaces', image: '', description: '' };
  renderApp();
}
"""

code = code.replace(old_admin_state, new_admin_state)

# Add Product Form UI inside renderAdminView
admin_view_button_target = """<button onclick="handleAdminLogout()" class="border border-rose-500/40 hover:bg-rose-500/10 text-rose-400 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              Logout
            </button>"""

admin_view_button_replacement = """<button onclick="adminState.showAddProductForm = !adminState.showAddProductForm; renderApp();" class="bg-amber-500 hover:bg-amber-600 text-slate-950 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-lg flex items-center gap-1.5">
              ✨ Add New Product
            </button>
            <button onclick="handleAdminLogout()" class="border border-rose-500/40 hover:bg-rose-500/10 text-rose-400 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              Logout
            </button>"""

code = code.replace(admin_view_button_target, admin_view_button_replacement)

# Add Add Product Form Modal render in renderAdminView
orders_section_target = """<div class="grid grid-cols-1 sm:grid-cols-4 gap-4 text-center">"""

add_product_form_html = """
        ${adminState.showAddProductForm ? `
          <div class="bg-slate-900 border border-amber-500/40 rounded-3xl p-6 sm:p-8 space-y-6 shadow-2xl animate-fade-in">
            <div class="flex items-center justify-between border-b border-slate-800 pb-4">
              <div class="flex items-center gap-3">
                <span class="text-2xl">✨</span>
                <div>
                  <h3 class="font-serif text-xl font-bold text-white uppercase tracking-wider">Publish New Product to Storefront</h3>
                  <p class="text-xs text-slate-400">Fill in details below to instantly list a new product on www.cieloria.com</p>
                </div>
              </div>
              <button onclick="adminState.showAddProductForm=false; renderApp();" class="text-slate-400 hover:text-white text-lg">✕</button>
            </div>

            <form onsubmit="handleAddNewProductSubmit(event)" class="space-y-5 text-left">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="space-y-1.5">
                  <label class="text-xs font-bold text-slate-300">Product Title *</label>
                  <input type="text" required placeholder="e.g. Royal Solitaire 18K Gold Necklace" value="${adminState.newProd.title}" oninput="adminState.newProd.title=this.value" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-400" />
                </div>

                <div class="space-y-1.5">
                  <label class="text-xs font-bold text-slate-300">Category Tag *</label>
                  <select onchange="adminState.newProd.category=this.value" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-400 cursor-pointer">
                    <option value="BestSeller" ${adminState.newProd.category==='BestSeller'?'selected':''}>Best Seller 🔥</option>
                    <option value="NewArrivals" ${adminState.newProd.category==='NewArrivals'?'selected':''}>New Arrival ✨</option>
                    <option value="FineSilver" ${adminState.newProd.category==='FineSilver'?'selected':''}>Fine Silver 925 💎</option>
                    <option value="NineKTGold" ${adminState.newProd.category==='NineKTGold'?'selected':''}>9KT Solid Gold 👑</option>
                    <option value="Demifine" ${adminState.newProd.category==='Demifine'?'selected':''}>Demifine ® Collection</option>
                  </select>
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div class="space-y-1.5">
                  <label class="text-xs font-bold text-slate-300">Selling Price (₹) *</label>
                  <input type="number" required placeholder="e.g. 1499" value="${adminState.newProd.price}" oninput="adminState.newProd.price=this.value" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-400" />
                </div>

                <div class="space-y-1.5">
                  <label class="text-xs font-bold text-slate-300">Original MRP (₹)</label>
                  <input type="number" placeholder="e.g. 2999" value="${adminState.newProd.mrp}" oninput="adminState.newProd.mrp=this.value" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-400" />
                </div>

                <div class="space-y-1.5">
                  <label class="text-xs font-bold text-slate-300">Jewelry Type</label>
                  <select onchange="adminState.newProd.type=this.value" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-400 cursor-pointer">
                    <option value="Necklaces">Necklace / Pendant</option>
                    <option value="Earrings">Earrings / Studs</option>
                    <option value="Rings">Rings</option>
                    <option value="Bracelets">Bracelets / Bangles</option>
                  </select>
                </div>
              </div>

              <div class="space-y-1.5">
                <label class="text-xs font-bold text-slate-300">Product Image URL (HD Photo Link)</label>
                <input type="url" placeholder="https://images.unsplash.com/... or image link" value="${adminState.newProd.image}" oninput="adminState.newProd.image=this.value" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-400" />
              </div>

              <div class="space-y-1.5">
                <label class="text-xs font-bold text-slate-300">Short Product Description</label>
                <textarea rows="2" placeholder="e.g. 100% waterproof 18k gold plated solitaire necklace crafted in Lucknow HQ..." oninput="adminState.newProd.description=this.value" class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-amber-400">${adminState.newProd.description}</textarea>
              </div>

              <div class="flex items-center gap-3 pt-2">
                <button type="submit" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold px-6 py-3 rounded-xl text-xs uppercase tracking-wider transition-colors shadow-lg">
                  🚀 Publish Product Live Now
                </button>
                <button type="button" onclick="adminState.showAddProductForm=false; renderApp();" class="text-slate-400 hover:text-white px-4 py-3 text-xs">
                  Cancel
                </button>
              </div>
            </form>
          </div>
        ` : ''}

        <div class="grid grid-cols-1 sm:grid-cols-4 gap-4 text-center">"""

code = code.replace(orders_section_target, add_product_form_html)

with open('clean_app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully updated clean_app.py with Add New Product Listing feature!')
