import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add admin route detection in initial state
js = js.replace("viewMode: 'homepage'", "viewMode: (window.location.search.includes('view=admin') || window.location.hash.includes('admin') || window.location.pathname.includes('/admin')) ? 'admin' : 'homepage'")

# Add renderAdminView inside main viewMode router
target_str = "${state.viewMode === 'order_confirmed' ? renderOrderConfirmedView() : ''}"
replacement_str = "${state.viewMode === 'order_confirmed' ? renderOrderConfirmedView() : ''}\n      ${state.viewMode === 'admin' ? renderAdminView() : ''}"

js = js.replace(target_str, replacement_str)

# Append admin helper functions and renderAdminView ONCE
admin_code = """

// CIELORIA Merchant Admin Portal Logic
let adminState = {
  isAuthenticated: sessionStorage.getItem('cieloria_admin_auth') === 'true',
  passcode: '',
  allOrders: (typeof getAllCumulativeOrders === 'function') ? getAllCumulativeOrders() : getStoredData('cieloria_merchant_all_orders', []),
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


function fetchCloudOrders() {
  fetch('/api/sync?action=get_all_orders')
    .then(res => res.json())
    .then(data => {
      let masterMap = new Map();
      getAllCumulativeOrders().forEach(o => { if (o && o.orderId) masterMap.set(o.orderId, o); });

      if (data && data.orders && Array.isArray(data.orders) && data.orders.length > 0) {
        data.orders.forEach(co => {
          if (co && co.orderId) {
            if (!masterMap.has(co.orderId)) {
              masterMap.set(co.orderId, co);
            } else {
              let existing = masterMap.get(co.orderId);
              if (co.status && co.status !== existing.status) {
                existing.status = co.status;
                existing.statusColor = co.statusColor;
              }
            }
          }
        });
      }

      const mergedList = Array.from(masterMap.values());
      adminState.allOrders = mergedList;
      state.ordersList = mergedList;
      setStoredData('cieloria_master_permanent_orders_v1', mergedList);
      setStoredData('cieloria_merchant_all_orders', mergedList);
      if (adminState.isAuthenticated && state.viewMode === 'admin') {
        // Only re-render if count or statuses changed to prevent UI flicker
        if (!adminState.lastCount || adminState.lastCount !== mergedList.length) {
          adminState.lastCount = mergedList.length;
          renderApp();
        }
      }
    }).catch(e => console.log('Admin Cloud Fetch Note:', e));
}

setInterval(fetchCloudOrders, 4000);

function handleAdminLogin(e) {
  if (e) e.preventDefault();
  if (adminState.passcode === '42961' || adminState.passcode === '2yyq6ziimeofq998' || adminState.passcode === 'cieloria123') {
    adminState.isAuthenticated = true;
    sessionStorage.setItem('cieloria_admin_auth', 'true');
    renderApp();
  } else {
    alert('❌ Invalid Merchant Passcode! Use your Merchant Code: 42961');
  }
}

function handleAdminLogout() {
  adminState.isAuthenticated = false;
  sessionStorage.removeItem('cieloria_admin_auth');
  renderApp();
}

function handleOrderStatusChange(orderId, newStatus) {
  let orders = getStoredData('cieloria_merchant_all_orders', []);
  let target = orders.find(o => o.orderId === orderId);
  let statusColor = 'bg-blue-100 text-blue-800 border-blue-300';

  if (newStatus === 'Dispatched') statusColor = 'bg-blue-100 text-blue-800 border-blue-300';
  if (newStatus === 'In Transit') statusColor = 'bg-indigo-100 text-indigo-800 border-indigo-300';
  if (newStatus === 'Out for Delivery') statusColor = 'bg-amber-100 text-amber-800 border-amber-300';
  if (newStatus === 'Delivered') statusColor = 'bg-emerald-100 text-emerald-800 border-emerald-300';

  if (target) {
    target.status = newStatus;
    target.statusColor = statusColor;
  }

  setStoredData('cieloria_merchant_all_orders', orders);

  try {
    fetch('/api/sync', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        action: 'update_order_status',
        data: { orderId: orderId, newStatus: newStatus, statusColor: statusColor }
      })
    }).catch(e => console.log('Admin Cloud Order Status Write Note:', e));
  } catch(e) {}

  let custOrders = getStoredData('cieloria_orders', []);
  let custTarget = custOrders.find(o => o.orderId === orderId);
  if (custTarget) {
    custTarget.status = newStatus;
    custTarget.statusColor = statusColor;
    setStoredData('cieloria_orders', custOrders);
  }

  adminState.allOrders = orders;
  alert(`✅ Order ${orderId} status updated to '${newStatus}' on Google Cloud DB! Customer will see this live in My Account.`);
  renderApp();
}

function renderAdminView() {
  if (!adminState.isAuthenticated) {
    return `
      <div class="min-h-screen flex items-center justify-center p-4 bg-[#0F172A] text-slate-100">
        <div class="w-full max-w-md bg-slate-900 border border-slate-800 rounded-3xl p-8 shadow-2xl text-center space-y-6">
          <div class="w-16 h-16 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-2xl font-bold flex items-center justify-center mx-auto">
            🔒
          </div>

          <div class="space-y-2">
            <h1 class="font-serif text-2xl font-bold text-white uppercase tracking-wider">CIELORIA STORE ADMIN</h1>
            <p class="text-xs text-slate-400">Enter Merchant Passcode or Merchant Code to access Orders Dashboard.</p>
          </div>

          <form onsubmit="handleAdminLogin(event)" class="space-y-4">
            <input 
              type="password" 
              value="${adminState.passcode}" 
              oninput="adminState.passcode=this.value" 
              placeholder="Enter Merchant Code (e.g. 42961)" 
              required 
              class="w-full bg-slate-800 border border-slate-700 rounded-xl px-4 py-3 text-xs text-white focus:outline-none focus:border-amber-400 font-medium text-center tracking-widest text-lg" 
            />

            <button type="submit" class="w-full bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold py-3.5 rounded-xl text-xs uppercase tracking-wider transition-colors shadow-lg">
              Login to Admin Portal →
            </button>
          </form>

          <div class="text-[10px] text-slate-500 font-mono">
            Merchant ID: 2yyq6ziimeofq998 • Passcode Hint: 42961
          </div>
        </div>
      </div>
    `;
  }

  const orders = (typeof getAllCumulativeOrders === 'function') ? getAllCumulativeOrders() : (adminState.allOrders || []);
  adminState.allOrders = orders;
  const totalRev = orders.reduce((sum, o) => sum + (o.totalAmount || 0), 0);

  return `
    <div class="min-h-screen py-8 text-left bg-[#0F172A] text-slate-100">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-8">
        
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center pb-6 border-b border-slate-800 gap-4">
          <div>
            <div class="flex items-center gap-3">
              <span class="text-3xl">⚙️</span>
              <h1 class="font-serif text-3xl font-bold text-amber-400 uppercase tracking-widest">CIELORIA MERCHANT ADMIN DASHBOARD</h1>
            </div>
            <p class="text-xs text-slate-400 pt-1">Manage Customer Orders, Customer Contact Details & Update Dispatch Status (Merchant ID: 2yyq6ziimeofq998 • Live Cloud API Active)</p>
          </div>

          <div class="flex items-center gap-3">
            <button onclick="adminState.allOrders = getAllCumulativeOrders(); renderApp(); alert('✅ Synced & restored all past customer orders across storage!');" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-md flex items-center gap-1">
              🔄 Sync All Orders
            </button>
            <button onclick="state.viewMode='homepage'; renderApp();" class="bg-slate-800 hover:bg-slate-700 text-white px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              🌐 Visit Storefront
            </button>
            <button onclick="adminState.showAddProductForm = !adminState.showAddProductForm; renderApp();" class="bg-amber-500 hover:bg-amber-600 text-slate-950 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-lg flex items-center gap-1.5">
              ✨ Add New Product
            </button>
            <button onclick="handleAdminLogout()" class="border border-rose-500/40 hover:bg-rose-500/10 text-rose-400 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              Logout
            </button>
          </div>
        </div>

        
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

        <div class="grid grid-cols-1 sm:grid-cols-4 gap-4 text-center">
          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Total Received Orders</span>
            <span class="text-3xl font-bold text-white pt-1 block">${orders.length}</span>
          </div>

          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Total Revenue (₹)</span>
            <span class="text-3xl font-bold text-emerald-400 pt-1 block">₹${totalRev.toLocaleString()}</span>
          </div>

          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Dispatched Orders</span>
            <span class="text-3xl font-bold text-blue-400 pt-1 block">${orders.filter(o => o.status === 'Dispatched' || o.status === 'In Transit' || o.status === 'Out for Delivery' || o.status === 'Delivered').length}</span>
          </div>

          <div class="bg-slate-900 border border-slate-800 p-5 rounded-2xl">
            <span class="text-slate-400 text-[10px] uppercase font-bold block">Delivered Orders</span>
            <span class="text-3xl font-bold text-amber-400 pt-1 block">${orders.filter(o => o.status === 'Delivered').length}</span>
          </div>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 space-y-6 shadow-2xl">
          <div class="flex items-center justify-between">
            <h3 class="font-serif text-2xl font-bold text-white">Customer Orders List (${orders.length})</h3>
            <span class="text-xs text-slate-400 font-medium">Select new status from dropdown to update live tracking for customer!</span>
          </div>

          ${orders.length === 0 ? `
            <div class="text-center py-16 text-slate-500 space-y-3">
              <span class="text-5xl block">📦</span>
              <h4 class="font-bold text-slate-300">No Customer Orders Received Yet</h4>
              <p class="text-xs max-w-sm mx-auto">When customers place orders on www.cieloria.com, their name, mobile number, delivery address, and ordered items will appear here automatically!</p>
            </div>
          ` : `
            <div class="overflow-x-auto pb-6">
              <table class="w-full text-left text-xs text-slate-200">
                <thead class="bg-slate-800 text-slate-400 uppercase text-[10px]">
                  <tr>
                    <th class="p-3.5">Order ID & Date</th>
                    <th class="p-3.5">Customer Name & Phone</th>
                    <th class="p-3.5">Delivery Address</th>
                    <th class="p-3.5">Total Payable</th>
                    <th class="p-3.5">Current Status</th>
                    <th class="p-3.5">Update Order Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-800">
                  ${orders.map(ord => `
                    <tr class="hover:bg-slate-800/50 transition-colors">
                      <td class="p-3.5 font-bold text-white">
                        ${ord.orderId}<br/>
                        <span class="text-[10px] text-slate-400 font-normal">${ord.date}</span>
                      </td>
                      <td class="p-3.5 font-medium text-amber-300">
                        ${ord.customerName || 'Customer'}<br/>
                        <span class="text-[10px] text-slate-400 font-normal">+91 ${ord.customerPhone}</span>
                      </td>
                      <td class="p-3.5 max-w-xs truncate font-medium text-slate-300">
                        ${ord.customerAddress || 'Lucknow, UP'} (Pincode: ${ord.pincode || '226001'})
                      </td>
                      <td class="p-3.5 font-bold text-emerald-400">
                        ₹${(ord.totalAmount || 999).toLocaleString()}.00
                      </td>
                      <td class="p-3.5">
                        <span class="px-3 py-1 rounded-full text-[10px] font-bold ${ord.statusColor || 'bg-blue-900 text-blue-200'} border">
                          ${ord.status}
                        </span>
                      </td>
                      <td class="p-3.5">
                        <select onchange="handleOrderStatusChange('${ord.orderId}', this.value)" class="bg-slate-800 text-white border border-slate-700 rounded-xl p-2.5 text-xs focus:outline-none focus:border-amber-400 cursor-pointer font-semibold">
                          <option value="Order Placed" ${ord.status==='Order Placed'?'selected':''}>1. Order Received (Order Placed)</option>
                          <option value="Dispatched" ${ord.status==='Dispatched'?'selected':''}>2. Dispatched from Lucknow HQ</option>
                          <option value="In Transit" ${ord.status==='In Transit'?'selected':''}>3. In Transit (Bluedart Express)</option>
                          <option value="Out for Delivery" ${ord.status==='Out for Delivery'?'selected':''}>4. Out for Delivery</option>
                          <option value="Delivered" ${ord.status==='Delivered'?'selected':''}>5. Delivered Successfully 🎉</option>
                        </select>
                      </td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          `}
        </div>

      </div>
    </div>
  `;
}
"""

