# app/api/v1/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
async def signup():
    return {"message": "회원가입 테스트"}

@router.post("/login")
async def login():
    return {"message": "로그인 테스트"}
