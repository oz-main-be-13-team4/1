from pydantic import BaseModel


class QuestionOut(BaseModel):
    id: int
    text: str

    class Config:
        from_attributes = True
