import os
from dotenv import load_dotenv
# Load environment variables from the .env file in the backend folder
load_dotenv()
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
from openai import OpenAI


app = FastAPI(title="Vendor Review & AI Summary API (OpenAI)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the OpenAI client (automatically reads OPENAI_API_KEY from environment variables)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

NOW = datetime.utcnow()

DUMMY_VENDORS = [
    {
        "id": 1,
        "name": "Grand Palace Ballroom & Resort",
        "category": "Wedding Venue",
        "rating": 4.9,
        "verified_count": 20,
        "image": "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=600&q=80",
        "reviews": [
            {
                "id": 101,
                "couple": "Sarah & Michael",
                "date": (NOW - timedelta(days=30)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "Holding our wedding reception at Grand Palace Ballroom was the best decision we ever made! The staff went above and beyond to make every moment magical, and our guests are still raving about the food and ambiance.",
            },
            {
                "id": 102,
                "couple": "Jessica & David",
                "date": (NOW - timedelta(days=60)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "An absolutely breathtaking venue with incredible coordination. Every single detail was meticulously handled by the banquet team.",
            },
            {
                "id": 103,
                "couple": "Emily & Chris",
                "date": (NOW - timedelta(days=90)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "The ballroom setup took our breath away as soon as we walked in. Our coordinator ensured everything ran smoothly from start to finish.",
            },
            {
                "id": 104,
                "couple": "Rachel & Mark",
                "date": (NOW - timedelta(days=120)).isoformat(),
                "verified": True,
                "rating": 4,
                "comment": "Gorgeous venue with a stunning backdrop for photos. The catering options were diverse and tasted wonderful during our reception.",
            },
            {
                "id": 105,
                "couple": "Amanda & Jason",
                "date": (NOW - timedelta(days=150)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "All of our guests mentioned it was the best wedding they had ever attended. The hospitality and luxurious atmosphere are unmatched.",
            },
            {
                "id": 106,
                "couple": "Nicole & Brian",
                "date": (NOW - timedelta(days=180)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "We fell in love with the grand chandeliers and historic architecture. The management team made planning effortless and stress-free.",
            },
            {
                "id": 107,
                "couple": "Samantha & Kevin",
                "date": (NOW - timedelta(days=210)).isoformat(),
                "verified": True,
                "rating": 4,
                "comment": "A truly magical location for a large wedding celebration. The seating layout and acoustics during speeches were exceptionally clear.",
            },
            {
                "id": 108,
                "couple": "Ashley & Ryan",
                "date": (NOW - timedelta(days=240)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "Exceptional service from the valet to the late-night snacks. We could not have asked for a more professional wedding venue.",
            },
            {
                "id": 109,
                "couple": "Brittany & Tyler",
                "date": (NOW - timedelta(days=270)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "Every corner of this resort offers incredible photo opportunities. Our bridal suite was spacious, luxurious, and beautifully prepared.",
            },
            {
                "id": 110,
                "couple": "Lauren & Justin",
                "date": (NOW - timedelta(days=300)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "From our initial tour to our final send-off sparkler exit, the experience was phenomenal. Highly recommend this venue to future couples.",
            },
            {
                "id": 111,
                "couple": "Hannah & Kyle",
                "date": (NOW - timedelta(days=400)).isoformat(),
                "verified": True,
                "rating": 4,
                "comment": "Nice place.",
            }
        ]
    },
    {
        "id": 2,
        "name": "Luminous Moments Photography",
        "category": "Photography & Videography",
        "rating": 3.4,
        "verified_count": 18,
        "image": "https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=600&q=80",
        "reviews": [
            {
                "id": 201,
                "couple": "Amanda & Kevin",
                "date": (NOW - timedelta(days=15)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "Luminous Moments captured our wedding day with such breathtaking artistic vision and emotion. Looking through our album feels like reliving the exact feeling of the ceremony all over again!",
            },
            {
                "id": 202,
                "couple": "Rachel & Tom",
                "date": (NOW - timedelta(days=45)).isoformat(),
                "verified": True,
                "rating": 2,
                "comment": "We were quite disappointed with the communication leading up to our big day. Our lead photographer showed up late and missed a few requested family portraits during the ceremony.",
            },
            {
                "id": 203,
                "couple": "Megan & Alex",
                "date": (NOW - timedelta(days=75)).isoformat(),
                "verified": True,
                "rating": 3,
                "comment": "The final pictures turned out okay, but it took nearly four months longer than promised to receive our digital gallery links and printed albums.",
            },
            {
                "id": 204,
                "couple": "Chloe & Nathan",
                "date": (NOW - timedelta(days=105)).isoformat(),
                "verified": True,
                "rating": 4,
                "comment": "Professional and punctual team, though some of the candid reception shots were slightly out of focus due to low lighting conditions.",
            },
            {
                "id": 205,
                "couple": "Danielle & Sean",
                "date": (NOW - timedelta(days=135)).isoformat(),
                "verified": True,
                "rating": 1,
                "comment": "Terrible experience overall. Half of our video footage was corrupted, and customer support was completely unresponsive when we asked for a partial refund.",
            },
            {
                "id": 206,
                "couple": "Victoria & Andrew",
                "date": (NOW - timedelta(days=165)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "The drone shots of our outdoor ceremony venue were stunning beyond words. We are so grateful for their hard work and creativity.",
            },
            {
                "id": 207,
                "couple": "Grace & Matthew",
                "date": (NOW - timedelta(days=195)).isoformat(),
                "verified": True,
                "rating": 3,
                "comment": "Average service. The photographers were polite on-site, but editing styles felt inconsistent across different parts of the wedding day.",
            },
            {
                "id": 208,
                "couple": "Taylor & Jordan",
                "date": (NOW - timedelta(days=225)).isoformat(),
                "verified": True,
                "rating": 2,
                "comment": "Not worth the high price tag. They missed capturing our cake-cutting moment entirely because the second shooter took an unapproved break.",
            },
            {
                "id": 209,
                "couple": "Kayla & Brandon",
                "date": (NOW - timedelta(days=255)).isoformat(),
                "verified": True,
                "rating": 5,
                "comment": "Their artistic eye for natural lighting and framing made our wedding portraits look like high-end editorial spreads.",
            },
            {
                "id": 210,
                "couple": "Morgan & Cody",
                "date": (NOW - timedelta(days=285)).isoformat(),
                "verified": True,
                "rating": 3,
                "comment": "Mixed feelings. Some photos were absolute masterpieces while others looked completely washed out and unedited.",
            },
            {
                "id": 211,
                "couple": "Paige & Logan",
                "date": (NOW - timedelta(days=420)).isoformat(),
                "verified": True,
                "rating": 4,
                "comment": "Good photos.",
            }
        ]
    }
]

@app.get("/api/vendors")
def get_vendors():
    return DUMMY_VENDORS

@app.get("/api/vendors/{vendor_id}")
def get_vendor_detail(vendor_id: int):
    vendor = next((v for v in DUMMY_VENDORS if v["id"] == vendor_id), None)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return vendor

@app.post("/api/vendors/{vendor_id}/regenerate-summary")
def regenerate_ai_summary(vendor_id: int):
    vendor = next((v for v in DUMMY_VENDORS if v["id"] == vendor_id), None)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    one_year_ago = NOW - timedelta(days=365)
    
    # 1. Filter: reviews within past year AND word count > 10
    filtered_reviews = []
    for r in vendor["reviews"]:
        r_date = datetime.fromisoformat(r["date"])
        word_count = len(r["comment"].split())
        if r_date >= one_year_ago and word_count > 10:
            filtered_reviews.append(r)

    if not filtered_reviews:
        return {
            "status": "success",
            "analyzed_reviews_count": 0,
            "sentiment_score": 0.0,
            "ai_summary": "No reviews met the criteria (>10 words and within 1 year) for analysis.",
            "top_qualifying_reviews": []
        }

    # 2. Format filtered reviews text for OpenAI prompt
    reviews_text = "\n".join([
        f"- Couple: {r['couple']} | Rating: {r['rating']}/5 | Comment: {r['comment']}" 
        for r in filtered_reviews
    ])

    prompt = f"""
    You are an expert AI sentiment analyst for wedding vendors. Analyze the following verified couple reviews from the past year:

    {reviews_text}

    Provide a professional 2-3 sentence executive summary highlighting what couples loved or complained about based strictly on these reviews.
    """

    try:
        # 3. Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        
        ai_summary_text = response.choices[0].message.content

        # Calculate average score for the badge display
        total_score = sum([r["rating"] for r in filtered_reviews])
        avg_sentiment = round(total_score / len(filtered_reviews), 1)

        return {
            "status": "success",
            "analyzed_reviews_count": len(filtered_reviews),
            "sentiment_score": avg_sentiment,
            "ai_summary": ai_summary_text.strip(),
            "top_qualifying_reviews": filtered_reviews
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))