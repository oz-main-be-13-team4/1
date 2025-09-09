from tortoise.contrib.fastapi import register_tortoise
from app.core.config import DB_URL

def init_db(app):
    register_tortoise(
        app,
        db_url=DB_URL,
        modules={"models": ["app.models.user", "app.models.diary", "app.models.quote", "app.models.question"]},
        generate_schemas=True,   # 개발 중엔 True, 운영에서는 False + aerich
        add_exception_handlers=True,
    )
