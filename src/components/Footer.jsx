import React from 'react';
import { ShieldCheck, Lock, Truck, CreditCard, Instagram, Facebook, Mail, Phone, Heart } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-[#07090D] text-slate-400 border-t border-white/10 pt-16 pb-8 text-xs">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 text-left">
          
          {/* Brand Info */}
          <div className="space-y-4">
            <div className="flex items-center gap-3">
              <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-[#D4AF37] to-[#FFF0B8] flex items-center justify-center text-[#0A0D12] font-serif font-bold text-lg">
                C
              </div>
              <span className="font-serif text-2xl font-bold tracking-widest text-white">CIELORIA</span>
            </div>
            <p className="text-slate-400 leading-relaxed text-xs">
              India's premier demi-fine jewelry brand inspired by everyday luxury. 100% waterproof, anti-tarnish 18K gold plated pieces designed to last a lifetime.
            </p>
            <div className="flex items-center gap-2 text-[#E6CA65] font-semibold">
              <ShieldCheck size={16} /> 100% Anti-Tarnish Guarantee
            </div>
          </div>

          {/* Quick Links */}
          <div className="space-y-3">
            <h4 className="font-serif text-sm font-bold text-white uppercase tracking-wider">Quick Links</h4>
            <ul className="space-y-2">
              <li><a href="#" className="hover:text-[#E6CA65] transition-colors">About Cieloria</a></li>
              <li><a href="#" className="hover:text-[#E6CA65] transition-colors">Anti-Tarnish Technology</a></li>
              <li><a href="#" className="hover:text-[#E6CA65] transition-colors">Track Shiprocket Order</a></li>
              <li><a href="#" className="hover:text-[#E6CA65] transition-colors">Shipping & COD Policy</a></li>
              <li><a href="#" className="hover:text-[#E6CA65] transition-colors">Lifetime Warranty Claim</a></li>
            </ul>
          </div>

          {/* Customer Care */}
          <div className="space-y-3">
            <h4 className="font-serif text-sm font-bold text-white uppercase tracking-wider">Customer Support</h4>
            <div className="space-y-2 text-slate-300">
              <div className="flex items-center gap-2">
                <Mail size={14} className="text-[#D4AF37]" />
                <span>support@cieloria.com</span>
              </div>
              <div className="flex items-center gap-2">
                <Phone size={14} className="text-[#D4AF37]" />
                <span>+91 98765 43210 (Mon-Sat 10am-7pm)</span>
              </div>
              <div className="flex items-center gap-2 pt-2">
                <Lock size={14} className="text-emerald-400" />
                <span className="text-emerald-400 font-bold">cieloria.com (SSL Secured)</span>
              </div>
            </div>
          </div>

          {/* Newsletter */}
          <div className="space-y-3">
            <h4 className="font-serif text-sm font-bold text-white uppercase tracking-wider">Join Cieloria Club</h4>
            <p className="text-xs text-slate-400">Subscribe for secret sales and 15% off your first 18K gold order.</p>
            <form onSubmit={(e) => { e.preventDefault(); alert('Subscribed to Cieloria VIP Club!'); }} className="flex gap-2">
              <input 
                type="email" 
                placeholder="Enter email..."
                required
                className="w-full bg-[#121722] text-white text-xs border border-white/10 rounded-xl px-3 py-2 focus:border-[#D4AF37] focus:outline-none"
              />
              <button className="bg-[#D4AF37] text-[#0A0D12] text-xs font-bold px-4 py-2 rounded-xl hover:bg-[#E6CA65]">
                Join
              </button>
            </form>
          </div>

        </div>

        {/* Payment & Courier Partners Row (Task 1.1) */}
        <div className="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-center md:text-left">
          <div className="flex flex-wrap items-center justify-center gap-3">
            <span className="text-slate-500 font-semibold">Payment Gateways:</span>
            <span className="bg-[#121722] border border-white/10 text-[#E6CA65] font-bold px-2.5 py-1 rounded">Razorpay</span>
            <span className="bg-[#121722] border border-white/10 text-slate-300 font-bold px-2.5 py-1 rounded">Stripe</span>
            <span className="bg-[#121722] border border-white/10 text-emerald-400 font-bold px-2.5 py-1 rounded">UPI / GPay</span>
            <span className="bg-[#121722] border border-white/10 text-slate-300 font-bold px-2.5 py-1 rounded">COD Verified</span>
          </div>

          <div className="flex items-center gap-3">
            <span className="text-slate-500 font-semibold">Logistics:</span>
            <span className="bg-[#121722] border border-white/10 text-slate-200 font-bold px-2.5 py-1 rounded flex items-center gap-1">
              <Truck size={12} className="text-[#D4AF37]" /> Shiprocket
            </span>
            <span className="bg-[#121722] border border-white/10 text-slate-200 font-bold px-2.5 py-1 rounded">Delhivery</span>
          </div>
        </div>

        {/* Bottom Copyright */}
        <div className="border-t border-white/5 pt-6 text-center text-slate-500 text-[11px]">
          © {new Date().getFullYear()} CIELORIA (cieloria.com). All Rights Reserved. Crafted with <Heart size={10} className="inline text-rose-500" /> for demi-fine jewelry lovers.
        </div>

      </div>
    </footer>
  );
}
