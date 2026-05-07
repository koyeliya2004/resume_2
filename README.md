# AI Resume Scorer

An intelligent resume scoring system that:
- Extracts structured sections from resume PDFs using Groq LLM
- Scores each section (Skills, Education, Certifications, Experience, Projects) against a database
- Predicts an overall resume score using a trained ML model
- Generates prioritized AI feedback on what to improve

## Project Phases
- [x] Phase 1 - Setup & Folder Structure
- [ ] Phase 2 - PDF Parsing + Groq Extraction
- [ ] Phase 3 - Database + Section Scoring
- [ ] Phase 4 - ML Model Training (Kaggle)
- [ ] Phase 5 - Feedback Generation
- [ ] Phase 6 - Frontend UI
- [ ] Phase 7 - Deployment

## Tech Stack
- **Backend**: FastAPI + Python
- **LLM**: Groq API (LLaMA 3.3 70B)
- **PDF Parsing**: PyMuPDF
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **ML Model**: XGBoost + Scikit-learn
- **Frontend**: React + Tailwind CSS
- **Deployment**: Render (backend) + Vercel (frontend)

## Setup
```bash
cd backend
pip install -r requirements.txt
cp ../.env.example .env
# Add your GROQ_API_KEY in .env
uvicorn app.main:app --reload
```

## API Docs
After running, open: http://127.0.0.1:8000/docs
