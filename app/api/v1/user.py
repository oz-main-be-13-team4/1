from tortoise import fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True, null=False)
    password = fields.CharField(max_length=50, null=False)
    email = fields.CharField(max_length=100, unique=True, null=False)
    birthday = fields.DateField(null=True)
    gender = fields.CharField(max_length=20, null=True)

    class Meta:
        table = "users"
