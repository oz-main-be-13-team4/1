
from fastapi import FastAPI
from app.db.database import init_db
from app.api.v1 import auth, diary, quote, question

app = FastAPI()

# DB 초기화
init_db(app)

# 라우터 등록
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(diary.router, prefix="/api/v1/diary", tags=["diary"])
app.include_router(quote.router, prefix="/api/v1/quote", tags=["quote"])
app.include_router(question.router, prefix="/api/v1/question", tags=["question"])
