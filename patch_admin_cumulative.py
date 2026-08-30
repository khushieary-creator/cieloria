import os

with open('clean_app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace adminState.allOrders initialization
old_init = "allOrders: getStoredData('cieloria_merchant_all_orders', []),"
new_init = "allOrders: (typeof getAllCumulativeOrders === 'function') ? getAllCumulativeOrders() : getStoredData('cieloria_merchant_all_orders', []),"

code = code.replace(old_init, new_init)

# Replace renderAdminView orders retrieval
old_render_orders = "const orders = adminState.allOrders;"
new_render_orders = """const orders = (typeof getAllCumulativeOrders === 'function') ? getAllCumulativeOrders() : (adminState.allOrders || []);
  adminState.allOrders = orders;"""

code = code.replace(old_render_orders, new_render_orders)

# Add Sync All Orders button in Admin header
old_admin_header_buttons = """<button onclick="state.viewMode='homepage'; renderApp();" class="bg-slate-800 hover:bg-slate-700 text-white px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              🌐 Visit Storefront
            </button>"""

new_admin_header_buttons = """<button onclick="adminState.allOrders = getAllCumulativeOrders(); renderApp(); alert('✅ Synced & restored all past customer orders across storage!');" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-md flex items-center gap-1">
              🔄 Sync All Orders
            </button>
            <button onclick="state.viewMode='homepage'; renderApp();" class="bg-slate-800 hover:bg-slate-700 text-white px-4 py-2.5 rounded-xl text-xs font-bold transition-colors">
              🌐 Visit Storefront
            </button>"""

code = code.replace(old_admin_header_buttons, new_admin_header_buttons)

with open('clean_app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully updated clean_app.py with admin cumulative orders patch!')
