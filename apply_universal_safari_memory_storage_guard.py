import os, re

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace getStoredData and setStoredData with universal memory-backed storage guard
storage_guard_code = """const memoryStorage = {};

function getStoredData(key, fallback) {
  try {
    if (typeof window === 'undefined' || typeof localStorage === 'undefined') {
      return memoryStorage[key] !== undefined ? memoryStorage[key] : fallback;
    }
    const val = localStorage.getItem(key);
    if (!val || val === 'undefined' || val === 'null' || val === '[object Object]') {
      return memoryStorage[key] !== undefined ? memoryStorage[key] : fallback;
    }
    return JSON.parse(val);
  } catch(e) {
    return memoryStorage[key] !== undefined ? memoryStorage[key] : fallback;
  }
}

function setStoredData(key, val) {
  try {
    memoryStorage[key] = val;
    if (typeof window !== 'undefined' && typeof localStorage !== 'undefined') {
      localStorage.setItem(key, JSON.stringify(val));
    }
  } catch(e) {}
}
"""

js = re.sub(r'function getStoredData\(.*?\}\n\}', storage_guard_code, js, flags=re.DOTALL)

# Wrap getAllCumulativeOrders in bulletproof try-catch for localStorage.length
safe_orders_code = """function getAllCumulativeOrders() {
  let all = [];
  try {
    if (typeof window !== 'undefined' && typeof localStorage !== 'undefined') {
      const len = localStorage.length || 0;
      for (let i = 0; i < len; i++) {
        try {
          let key = localStorage.key(i);
          if (key && key.startsWith('cieloria_orders_')) {
            let items = getStoredData(key, []);
            if (Array.isArray(items)) {
              all.push(...items);
            }
          }
        } catch(e) {}
      }
    }
  } catch(e) {}
  if (Array.isArray(state.ordersList)) {
    all.push(...state.ordersList);
  }
  const uniqueMap = new Map();
  all.forEach(item => {
    if (item && item.id) uniqueMap.set(item.id, item);
  });
  return Array.from(uniqueMap.values());
}"""

js = re.sub(r'function getAllCumulativeOrders\(\) \{.*?return Array\.from\(uniqueMap\.values\(\)\);\n\}', safe_orders_code, js, flags=re.DOTALL)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully applied Universal Safari & Incognito Memory Storage Guard v59000.0.0!')
