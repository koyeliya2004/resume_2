import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.pdf_parser import extract_text_from_pdf
from app.services.groq_extractor import extract_resume_sections
from app.scoring.combined_scorer import score_all_sections
from app.database.models import get_db

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/extract-resume")
async def extract_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    """Upload PDF → extract sections via Groq → score each section → return all scores."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    temp_filename = f"{uuid.uuid4()}.pdf"
    temp_path = os.path.join(UPLOAD_DIR, temp_filename)

    try:
        with open(temp_path, "wb") as f:
            f.write(await file.read())

        # Step 1: Extract text from PDF
        resume_text = extract_text_from_pdf(temp_path)
        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="No text could be extracted from the PDF.")

        # Step 2: Groq extracts structured sections
        extracted_data = extract_resume_sections(resume_text)

        # Step 3: Score each section against the database
        scoring_result = score_all_sections(extracted_data, db)

        return {
            "success": True,
            "filename": file.filename,
            "extracted": extracted_data,
            "scores": scoring_result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
