# app/api/v1/diary.py
from fastapi import APIRouter
from app.models.diary import Diary

router = APIRouter()

@router.get("/")
async def get_diaries():
    diaries = await Diary.all().values()
    return diaries
