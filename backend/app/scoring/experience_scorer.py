from sqlalchemy.orm import Session
from app.database.models import ExperienceDB


def score_experience(extracted_experience: list, db: Session) -> dict:
    """
    Compare extracted experience with experience_db.
    Returns score 0-100 based on role relevance and count.
    """
    if not extracted_experience:
        return {"score": 0.0, "matched_roles": [], "count": 0}

    matched_roles = []
    total_score = 0.0
    all_roles = db.query(ExperienceDB).all()

    for exp in extracted_experience:
        job_title = exp.get("job_title", "").lower()
        description = exp.get("description", "").lower()
        combined = job_title + " " + description

        best_score = 0.0
        best_role = None

        for db_role in all_roles:
            if db_role.role_keyword.lower() in combined:
                if db_role.score_value > best_score:
                    best_score = db_role.score_value
                    best_role = db_role.role_keyword

        if best_role:
            matched_roles.append(best_role)
            total_score += best_score
        else:
            # Give base score even for unknown roles (some experience is better than none)
            total_score += 40.0

    # Normalize: 3+ experiences = full score cap
    experience_count = len(extracted_experience)
    normalized = min(total_score / max(experience_count, 1), 100.0)

    return {
        "score": round(normalized, 2),
        "matched_roles": matched_roles,
        "count": experience_count
    }
