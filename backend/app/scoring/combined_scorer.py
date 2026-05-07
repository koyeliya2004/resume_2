from sqlalchemy.orm import Session
from app.scoring.skills_scorer import score_skills
from app.scoring.education_scorer import score_education
from app.scoring.certification_scorer import score_certifications
from app.scoring.experience_scorer import score_experience
from app.scoring.projects_scorer import score_projects

# Section weights — must sum to 1.0
WEIGHTS = {
    "skills": 0.30,
    "experience": 0.25,
    "education": 0.20,
    "certifications": 0.15,
    "projects": 0.10,
}


def score_all_sections(extracted_data: dict, db: Session) -> dict:
    """
    Run all section scorers and return individual + weighted overall score.
    This output is used as features for the ML model.
    """
    skills_result = score_skills(extracted_data.get("skills", []), db)
    education_result = score_education(extracted_data.get("education", []), db)
    cert_result = score_certifications(extracted_data.get("certifications", []), db)
    exp_result = score_experience(extracted_data.get("experience", []), db)
    projects_result = score_projects(extracted_data.get("projects", []), db)

    section_scores = {
        "skills_score": skills_result["score"],
        "education_score": education_result["score"],
        "certification_score": cert_result["score"],
        "experience_score": exp_result["score"],
        "projects_score": projects_result["score"],
    }

    # Weighted overall score (rule-based, before ML model)
    weighted_score = (
        section_scores["skills_score"] * WEIGHTS["skills"] +
        section_scores["education_score"] * WEIGHTS["education"] +
        section_scores["certification_score"] * WEIGHTS["certifications"] +
        section_scores["experience_score"] * WEIGHTS["experience"] +
        section_scores["projects_score"] * WEIGHTS["projects"]
    )

    return {
        "section_scores": section_scores,
        "weighted_score": round(weighted_score, 2),
        "details": {
            "skills": skills_result,
            "education": education_result,
            "certifications": cert_result,
            "experience": exp_result,
            "projects": projects_result,
        }
    }
