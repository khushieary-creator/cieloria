import React, { useState } from 'react';
import { X, Truck, Search, CheckCircle, Clock, PackageCheck, MapPin } from 'lucide-react';

export default function ShiprocketTrackerModal({ isOpen, onClose }) {
  const [orderQuery, setOrderQuery] = useState('CL-84920');
  const [trackingData, setTrackingData] = useState(null);

  if (!isOpen) return null;

  const handleTrack = (e) => {
    e.preventDefault();
    setTrackingData({
      orderId: orderQuery || 'CL-84920',
      status: 'In-Transit via Delhivery Air',
      courier: 'Shiprocket Express (Delhivery Air)',
      awb: 'DEL948201948IN',
      estDelivery: 'Tomorrow, 5:00 PM',
      steps: [
        { title: 'Order Confirmed & Verified', time: 'Today, 10:30 AM', done: true },
        { title: 'Packed in Cieloria Luxury Box', time: 'Today, 1:15 PM', done: true },
        { title: 'Handed Over to Shiprocket Courier', time: 'Today, 4:00 PM', done: true },
        { title: 'In-Transit (Mumbai Hub to Destination)', time: 'Active', done: false },
        { title: 'Out for Delivery', time: 'Pending', done: false }
      ]
    });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/80 backdrop-blur-md">
      <div className="relative w-full max-w-xl bg-[#121722] border border-[#D4AF37]/30 rounded-3xl overflow-hidden shadow-2xl p-6 text-left space-y-6">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-white/10 pb-4">
          <div className="flex items-center gap-2.5">
            <Truck className="text-[#D4AF37]" size={24} />
            <div>
              <h2 className="font-serif text-xl font-bold text-white">Shiprocket Live Tracking</h2>
              <p className="text-[11px] text-slate-400">Integrated Courier Logistics for Cieloria</p>
            </div>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-white p-2">
            <X size={20} />
          </button>
        </div>

        {/* Track Form */}
        <form onSubmit={handleTrack} className="flex gap-2">
          <div className="relative flex-1">
            <Search size={16} className="absolute left-3 top-3 text-[#D4AF37]" />
            <input 
              type="text" 
              placeholder="Enter Order ID (e.g. CL-84920)"
              value={orderQuery}
              onChange={(e) => setOrderQuery(e.target.value)}
              className="w-full bg-[#19202E] text-xs text-white border border-white/10 rounded-xl pl-9 pr-3 py-2.5 focus:border-[#D4AF37] focus:outline-none"
            />
          </div>
          <button 
            type="submit"
            className="bg-[#D4AF37] hover:bg-[#E6CA65] text-[#0A0D12] text-xs font-bold px-5 py-2.5 rounded-xl"
          >
            Track Status
          </button>
        </form>

        {/* Tracking Details */}
        {trackingData && (
          <div className="bg-[#19202E] p-5 rounded-2xl border border-white/5 space-y-4 text-xs">
            <div className="flex items-center justify-between border-b border-white/10 pb-3">
              <div>
                <span className="text-slate-400 block text-[10px]">AWB Tracking No:</span>
                <span className="font-mono font-bold text-white text-sm">{trackingData.awb}</span>
              </div>
              <div className="text-right">
                <span className="text-slate-400 block text-[10px]">Courier Partner:</span>
                <span className="font-bold text-[#E6CA65]">{trackingData.courier}</span>
              </div>
            </div>

            {/* Timeline Steps */}
            <div className="space-y-3 pt-2">
              {trackingData.steps.map((step, idx) => (
                <div key={idx} className="flex items-start gap-3">
                  <div className={`w-6 h-6 rounded-full flex items-center justify-center text-xs shrink-0 mt-0.5 ${
                    step.done 
                      ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500' 
                      : step.time === 'Active'
                        ? 'bg-[#D4AF37]/20 text-[#E6CA65] border border-[#D4AF37] animate-pulse'
                        : 'bg-[#0A0D12] text-slate-600 border border-white/10'
                  }`}>
                    {step.done ? <CheckCircle size={14} /> : idx + 1}
                  </div>
                  <div className="flex-1">
                    <h4 className={`font-semibold ${step.done ? 'text-white' : step.time === 'Active' ? 'text-[#E6CA65]' : 'text-slate-500'}`}>
                      {step.title}
                    </h4>
                    <span className="text-[10px] text-slate-400">{step.time}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  );
}
