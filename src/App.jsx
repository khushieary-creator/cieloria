import React, { useState } from 'react';
import Navbar from './components/Navbar';
import HeroBanner from './components/HeroBanner';
import AntiTarnishBadge from './components/AntiTarnishBadge';
import ProductCard from './components/ProductCard';
import ProductQuickViewModal from './components/ProductQuickViewModal';
import CartDrawer from './components/CartDrawer';
import CheckoutModal from './components/CheckoutModal';
import ShiprocketTrackerModal from './components/ShiprocketTrackerModal';
import Footer from './components/Footer';
import { PRODUCTS, CATEGORIES } from './data/products';
import { Sparkles, SlidersHorizontal, ArrowUpDown, Check } from 'lucide-react';

export default function App() {
  const [cartItems, setCartItems] = useState([
    { ...PRODUCTS[0], quantity: 1 } // Default sample item in bag
  ]);
  const [wishlist, setWishlist] = useState(['ring-101']);
  const [selectedCategory, setSelectedCategory] = useState('All');
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [isCartOpen, setIsCartOpen] = useState(false);
  const [isCheckoutOpen, setIsCheckoutOpen] = useState(false);
  const [isTrackerOpen, setIsTrackerOpen] = useState(false);
  const [sortBy, setSortBy] = useState('featured');

  // Filter & Sort Logic
  const filteredProducts = PRODUCTS.filter((item) => {
    const matchesCategory = selectedCategory === 'All' || item.category === selectedCategory;
    const matchesSearch = item.name.toLowerCase().includes(searchTerm.toLowerCase()) || 
                          item.description.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesCategory && matchesSearch;
  }).sort((a, b) => {
    if (sortBy === 'price-low') return a.price - b.price;
    if (sortBy === 'price-high') return b.price - a.price;
    if (sortBy === 'rating') return b.rating - a.rating;
    return 0;
  });

  // Cart Operations
  const handleAddToCart = (product) => {
    setCartItems((prev) => {
      const existing = prev.find((item) => item.id === product.id);
      if (existing) {
        return prev.map((item) =>
          item.id === product.id ? { ...item, quantity: item.quantity + 1 } : item
        );
      }
      return [...prev, { ...product, quantity: 1 }];
    });
    setIsCartOpen(true);
  };

  const handleUpdateQuantity = (id, newQty) => {
    if (newQty <= 0) {
      handleRemoveItem(id);
      return;
    }
    setCartItems((prev) =>
      prev.map((item) => (item.id === id ? { ...item, quantity: newQty } : item))
    );
  };

  const handleRemoveItem = (id) => {
    setCartItems((prev) => prev.filter((item) => item.id !== id));
  };

  const handleToggleWishlist = (id) => {
    setWishlist((prev) =>
      prev.includes(id) ? prev.filter((wId) => wId !== id) : [...prev, id]
    );
  };

  const handleBuyNow = (product) => {
    handleAddToCart(product);
    setIsCartOpen(false);
    setIsCheckoutOpen(true);
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#0A0D12] text-slate-100 font-sans selection:bg-[#D4AF37] selection:text-[#0A0D12]">
      
      {/* Navigation Header */}
      <Navbar 
        cartCount={cartItems.reduce((acc, item) => acc + item.quantity, 0)}
        wishlistCount={wishlist.length}
        onOpenCart={() => setIsCartOpen(true)}
        onOpenTracker={() => setIsTrackerOpen(true)}
        searchTerm={searchTerm}
        setSearchTerm={setSearchTerm}
        selectedCategory={selectedCategory}
        setSelectedCategory={setSelectedCategory}
      />

      {/* Main Content */}
      <main className="flex-1">
        
        {/* Hero Section */}
        <HeroBanner />

        {/* Anti-Tarnish Feature Matrix */}
        <AntiTarnishBadge />

        {/* Products Section */}
        <section id="products-section" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-8">
          
          {/* Section Heading & Controls */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-white/10 pb-6 text-left">
            <div>
              <div className="flex items-center gap-2 text-xs uppercase tracking-widest text-[#D4AF37] font-semibold">
                <Sparkles size={14} /> Palmonas Style Demi-Fine Store
              </div>
              <h2 className="font-serif text-3xl sm:text-4xl font-bold text-white mt-1">
                Anti-Tarnish Jewelry Collection
              </h2>
            </div>

            {/* Controls: Category Pills & Sort */}
            <div className="flex flex-wrap items-center gap-3">
              {CATEGORIES.map((cat) => (
                <button
                  key={cat}
                  onClick={() => setSelectedCategory(cat)}
                  className={`px-4 py-2 rounded-full text-xs font-semibold transition-all ${
                    selectedCategory === cat
                      ? 'bg-gradient-to-r from-[#D4AF37] to-[#B89018] text-[#0A0D12] shadow-md shadow-[#D4AF37]/20 font-bold'
                      : 'bg-[#121722] text-slate-300 hover:text-white border border-white/10 hover:border-[#D4AF37]/40'
                  }`}
                >
                  {cat === 'All' ? '✨ All' : cat}
                </button>
              ))}

              {/* Sort Selector */}
              <div className="relative inline-flex items-center bg-[#121722] border border-white/10 rounded-full px-3 py-1.5 text-xs text-slate-300">
                <ArrowUpDown size={14} className="text-[#D4AF37] mr-1.5" />
                <select 
                  value={sortBy}
                  onChange={(e) => setSortBy(e.target.value)}
                  className="bg-transparent text-xs text-slate-200 focus:outline-none cursor-pointer pr-2"
                >
                  <option value="featured" className="bg-[#121722]">Sort: Featured</option>
                  <option value="price-low" className="bg-[#121722]">Price: Low to High</option>
                  <option value="price-high" className="bg-[#121722]">Price: High to Low</option>
                  <option value="rating" className="bg-[#121722]">Highest Rated</option>
                </select>
              </div>
            </div>
          </div>

          {/* Search Result Banner */}
          {searchTerm && (
            <div className="text-xs text-slate-300 bg-[#121722] p-3 rounded-xl border border-[#D4AF37]/30 flex items-center justify-between">
              <span>Showing results for "<strong className="text-[#E6CA65]">{searchTerm}</strong>" ({filteredProducts.length} items)</span>
              <button onClick={() => setSearchTerm('')} className="text-slate-400 hover:text-white underline">
                Clear Search
              </button>
            </div>
          )}

          {/* Product Cards Grid */}
          {filteredProducts.length === 0 ? (
            <div className="text-center py-20 bg-[#121722] rounded-3xl border border-white/5 space-y-3">
              <p className="text-lg font-serif font-bold text-white">No jewelry found matching your filter</p>
              <button 
                onClick={() => { setSelectedCategory('All'); setSearchTerm(''); }}
                className="btn-gold text-xs py-2 px-4"
              >
                Reset Filters
              </button>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8">
              {filteredProducts.map((product) => (
                <ProductCard 
                  key={product.id}
                  product={product}
                  onQuickView={setSelectedProduct}
                  onAddToCart={handleAddToCart}
                  isWishlisted={wishlist.includes(product.id)}
                  onToggleWishlist={handleToggleWishlist}
                />
              ))}
            </div>
          )}

        </section>

      </main>

      {/* Quick View Modal */}
      <ProductQuickViewModal 
        product={selectedProduct}
        onClose={() => setSelectedProduct(null)}
        onAddToCart={handleAddToCart}
        onBuyNow={handleBuyNow}
      />

      {/* Cart Slide-Over Drawer */}
      <CartDrawer 
        isOpen={isCartOpen}
        onClose={() => setIsCartOpen(false)}
        cartItems={cartItems}
        onUpdateQuantity={handleUpdateQuantity}
        onRemoveItem={handleRemoveItem}
        onProceedToCheckout={() => setIsCheckoutOpen(true)}
      />

      {/* Checkout Modal (Task 1.1) */}
      <CheckoutModal 
        isOpen={isCheckoutOpen}
        onClose={() => setIsCheckoutOpen(false)}
        cartItems={cartItems}
        onOrderPlaced={() => setCartItems([])}
      />

      {/* Shiprocket Tracker Modal */}
      <ShiprocketTrackerModal 
        isOpen={isTrackerOpen}
        onClose={() => setIsTrackerOpen(false)}
      />

      {/* Footer */}
      <Footer />

    </div>
  );
}
