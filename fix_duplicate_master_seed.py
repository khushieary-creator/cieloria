import os, re, json

with open('orders_database.json', 'r', encoding='utf-8') as f:
    orders = json.load(f)

orders_json_str = json.dumps(orders)

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Remove all existing MASTER_SEED_ORDERS declarations from cieloria_app.js
js = re.sub(r'const MASTER_SEED_ORDERS\s*=\s*\[.*?\];\s*', '', js, flags=re.DOTALL)

# 2. Add single MASTER_SEED_ORDERS declaration right above getAllCumulativeOrders
target_getAll = "function getAllCumulativeOrders() {"
replacement_getAll = f"const MASTER_SEED_ORDERS = {orders_json_str};\n\nfunction getAllCumulativeOrders() {{"

js = js.replace(target_getAll, replacement_getAll, 1)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Clean clean_app.py to remove any duplicate MASTER_SEED_ORDERS
with open('clean_app.py', 'r', encoding='utf-8') as f:
    clean_code = f.read()

clean_code = re.sub(r'const MASTER_SEED_ORDERS\s*=\s*\[.*?\];\s*', '', clean_code, flags=re.DOTALL)

with open('clean_app.py', 'w', encoding='utf-8') as f:
    f.write(clean_code)

print('Successfully cleaned duplicate MASTER_SEED_ORDERS declarations!')
