# app/api/v1/quote.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/random")
async def get_random_quote():
    return {"quote": "quote 테스트 입니다."}
