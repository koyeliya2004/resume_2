"""Seed the database with initial scoring data."""
from app.database.models import SkillDB, EducationDB, CertificationDB, ExperienceDB, ProjectDB, SessionLocal, init_db


def seed_skills(db):
    skills = [
        # Programming - High demand
        {"skill_name": "Python", "category": "programming", "demand_level": "high", "score_weight": 10.0},
        {"skill_name": "JavaScript", "category": "programming", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "Java", "category": "programming", "demand_level": "high", "score_weight": 8.5},
        {"skill_name": "C++", "category": "programming", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "TypeScript", "category": "programming", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "Go", "category": "programming", "demand_level": "high", "score_weight": 8.5},
        {"skill_name": "Rust", "category": "programming", "demand_level": "medium", "score_weight": 7.5},
        {"skill_name": "SQL", "category": "database", "demand_level": "high", "score_weight": 8.0},
        # ML/AI
        {"skill_name": "TensorFlow", "category": "ml", "demand_level": "high", "score_weight": 9.5},
        {"skill_name": "PyTorch", "category": "ml", "demand_level": "high", "score_weight": 9.5},
        {"skill_name": "Scikit-learn", "category": "ml", "demand_level": "high", "score_weight": 8.5},
        {"skill_name": "Keras", "category": "ml", "demand_level": "medium", "score_weight": 7.5},
        {"skill_name": "XGBoost", "category": "ml", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "Hugging Face", "category": "ml", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "OpenCV", "category": "ml", "demand_level": "medium", "score_weight": 7.0},
        {"skill_name": "NLP", "category": "ml", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "LangChain", "category": "ml", "demand_level": "high", "score_weight": 9.0},
        # Web
        {"skill_name": "React", "category": "web", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "Node.js", "category": "web", "demand_level": "high", "score_weight": 8.5},
        {"skill_name": "FastAPI", "category": "web", "demand_level": "high", "score_weight": 8.5},
        {"skill_name": "Flask", "category": "web", "demand_level": "medium", "score_weight": 7.5},
        {"skill_name": "Django", "category": "web", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "Next.js", "category": "web", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "Tailwind CSS", "category": "web", "demand_level": "high", "score_weight": 7.5},
        {"skill_name": "HTML", "category": "web", "demand_level": "medium", "score_weight": 5.0},
        {"skill_name": "CSS", "category": "web", "demand_level": "medium", "score_weight": 5.0},
        # Cloud
        {"skill_name": "AWS", "category": "cloud", "demand_level": "high", "score_weight": 9.5},
        {"skill_name": "GCP", "category": "cloud", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "Azure", "category": "cloud", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "Docker", "category": "devops", "demand_level": "high", "score_weight": 9.0},
        {"skill_name": "Kubernetes", "category": "devops", "demand_level": "high", "score_weight": 9.5},
        {"skill_name": "Git", "category": "tools", "demand_level": "high", "score_weight": 7.0},
        {"skill_name": "GitHub", "category": "tools", "demand_level": "high", "score_weight": 7.0},
        # Data
        {"skill_name": "Pandas", "category": "data", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "NumPy", "category": "data", "demand_level": "high", "score_weight": 7.5},
        {"skill_name": "Power BI", "category": "data", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "Tableau", "category": "data", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "PostgreSQL", "category": "database", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "MongoDB", "category": "database", "demand_level": "high", "score_weight": 8.0},
        {"skill_name": "Redis", "category": "database", "demand_level": "medium", "score_weight": 7.0},
    ]
    for s in skills:
        exists = db.query(SkillDB).filter(SkillDB.skill_name == s["skill_name"]).first()
        if not exists:
            db.add(SkillDB(**s))
    db.commit()


def seed_education(db):
    education = [
        {"degree": "B.Tech", "tier": 1, "min_cgpa": 8.0, "score_value": 95.0},
        {"degree": "B.Tech", "tier": 2, "min_cgpa": 7.0, "score_value": 80.0},
        {"degree": "B.Tech", "tier": 3, "min_cgpa": 6.0, "score_value": 65.0},
        {"degree": "M.Tech", "tier": 1, "min_cgpa": 8.0, "score_value": 100.0},
        {"degree": "M.Tech", "tier": 2, "min_cgpa": 7.0, "score_value": 85.0},
        {"degree": "MCA", "tier": 1, "min_cgpa": 8.0, "score_value": 85.0},
        {"degree": "MCA", "tier": 2, "min_cgpa": 7.0, "score_value": 70.0},
        {"degree": "BCA", "tier": 1, "min_cgpa": 8.0, "score_value": 70.0},
        {"degree": "BCA", "tier": 2, "min_cgpa": 6.5, "score_value": 55.0},
        {"degree": "B.Sc", "tier": 2, "min_cgpa": 6.0, "score_value": 55.0},
        {"degree": "PhD", "tier": 1, "min_cgpa": 0.0, "score_value": 100.0},
        {"degree": "MBA", "tier": 1, "min_cgpa": 0.0, "score_value": 75.0},
    ]
    for e in education:
        exists = db.query(EducationDB).filter(
            EducationDB.degree == e["degree"],
            EducationDB.tier == e["tier"]
        ).first()
        if not exists:
            db.add(EducationDB(**e))
    db.commit()


