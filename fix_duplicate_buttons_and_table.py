import os

with open('clean_app.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the 3 duplicate Add New Product buttons with EXACTLY ONE button
old_buttons = """<button onclick="adminState.showAddProductForm = !adminState.showAddProductForm; renderApp();" class="bg-amber-500 hover:bg-amber-600 text-slate-950 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-lg flex items-center gap-1.5">
              ✨ Add New Product
            </button>
            <button onclick="adminState.showAddProductForm = !adminState.showAddProductForm; renderApp();" class="bg-amber-500 hover:bg-amber-600 text-slate-950 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-lg flex items-center gap-1.5">
              ✨ Add New Product
            </button>
            <button onclick="adminState.showAddProductForm = !adminState.showAddProductForm; renderApp();" class="bg-amber-500 hover:bg-amber-600 text-slate-950 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-lg flex items-center gap-1.5">
              ✨ Add New Product
            </button>"""

new_buttons = """<button onclick="adminState.showAddProductForm = !adminState.showAddProductForm; renderApp();" class="bg-amber-500 hover:bg-amber-600 text-slate-950 px-4 py-2.5 rounded-xl text-xs font-bold transition-colors shadow-lg flex items-center gap-1.5">
              ✨ Add New Product
            </button>"""

code = code.replace(old_buttons, new_buttons)

# Expand container padding & remove table clipping
old_table_container = '<div class="overflow-x-auto">'
new_table_container = '<div class="overflow-x-auto pb-6">'

code = code.replace(old_table_container, new_table_container)

with open('clean_app.py', 'w', encoding='utf-8') as f:
    f.write(code)

print('Successfully fixed duplicate buttons and expanded table container!')
