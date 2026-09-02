import os

# Clean Vercel Rewrites Configuration (Modern Vercel Standard)
vercel_config = """{
  "rewrites": [
    {
      "source": "/category/:slug*",
      "destination": "/index.html"
    },
    {
      "source": "/product/:id*",
      "destination": "/index.html"
    },
    {
      "source": "/about",
      "destination": "/index.html"
    },
    {
      "source": "/account",
      "destination": "/index.html"
    },
    {
      "source": "/wishlist",
      "destination": "/index.html"
    },
    {
      "source": "/order-confirmed",
      "destination": "/index.html"
    }
  ]
}
"""

with open('vercel.json', 'w', encoding='utf-8') as f:
    f.write(vercel_config)

print('Successfully updated vercel.json with clean rewrites!')