def seed_certifications(db):
    certs = [
        {"cert_name": "AWS Certified Solutions Architect", "issuer": "AWS", "industry_value": "high", "score_value": 95.0},
        {"cert_name": "AWS Cloud Practitioner", "issuer": "AWS", "industry_value": "high", "score_value": 80.0},
        {"cert_name": "Google Cloud Professional", "issuer": "Google", "industry_value": "high", "score_value": 95.0},
        {"cert_name": "Google Cloud Associate", "issuer": "Google", "industry_value": "high", "score_value": 80.0},
        {"cert_name": "TensorFlow Developer", "issuer": "Google", "industry_value": "high", "score_value": 90.0},
        {"cert_name": "Azure Fundamentals", "issuer": "Microsoft", "industry_value": "high", "score_value": 75.0},
        {"cert_name": "Azure Data Scientist", "issuer": "Microsoft", "industry_value": "high", "score_value": 90.0},
        {"cert_name": "Oracle AI Foundations", "issuer": "Oracle", "industry_value": "medium", "score_value": 70.0},
        {"cert_name": "IBM Data Science", "issuer": "IBM", "industry_value": "high", "score_value": 85.0},
        {"cert_name": "IBM AI Product Management", "issuer": "IBM", "industry_value": "high", "score_value": 80.0},
        {"cert_name": "Meta Frontend Developer", "issuer": "Meta", "industry_value": "high", "score_value": 85.0},
        {"cert_name": "Deep Learning Specialization", "issuer": "Coursera", "industry_value": "high", "score_value": 90.0},
        {"cert_name": "Machine Learning Specialization", "issuer": "Coursera", "industry_value": "high", "score_value": 88.0},
        {"cert_name": "Kubernetes Administrator", "issuer": "CNCF", "industry_value": "high", "score_value": 95.0},
        {"cert_name": "GitHub Foundations", "issuer": "GitHub", "industry_value": "medium", "score_value": 65.0},
        {"cert_name": "Generative AI", "issuer": "Google", "industry_value": "high", "score_value": 85.0},
    ]
    for c in certs:
        exists = db.query(CertificationDB).filter(CertificationDB.cert_name == c["cert_name"]).first()
        if not exists:
            db.add(CertificationDB(**c))
    db.commit()


def seed_experience(db):
    roles = [
        {"role_keyword": "software engineer", "relevance": "high", "score_value": 90.0},
        {"role_keyword": "data scientist", "relevance": "high", "score_value": 95.0},
        {"role_keyword": "ml engineer", "relevance": "high", "score_value": 95.0},
        {"role_keyword": "backend developer", "relevance": "high", "score_value": 88.0},
        {"role_keyword": "frontend developer", "relevance": "high", "score_value": 85.0},
        {"role_keyword": "full stack developer", "relevance": "high", "score_value": 90.0},
        {"role_keyword": "devops engineer", "relevance": "high", "score_value": 88.0},
        {"role_keyword": "cloud engineer", "relevance": "high", "score_value": 88.0},
        {"role_keyword": "data analyst", "relevance": "high", "score_value": 80.0},
        {"role_keyword": "intern", "relevance": "medium", "score_value": 55.0},
        {"role_keyword": "research", "relevance": "medium", "score_value": 65.0},
        {"role_keyword": "freelance", "relevance": "medium", "score_value": 60.0},
    ]
    for r in roles:
        exists = db.query(ExperienceDB).filter(ExperienceDB.role_keyword == r["role_keyword"]).first()
        if not exists:
            db.add(ExperienceDB(**r))
    db.commit()


def seed_projects(db):
    techs = [
        {"tech_keyword": "machine learning", "complexity": "high", "score_value": 90.0},
        {"tech_keyword": "deep learning", "complexity": "high", "score_value": 92.0},
        {"tech_keyword": "computer vision", "complexity": "high", "score_value": 90.0},
        {"tech_keyword": "nlp", "complexity": "high", "score_value": 90.0},
        {"tech_keyword": "llm", "complexity": "high", "score_value": 95.0},
        {"tech_keyword": "react", "complexity": "medium", "score_value": 75.0},
        {"tech_keyword": "fastapi", "complexity": "medium", "score_value": 78.0},
        {"tech_keyword": "docker", "complexity": "high", "score_value": 85.0},
        {"tech_keyword": "kubernetes", "complexity": "high", "score_value": 90.0},
        {"tech_keyword": "aws", "complexity": "high", "score_value": 88.0},
        {"tech_keyword": "blockchain", "complexity": "high", "score_value": 85.0},
        {"tech_keyword": "real-time", "complexity": "high", "score_value": 85.0},
        {"tech_keyword": "api", "complexity": "medium", "score_value": 70.0},
        {"tech_keyword": "tensorflow", "complexity": "high", "score_value": 88.0},
        {"tech_keyword": "pytorch", "complexity": "high", "score_value": 88.0},
        {"tech_keyword": "flask", "complexity": "medium", "score_value": 65.0},
        {"tech_keyword": "streamlit", "complexity": "medium", "score_value": 65.0},
        {"tech_keyword": "web scraping", "complexity": "medium", "score_value": 60.0},
        {"tech_keyword": "recommendation system", "complexity": "high", "score_value": 88.0},
        {"tech_keyword": "chatbot", "complexity": "medium", "score_value": 75.0},
    ]
    for t in techs:
        exists = db.query(ProjectDB).filter(ProjectDB.tech_keyword == t["tech_keyword"]).first()
        if not exists:
            db.add(ProjectDB(**t))
    db.commit()


def run_seed():
    init_db()
    db = SessionLocal()
    try:
        print("Seeding skills...")
        seed_skills(db)
        print("Seeding education...")
        seed_education(db)
        print("Seeding certifications...")
        seed_certifications(db)
        print("Seeding experience...")
        seed_experience(db)
        print("Seeding projects...")
        seed_projects(db)
        print("Database seeded successfully!")
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
