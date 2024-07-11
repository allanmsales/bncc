from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates
from use_case import rag
from entity.history import History


router = APIRouter(
    prefix="/agent",
    tags=['AGENT']
)

templates = Jinja2Templates(directory="templates")
history = History()


@router.get("/", response_class=HTMLResponse)
def front_index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "content": []})


@router.post("/send_question")
def get_send_question(request: Request, question: str = Form(...)):
    history.add_to_history_user(question)
    content = rag.rag_pipeline(question, history)
    return templates.TemplateResponse("home.html", {"request": request, "content": content})
