from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import requests
import json
from recommend import recommend_assessments

class RecommendRequest(BaseModel):
    query: str

class Assessment(BaseModel):
    name: str
    url: str
    duration: str
    remote_support: str
    adaptive_support: str
    test_type: str

class RecommendResponse(BaseModel):
    query: str
    recommendations: List[Assessment]

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.post("/recommend", response_model=RecommendResponse)
def recommend(request: RecommendRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query text is required.")

    if query.lower().startswith("http"):
        try:
            page = requests.get(query, headers={"User-Agent": "Mozilla/5.0"})
            page.raise_for_status()
            query = page.text
        except Exception:
            raise HTTPException(status_code=400, detail="Unable to fetch URL content.")

    recommendations = recommend_assessments(query)
    return RecommendResponse(query=request.query, recommendations=recommendations)