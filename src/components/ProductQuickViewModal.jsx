import React, { useState } from 'react';
import { X, Star, ShieldCheck, Droplets, MapPin, Truck, Check, ShoppingBag, Zap } from 'lucide-react';
import { PINCODES } from '../data/products';

export default function ProductQuickViewModal({ product, onClose, onAddToCart, onBuyNow }) {
  const [pincode, setPincode] = useState('');
  const [pincodeStatus, setPincodeStatus] = useState(null);

  if (!product) return null;

  const handlePincodeCheck = (e) => {
    e.preventDefault();
    if (!pincode.trim()) return;
    const lookup = PINCODES[pincode.trim()];
    if (lookup) {
      setPincodeStatus({ verified: true, ...lookup });
    } else {
      setPincodeStatus({ 
        verified: true, 
        location: 'Pan India Delivery', 
        estDays: '2-3 Business Days', 
        cod: true, 
        shiprocketCourier: 'Shiprocket Air Service' 
      });
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md overflow-y-auto">
      <div className="relative w-full max-w-4xl bg-[#121722] border border-[#D4AF37]/30 rounded-3xl overflow-hidden shadow-2xl shadow-[#D4AF37]/10 my-8">
        
        {/* Close Button */}
        <button 
          onClick={onClose}
          className="absolute top-4 right-4 z-10 w-9 h-9 rounded-full bg-[#0A0D12]/80 text-slate-300 hover:text-white border border-white/10 flex items-center justify-center transition-colors"
        >
          <X size={20} />
        </button>

        <div className="grid grid-cols-1 md:grid-cols-2">
          {/* Left Column: Product Image */}
          <div className="bg-[#19202E] relative p-6 flex items-center justify-center border-b md:border-b-0 md:border-r border-white/10">
            <img 
              src={product.image} 
              alt={product.name} 
              className="w-full max-h-[420px] object-cover rounded-2xl border border-white/5"
            />
            <div className="absolute bottom-8 left-8 bg-[#0A0D12]/80 backdrop-blur-md border border-[#D4AF37]/40 text-[#E6CA65] text-xs font-bold px-3 py-1.5 rounded-full flex items-center gap-1.5">
              <ShieldCheck size={14} /> 100% Anti-Tarnish Guarantee
            </div>
          </div>

          {/* Right Column: Information & Delivery Check */}
          <div className="p-6 md:p-8 space-y-5 text-left flex flex-col justify-between">
            <div>
              <div className="flex items-center gap-2">
                <span className="bg-[#D4AF37]/20 text-[#E6CA65] text-xs font-semibold px-2.5 py-0.5 rounded-full border border-[#D4AF37]/30 uppercase">
                  {product.metal}
                </span>
                <div className="flex items-center gap-1 text-[#E6CA65] text-xs">
                  <Star size={14} fill="currentColor" />
                  <span className="font-bold">{product.rating}</span>
                  <span className="text-slate-400">({product.reviewCount} verified reviews)</span>
                </div>
              </div>

              <h2 className="font-serif text-2xl md:text-3xl font-bold text-white mt-2">
                {product.name}
              </h2>

              {/* Price */}
              <div className="flex items-baseline gap-3 mt-3">
                <span className="text-3xl font-bold text-white">₹{product.price}</span>
                <span className="text-sm text-slate-400 line-through">₹{product.originalPrice}</span>
                <span className="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
                  Save {product.discountPercent}%
                </span>
              </div>

              <p className="text-slate-300 text-xs leading-relaxed mt-3 font-light">
                {product.description}
              </p>

              {/* Bullet Features */}
              <ul className="space-y-1.5 mt-4 text-xs text-slate-200">
                {product.features.map((feat, idx) => (
                  <li key={idx} className="flex items-center gap-2">
                    <Check size={14} className="text-[#D4AF37] shrink-0" />
                    <span>{feat}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Pincode & Delivery Checker (Task 1.1 Requirement) */}
            <div className="bg-[#19202E] p-4 rounded-2xl border border-white/5 space-y-2">
              <label className="block text-xs font-semibold text-slate-300 flex items-center gap-1.5">
                <Truck size={14} className="text-[#D4AF37]" />
                Check COD & Express Delivery via Shiprocket
              </label>

              <form onSubmit={handlePincodeCheck} className="flex gap-2">
                <input 
                  type="text" 
                  placeholder="Enter Pincode (e.g. 400001)" 
                  value={pincode}
                  onChange={(e) => setPincode(e.target.value)}
                  maxLength={6}
                  className="bg-[#0A0D12] text-xs text-white placeholder-slate-500 border border-white/10 rounded-xl px-3 py-2 focus:outline-none focus:border-[#D4AF37] flex-1"
                />
                <button 
                  type="submit"
                  className="bg-[#D4AF37] hover:bg-[#E6CA65] text-[#0A0D12] text-xs font-bold px-4 py-2 rounded-xl transition-colors shrink-0"
                >
                  Verify
                </button>
              </form>

              {pincodeStatus && (
                <div className="mt-2 text-xs text-slate-300 bg-[#0A0D12] p-2.5 rounded-xl border border-emerald-500/30 flex items-center justify-between">
                  <div>
                    <span className="font-semibold text-white">{pincodeStatus.location}</span>
                    <span className="block text-[11px] text-slate-400">Est. Delivery: {pincodeStatus.estDays} ({pincodeStatus.shiprocketCourier})</span>
                  </div>
                  <span className="text-[10px] font-bold bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded">
                    COD Available
                  </span>
                </div>
              )}
            </div>

            {/* Action Buttons */}
            <div className="flex items-center gap-3 pt-2">
              <button 
                onClick={() => { onAddToCart(product); onClose(); }}
                className="flex-1 bg-[#19202E] hover:bg-[#232B3D] text-[#E6CA65] border border-[#D4AF37]/50 font-bold py-3 px-4 rounded-xl text-xs flex items-center justify-center gap-2 transition-colors"
              >
                <ShoppingBag size={16} />
                <span>Add to Bag</span>
              </button>

              <button 
                onClick={() => { onBuyNow(product); onClose(); }}
                className="flex-1 btn-gold py-3 px-4 rounded-xl text-xs font-bold justify-center shadow-lg"
              >
                <Zap size={16} />
                <span>Buy Now (Razorpay / COD)</span>
              </button>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}
