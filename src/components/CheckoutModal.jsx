import React, { useState } from 'react';
import { X, Lock, CheckCircle, ShieldCheck, Truck, CreditCard, Smartphone, Check, Sparkles, AlertCircle } from 'lucide-react';
import confetti from 'canvas-confetti';

export default function CheckoutModal({ isOpen, onClose, cartItems, onOrderPlaced }) {
  const [step, setStep] = useState(1); // 1: Shipping, 2: Logistics & Payment, 3: Success
  const [paymentMethod, setPaymentMethod] = useState('razorpay'); // razorpay, cod, stripe
  const [courierPartner, setCourierPartner] = useState('delhivery'); // delhivery, shiprocket
  const [codOtp, setCodOtp] = useState('');
  const [otpVerified, setOtpVerified] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [orderId, setOrderId] = useState('');

  const [formData, setFormData] = useState({
    name: 'Khushi Sharma',
    phone: '9876543210',
    email: 'khushi@cieloria.com',
    address: 'Flat 402, Royal Palms, Bandra West',
    city: 'Mumbai',
    state: 'Maharashtra',
    pincode: '400050'
  });

  if (!isOpen) return null;

  const subtotal = cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
  const isOnlinePayment = paymentMethod === 'razorpay' || paymentMethod === 'stripe';
  const onlineDiscount = isOnlinePayment ? Math.round(subtotal * 0.05) : 0;
  const totalAmount = Math.max(0, subtotal - onlineDiscount);

  const handleVerifyOtp = () => {
    if (codOtp === '1234' || codOtp.length === 4) {
      setOtpVerified(true);
    } else {
      alert('Default test OTP is 1234');
    }
  };

  const handlePlaceOrder = () => {
    if (paymentMethod === 'cod' && !otpVerified) {
      alert('Please verify COD OTP (Enter 1234) before proceeding');
      return;
    }

    setIsProcessing(true);

    setTimeout(() => {
      const generatedId = `CL-${Math.floor(10000 + Math.random() * 90000)}`;
      setOrderId(generatedId);
      setIsProcessing(false);
      setStep(3);

      // Trigger Confetti!
      try {
        confetti({
          particleCount: 120,
          spread: 80,
          origin: { y: 0.6 }
        });
      } catch (e) {
        console.log('Confetti triggered');
      }

      onOrderPlaced({
        orderId: generatedId,
        items: cartItems,
        total: totalAmount,
        paymentMethod,
        courierPartner,
        shippingAddress: formData
      });
    }, 1500);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-md overflow-y-auto">
      <div className="relative w-full max-w-2xl bg-[#121722] border border-[#D4AF37]/40 rounded-3xl overflow-hidden shadow-2xl my-8 text-left">
        
        {/* Header */}
        <div className="p-6 bg-[#19202E] border-b border-white/10 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-[#D4AF37]/20 text-[#E6CA65] flex items-center justify-center font-bold text-xs border border-[#D4AF37]/40">
              <Lock size={16} />
            </div>
            <div>
              <h2 className="font-serif text-xl font-bold text-white">Cieloria Secure Checkout</h2>
              <div className="flex items-center gap-2 text-[11px] text-emerald-400">
                <ShieldCheck size={12} />
                <span>https://cieloria.com • SSL 256-Bit Encrypted</span>
              </div>
            </div>
          </div>
          {step !== 3 && (
            <button onClick={onClose} className="text-slate-400 hover:text-white p-2 rounded-full">
              <X size={20} />
            </button>
          )}
        </div>

        {/* Step Indicator */}
        {step !== 3 && (
          <div className="grid grid-cols-2 bg-[#0A0D12] text-xs font-semibold border-b border-white/10 text-center">
            <div className={`py-3 ${step === 1 ? 'text-[#E6CA65] border-b-2 border-[#D4AF37] bg-[#121722]' : 'text-slate-500'}`}>
              1. Delivery & Address
            </div>
            <div className={`py-3 ${step === 2 ? 'text-[#E6CA65] border-b-2 border-[#D4AF37] bg-[#121722]' : 'text-slate-500'}`}>
              2. Payment & Shiprocket Courier
            </div>
          </div>
        )}

        {/* Content Body */}
        <div className="p-6 sm:p-8 space-y-6">

          {/* STEP 1: Address */}
          {step === 1 && (
            <div className="space-y-4">
              <h3 className="font-serif text-lg font-bold text-white flex items-center gap-2">
                <span>Shipping Address</span>
              </h3>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs">
                <div>
                  <label className="block text-slate-400 mb-1">Full Name</label>
                  <input 
                    type="text" 
                    value={formData.name}
                    onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                    className="w-full bg-[#19202E] text-white border border-white/10 rounded-xl px-3 py-2.5 focus:border-[#D4AF37] focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block text-slate-400 mb-1">Phone Number (for COD verification)</label>
                  <input 
                    type="text" 
                    value={formData.phone}
                    onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                    className="w-full bg-[#19202E] text-white border border-white/10 rounded-xl px-3 py-2.5 focus:border-[#D4AF37] focus:outline-none"
                  />
                </div>
                <div className="sm:col-span-2">
                  <label className="block text-slate-400 mb-1">Street Address</label>
                  <input 
                    type="text" 
                    value={formData.address}
                    onChange={(e) => setFormData({ ...formData, address: e.target.value })}
                    className="w-full bg-[#19202E] text-white border border-white/10 rounded-xl px-3 py-2.5 focus:border-[#D4AF37] focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block text-slate-400 mb-1">City</label>
                  <input 
                    type="text" 
                    value={formData.city}
                    onChange={(e) => setFormData({ ...formData, city: e.target.value })}
                    className="w-full bg-[#19202E] text-white border border-white/10 rounded-xl px-3 py-2.5 focus:border-[#D4AF37] focus:outline-none"
                  />
                </div>
                <div>
                  <label className="block text-slate-400 mb-1">Pincode</label>
                  <input 
                    type="text" 
                    value={formData.pincode}
                    onChange={(e) => setFormData({ ...formData, pincode: e.target.value })}
                    className="w-full bg-[#19202E] text-white border border-white/10 rounded-xl px-3 py-2.5 focus:border-[#D4AF37] focus:outline-none"
                  />
                </div>
              </div>

              <button 
                onClick={() => setStep(2)}
                className="w-full btn-gold justify-center py-3 text-sm mt-4 font-bold"
              >
                Continue to Payment & Shipping
              </button>
            </div>
          )}

          {/* STEP 2: Logistics & Payment */}
          {step === 2 && (
            <div className="space-y-6">
              
              {/* Shiprocket Courier Integration Selector */}
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-2 flex items-center gap-1.5">
                  <Truck size={14} className="text-[#D4AF37]" />
                  Select Logistics Integration (Task 1.1)
                </label>

                <div className="grid grid-cols-2 gap-3 text-xs">
                  <button 
                    type="button"
                    onClick={() => setCourierPartner('delhivery')}
                    className={`p-3 rounded-2xl border text-left transition-all ${
                      courierPartner === 'delhivery' 
                        ? 'bg-[#19202E] border-[#D4AF37] text-white shadow-md shadow-[#D4AF37]/10' 
                        : 'bg-[#0A0D12] border-white/10 text-slate-400'
                    }`}
                  >
                    <div className="font-bold flex items-center justify-between text-slate-200">
                      <span>Delhivery Express Air</span>
                      {courierPartner === 'delhivery' && <CheckCircle size={14} className="text-[#D4AF37]" />}
                    </div>
                    <span className="text-[11px] text-emerald-400 block mt-1">Delivery in 2 Days • Free</span>
                  </button>

                  <button 
                    type="button"
                    onClick={() => setCourierPartner('shiprocket')}
                    className={`p-3 rounded-2xl border text-left transition-all ${
                      courierPartner === 'shiprocket' 
                        ? 'bg-[#19202E] border-[#D4AF37] text-white shadow-md shadow-[#D4AF37]/10' 
                        : 'bg-[#0A0D12] border-white/10 text-slate-400'
                    }`}
                  >
                    <div className="font-bold flex items-center justify-between text-slate-200">
                      <span>Shiprocket Direct</span>
                      {courierPartner === 'shiprocket' && <CheckCircle size={14} className="text-[#D4AF37]" />}
                    </div>
                    <span className="text-[11px] text-emerald-400 block mt-1">Bluedart / Xpressbees • Free</span>
                  </button>
                </div>
              </div>

              {/* Payment Method Selector */}
              <div>
                <label className="block text-xs font-semibold text-slate-300 mb-2 flex items-center gap-1.5">
                  <CreditCard size={14} className="text-[#D4AF37]" />
                  Select Payment Gateway
                </label>

                <div className="space-y-3">
                  {/* Razorpay / UPI */}
                  <label className={`block p-4 rounded-2xl border cursor-pointer transition-all ${
                    paymentMethod === 'razorpay' 
                      ? 'bg-[#19202E] border-[#D4AF37] shadow-lg' 
                      : 'bg-[#0A0D12] border-white/10'
                  }`}>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-3">
                        <input 
                          type="radio" 
                          name="payment" 
                          checked={paymentMethod === 'razorpay'} 
                          onChange={() => setPaymentMethod('razorpay')}
                          className="accent-[#D4AF37]"
                        />
                        <div>
                          <span className="font-bold text-sm text-white block">Razorpay / UPI / GPay / PhonePe</span>
                          <span className="text-[11px] text-emerald-400">⚡ Extra 5% Instant Discount Applied</span>
                        </div>
                      </div>
                      <span className="text-xs bg-[#D4AF37]/20 text-[#E6CA65] px-2 py-0.5 rounded font-bold">Recommended</span>
                    </div>
                  </label>

                  {/* Cash on Delivery */}
                  <label className={`block p-4 rounded-2xl border cursor-pointer transition-all ${
                    paymentMethod === 'cod' 
                      ? 'bg-[#19202E] border-[#D4AF37] shadow-lg' 
                      : 'bg-[#0A0D12] border-white/10'
                  }`}>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-3">
                        <input 
                          type="radio" 
                          name="payment" 
                          checked={paymentMethod === 'cod'} 
                          onChange={() => setPaymentMethod('cod')}
                          className="accent-[#D4AF37]"
                        />
                        <div>
                          <span className="font-bold text-sm text-white block">Cash on Delivery (COD Verification)</span>
                          <span className="text-[11px] text-slate-400">Pay cash upon delivery via Shiprocket</span>
                        </div>
                      </div>
                      <span className="text-xs bg-slate-800 text-slate-300 px-2 py-0.5 rounded">OTP Required</span>
                    </div>

                    {/* COD OTP Verification Drawer */}
                    {paymentMethod === 'cod' && (
                      <div className="mt-3 pt-3 border-t border-white/10 space-y-2">
                        <p className="text-xs text-slate-300">Enter OTP sent to <strong>{formData.phone}</strong> (Test OTP: <strong className="text-[#E6CA65]">1234</strong>):</p>
                        <div className="flex gap-2">
                          <input 
                            type="text" 
                            placeholder="Enter 1234"
                            value={codOtp}
                            onChange={(e) => setCodOtp(e.target.value)}
                            maxLength={4}
                            className="bg-[#0A0D12] text-white text-xs border border-white/10 rounded-xl px-3 py-2 w-32 text-center tracking-widest focus:border-[#D4AF37] focus:outline-none"
                          />
                          <button 
                            type="button"
                            onClick={handleVerifyOtp}
                            className="bg-[#D4AF37] text-[#0A0D12] text-xs font-bold px-4 py-2 rounded-xl"
                          >
                            {otpVerified ? 'Verified ✓' : 'Verify OTP'}
                          </button>
                        </div>
                        {otpVerified && (
                          <span className="text-[11px] text-emerald-400 font-bold block">✓ Mobile OTP Verified for COD Dispatch!</span>
                        )}
                      </div>
                    )}
                  </label>
                </div>
              </div>

              {/* Order Total Summary */}
              <div className="bg-[#0A0D12] p-4 rounded-2xl border border-white/10 space-y-1 text-xs">
                <div className="flex justify-between text-slate-400">
                  <span>Items Total ({cartItems.length})</span>
                  <span>₹{subtotal}</span>
                </div>
                {isOnlinePayment && (
                  <div className="flex justify-between text-emerald-400 font-semibold">
                    <span>Razorpay Online Discount (5%)</span>
                    <span>-₹{onlineDiscount}</span>
                  </div>
                )}
                <div className="flex justify-between text-[#E6CA65] font-bold text-base pt-2 border-t border-white/10">
                  <span>Payable Amount</span>
                  <span>₹{totalAmount}</span>
                </div>
              </div>

              {/* Navigation */}
              <div className="flex gap-3">
                <button 
                  onClick={() => setStep(1)} 
                  className="bg-[#19202E] text-slate-300 hover:text-white px-5 py-3 rounded-xl text-xs font-bold"
                >
                  Back
                </button>
                <button 
                  onClick={handlePlaceOrder}
                  disabled={isProcessing}
                  className="flex-1 btn-gold justify-center py-3 text-sm font-bold shadow-xl"
                >
                  {isProcessing ? (
                    <span>Processing Order...</span>
                  ) : (
                    <span>Confirm Order (₹{totalAmount})</span>
                  )}
                </button>
              </div>

            </div>
          )}

          {/* STEP 3: Order Success Screen */}
          {step === 3 && (
            <div className="text-center py-8 space-y-6">
              <div className="w-20 h-20 bg-[#D4AF37]/20 border-2 border-[#D4AF37] text-[#E6CA65] rounded-full flex items-center justify-center mx-auto shadow-2xl shadow-[#D4AF37]/30">
                <CheckCircle size={44} />
              </div>

              <div className="space-y-2">
                <span className="text-xs uppercase tracking-widest text-[#E6CA65] font-bold">Order Confirmed!</span>
                <h3 className="font-serif text-3xl font-bold text-white">Thank You for Shopping at Cieloria</h3>
                <p className="text-xs text-slate-300 max-w-sm mx-auto">
                  Your 18K Anti-Tarnish jewelry is being packed and prepared for shipment.
                </p>
              </div>

              <div className="bg-[#19202E] p-4 rounded-2xl border border-[#D4AF37]/30 max-w-md mx-auto text-xs text-left space-y-2">
                <div className="flex justify-between border-b border-white/10 pb-2">
                  <span className="text-slate-400">Order ID:</span>
                  <span className="font-bold text-[#E6CA65] font-mono">{orderId}</span>
                </div>
                <div className="flex justify-between border-b border-white/10 pb-2">
                  <span className="text-slate-400">Payment Status:</span>
                  <span className="font-bold text-emerald-400 uppercase">{paymentMethod === 'cod' ? 'COD Verified' : 'Razorpay Paid'}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">Logistics Partner:</span>
                  <span className="font-bold text-white">{courierPartner === 'delhivery' ? 'Delhivery Express' : 'Shiprocket Direct'}</span>
                </div>
              </div>

              <button 
                onClick={onClose}
                className="btn-gold px-8 py-3 text-xs font-bold inline-flex"
              >
                Continue Shopping
              </button>
            </div>
          )}

        </div>

      </div>
    </div>
  );
}
