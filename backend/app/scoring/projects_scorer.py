from sqlalchemy.orm import Session
from app.database.models import ProjectDB


def score_projects(extracted_projects: list, db: Session) -> dict:
    """
    Compare extracted project tech stacks with projects_db.
    Returns score 0-100 based on tech relevance and complexity.
    """
    if not extracted_projects:
        return {"score": 0.0, "matched_techs": [], "count": 0}

    all_techs = db.query(ProjectDB).all()
    total_score = 0.0
    all_matched_techs = []

    for project in extracted_projects:
        project_name = project.get("project_name", "").lower()
        description = project.get("description", "").lower()
        technologies = [t.lower() for t in project.get("technologies", [])]
        combined = project_name + " " + description + " " + " ".join(technologies)

        project_score = 0.0
        matched_techs = []

        for db_tech in all_techs:
            if db_tech.tech_keyword.lower() in combined:
                project_score += db_tech.score_value * 0.1  # weighted contribution
                matched_techs.append(db_tech.tech_keyword)

        # Cap per project at 100
        project_score = min(project_score, 100.0)
        total_score += project_score
        all_matched_techs.extend(matched_techs)

    # Normalize across projects (2+ good projects = solid score)
    project_count = len(extracted_projects)
    final_score = min(total_score / max(project_count, 1), 100.0)

    # Bonus for having many projects
    if project_count >= 3:
        final_score = min(final_score * 1.1, 100.0)

    return {
        "score": round(final_score, 2),
        "matched_techs": list(set(all_matched_techs)),
        "count": project_count
    }
