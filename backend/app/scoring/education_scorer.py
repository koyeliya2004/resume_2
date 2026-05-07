from sqlalchemy.orm import Session
from app.database.models import EducationDB


def score_education(extracted_education: list, db: Session) -> dict:
    """
    Compare extracted education with education_db.
    Returns score 0-100 based on degree type and institution tier.
    """
    if not extracted_education:
        return {"score": 0.0, "details": "No education found"}

    best_score = 0.0
    best_match = None

    for edu in extracted_education:
        degree = edu.get("degree", "").lower()

        # Match degree type
        for db_edu in db.query(EducationDB).all():
            if db_edu.degree.lower() in degree:
                # Try to parse CGPA/percentage from score field
                score_str = edu.get("score", "0")
                try:
                    cgpa = float("".join(filter(lambda x: x.isdigit() or x == ".", score_str)))
                    # Normalize percentage to CGPA scale if > 10
                    if cgpa > 10:
                        cgpa = cgpa / 10
                except:
                    cgpa = 7.0  # default if not parseable

                # Apply CGPA bonus
                base_score = db_edu.score_value
                if cgpa >= db_edu.min_cgpa:
                    final_score = base_score
                else:
                    # Partial score if CGPA below threshold
                    final_score = base_score * 0.75

                if final_score > best_score:
                    best_score = final_score
                    best_match = db_edu.degree

    return {
        "score": round(min(best_score, 100.0), 2),
        "matched_degree": best_match
    }
