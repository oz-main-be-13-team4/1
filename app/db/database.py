from tortoise.contrib.fastapi import register_tortoise
from app.core.config import DB_URL

# aerich가 인식할 전역 설정 딕셔너리
TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": [
                "app.models.user",
                "app.models.diary",
                "app.models.quote",
                "app.models.question",
                "app.models.bookmark",
                "app.models.user_question",
                "aerich.models",  # aerich migration 기록용
            ],
            "default_connection": "default",
        },
    },
}

def init_db(app):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,  # 개발 중에는 True 가능, 운영/팀 협업 시엔 False + aerich
        add_exception_handlers=True,
    )
