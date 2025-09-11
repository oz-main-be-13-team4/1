from random import randint
from typing import Optional, List

from tortoise.exceptions import IntegrityError

from app.models import Quote, Bookmark


async def get_random_quote():
    total = await Quote.all().count()
    if total == 0:
        return None
    offset = randint(0, max(0, total - 1))
    return await Quote.all().offset(offset).limit(1).first()


async def list_bookmarked_quotes(user_id: int) -> List[Quote]:
    quote_ids = await Bookmark.filter(user_id=user_id).values_list("quote_id", flat=True)
    if not quote_ids:
        return []
    return await Quote.filter(id__in=list(quote_ids))


async def add_bookmark(user_id: int, quote_id: int) -> bool:
    exists = await Bookmark.filter(user_id=user_id, quote_id=quote_id).exists()
    if exists:
        return False
    try:
        await Bookmark.create(user_id=user_id, quote_id=quote_id)
        return True
    except IntegrityError:
        return False


async def remove_bookmark(user_id: int, quote_id: int) -> int:
    return await Bookmark.filter(user_id=user_id, quote_id=quote_id).delete()
