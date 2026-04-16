from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.resume_parser import parse_resume
from app.database.session import get_db
from app.database.crud import save_resume
import json

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(('.pdf', '.docx')):
        raise HTTPException(400, "Only PDF or DOCX allowed")
    content = await file.read()
    # Save temporarily
    temp_path = f"uploads/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(content)
    # Parse
    text, parsed_dict = parse_resume(temp_path)
    # Save to DB
    resume_obj = save_resume(db, file.filename, text, json.dumps(parsed_dict))
    return {"resume_id": resume_obj.id, "parsed_data": parsed_dict}