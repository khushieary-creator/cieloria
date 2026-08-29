import React, { useState } from 'react';
import { X, Trash2, Plus, Minus, ShoppingBag, ShieldCheck, ArrowRight, Tag, Zap } from 'lucide-react';

export default function CartDrawer({ 
  isOpen, 
  onClose, 
  cartItems, 
  onUpdateQuantity, 
  onRemoveItem, 
  onProceedToCheckout 
}) {
  const [promoCode, setPromoCode] = useState('');
  const [promoApplied, setPromoApplied] = useState(false);

  if (!isOpen) return null;

  const subtotal = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
  const discount = promoApplied ? Math.round(subtotal * 0.1) : 0;
  const freeShippingThreshold = 999;
  const shippingFee = subtotal >= freeShippingThreshold || cartItems.length === 0 ? 0 : 99;
  const total = Math.max(0, subtotal - discount + shippingFee);

  const progressPercent = Math.min(100, Math.round((subtotal / freeShippingThreshold) * 100));

  const handleApplyPromo = (e) => {
    e.preventDefault();
    if (promoCode.trim().toUpperCase() === 'CIELORIA10') {
      setPromoApplied(true);
    } else {
      alert('Invalid Promo Code. Try: CIELORIA10');
    }
  };

  return (
    <div className="fixed inset-0 z-50 overflow-hidden bg-black/70 backdrop-blur-sm">
      <div className="absolute inset-y-0 right-0 max-w-full flex pl-10">
        <div className="w-screen max-w-md bg-[#121722] border-l border-[#D4AF37]/30 shadow-2xl flex flex-col justify-between text-left">
          
          {/* Header */}
          <div className="p-6 border-b border-white/10 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <ShoppingBag className="text-[#D4AF37]" size={22} />
              <h2 className="font-serif text-xl font-bold text-white">Your Jewelry Bag</h2>
              <span className="bg-[#D4AF37]/20 text-[#E6CA65] text-xs font-bold px-2 py-0.5 rounded-full">
                {cartItems.reduce((sum, item) => sum + item.quantity, 0)} Items
              </span>
            </div>
            <button 
              onClick={onClose}
              className="text-slate-400 hover:text-white p-2 rounded-full hover:bg-white/5 transition-colors"
            >
              <X size={20} />
            </button>
          </div>

          {/* Free Shipping Meter */}
          <div className="bg-[#19202E] px-6 py-3 border-b border-white/5">
            <div className="flex items-center justify-between text-xs text-slate-300 font-medium mb-1.5">
              <span>
                {subtotal >= freeShippingThreshold ? (
                  <strong className="text-emerald-400">🎉 Free Express Shipping Unlocked!</strong>
                ) : (
                  <>Add <strong className="text-[#E6CA65]">₹{freeShippingThreshold - subtotal}</strong> more for Free Shipping</>
                )}
              </span>
              <span>{progressPercent}%</span>
            </div>
            <div className="w-full h-1.5 bg-[#0A0D12] rounded-full overflow-hidden">
              <div 
                className="h-full bg-gradient-to-r from-[#D4AF37] to-[#E6CA65] transition-all duration-500"
                style={{ width: `${progressPercent}%` }}
              ></div>
            </div>
          </div>

          {/* Cart Items List */}
          <div className="flex-1 overflow-y-auto p-6 space-y-4">
            {cartItems.length === 0 ? (
              <div className="text-center py-16 space-y-4">
                <div className="w-16 h-16 rounded-full bg-[#19202E] border border-[#D4AF37]/20 text-[#D4AF37] flex items-center justify-center mx-auto">
                  <ShoppingBag size={28} />
                </div>
                <h3 className="font-serif text-xl font-bold text-white">Your Bag is Empty</h3>
                <p className="text-xs text-slate-400 max-w-xs mx-auto">
                  Explore our demi-fine collection and add anti-tarnish 18K gold jewelry to your bag.
                </p>
                <button 
                  onClick={onClose}
                  className="btn-gold text-xs py-2.5 px-6 inline-flex"
                >
                  Start Shopping
                </button>
              </div>
            ) : (
              cartItems.map((item) => (
                <div 
                  key={item.id}
                  className="flex gap-4 p-3 bg-[#19202E] rounded-2xl border border-white/5 relative group"
                >
                  <img 
                    src={item.image} 
                    alt={item.name} 
                    className="w-20 h-20 object-cover rounded-xl border border-white/5"
                  />

                  <div className="flex-1 space-y-1">
                    <h4 className="font-serif text-sm font-bold text-white line-clamp-1">{item.name}</h4>
                    <span className="text-[10px] text-[#E6CA65] bg-[#D4AF37]/10 px-2 py-0.5 rounded font-semibold">
                      {item.metal}
                    </span>

                    <div className="flex items-center justify-between pt-2">
                      <span className="font-bold text-sm text-white">₹{item.price * item.quantity}</span>

                      {/* Quantity Controller */}
                      <div className="flex items-center gap-2 bg-[#0A0D12] border border-white/10 rounded-lg px-2 py-1 text-xs">
                        <button 
                          onClick={() => onUpdateQuantity(item.id, item.quantity - 1)}
                          className="text-slate-400 hover:text-white"
                        >
                          <Minus size={12} />
                        </button>
                        <span className="font-bold text-white w-4 text-center">{item.quantity}</span>
                        <button 
                          onClick={() => onUpdateQuantity(item.id, item.quantity + 1)}
                          className="text-slate-400 hover:text-white"
                        >
                          <Plus size={12} />
                        </button>
                      </div>
                    </div>
                  </div>

                  {/* Remove Button */}
                  <button 
                    onClick={() => onRemoveItem(item.id)}
                    className="text-slate-500 hover:text-rose-400 p-1"
                    title="Remove Item"
                  >
                    <Trash2 size={16} />
                  </button>
                </div>
              ))
            )}
          </div>

          {/* Footer Checkout Summary */}
          {cartItems.length > 0 && (
            <div className="p-6 bg-[#0A0D12] border-t border-white/10 space-y-4">
              {/* Promo Code Input */}
              <form onSubmit={handleApplyPromo} className="flex gap-2">
                <div className="relative flex-1">
                  <Tag size={14} className="absolute left-3 top-3 text-[#D4AF37]" />
                  <input 
                    type="text" 
                    placeholder="Promo Code (CIELORIA10)"
                    value={promoCode}
                    onChange={(e) => setPromoCode(e.target.value)}
                    className="w-full bg-[#19202E] text-xs text-white placeholder-slate-500 border border-white/10 rounded-xl pl-9 pr-3 py-2.5 focus:outline-none focus:border-[#D4AF37]"
                  />
                </div>
                <button 
                  type="submit"
                  className="bg-[#19202E] hover:bg-[#232B3D] text-[#E6CA65] border border-[#D4AF37]/40 text-xs font-bold px-4 py-2.5 rounded-xl transition-colors"
                >
                  Apply
                </button>
              </form>

              {promoApplied && (
                <div className="text-xs text-emerald-400 flex items-center justify-between bg-emerald-500/10 px-3 py-1.5 rounded-lg border border-emerald-500/20">
                  <span>Code CIELORIA10 Applied!</span>
                  <span className="font-bold">-₹{discount}</span>
                </div>
              )}

              {/* Price Breakdown */}
              <div className="space-y-1.5 text-xs text-slate-300">
                <div className="flex justify-between">
                  <span>Subtotal</span>
                  <span>₹{subtotal}</span>
                </div>
                {promoApplied && (
                  <div className="flex justify-between text-emerald-400">
                    <span>Coupon Discount</span>
                    <span>-₹{discount}</span>
                  </div>
                )}
                <div className="flex justify-between">
                  <span>Estimated Express Shipping</span>
                  <span>{shippingFee === 0 ? <strong className="text-emerald-400">FREE</strong> : `₹${shippingFee}`}</span>
                </div>
                <div className="flex justify-between text-sm font-bold text-white pt-2 border-t border-white/10">
                  <span>Total Amount</span>
                  <span className="text-[#E6CA65] text-base">₹{total}</span>
                </div>
              </div>

              {/* Online Payment Discount Offer */}
              <div className="text-[11px] text-[#E6CA65] bg-[#D4AF37]/10 p-2.5 rounded-xl border border-[#D4AF37]/30 flex items-center gap-2">
                <Zap size={14} className="shrink-0" />
                <span>Get <strong>Extra 5% OFF</strong> on Razorpay / UPI online payments!</span>
              </div>

              {/* Checkout Button */}
              <button 
                onClick={() => { onClose(); onProceedToCheckout(); }}
                className="w-full btn-gold justify-center py-3.5 text-sm font-bold shadow-xl shadow-[#D4AF37]/20"
              >
                <span>Proceed to Razorpay & COD Checkout</span>
                <ArrowRight size={18} />
              </button>

              <div className="flex items-center justify-center gap-2 text-[10px] text-slate-400 text-center">
                <ShieldCheck size={14} className="text-[#D4AF37]" />
                <span>SSL Encrypted Checkout • Razorpay Secured • 100% Anti-Tarnish</span>
              </div>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}
