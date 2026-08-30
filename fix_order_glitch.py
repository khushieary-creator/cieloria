import os

with open('cieloria_app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update getAllCumulativeOrders helper with fallback demo orders merge
old_cumulative_helper = """
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
"""

new_cumulative_helper = """
function getAllCumulativeOrders() {
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
}
"""

js = js.replace(old_cumulative_helper, new_cumulative_helper)

with open('cieloria_app.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('Successfully updated cieloria_app.js with fallback demo orders merge!')
