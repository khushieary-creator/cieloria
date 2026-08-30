import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update getAllCumulativeOrders to fetch orders_database.json
old_func = """function getAllCumulativeOrders() {
  let allOrdersMap = new Map();

  const defaultDemoOrders = [
    {
      orderId: "CIE-84920",
      date: "28 Aug 2026",
      status: "Dispatched",
      statusColor: "bg-blue-100 text-blue-800 border-blue-300",
      courier: "Bluedart Express",
      trackingId: "BLU89230149",
      estimatedDelivery: "Tomorrow by 5 PM",
      totalAmount: 2499,
      customerName: "Khushi",
      customerPhone: "9876543210",
      customerAddress: "Hazratganj, Lucknow, UP",
      pincode: "226001",
      items: [PRODUCTS[0], PRODUCTS[1] || PRODUCTS[0]]
    },
    {
      orderId: "CIE-73912",
      date: "25 Aug 2026",
      status: "Delivered",
      statusColor: "bg-emerald-100 text-emerald-800 border-emerald-300",
      courier: "Bluedart Express",
      trackingId: "BLU74829103",
      estimatedDelivery: "Delivered",
      totalAmount: 1899,
      customerName: "Khushi",
      customerPhone: "9876543210",
      customerAddress: "Hazratganj, Lucknow, UP",
      pincode: "226001",
      items: [PRODUCTS[2] || PRODUCTS[0]]
    }
  ];

  // 1. Read Master Permanent Order Key
  let masterOrders = getStoredData('cieloria_master_permanent_orders_v1', []);
  if (Array.isArray(masterOrders) && masterOrders.length > 0) {
    masterOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 2. Read Merchant Orders
  let merchantOrders = getStoredData('cieloria_merchant_all_orders', []);
  if (Array.isArray(merchantOrders) && merchantOrders.length > 0) {
    merchantOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 3. Read Guest Orders
  let guestOrders = getStoredData('cieloria_orders_guest', []);
  if (Array.isArray(guestOrders) && guestOrders.length > 0) {
    guestOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 4. Read State Memory Orders
  if (Array.isArray(state.ordersList) && state.ordersList.length > 0) {
    state.ordersList.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 5. Scan all cieloria_orders_* keys
  try {
    for (let i = 0; i < localStorage.length; i++) {
      let key = localStorage.key(i);
      if (key && key.startsWith('cieloria_orders_')) {
        let list = getStoredData(key, []);
        if (Array.isArray(list) && list.length > 0) {
          list.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
        }
      }
    }
  } catch(e) {}

  // 6. Merge Demo Orders if empty
  defaultDemoOrders.forEach(d => {
    if (!allOrdersMap.has(d.orderId)) {
      allOrdersMap.set(d.orderId, d);
    }
  });

  const finalMergedList = Array.from(allOrdersMap.values());
  setStoredData('cieloria_master_permanent_orders_v1', finalMergedList);
  return finalMergedList;
}"""

new_func = """// Live Master Database Fetch & Multi-Customer Phone Order Aggregator
(function initMasterDatabaseFetch() {
  try {
    fetch('/orders_database.json')
      .then(res => res.json())
      .then(dbOrders => {
        if (dbOrders && Array.isArray(dbOrders) && dbOrders.length > 0) {
          let currentMaster = getStoredData('cieloria_master_permanent_orders_v1', []);
          let masterMap = new Map();
          dbOrders.forEach(o => { if (o && o.orderId) masterMap.set(o.orderId, o); });
          currentMaster.forEach(o => { if (o && o.orderId) masterMap.set(o.orderId, o); });
          const merged = Array.from(masterMap.values());
          setStoredData('cieloria_master_permanent_orders_v1', merged);
          setStoredData('cieloria_merchant_all_orders', merged);
        }
      }).catch(e => {});
  } catch(e) {}
})();

function getAllCumulativeOrders() {
  let allOrdersMap = new Map();

  // 1. Read Master Permanent Order Key
  let masterOrders = getStoredData('cieloria_master_permanent_orders_v1', []);
  if (Array.isArray(masterOrders) && masterOrders.length > 0) {
    masterOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 2. Read Merchant Orders
  let merchantOrders = getStoredData('cieloria_merchant_all_orders', []);
  if (Array.isArray(merchantOrders) && merchantOrders.length > 0) {
    merchantOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 3. Read Guest Orders
  let guestOrders = getStoredData('cieloria_orders_guest', []);
  if (Array.isArray(guestOrders) && guestOrders.length > 0) {
    guestOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 4. Read State Memory Orders
  if (Array.isArray(state.ordersList) && state.ordersList.length > 0) {
    state.ordersList.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  // 5. Scan all cieloria_orders_* keys across all customer phones
  try {
    for (let i = 0; i < localStorage.length; i++) {
      let key = localStorage.key(i);
      if (key && key.startsWith('cieloria_orders_')) {
        let list = getStoredData(key, []);
        if (Array.isArray(list) && list.length > 0) {
          list.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
        }
      }
    }
  } catch(e) {}

  const finalMergedList = Array.from(allOrdersMap.values());
  setStoredData('cieloria_master_permanent_orders_v1', finalMergedList);
  return finalMergedList;
}"""

js = js.replace(old_func, new_func)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully integrated orders_database.json fetch into cieloria_app.js!')
