from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import resume, jd, bias, behavior, questions, scoring
from app.database.session import engine, Base

app = FastAPI(title="AI Resume Intelligence System", version="1.0.0")

# Allow all origins for development (your frontend may be on port 5173 or 5174)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(resume.router, prefix="/api/resume", tags=["Resume"])
app.include_router(jd.router, prefix="/api/jd", tags=["Job Description"])
app.include_router(bias.router, prefix="/api/bias", tags=["Bias Detection"])
app.include_router(behavior.router, prefix="/api/behavior", tags=["Behavioral Prediction"])
app.include_router(questions.router, prefix="/api/questions", tags=["Interview Questions"])
app.include_router(scoring.router, prefix="/api/scoring", tags=["Scoring & Explainability"])

@app.get("/")
def root():
    return {"message": "AI Resume Intelligence API is running"}