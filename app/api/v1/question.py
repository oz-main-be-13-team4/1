# app/api/v1/question.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/random")
async def get_random_question():
    return {"question": "question 테스트 입니다."}
