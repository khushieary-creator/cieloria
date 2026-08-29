import React from 'react';
import { Heart, ShoppingBag, Eye, Star, ShieldCheck, Sparkles } from 'lucide-react';

export default function ProductCard({ 
  product, 
  onQuickView, 
  onAddToCart, 
  isWishlisted, 
  onToggleWishlist 
}) {
  return (
    <div className="group relative bg-[#121722] rounded-2xl border border-white/5 hover:border-[#D4AF37]/40 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl hover:shadow-[#D4AF37]/10 flex flex-col justify-between overflow-hidden">
      
      {/* Top Image Container */}
      <div className="relative aspect-square w-full bg-[#19202E] overflow-hidden">
        <img 
          src={product.image} 
          alt={product.name}
          className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-108"
        />
        
        {/* Badges */}
        <div className="absolute top-3 left-3 flex flex-col gap-1 z-10">
          {product.isBestseller && (
            <span className="bg-[#D4AF37] text-[#0A0D12] text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md shadow">
              BESTSELLER
            </span>
          )}
          {product.isNew && (
            <span className="bg-rose-500 text-white text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md shadow">
              NEW LAUNCH
            </span>
          )}
          <span className="bg-[#0A0D12]/80 backdrop-blur-md text-[#E6CA65] border border-[#D4AF37]/30 text-[10px] font-semibold px-2 py-0.5 rounded-md">
            {product.metal}
          </span>
        </div>

        {/* Wishlist Button */}
        <button 
          onClick={() => onToggleWishlist(product.id)}
          className={`absolute top-3 right-3 p-2 rounded-full backdrop-blur-md border transition-all z-10 ${
            isWishlisted 
              ? 'bg-rose-500/20 border-rose-500 text-rose-500' 
              : 'bg-[#0A0D12]/60 border-white/10 text-slate-300 hover:text-white'
          }`}
          title="Add to Wishlist"
        >
          <Heart size={16} fill={isWishlisted ? 'currentColor' : 'none'} />
        </button>

        {/* Quick Actions Hover Overlay */}
        <div className="absolute inset-0 bg-gradient-to-t from-[#0A0D12] via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end justify-center p-4 gap-2">
          <button 
            onClick={() => onQuickView(product)}
            className="flex-1 bg-white/10 hover:bg-white/20 backdrop-blur-md text-white text-xs font-semibold py-2.5 rounded-xl border border-white/20 transition-colors flex items-center justify-center gap-1.5"
          >
            <Eye size={14} />
            <span>Quick View</span>
          </button>
          <button 
            onClick={() => onAddToCart(product)}
            className="bg-[#D4AF37] hover:bg-[#E6CA65] text-[#0A0D12] text-xs font-bold p-2.5 rounded-xl shadow-lg transition-transform hover:scale-105"
            title="Add to Bag"
          >
            <ShoppingBag size={16} />
          </button>
        </div>
      </div>

      {/* Bottom Product Details */}
      <div className="p-4 space-y-2 text-left">
        {/* Rating & COD badge */}
        <div className="flex items-center justify-between text-xs text-slate-400">
          <div className="flex items-center gap-1 text-[#E6CA65]">
            <Star size={12} fill="currentColor" />
            <span className="font-bold text-white text-xs">{product.rating}</span>
            <span className="text-[11px] text-slate-400">({product.reviewCount})</span>
          </div>
          <span className="text-[10px] text-emerald-400 font-semibold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
            COD Eligible
          </span>
        </div>

        {/* Title */}
        <h3 
          onClick={() => onQuickView(product)}
          className="font-serif text-base font-bold text-white group-hover:text-[#E6CA65] transition-colors cursor-pointer line-clamp-1"
        >
          {product.name}
        </h3>

        {/* Anti-Tarnish Feature Pill */}
        <div className="flex items-center gap-1 text-[11px] text-[#E6CA65]">
          <ShieldCheck size={12} />
          <span>100% Anti-Tarnish & Waterproof</span>
        </div>

        {/* Price & Buy Button */}
        <div className="pt-2 border-t border-white/5 flex items-center justify-between">
          <div>
            <span className="text-xs text-slate-400 line-through mr-2">₹{product.originalPrice}</span>
            <span className="font-bold text-lg text-white">₹{product.price}</span>
            <span className="text-[10px] text-emerald-400 font-bold ml-1.5">{product.discountPercent}% OFF</span>
          </div>
          
          <button 
            onClick={() => onAddToCart(product)}
            className="text-xs text-[#E6CA65] hover:text-white font-bold tracking-wide transition-colors uppercase border-b border-[#D4AF37]/50 hover:border-white py-0.5"
          >
            + Add to Bag
          </button>
        </div>
      </div>

    </div>
  );
}