full_js = js + admin_code

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

with open('style.css', 'r', encoding='utf-8') as f:
    css_code = f.read()

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CIELORIA | Demi-Fine Anti-Tarnish Luxury Jewelry</title>
  <meta name="description" content="Shop 100% waterproof, anti-tarnish 18K gold plated demi-fine jewelry at Cieloria. Warm Nude & Champagne Gold luxury collection.">
  <meta name="google-site-verification" content="wl6j0pA_TmjRllzBhmc--7AGpBvcKpCBQ_eSetJd1-I" />
  <!-- CIELORIA Luxury Diamond Icon Favicon -->
  <link rel="icon" type="image/jpeg" href="/favicon.jpg" />
  <link rel="icon" type="image/jpeg" href="data:image/jpeg;base64,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" />
  <link rel="shortcut icon" type="image/jpeg" href="/favicon.jpg" />
  <link rel="apple-touch-icon" href="/favicon.jpg" />

  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    if (window.tailwind) {{
      tailwind.config = {{
        theme: {{
          extend: {{
            colors: {{
              nude: {{
                50: '#FAF8F5',
                100: '#F7F4F0',
                200: '#EBE5DF',
                300: '#D9D0C7',
                900: '#1A1A1A'
              }},
              champagne: {{
                300: '#F4E4BA',
                400: '#E6CA65',
                500: '#C5A059',
                600: '#A38038'
              }}
            }},
            fontFamily: {{
              serif: ['"Cormorant Garamond"', '"Playfair Display"', 'serif'],
              sans: ['"Inter"', '"Montserrat"', 'sans-serif']
            }}
          }}
        }}
      }}
    }}
  </script>

  <!-- Firebase Cloud SDK Integration for Permanent Customer DB -->
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>

  <style>
{css_code}
  </style>
</head>
<body class="bg-white text-[#1A1A1A] font-sans antialiased selection:bg-[#C5A059] selection:text-white min-h-screen flex flex-col justify-between">
  
  <!-- Main Application Container (Instant Direct Render) -->
  <div id="app"></div>

  <!-- Inline Full Application Logic -->
  <script>
{full_js}

    if (typeof renderApp === 'function') {{
      try {{ renderApp(); }} catch(e) {{ console.error(e); }}
    }}
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

os.makedirs('dist', exist_ok=True)
with open('dist/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('dist/app.js', 'w', encoding='utf-8') as f:
    f.write(full_js)

print('Successfully cleaned app.js and generated clean index.html!')
