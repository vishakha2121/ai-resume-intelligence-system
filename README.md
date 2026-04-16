# AI Resume Intelligence & Behavioral Prediction System

A practice project that parses resumes, matches them with job descriptions using semantic similarity, detects bias, predicts behavior from social data, generates interview questions, and provides explainable AI scoring.

## Features
- Resume parsing (PDF/DOCX) with NER
- JD matching using sentence‑transformers
- Bias detection (gender, age, race)
- Behavioral prediction from GitHub/Twitter
- Auto interview question generation (Gemini API)
- Graph‑based scoring & SHAP explanations
- Guardrails for fairness & privacy
- React frontend with dark mode & charts

## Tech Stack
- **Backend:** FastAPI, SQLAlchemy, SQLite, spaCy, sentence‑transformers, Gemini API
- **Frontend:** React, Vite, TailwindCSS, Recharts, D3.js
- **Optional:** Docker

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-resume-intelligence-system