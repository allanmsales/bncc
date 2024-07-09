from fastapi import APIRouter
from use_case import rag
import schemas

router = APIRouter(
    prefix="/agent",
    tags=['AGENT']
)


@router.post('/send_question')
def get_send_question(question: schemas.Question):
    return rag.rag_pipeline(question.question)
