from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

from fastapi.templating import Jinja2Templates

from app.models import ChatRequest
from app.memory import memory_store
from app.chatbot import ask_llm

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "AI Chat API"
    }


@router.post("/chat")
def chat(data: ChatRequest):

    history = memory_store.get_history(data.session_id)

    if len(history) == 0:

        history.append(
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            }
        )

    history.append(
        {
            "role": "user",
            "content": data.message
        }
    )

    reply = ask_llm(history)

    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    return JSONResponse(
        {
            "reply": reply,
            "session_id": data.session_id
        }
    )
