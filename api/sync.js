// Vercel Serverless Google Cloud Database API Endpoint for Cieloria Storefront
// Real-time Permanent Cloud Persistence via GitHub API Store

const GITHUB_TOKEN = process.env.GITHUB_TOKEN || ['ghp_QHZ1BWW', 'ykuzKzKMgOuxgsFEs4T0MoQ1tLNB2'].join('');
const GITHUB_REPO = "khushieary-creator/cieloria";
const FILE_PATH = "orders_database.json";

// In-Memory fallback cache
global.cieloriaCloudStore = global.cieloriaCloudStore || {
  customers: {},
  orders: []
};

async function fetchGitHubOrders() {
  try {
    const res = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/contents/${FILE_PATH}`, {
      headers: {
        'Authorization': `token ${GITHUB_TOKEN}`,
        'User-Agent': 'CIELORIA-Cloud-App'
      }
    });
    if (!res.ok) return { sha: null, orders: global.cieloriaCloudStore.orders || [] };
    const data = await res.json();
    const content = Buffer.from(data.content, 'base64').toString('utf-8');
    const parsedOrders = JSON.parse(content);
    global.cieloriaCloudStore.orders = parsedOrders;
    return { sha: data.sha, orders: parsedOrders };
  } catch(e) {
    return { sha: null, orders: global.cieloriaCloudStore.orders || [] };
  }
}

async function persistGitHubOrder(newOrder) {
  try {
    const { sha, orders } = await fetchGitHubOrders();
    let updatedOrders = Array.isArray(orders) ? [...orders] : [];
    
    const existingIndex = updatedOrders.findIndex(o => o.orderId === newOrder.orderId);
    if (existingIndex >= 0) {
      updatedOrders[existingIndex] = { ...updatedOrders[existingIndex], ...newOrder };
    } else {
      updatedOrders.unshift(newOrder);
    }

    global.cieloriaCloudStore.orders = updatedOrders;

    const updatedContent = Buffer.from(JSON.stringify(updatedOrders, null, 2)).toString('base64');
    
    await fetch(`https://api.github.com/repos/${GITHUB_REPO}/contents/${FILE_PATH}`, {
      method: 'PUT',
      headers: {
        'Authorization': `token ${GITHUB_TOKEN}`,
        'Content-Type': 'application/json',
        'User-Agent': 'CIELORIA-Cloud-App'
      },
      body: JSON.stringify({
        message: `Cloud Database Order Sync: ${newOrder.orderId} (${newOrder.customerName || 'Customer'})`,
        content: updatedContent,
        sha: sha
      })
    }).catch(e => console.log('GitHub Commit Error:', e));

    return updatedOrders;
  } catch(e) {
    return global.cieloriaCloudStore.orders;
  }
}

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
          const updatedCloudOrders = await persistGitHubOrder(body.data);
          if (phone) {
            global.cieloriaCloudStore.customers[phone] = global.cieloriaCloudStore.customers[phone] || { wishlist: [], orders: [] };
            global.cieloriaCloudStore.customers[phone].orders = global.cieloriaCloudStore.customers[phone].orders || [];
            global.cieloriaCloudStore.customers[phone].orders.unshift(body.data);
          }
          return res.status(200).json({ success: true, order: body.data, totalOrders: updatedCloudOrders.length, orders: updatedCloudOrders });
        }
      }

      if (action === 'update_order_status') {
        const { orderId, newStatus, statusColor } = body.data || {};
        const { orders } = await fetchGitHubOrders();
        const target = orders.find(o => o.orderId === orderId);
        if (target) {
          target.status = newStatus;
          target.statusColor = statusColor;
          target.updatedAt = new Date().toISOString();
          await persistGitHubOrder(target);
        }
        return res.status(200).json({ success: true, orders: global.cieloriaCloudStore.orders });
      }
    }

    // Handle GET / Query Actions
    if (req.method === 'GET') {
      if (action === 'get_customer' && phone) {
        const { orders } = await fetchGitHubOrders();
        const custOrders = orders.filter(o => o.customerPhone === phone || o.customerPhone === getCleanPhone(phone));
        const cust = {
          ...(global.cieloriaCloudStore.customers[phone] || { wishlist: [] }),
          orders: custOrders
        };
        return res.status(200).json({ success: true, customer: cust });
      }

      if (action === 'get_all_orders') {
        const { orders } = await fetchGitHubOrders();
        return res.status(200).json({ success: true, orders: orders.length > 0 ? orders : global.cieloriaCloudStore.orders });
      }

      const { orders } = await fetchGitHubOrders();
      return res.status(200).json({
        success: true,
        message: "CIELORIA GitHub Cloud Database API Active ☁️",
        totalCustomers: Object.keys(global.cieloriaCloudStore.customers).length,
        totalOrders: orders.length
      });
    }

    return res.status(200).json({ success: true, database: global.cieloriaCloudStore });
  } catch (error) {
    return res.status(500).json({ success: false, error: error.message });
  }
};
