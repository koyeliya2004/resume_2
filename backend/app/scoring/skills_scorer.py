from sqlalchemy.orm import Session
from app.database.models import SkillDB


def score_skills(extracted_skills: list, db: Session) -> dict:
    """
    Compare extracted skills with skills_db.
    Returns score 0-100 and matched/missing skills.
    """
    if not extracted_skills:
        return {"score": 0.0, "matched": [], "total_extracted": 0}

    matched = []
    total_weight = 0.0
    matched_weight = 0.0

    # Normalize extracted skills to lowercase for comparison
    normalized_extracted = [s.lower().strip() for s in extracted_skills]

    # Get all skills from DB
    all_db_skills = db.query(SkillDB).all()

    for db_skill in all_db_skills:
        if db_skill.skill_name.lower() in normalized_extracted:
            matched.append(db_skill.skill_name)
            matched_weight += db_skill.score_weight
        total_weight += db_skill.score_weight

    # Score = (matched weight / max possible weight) * 100
    # Cap max at top 15 skills worth to avoid penalizing specialists
    top_15_weight = sum(
        sorted([s.score_weight for s in all_db_skills], reverse=True)[:15]
    )
    score = min((matched_weight / top_15_weight) * 100, 100.0) if top_15_weight > 0 else 0.0

    return {
        "score": round(score, 2),
        "matched": matched,
        "total_extracted": len(extracted_skills)
    }
