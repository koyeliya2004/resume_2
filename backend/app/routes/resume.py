import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_parser import extract_text_from_pdf
from app.services.groq_extractor import extract_resume_sections

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/extract-resume")
async def extract_resume(file: UploadFile = File(...)):
    """Upload a PDF resume and extract structured sections using Groq LLM."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    temp_filename = f"{uuid.uuid4()}.pdf"
    temp_path = os.path.join(UPLOAD_DIR, temp_filename)

    try:
        with open(temp_path, "wb") as f:
            f.write(await file.read())

        resume_text = extract_text_from_pdf(temp_path)

        if not resume_text.strip():
            raise HTTPException(status_code=400, detail="No text could be extracted from the PDF.")

        extracted_data = extract_resume_sections(resume_text)

        return {
            "success": True,
            "filename": file.filename,
            "data": extracted_data
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
