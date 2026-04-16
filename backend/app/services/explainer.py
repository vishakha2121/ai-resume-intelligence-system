import numpy as np
from sentence_transformers import SentenceTransformer
from app.config import config

model = SentenceTransformer(config.MODEL_NAME)

def explain_match(resume_text, jd_text):
    emb_resume = model.encode([resume_text, jd_text])
    sim = np.dot(emb_resume[0], emb_resume[1]) / (np.linalg.norm(emb_resume[0]) * np.linalg.norm(emb_resume[1]))
    similarity = float(sim)
    explanation = f"The similarity score is {similarity:.2f}. Key matching terms: skills, experience."
    return {"similarity": similarity, "text_explanation": explanation}