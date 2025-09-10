# app/api/v1/auth.py
from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserOut

router = APIRouter(prefix="/users", tags=["users"])

#회원가입
@router.post("/", response_model=UserOut)
async def create_user(user: UserCreate):
    if await User.filter(username=user.username).exists():
        raise HTTPException(status_code=400, detail= "이미 존재하는 아이디입니다.")
    if await User.filter(email=user.email).exists():
        raise HTTPException(status_code=400, detail= "이미 존재하는 이메일 입니다.")

    #사용자 생성
    obj = await User.create(**user.dict())
    return await UserOut.from_torrent_orm(obj)


# 로그인
@router.post("/login")
async def login(username: str, password: str):
    user = await User.get_or_none(username=username)
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 올바르지 않습니다.")
    return {"message": f"{user.username}님 환영합니다!"}
