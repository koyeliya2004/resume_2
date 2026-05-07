from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.resume import router as resume_router

app = FastAPI(
    title="AI Resume Scorer API",
    description="Upload a resume PDF and get section-wise scores + overall score + feedback",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router, prefix="/api", tags=["Resume"])

@app.get("/")
def root():
    return {"message": "AI Resume Scorer API is running!", "status": "ok"}
