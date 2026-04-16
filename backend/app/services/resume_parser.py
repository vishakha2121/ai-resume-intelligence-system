import re
import json
import pdfplumber
from docx import Document
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_file(filepath):
    if filepath.endswith('.pdf'):
        with pdfplumber.open(filepath) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    elif filepath.endswith('.docx'):
        doc = Document(filepath)
        text = "\n".join(para.text for para in doc.paragraphs)
    else:
        with open(filepath, 'r') as f:
            text = f.read()
    return text

def parse_resume(filepath):
    text = extract_text_from_file(filepath)
    doc = nlp(text)
    # Extract entities
    name = None
    email = None
    phone = None
    skills = []
    for ent in doc.ents:
        if ent.label_ == "PERSON" and name is None:
            name = ent.text
        elif ent.label_ == "EMAIL":
            email = ent.text
        elif ent.label_ == "PHONE":
            phone = ent.text
    # Simple skill extraction (common tech skills)
    skill_keywords = ["python", "java", "sql", "aws", "docker", "react", "node", "tensorflow"]
    for token in doc:
        if token.text.lower() in skill_keywords:
            skills.append(token.text)
    parsed = {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": list(set(skills)),
        "full_text": text[:5000]  # limit
    }
    return text, parsed