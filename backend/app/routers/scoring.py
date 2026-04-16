from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.graph_scorer import build_graph, compute_page_rank
from app.services.explainer import explain_match
from app.database.session import get_db
from app.database import models

router = APIRouter()

@router.get("/graph_score/{resume_id}/{jd_id}")
def graph_score(resume_id: int, jd_id: int, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    jd = db.query(models.JobDescription).filter(models.JobDescription.id == jd_id).first()
    if not resume or not jd:
        raise HTTPException(404, "Resume or JD not found")
    graph = build_graph(resume.text, jd.text)
    score = compute_page_rank(graph)
    return {"graph_based_score": score}

@router.get("/explain/{resume_id}/{jd_id}")
def explain(resume_id: int, jd_id: int, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    jd = db.query(models.JobDescription).filter(models.JobDescription.id == jd_id).first()
    if not resume or not jd:
        raise HTTPException(404, "Resume or JD not found")
    explanation = explain_match(resume.text, jd.text)
    return {"explanation": explanation}