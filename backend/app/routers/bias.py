from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.bias_detector import detect_bias
from app.database.session import get_db
from app.database import models
from app.database.crud import save_bias_report

router = APIRouter()

@router.get("/detect/{resume_id}")
def bias_detection(resume_id: int, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(404, "Resume not found")
    bias_result = detect_bias(resume.text, resume.parsed_data)
    # Save report
    save_bias_report(
        db, resume_id,
        bias_result["gender_bias"], bias_result["age_bias"], bias_result["race_bias"],
        bias_result["overall_flag"], bias_result["details"]
    )
    return bias_result