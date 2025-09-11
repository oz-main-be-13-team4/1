from random import randint
from typing import Optional, List

from app.models import Question, UserQuestion


async def get_random_question() -> Optional[Question]:
    total = await Question.all().count()
    if total == 0:
        return None
    offset = randint(0, max(0, total - 1))
    return await Question.all().offset(offset).limit(1).first()

async def record_user_question(user_id: int, question_id: int) -> None:
    await UserQuestion.get_or_create(user_id=user_id, question_id=question_id)

async def list_user_questions(user_id: int) -> List[Question]:
    qids = await UserQuestion.filter(user_id=user_id).values_list("question_id", flat=True)
    if not qids:
        return []
    return await Question.filter(id__in=list(qids))
