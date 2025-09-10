from tortoise import fields, models

class UserQuestion(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="questions", on_delete=fields.CASCADE)
    question = fields.ForeignKeyField("models.Question", related_name="user_questions", on_delete=fields.CASCADE)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "user_question"
        unique_together = ("user", "question")