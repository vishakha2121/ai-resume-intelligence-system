from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.services.social_analyzer import fetch_github_data, analyze_behavior
from app.database.session import get_db
from app.database import models
from app.database.crud import save_behavioral

router = APIRouter()

@router.get("/predict/{resume_id}")
def predict_behavior(resume_id: int, github_username: str = Query(None), db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(404, "Resume not found")
    social_text = ""
    source = "none"
    if github_username:
        social_text = fetch_github_data(github_username)
        source = "github"
    # If no social data, use resume text only
    personality, risk = analyze_behavior(resume.text + " " + social_text)
    # Save
    save_behavioral(db, resume_id, source,
                    personality["openness"], personality["conscientiousness"],
                    personality["extraversion"], personality["agreeableness"],
                    personality["neuroticism"], risk)
    return {"personality": personality, "job_hopping_risk": risk}