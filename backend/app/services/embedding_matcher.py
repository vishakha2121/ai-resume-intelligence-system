from sentence_transformers import SentenceTransformer, util
from app.config import config
import numpy as np

model = SentenceTransformer(config.MODEL_NAME)

def compute_similarity(resume_text, jd_text):
    # Create embeddings
    emb_resume = model.encode(resume_text, convert_to_tensor=True)
    emb_jd = model.encode(jd_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(emb_resume, emb_jd).item()
    # Mock skill/exp/edu scores (in practice, parse skills and compare)
    skill_score = similarity * 0.8
    exp_score = similarity * 0.7
    edu_score = similarity * 0.6
    explanation = f"Overall semantic similarity: {similarity:.2f}. Skills moderately aligned."
    return similarity, skill_score, exp_score, edu_score, explanation