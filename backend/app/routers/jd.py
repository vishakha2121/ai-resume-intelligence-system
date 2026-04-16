from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.resume_parser import extract_text_from_file
from app.database.session import get_db
from app.database.crud import save_jd, save_match_score
from app.services.embedding_matcher import compute_similarity
from app.database import models

router = APIRouter()

@router.post("/upload")
async def upload_jd(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(('.pdf', '.docx', '.txt')):
        raise HTTPException(400, "Invalid file type")
    content = await file.read()
    temp_path = f"uploads/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(content)
    text = extract_text_from_file(temp_path)
    title = file.filename.split('.')[0]
    jd_obj = save_jd(db, file.filename, title, text)
    return {"jd_id": jd_obj.id, "text_preview": text[:500]}

@router.post("/match/{resume_id}/{jd_id}")
async def match_resume_jd(resume_id: int, jd_id: int, db: Session = Depends(get_db)):
    resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    jd = db.query(models.JobDescription).filter(models.JobDescription.id == jd_id).first()
    if not resume or not jd:
        raise HTTPException(404, "Resume or JD not found")
    similarity, skill_score, exp_score, edu_score, explanation = compute_similarity(resume.text, jd.text)
    graph_score = similarity * 0.9
    match = save_match_score(db, resume_id, jd_id, similarity, skill_score, exp_score, edu_score, graph_score, explanation)
    return {"match_score": similarity, "explanation": explanation}