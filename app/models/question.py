from tortoise import fields, models

class Question(models.Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()

    class Meta:
        table = "question"
