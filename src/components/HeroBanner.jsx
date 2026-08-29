import React, { useState } from 'react';
import { Sparkles, Shield, Droplets, CheckCircle, ArrowRight, Truck, MapPin } from 'lucide-react';
import { PINCODES } from '../data/products';

export default function HeroBanner({ onQuickPincodeCheck }) {
  const [pincode, setPincode] = useState('');
  const [pincodeResult, setPincodeResult] = useState(null);

  const handleCheckPincode = (e) => {
    e.preventDefault();
    if (!pincode.trim()) return;
    const res = PINCODES[pincode.trim()];
    if (res) {
      setPincodeResult({ success: true, ...res });
    } else {
      setPincodeResult({ 
        success: true, 
        location: 'Delivery Available Across India', 
        estDays: '3-4 Days Standard', 
        cod: true, 
        shiprocketCourier: 'Shiprocket Partner' 
      });
    }
  };

  return (
    <section className="relative overflow-hidden py-16 lg:py-24 bg-[#0A0D12]">
      {/* Background Lighting Orbs */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#D4AF37]/10 rounded-full blur-[120px] pointer-events-none animate-pulse-slow"></div>
      <div className="absolute bottom-10 right-10 w-80 h-80 bg-[#E8A89A]/10 rounded-full blur-[100px] pointer-events-none"></div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
          
          {/* Left Column: Headlines & CTA */}
          <div className="lg:col-span-7 space-y-6 text-left">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#19202E] border border-[#D4AF37]/40 text-[#E6CA65] text-xs font-semibold uppercase tracking-wider">
              <Sparkles size={14} className="text-[#D4AF37]" />
              Palmonas-Inspired Anti-Tarnish Technology
            </div>

            <h1 className="font-serif text-4xl sm:text-5xl lg:text-6xl font-bold tracking-tight text-white leading-[1.15]">
              Everyday Luxury <br />
              <span className="gold-gradient-text">That Never Tarnishes.</span>
            </h1>

            <p className="text-slate-300 text-base sm:text-lg max-w-2xl font-light leading-relaxed">
              Elevate your daily style with <strong className="text-white font-medium">18K Gold Plated Demi-Fine Jewelry</strong>. Designed to be 100% waterproof, sweatproof, and skin-friendly for non-stop elegance.
            </p>

            {/* Anti-Tarnish Feature Bullets */}
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 pt-2">
              <div className="flex items-center gap-2 text-xs font-semibold text-slate-200 bg-[#121722] p-2.5 rounded-xl border border-white/5">
                <Shield size={16} className="text-[#D4AF37]" />
                <span>Lifetime Color Guarantee</span>
              </div>
              <div className="flex items-center gap-2 text-xs font-semibold text-slate-200 bg-[#121722] p-2.5 rounded-xl border border-white/5">
                <Droplets size={16} className="text-cyan-400" />
                <span>100% Waterproof</span>
              </div>
              <div className="flex items-center gap-2 text-xs font-semibold text-slate-200 bg-[#121722] p-2.5 rounded-xl border border-white/5">
                <CheckCircle size={16} className="text-emerald-400" />
                <span>COD Verification</span>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-wrap items-center gap-4 pt-4">
              <a href="#products-section" className="btn-gold">
                <span>Shop Demi-Fine Collection</span>
                <ArrowRight size={18} />
              </a>

              {/* Quick Pincode Checker Dropdown */}
              <form onSubmit={handleCheckPincode} className="flex items-center bg-[#19202E] border border-[#D4AF37]/30 rounded-full p-1 pl-4">
                <MapPin size={16} className="text-[#D4AF37] mr-2 shrink-0" />
                <input 
                  type="text" 
                  placeholder="Enter Pincode (e.g. 400001)" 
                  value={pincode}
                  onChange={(e) => setPincode(e.target.value)}
                  maxLength={6}
                  className="bg-transparent text-xs text-white placeholder-slate-400 focus:outline-none w-36"
                />
                <button type="submit" className="bg-[#D4AF37]/20 hover:bg-[#D4AF37] text-[#E6CA65] hover:text-[#0A0D12] text-xs font-bold px-3 py-2 rounded-full transition-colors">
                  Check Delivery
                </button>
              </form>
            </div>

            {/* Pincode Result Alert */}
            {pincodeResult && (
              <div className="mt-3 p-3 bg-[#121722] border border-[#D4AF37]/40 rounded-xl text-xs flex items-center justify-between text-slate-200">
                <div className="flex items-center gap-2">
                  <Truck size={16} className="text-[#D4AF37]" />
                  <span>
                    <strong>{pincodeResult.location}</strong> — {pincodeResult.estDays} via <span className="text-[#E6CA65] font-semibold">{pincodeResult.shiprocketCourier}</span>
                  </span>
                </div>
                <span className="bg-emerald-500/20 text-emerald-400 font-bold px-2 py-0.5 rounded text-[10px] uppercase">
                  COD Verified
                </span>
              </div>
            )}
          </div>

          {/* Right Column: Hero Visual Display */}
          <div className="lg:col-span-5 relative">
            <div className="relative mx-auto rounded-3xl overflow-hidden border border-[#D4AF37]/30 shadow-2xl shadow-[#D4AF37]/10 group">
              <img 
                src="/hero_banner.jpg" 
                alt="Cieloria Demi-Fine Jewelry Banner" 
                className="w-full h-[440px] object-cover transition-transform duration-700 group-hover:scale-105"
              />
              
              {/* Overlay Glass Card */}
              <div className="absolute bottom-4 left-4 right-4 p-4 rounded-2xl glass-panel border border-white/10 flex items-center justify-between">
                <div>
                  <h4 className="font-serif text-lg font-bold text-white">Lumière Royal Collection</h4>
                  <p className="text-xs text-[#E6CA65]">18K Gold & Sapphire Gemstones</p>
                </div>
                <div className="text-right">
                  <span className="text-xs text-slate-400 line-through">₹5,999</span>
                  <span className="block font-bold text-lg text-white">₹2,999</span>
                </div>
              </div>

              {/* Floating Badge */}
              <div className="absolute top-4 right-4 bg-[#0A0D12]/80 backdrop-blur-md border border-[#D4AF37]/50 text-[#E6CA65] text-xs font-bold px-3 py-1.5 rounded-full flex items-center gap-1.5 shadow-lg">
                <Sparkles size={14} /> 50% OFF Limited Launch
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
}
