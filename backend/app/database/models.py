from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

Base = declarative_base()


class SkillDB(Base):
    __tablename__ = "skills_db"
    id = Column(Integer, primary_key=True, index=True)
    skill_name = Column(String, unique=True, index=True)
    category = Column(String)        # e.g. 'programming', 'ml', 'cloud', 'web'
    demand_level = Column(String)    # 'high', 'medium', 'low'
    score_weight = Column(Float)     # how much this skill contributes


class EducationDB(Base):
    __tablename__ = "education_db"
    id = Column(Integer, primary_key=True, index=True)
    degree = Column(String)          # e.g. 'B.Tech', 'M.Tech', 'BCA', 'MCA'
    tier = Column(Integer)           # 1=top, 2=mid, 3=others
    min_cgpa = Column(Float)
    score_value = Column(Float)      # base score for this degree+tier combo


class CertificationDB(Base):
    __tablename__ = "certification_db"
    id = Column(Integer, primary_key=True, index=True)
    cert_name = Column(String, index=True)
    issuer = Column(String)          # e.g. 'Google', 'AWS', 'IBM', 'Oracle'
    industry_value = Column(String)  # 'high', 'medium', 'low'
    score_value = Column(Float)


class ExperienceDB(Base):
    __tablename__ = "experience_db"
    id = Column(Integer, primary_key=True, index=True)
    role_keyword = Column(String)    # e.g. 'software engineer', 'data scientist'
    relevance = Column(String)       # 'high', 'medium', 'low'
    score_value = Column(Float)


class ProjectDB(Base):
    __tablename__ = "projects_db"
    id = Column(Integer, primary_key=True, index=True)
    tech_keyword = Column(String)    # e.g. 'React', 'TensorFlow', 'FastAPI'
    complexity = Column(String)      # 'high', 'medium', 'low'
    score_value = Column(Float)


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
