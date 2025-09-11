from pydantic import BaseModel
from typing import Optional


class QuoteOut(BaseModel):
    id: int
    content: str
    author: Optional[str] = None

    class Config:
        from_attributes = True