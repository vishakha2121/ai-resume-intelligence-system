from sqlalchemy.orm import Session
from app.database import models

# ---------- Resume ----------
def save_resume(db: Session, filename: str, text: str, parsed_json: str):
    existing = db.query(models.Resume).filter(models.Resume.filename == filename).first()
    if existing:
        existing.text = text
        existing.parsed_data = parsed_json
        db.commit()
        db.refresh(existing)
        return existing
    db_resume = models.Resume(filename=filename, text=text, parsed_data=parsed_json)
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

# ---------- Job Description ----------
def save_jd(db: Session, filename: str, title: str, text: str):
    existing = db.query(models.JobDescription).filter(models.JobDescription.filename == filename).first()
    if existing:
        existing.title = title
        existing.text = text
        db.commit()
        db.refresh(existing)
        return existing
    db_jd = models.JobDescription(filename=filename, title=title, text=text)
    db.add(db_jd)
    db.commit()
    db.refresh(db_jd)
    return db_jd

# ---------- Match Score ----------
def save_match_score(db: Session, resume_id: int, jd_id: int, similarity: float,
                     skills_match: float, experience_match: float, education_match: float,
                     graph_score: float, explanation: str):
    match = models.MatchScore(
        resume_id=resume_id, jd_id=jd_id, similarity=similarity,
        skills_match=skills_match, experience_match=experience_match,
        education_match=education_match, graph_score=graph_score,
        explanation=explanation
    )
    db.add(match)
    db.commit()
    db.refresh(match)
    return match

# ---------- Bias Report ----------
def save_bias_report(db: Session, resume_id: int, gender_bias: float, age_bias: float,
                     race_bias: float, overall_flag: int, details: str):
    report = models.BiasReport(
        resume_id=resume_id, gender_bias_score=gender_bias, age_bias_score=age_bias,
        race_bias_score=race_bias, overall_bias_flag=overall_flag, details=details
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

# ---------- Behavioral Prediction ----------
def save_behavioral(db: Session, resume_id: int, source: str, openness: float,
                    conscientiousness: float, extraversion: float, agreeableness: float,
                    neuroticism: float, risk: float):
    pred = models.BehavioralPrediction(
        resume_id=resume_id, social_data_source=source,
        openness=openness, conscientiousness=conscientiousness,
        extraversion=extraversion, agreeableness=agreeableness,
        neuroticism=neuroticism, job_hopping_risk=risk
    )
    db.add(pred)
    db.commit()
    db.refresh(pred)
    return pred

# ---------- Interview Questions ----------
def save_question(db: Session, resume_id: int, jd_id: int, text: str, q_type: str, difficulty: str):
    q = models.InterviewQuestion(
        resume_id=resume_id, jd_id=jd_id, question_text=text,
        question_type=q_type, difficulty=difficulty
    )
    db.add(q)
    db.commit()
    db.refresh(q)
    return q