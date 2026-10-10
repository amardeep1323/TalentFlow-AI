
from fastapi import FastAPI

app = FastAPI(
    title="TalentFlow AI API",
    description="Backend API for TalentFlow AI",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "TalentFlow AI backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "talentflow-api"
    }
