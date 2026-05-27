from fastapi import APIRouter
from app.schemas import ChatRequest
from app.chatbot import get_ai_response

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    reply = get_ai_response(request.message)

    return {
        "user_message": request.message,
        "bot_response": reply
    }