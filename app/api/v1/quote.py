# app/api/v1/quote.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.quote import QuoteOut
from app.crud import quote as quote_crud

router = APIRouter(prefix="/quotes", tags=["quotes"])

# 교체 할 부분
async def get_current_user():
    from app.models.user import User
    u = await User.get_or_none(id=1)
    if not u:
        u = await User.create(id=1, username="subin", password="hashed", email="subin@example.com")
    return u



@router.get("/random", response_model=QuoteOut)
async def get_random_quote():
    row = await quote_crud.get_random_quote()
    if not row:
        raise HTTPException(404, "No quotes available")
    return QuoteOut.model_validate(row)

@router.post("/{quote_id}/bookmark", status_code=status.HTTP_201_CREATED)
async def add_bookmark(quote_id: int, user=Depends(get_current_user)):
    created = await quote_crud.add_bookmark(user.id, quote_id)
    if not created:
        return {"detail":"Already bookmarked"}
    return {"detail":"Bookmark added"}

@router.get("/bookmarks", response_model=List[QuoteOut])
async def list_bookmarks(user=Depends(get_current_user)):
    rows = await quote_crud.list_bookmarked_quotes(user.id)
    return [QuoteOut.model_validate(r) for r in rows]

@router.delete("/{quote_id}/bookmark", status_code=status.HTTP_204_NO_CONTENT)
async def remove_bookmark(quote_id: int,  user=Depends(get_current_user)):
    deleted = await quote_crud.remove_bookmark(user.id, quote_id)
    if deleted == 0:
        raise HTTPException(404, "No quotes available")
    return

