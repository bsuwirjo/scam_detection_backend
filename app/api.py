from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.scam_detector import ScamDetector
from app.services.ai_service import AIService
from app.cache import Cache
from app.models import ScamClassification
from pydantic import BaseModel 
from .cache import get_redis

app = FastAPI()
cache = Cache()
scam_detector = ScamDetector()

class Message_Body(BaseModel):
    message: str
    question: str = None


@app.post("/detect_scam")
def detect_scam(message_body: Message_Body, db: Session = Depends(get_db)):
    message = message_body.message
    classification = scam_detector.classify(message)
    scam = ScamClassification(
        message_text=message,
        is_scam=classification["is_scam"],
        confidence=classification["confidence"]
    )
    db.add(scam)
    db.commit()
    return {"message": message, "classification": classification}

@app.post("/explain")
def explain(message_body: Message_Body):
    message = message_body.message
    question = message_body.question
    cache_key = f"explanation:{message}:{question or 'default'}"
    cached = cache.get(cache_key)
    if cached:
        return {"message": message, "response": cached}
    if question:
        message = [{"role": "user", "content": f"I am looking at the following message: \n\n{message}"},
         {"role": "user", "content": f"{question}"}]
    else:
        message = [{"role": "user", "content": f"Why is this message a scam? \n\n{message}"}]
    response = AIService.generate_explanation(message)
    cache.set(cache_key, response)
    
    return {"message": message, "response": response}

@app.get("/health")
async def health_check():
    """Health check endpoint for container orchestration"""
    try:
        # Check database connection
        db = next(get_db())
        db.execute("SELECT 1")
        
        # Check Redis connection
        redis = get_redis()
        await redis.ping()
        
        return {"status": "healthy", "services": {"database": "up", "redis": "up"}}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
