from tortoise import fields, models

class Quote(models.Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()
    author = fields.CharField(max_length=120, null=True)

    # 유저 북마크: 다대다 관계
    bookmarked_by: fields.ManyToManyRelation["User"] = fields.ManyToManyField(
        "models.User", related_name="bookmarked_quotes", through="user_quote"
    )

    class Meta:
        table = "quote"
