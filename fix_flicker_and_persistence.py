import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update getAllCumulativeOrders to read and update cieloria_master_permanent_orders_v1
old_cumulative_func = """function getAllCumulativeOrders() {
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

  let merchantOrders = getStoredData('cieloria_merchant_all_orders', []);
  if (Array.isArray(merchantOrders) && merchantOrders.length > 0) {
    merchantOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  let guestOrders = getStoredData('cieloria_orders_guest', []);
  if (Array.isArray(guestOrders) && guestOrders.length > 0) {
    guestOrders.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

  if (Array.isArray(state.ordersList) && state.ordersList.length > 0) {
    state.ordersList.forEach(o => { if (o && o.orderId) allOrdersMap.set(o.orderId, o); });
  }

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

  defaultDemoOrders.forEach(d => {
    if (!allOrdersMap.has(d.orderId)) {
      allOrdersMap.set(d.orderId, d);
    }
  });

  return Array.from(allOrdersMap.values());
}"""

new_cumulative_func = """function getAllCumulativeOrders() {
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

js = js.replace(old_cumulative_func, new_cumulative_func)

# 2. Fix syncAccountStorage cloud fetch overwrite (Line 3237)
old_cloud_sync_overwrite = "state.ordersList = res.customer.orders;\n            setStoredData(oKey, res.customer.orders);"
new_cloud_sync_merge = """let masterMap = new Map();
            getAllCumulativeOrders().forEach(o => { if (o && o.orderId) masterMap.set(o.orderId, o); });
            res.customer.orders.forEach(co => {
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
            const mergedOrders = Array.from(masterMap.values());
            state.ordersList = mergedOrders;
            setStoredData('cieloria_master_permanent_orders_v1', mergedOrders);
            setStoredData(oKey, mergedOrders);
            setStoredData('cieloria_merchant_all_orders', mergedOrders);"""

js = js.replace(old_cloud_sync_overwrite, new_cloud_sync_merge)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Also update fetchCloudOrders in clean_app.py
with open('clean_app.py', 'r', encoding='utf-8') as f:
    clean_code = f.read()

old_fetch_cloud_func = """function fetchCloudOrders() {
  fetch('/api/sync?action=get_all_orders')
    .then(res => res.json())
    .then(data => {
      if (data && data.orders && Array.isArray(data.orders) && data.orders.length > 0) {
        adminState.allOrders = data.orders;
        setStoredData('cieloria_merchant_all_orders', data.orders);
        if (adminState.isAuthenticated && state.viewMode === 'admin') renderApp();
      }
    }).catch(e => console.log('Admin Cloud Fetch Note:', e));
}"""

new_fetch_cloud_func = """function fetchCloudOrders() {
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
}"""

clean_code = clean_code.replace(old_fetch_cloud_func, new_fetch_cloud_func)

with open('clean_app.py', 'w', encoding='utf-8') as f:
    f.write(clean_code)

print('Successfully applied permanent master persistence and flicker elimination!')
