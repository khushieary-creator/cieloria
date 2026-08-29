import React from 'react';
import { ShieldCheck, Droplets, Sparkles, Flame, RefreshCw, Award } from 'lucide-react';

export default function AntiTarnishBadge() {
  return (
    <section className="py-12 bg-[#121722] border-y border-white/5">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-8">
        <div>
          <span className="text-xs uppercase tracking-widest text-[#D4AF37] font-semibold">The Cieloria Standard</span>
          <h2 className="font-serif text-3xl sm:text-4xl font-bold text-white mt-1">
            Why Choose Cieloria Anti-Tarnish Jewelry?
          </h2>
          <p className="text-slate-400 text-sm max-w-xl mx-auto mt-2 font-light">
            Engineered with 316L Surgical Grade Stainless Steel & Advanced PVD 18K Gold Vacuum Plating for lifetime shine.
          </p>
        </div>

        {/* Feature Grid */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="bg-[#19202E] p-6 rounded-2xl border border-white/5 hover:border-[#D4AF37]/40 transition-colors text-center space-y-3">
            <div className="w-12 h-12 rounded-full bg-[#D4AF37]/15 text-[#E6CA65] flex items-center justify-center mx-auto">
              <Droplets size={24} />
            </div>
            <h3 className="font-serif text-lg font-bold text-white">Shower & Swim Safe</h3>
            <p className="text-xs text-slate-400">Wear it while swimming, showering, or working out. 100% water and sweat resistant.</p>
          </div>

          <div className="bg-[#19202E] p-6 rounded-2xl border border-white/5 hover:border-[#D4AF37]/40 transition-colors text-center space-y-3">
            <div className="w-12 h-12 rounded-full bg-[#D4AF37]/15 text-[#E6CA65] flex items-center justify-center mx-auto">
              <ShieldCheck size={24} />
            </div>
            <h3 className="font-serif text-lg font-bold text-white">Hypoallergenic</h3>
            <p className="text-xs text-slate-400">Nickel-free and lead-free formula. Completely safe for sensitive skin with zero irritation.</p>
          </div>

          <div className="bg-[#19202E] p-6 rounded-2xl border border-white/5 hover:border-[#D4AF37]/40 transition-colors text-center space-y-3">
            <div className="w-12 h-12 rounded-full bg-[#D4AF37]/15 text-[#E6CA65] flex items-center justify-center mx-auto">
              <Flame size={24} />
            </div>
            <h3 className="font-serif text-lg font-bold text-white">10x Thicker 18K Gold</h3>
            <p className="text-xs text-slate-400">PVD vacuum gold plating process ensures color does not fade or turn skin green.</p>
          </div>

          <div className="bg-[#19202E] p-6 rounded-2xl border border-white/5 hover:border-[#D4AF37]/40 transition-colors text-center space-y-3">
            <div className="w-12 h-12 rounded-full bg-[#D4AF37]/15 text-[#E6CA65] flex items-center justify-center mx-auto">
              <Award size={24} />
            </div>
            <h3 className="font-serif text-lg font-bold text-white">Lifetime Replacements</h3>
            <p className="text-xs text-slate-400">Backed by our Cieloria warranty against tarnishing or color loss.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
