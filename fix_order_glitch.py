import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add getAllCumulativeOrders helper
cumulative_helper = """
function getAllCumulativeOrders() {
  let allOrdersMap = new Map();

  let merchantOrders = getStoredData('cieloria_merchant_all_orders', []);
  if (Array.isArray(merchantOrders)) {
    merchantOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  let guestOrders = getStoredData('cieloria_orders_guest', []);
  if (Array.isArray(guestOrders)) {
    guestOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  if (Array.isArray(state.ordersList)) {
    state.ordersList.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  try {
    for (let i = 0; i < localStorage.length; i++) {
      let key = localStorage.key(i);
      if (key && key.startsWith('cieloria_orders_')) {
        let list = getStoredData(key, []);
        if (Array.isArray(list)) {
          list.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
        }
      }
    }
  } catch(e) {}

  return Array.from(allOrdersMap.values());
}

// Live Google Cloud Database & Multi-Source Account Syncing
"""

js = js.replace("// Live Google Cloud Database & Multi-Source Account Syncing", cumulative_helper)

# 2. Replace syncAccountStorage order loading
old_sync_orders = "state.ordersList = getStoredData(oKey, []);"
new_sync_orders = """const cumulativeOrders = getAllCumulativeOrders();
  state.ordersList = cumulativeOrders;
  state.merchantAllOrders = cumulativeOrders;"""

js = js.replace(old_sync_orders, new_sync_orders)

# 3. Fix completeUserOrder order saving logic
old_complete_save = """  state.ordersList.unshift(newOrder);
  state.merchantAllOrders.unshift(newOrder);

  if (cleanPh) {
    setStoredData(`cieloria_orders_${cleanPh}`, state.ordersList);
  }
  setStoredData('cieloria_merchant_all_orders', state.merchantAllOrders);"""

new_complete_save = """  // Read all existing cumulative orders across all storage keys
  let existingCumulative = getAllCumulativeOrders();
  
  // Deduplicate by orderId ensuring newOrder is at top
  let mergedMap = new Map();
  mergedMap.set(newOrder.orderId, newOrder);
  existingCumulative.forEach(o => {
    if (o && o.orderId && !mergedMap.has(o.orderId)) {
      mergedMap.set(o.orderId, o);
    }
  });

  const finalCumulativeList = Array.from(mergedMap.values());

  state.ordersList = finalCumulativeList;
  state.merchantAllOrders = finalCumulativeList;
  if (typeof adminState !== 'undefined') {
    adminState.allOrders = finalCumulativeList;
  }

  // Save cumulative list to ALL storage keys so past orders are never lost
  setStoredData('cieloria_merchant_all_orders', finalCumulativeList);
  setStoredData('cieloria_orders_guest', finalCumulativeList);
  if (cleanPh) {
    setStoredData(`cieloria_orders_${cleanPh}`, finalCumulativeList);
  }"""

js = js.replace(old_complete_save, new_complete_save)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully patched cieloria_app.js with cumulative order retention!')
