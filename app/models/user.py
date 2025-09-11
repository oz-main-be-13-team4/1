
from tortoise import fields, models
import enum

class GenderEnum(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100, unique=True)
    birthday = fields.DateField(null=True)
    gender = fields.CharEnumField(GenderEnum, default=GenderEnum.OTHER)

    bookmarks: fields.ReverseRelation["Bookmark"]
    questions: fields.ReverseRelation["UserQuestion"]

    diaries: fields.ReverseRelation["Diary"]

    class Meta:
        table = "user"

    def __str__(self):
        return self.username
