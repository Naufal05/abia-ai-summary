'use client';
import { useState, useEffect, Suspense } from 'react';
import { useSearchParams, useRouter } from 'next/navigation';

function ReviewContent() {
  const searchParams = useSearchParams();
  const vendorId = searchParams.get('id');
  const router = useRouter();

  const [vendor, setVendor] = useState(null);
  const [loading, setLoading] = useState(true);
  const [analyzing, setAnalyzing] = useState(false);
  const [aiData, setAiData] = useState(null);

  useEffect(() => {
    if (!vendorId) return;
    fetch(`http://localhost:8000/api/vendors/${vendorId}`)
      .then(res => res.json())
      .then(data => {
        setVendor(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching vendor details:", err);
        setLoading(false);
      });
  }, [vendorId]);

  const handleRegenerateSummary = () => {
    setAnalyzing(true);
    fetch(`http://localhost:8000/api/vendors/${vendorId}/regenerate-summary`, {
      method: 'POST'
    })
      .then(res => res.json())
      .then(data => {
        setAiData(data);
        setAnalyzing(false);
      })
      .catch(err => {
        console.error("Error generating AI summary:", err);
        setAnalyzing(false);
      });
  };

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center text-slate-600">Loading reviews...</div>;
  }

  if (!vendor) {
    return <div className="min-h-screen flex items-center justify-center text-slate-600">Vendor not found.</div>;
  }

  return (
    <main className="min-h-screen bg-slate-50 py-12 px-6">
      <div className="max-w-4xl mx-auto">
        <button 
          onClick={() => router.push('/')}
          className="text-sm font-medium text-slate-600 hover:text-slate-900 mb-6 flex items-center space-x-1"
        >
          ← Back to Vendors
        </button>

        <div className="bg-white rounded-2xl shadow-sm border border-slate-200 p-8 mb-8">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div>
              <span className="text-rose-600 font-semibold text-sm uppercase tracking-wide">{vendor.category}</span>
              <h1 className="text-3xl font-bold text-slate-900 mt-1">{vendor.name}</h1>
              <p className="text-slate-500 mt-1">Verified couple count: <span className="font-semibold text-slate-700">{vendor.verified_count}</span> (Past year window)</p>
            </div>
            <button
              onClick={handleRegenerateSummary}
              disabled={analyzing}
              className="bg-rose-600 hover:bg-rose-700 text-white font-medium px-6 py-3 rounded-xl shadow transition disabled:opacity-50 flex items-center space-x-2"
            >
              {analyzing ? 'Analyzing Sentiments...' : '✨ Regenerate AI Summary'}
            </button>
          </div>

          {aiData && (
            <div className="mt-8 bg-rose-50/50 border border-rose-100 rounded-xl p-6">
              <div className="flex items-center justify-between mb-3">
                <h3 className="font-bold text-rose-900 text-lg flex items-center space-x-2">
                  <span>🧠 AI Sentiment & Review Summary</span>
                </h3>
                <span className="bg-rose-100 text-rose-700 text-xs font-bold px-3 py-1 rounded-full">
                  Score: {aiData.sentiment_score} / 5.0
                </span>
              </div>
              <p className="text-slate-700 text-sm leading-relaxed mb-4">{aiData.ai_summary}</p>
              <div className="text-xs text-rose-600 font-medium">
                Synthesized from {aiData.analyzed_reviews_count} qualifying reviews (&gt;10 words, within 1 year).
              </div>
            </div>
          )}
        </div>

        <h2 className="text-2xl font-bold text-slate-900 mb-6">Couple Reviews ({vendor.reviews.length})</h2>
        <div className="space-y-4">
          {vendor.reviews.map(review => {
            const wordCount = review.comment.split().length;
            return (
              <div key={review.id} className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
                <div className="flex items-center justify-between mb-3">
                  <div>
                    <h4 className="font-bold text-slate-900">{review.couple}</h4>
                    <span className="text-xs text-slate-400">{new Date(review.date).toLocaleDateString()}</span>
                  </div>
                  <div className="flex items-center space-x-2">
                    {review.verified && (
                      <span className="bg-emerald-50 text-emerald-700 text-xs font-semibold px-2.5 py-1 rounded-full">
                        ✓ Verified Couple
                      </span>
                    )}
                    <span className="text-amber-500 font-bold">★ {review.rating}</span>
                  </div>
                </div>
                <p className="text-slate-700 text-sm leading-relaxed">{review.comment}</p>
              </div>
            );
          })}
        </div>
      </div>
    </main>
  );
}

export default function ReviewsPage() {
  return (
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center">Loading...</div>}>
      <ReviewContent />
    </Suspense>
  );
}
