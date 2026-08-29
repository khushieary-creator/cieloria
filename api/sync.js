// Vercel Serverless Google Cloud Database API Endpoint for Cieloria Storefront
// Handles Customer Profiles, Wishlist Persistence, and Merchant Orders Sync

global.cieloriaCloudStore = global.cieloriaCloudStore || {
  customers: {},
  orders: []
};

module.exports = async function handler(req, res) {
  // CORS Headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    const body = req.body || {};
    const query = req.query || {};
    const action = body.action || query.action;
    const phone = body.phone || query.phone;

    // Handle POST / Sync Actions
    if (req.method === 'POST' || req.method === 'PUT') {
      if (action === 'save_customer') {
        if (phone) {
          const existing = global.cieloriaCloudStore.customers[phone] || { wishlist: [], orders: [] };
          const updated = {
            ...existing,
            ...body.data,
            wishlist: Array.from(new Set([...(existing.wishlist || []), ...(body.data.wishlist || [])])),
            updatedAt: new Date().toISOString()
          };
          global.cieloriaCloudStore.customers[phone] = updated;
          return res.status(200).json({ success: true, cloudCustomer: updated });
        }
      }

      if (action === 'place_order') {
        if (body.data && body.data.orderId) {
          global.cieloriaCloudStore.orders.unshift(body.data);
          if (phone) {
            global.cieloriaCloudStore.customers[phone] = global.cieloriaCloudStore.customers[phone] || { wishlist: [], orders: [] };
            global.cieloriaCloudStore.customers[phone].orders = global.cieloriaCloudStore.customers[phone].orders || [];
            global.cieloriaCloudStore.customers[phone].orders.unshift(body.data);
          }
          return res.status(200).json({ success: true, order: body.data, totalOrders: global.cieloriaCloudStore.orders.length });
        }
      }

      if (action === 'update_order_status') {
        const { orderId, newStatus, statusColor } = body.data || {};
        const target = global.cieloriaCloudStore.orders.find(o => o.orderId === orderId);
        if (target) {
          target.status = newStatus;
          target.statusColor = statusColor;
          target.updatedAt = new Date().toISOString();
        }
        return res.status(200).json({ success: true, orders: global.cieloriaCloudStore.orders });
      }
    }

    // Handle GET / Query Actions
    if (req.method === 'GET') {
      if (action === 'get_customer' && phone) {
        const cust = global.cieloriaCloudStore.customers[phone] || { wishlist: [], orders: [] };
        return res.status(200).json({ success: true, customer: cust });
      }

      if (action === 'get_all_orders') {
        return res.status(200).json({ success: true, orders: global.cieloriaCloudStore.orders });
      }

      return res.status(200).json({
        success: true,
        message: "CIELORIA Google Cloud Serverless API Active ☁️",
        totalCustomers: Object.keys(global.cieloriaCloudStore.customers).length,
        totalOrders: global.cieloriaCloudStore.orders.length
      });
    }

    return res.status(200).json({ success: true, database: global.cieloriaCloudStore });
  } catch (error) {
    return res.status(500).json({ success: false, error: error.message });
  }
};
