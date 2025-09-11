import enum
from tortoise import fields
from tortoise.models import Model


class MoodEnum(str, enum.Enum):
    HAPPY = "기쁨"
    SAD = "슬픔"
    CALM = "평온"
    ANGRY = "분노"


class WeatherEnum(str, enum.Enum):
    SUNNY = "맑음"
    CLOUDY = "흐림"
    RAINY = "비"
    SNOWY = "눈"


class Diary(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="diaries")

    title = fields.CharField(max_length=100)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    update_at = fields.DatetimeField(auto_now=True)

    mood = fields.CharEnumField(MoodEnum, null=True)
    weather = fields.CharEnumField(WeatherEnum, null=True)

    class Meta:
        table = "diary"
