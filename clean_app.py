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


function fetchCloudOrders() {
  fetch('/api/sync?action=get_all_orders')
    .then(res => res.json())
    .then(data => {
      if (data && data.orders && Array.isArray(data.orders) && data.orders.length > 0) {
        adminState.allOrders = data.orders;
        setStoredData('cieloria_merchant_all_orders', data.orders);
        if (adminState.isAuthenticated && state.viewMode === 'admin') renderApp();
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

  const orders = adminState.allOrders;
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
            <button onclick="state.viewMode='homepage'; renderApp();" class="bg-slate-800 hover:bg-slate-700 text-white px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              🌐 Visit Storefront
            </button>
            <button onclick="adminState.showAddProductForm = !adminState.showAddProductForm; renderApp();" class="bg-amber-500 hover:bg-amber-600 text-slate-950 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-lg flex items-center gap-1.5">
              ✨ Add New Product
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
            <div class="overflow-x-auto">
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
