from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True)
    text = Column(Text)
    parsed_data = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

class JobDescription(Base):
    __tablename__ = "job_descriptions"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True)
    title = Column(String)
    text = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class MatchScore(Base):
    __tablename__ = "match_scores"
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"))
    jd_id = Column(Integer, ForeignKey("job_descriptions.id"))
    similarity = Column(Float)
    skills_match = Column(Float)
    experience_match = Column(Float)
    education_match = Column(Float)
    graph_score = Column(Float, default=0.0)
    explanation = Column(Text)

class BiasReport(Base):
    __tablename__ = "bias_reports"
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"))
    gender_bias_score = Column(Float)
    age_bias_score = Column(Float)
    race_bias_score = Column(Float)
    overall_bias_flag = Column(Integer)  # 0 or 1
    details = Column(Text)

class BehavioralPrediction(Base):
    __tablename__ = "behavioral_predictions"
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"))
    social_data_source = Column(String)  # github, twitter
    openness = Column(Float)
    conscientiousness = Column(Float)
    extraversion = Column(Float)
    agreeableness = Column(Float)
    neuroticism = Column(Float)
    job_hopping_risk = Column(Float)

class InterviewQuestion(Base):
    __tablename__ = "interview_questions"
    id = Column(Integer, primary_key=True, index=True)
    resume_id = Column(Integer, ForeignKey("resumes.id"))
    jd_id = Column(Integer, ForeignKey("job_descriptions.id"))
    question_text = Column(Text)
    question_type = Column(String)  # technical, behavioral
    difficulty = Column(String)