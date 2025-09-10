from tortoise import fields, models


class Quote(models.Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=50, null=True)

    bookmarked_by: fields.ReverseRelation["Bookmark"]

    class Meta:
        table = "quote"
