Markdown
# ABIA AI-Powered Wedding Vendor Review MVP

A full-stack demonstration application built to aggregate wedding vendor reviews, filter authentic couple feedback, and generate professional AI-driven sentiment summaries.

## 🚀 Tech Stack
* **Frontend:** Next.js (App Router), Tailwind CSS
* **Backend:** Python, FastAPI, Uvicorn
* **AI Integration:** Supports multiple LLM providers (OpenAI, Google Gemini, Anthropic Claude) via secure environment variables.

---

## 📂 Project Structure
```text
abia-ai-summary/
├── backend/
│   ├── main.py            # FastAPI application and AI routing logic
│   ├── requirements.txt   # Python dependencies
│   └── .env               # API keys (ignored by git)
├── frontend/
│   ├── app/               # Next.js app router pages & components
│   └── package.json       # Node dependencies
└── .gitignore
⚙️ Getting Started Locally
1. Clone the Repository
Bash
git clone [https://github.com/YOUR_USERNAME/abia-ai-summary.git](https://github.com/YOUR_USERNAME/abia-ai-summary.git)
cd abia-ai-summary
2. Setup the Backend
Navigate to the backend directory and install dependencies:

Bash
cd backend
pip install fastapi uvicorn pydantic openai python-dotenv
Create a .env file inside the backend/ folder and add your LLM API key:

Plaintext
OPENAI_API_KEY=your_api_key_here
# OR for Gemini:
# GEMINI_API_KEY=your_gemini_key_here
Run the FastAPI server:

Bash
python -m uvicorn main:app --reload --port 8000
3. Setup the Frontend
Open a new terminal and navigate to the frontend directory:

Bash
cd frontend
npm install
(Optional) Create a .env.local file inside frontend/ if overriding the API URL:

Plaintext
NEXT_PUBLIC_API_URL=http://localhost:8000
Run the Next.js development server:

Bash
npm run dev
Open http://localhost:3000 in your browser.

🤖 AI & Review Filtering Logic
Quality Filter: The platform automatically filters out low-effort or outdated feedback, evaluating only reviews submitted within the past year and containing more than 10 words.

LLM Agnostic: Switch seamlessly between OpenAI (GPT-4o-mini), Google Gemini, or Claude by updating the backend client initialization and providing the respective API secret key.
