from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    username: str
    email: EmailStr
    birthday: date | None = None
    gender: str | None = None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
