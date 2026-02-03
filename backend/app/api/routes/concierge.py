from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_concierge import generate_reply

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    history: list = []

@router.post("/chat")
def chat(req: ChatRequest):
    reply = generate_reply(req.message, req.history)
    return {"reply": reply}
