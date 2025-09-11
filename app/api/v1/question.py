# app/api/v1/question.py
from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends

from app.schemas.question import QuestionOut
from app.crud import question as question_crud

router = APIRouter(prefix="/questions", tags=["questions"])

# JWT 의존성으로 교체해야됨
async def get_current_user():
    from app.models.user import User
    u = await User.get_or_none(id=1)
    if not u:
        u = await User.create(id=1, username="ruru", password="hashed", email="ruru@example.com")
    return u

@router.get("/random", response_model=QuestionOut)
async def get_random_question(user=Depends(get_current_user)):
    row = await question_crud.get_random_question()
    if not row:
        raise HTTPException(404, "Question not found")
    await question_crud.record_user_question(user.id, row.id)
    return QuestionOut.model_validate(row)

@router.get("/history", response_model=List[QuestionOut])
async def list_history(user=Depends(get_current_user)):
    rows = await question_crud.list_user_questions(user.id)
    return [QuestionOut.model_validate(r) for r in rows]
