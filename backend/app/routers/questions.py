from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.gemini_service import generate_interview_questions
from app.database.session import get_db
from app.database import models
from app.database.crud import save_question

router = APIRouter()

@router.get("/generate/{resume_id}/{jd_id}")
def generate_questions(resume_id: int, jd_id: int, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    jd = db.query(models.JobDescription).filter(models.JobDescription.id == jd_id).first()
    if not resume or not jd:
        raise HTTPException(404, "Resume or JD not found")
    questions = generate_interview_questions(resume.text, jd.text)
    for q in questions:
        save_question(db, resume_id, jd_id, q["text"], q["type"], q["difficulty"])
    return {"questions": questions}