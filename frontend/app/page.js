'use client';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function VendorsList() {
  const [vendors, setVendors] = useState([]);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    fetch('http://localhost:8000/api/vendors')
      .then(res => res.json())
      .then(data => {
        setVendors(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching vendors:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center text-xl text-slate-600">Loading vendors...</div>;
  }

  return (
    <main className="min-h-screen bg-slate-50 py-12 px-6">
      <div className="max-w-6xl mx-auto">
        <header className="mb-10 text-center">
          <span className="text-rose-600 font-semibold tracking-wide uppercase text-sm">Wedding Vendor Hub</span>
          <h1 className="text-4xl font-bold text-slate-900 mt-1">Explore Verified Wedding Vendors</h1>
          <p className="text-slate-600 mt-2">Select a business to view verified reviews and AI-generated sentiment summaries.</p>
        </header>

        <div className="grid md:grid-cols-2 gap-8">
          {vendors.map(vendor => (
            <div 
              key={vendor.id}
              onClick={() => router.push(`/reviews?id=${vendor.id}`)}
              className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden cursor-pointer hover:shadow-md transition group"
            >
              <div className="h-48 overflow-hidden relative">
                <img src={vendor.image} alt={vendor.name} className="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
                <span className="absolute top-4 right-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-xs font-medium text-slate-800">
                  {vendor.category}
                </span>
              </div>
              <div className="p-6">
                <h3 className="text-xl font-bold text-slate-900 group-hover:text-rose-600 transition">{vendor.name}</h3>
                <div className="flex items-center justify-between mt-4">
                  <div className="flex items-center space-x-1">
                    <span className="text-amber-500 font-bold">★</span>
                    <span className="font-semibold text-slate-800">{vendor.rating}</span>
                    <span className="text-slate-500 text-sm">({vendor.reviews.length} total reviews)</span>
                  </div>
                  <div className="text-sm font-medium text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full">
                    {vendor.verified_count} Verified Couples
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
