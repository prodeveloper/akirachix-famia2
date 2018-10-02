from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField)

DATABASE = SqliteDatabase("animal.db")


class Animal(Model):
    type_animal = CharField(max_length=100, unique=True)
    commercial_prep = TextField()
    homemade_prep = TextField()

    class Meta:
        database = DATABASE


DATABASE.create_tables([Animal], safe=True)
