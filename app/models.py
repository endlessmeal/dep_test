import peewee
import peewee_async
from app.settings import DATABASE

database = peewee_async.PostgresqlDatabase(
    database=DATABASE.get("NAME"),
    user=DATABASE.get("USER"),
    password=DATABASE.get("PASSWORD"),
    host=DATABASE.get("HOST"),
    port=DATABASE.get("PORT"),
)


class Page(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=255)
    slug = peewee.CharField(max_length=255)

    class Meta:
        database = database
        order_by = ['name']


class Block(peewee.Model):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField(max_length=255)
    url = peewee.CharField(max_length=255)
    page = peewee.ForeignKeyField(Page, backref='blocks')
    views = peewee.IntegerField(default=0, null=True)

    class Meta:
        database = database
        order_by = ['page']
