import React, { useState } from 'react';
import { ShoppingBag, Heart, Search, Truck, ShieldCheck, Sparkles, X, Menu } from 'lucide-react';

export default function Navbar({ 
  cartCount, 
  wishlistCount, 
  onOpenCart, 
  onOpenTracker, 
  searchTerm, 
  setSearchTerm,
  selectedCategory,
  setSelectedCategory
}) {
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="sticky top-0 z-40 w-full border-b border-white/10 bg-[#0A0D12]/90 backdrop-blur-md">
      {/* Top Announcement Ticker Bar */}
      <div className="bg-gradient-to-r from-[#19202E] via-[#D4AF37]/20 to-[#19202E] text-xs py-2 px-4 text-center border-b border-[#D4AF37]/20 flex items-center justify-between">
        <div className="hidden md:flex items-center gap-2 text-[#E6CA65] font-medium">
          <ShieldCheck size={14} /> 100% Anti-Tarnish & Waterproof Guarantee
        </div>
        <div className="w-full md:w-auto text-center font-medium text-slate-200 tracking-wide">
          ✨ Use Code <span className="text-[#E6CA65] font-bold">CIELORIA10</span> for Extra 10% OFF | Free Express Shipping & COD Available
        </div>
        <div className="hidden md:flex items-center gap-2 text-[#E6CA65] font-medium">
          <Truck size={14} /> Shiprocket Express Delivery
        </div>
      </div>

      {/* Main Navigation Bar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between gap-4">
        {/* Mobile Menu Toggle */}
        <button 
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          className="md:hidden text-slate-300 hover:text-white p-2"
        >
          <Menu size={24} />
        </button>

        {/* Brand Logo */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-full bg-gradient-to-tr from-[#D4AF37] to-[#FFF0B8] flex items-center justify-center text-[#0A0D12] font-serif font-bold text-xl shadow-lg shadow-[#D4AF37]/20">
            C
          </div>
          <div>
            <a href="#" className="font-serif text-2xl md:text-3xl font-bold tracking-widest text-white hover:text-[#E6CA65] transition-colors">
              CIELORIA
            </a>
            <span className="block text-[9px] tracking-[0.3em] text-[#D4AF37] font-semibold uppercase -mt-1">
              Demi-Fine Luxury
            </span>
          </div>
        </div>

        {/* Desktop Nav Links */}
        <nav className="hidden md:flex items-center gap-8 text-sm font-medium text-slate-300">
          <button 
            onClick={() => setSelectedCategory('All')} 
            className={`transition-colors hover:text-[#E6CA65] ${selectedCategory === 'All' ? 'text-[#E6CA65] font-semibold border-b border-[#D4AF37]' : ''}`}
          >
            All Collections
          </button>
          <button 
            onClick={() => setSelectedCategory('Rings')} 
            className={`transition-colors hover:text-[#E6CA65] ${selectedCategory === 'Rings' ? 'text-[#E6CA65] font-semibold border-b border-[#D4AF37]' : ''}`}
          >
            Rings
          </button>
          <button 
            onClick={() => setSelectedCategory('Necklaces')} 
            className={`transition-colors hover:text-[#E6CA65] ${selectedCategory === 'Necklaces' ? 'text-[#E6CA65] font-semibold border-b border-[#D4AF37]' : ''}`}
          >
            Necklaces
          </button>
          <button 
            onClick={() => setSelectedCategory('Earrings')} 
            className={`transition-colors hover:text-[#E6CA65] ${selectedCategory === 'Earrings' ? 'text-[#E6CA65] font-semibold border-b border-[#D4AF37]' : ''}`}
          >
            Earrings
          </button>
          <button 
            onClick={() => setSelectedCategory('Bracelets')} 
            className={`transition-colors hover:text-[#E6CA65] ${selectedCategory === 'Bracelets' ? 'text-[#E6CA65] font-semibold border-b border-[#D4AF37]' : ''}`}
          >
            Bracelets
          </button>
        </nav>

        {/* Action Buttons */}
        <div className="flex items-center gap-3">
          {/* Search Trigger */}
          <div className="relative">
            {isSearchOpen ? (
              <div className="flex items-center bg-[#19202E] border border-[#D4AF37]/40 rounded-full px-3 py-1.5 w-48 sm:w-64">
                <Search size={16} className="text-[#D4AF37] mr-2" />
                <input 
                  type="text" 
                  placeholder="Search jewelry..." 
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="bg-transparent text-xs text-white placeholder-slate-400 focus:outline-none w-full"
                  autoFocus
                />
                <button onClick={() => { setIsSearchOpen(false); setSearchTerm(''); }} className="text-slate-400 hover:text-white ml-1">
                  <X size={14} />
                </button>
              </div>
            ) : (
              <button 
                onClick={() => setIsSearchOpen(true)}
                className="p-2 text-slate-300 hover:text-[#E6CA65] transition-colors rounded-full hover:bg-white/5"
                title="Search Products"
              >
                <Search size={20} />
              </button>
            )}
          </div>

          {/* Track Order Button */}
          <button 
            onClick={onOpenTracker}
            className="hidden sm:flex items-center gap-1.5 text-xs text-[#E6CA65] hover:text-white bg-[#19202E] border border-[#D4AF37]/30 hover:border-[#D4AF37] px-3 py-1.5 rounded-full transition-all"
            title="Track Order Status"
          >
            <Truck size={14} />
            <span>Track Order</span>
          </button>

          {/* Wishlist */}
          <button 
            className="relative p-2 text-slate-300 hover:text-rose-400 transition-colors rounded-full hover:bg-white/5"
            title="Wishlist"
          >
            <Heart size={20} />
            {wishlistCount > 0 && (
              <span className="absolute top-0 right-0 w-4 h-4 bg-rose-500 text-white font-bold text-[10px] rounded-full flex items-center justify-center">
                {wishlistCount}
              </span>
            )}
          </button>

          {/* Cart Drawer Toggle */}
          <button 
            onClick={onOpenCart}
            className="relative p-2.5 bg-gradient-to-r from-[#D4AF37] to-[#B89018] text-[#0A0D12] rounded-full font-bold transition-transform hover:scale-105 shadow-md shadow-[#D4AF37]/20 flex items-center gap-2 px-4"
          >
            <ShoppingBag size={18} />
            <span className="hidden sm:inline text-xs">Bag</span>
            <span className="w-5 h-5 bg-[#0A0D12] text-[#E6CA65] rounded-full text-[11px] flex items-center justify-center font-bold">
              {cartCount}
            </span>
          </button>
        </div>
      </div>

      {/* Mobile Drawer Menu */}
      {mobileMenuOpen && (
        <div className="md:hidden border-t border-white/10 bg-[#121722] p-4 flex flex-col gap-3 text-slate-200 text-sm">
          {['All', 'Rings', 'Necklaces', 'Earrings', 'Bracelets'].map((cat) => (
            <button 
              key={cat}
              onClick={() => { setSelectedCategory(cat); setMobileMenuOpen(false); }}
              className={`text-left py-2 px-3 rounded-lg ${selectedCategory === cat ? 'bg-[#D4AF37]/20 text-[#E6CA65] font-bold' : 'hover:bg-white/5'}`}
            >
              {cat === 'All' ? '✨ All Collections' : cat}
            </button>
          ))}
          <button 
            onClick={() => { onOpenTracker(); setMobileMenuOpen(false); }}
            className="flex items-center gap-2 py-2 px-3 text-[#E6CA65] bg-[#19202E] rounded-lg border border-[#D4AF37]/30"
          >
            <Truck size={16} /> Track Shiprocket Order
          </button>
        </div>
      )}
    </header>
  );
}
