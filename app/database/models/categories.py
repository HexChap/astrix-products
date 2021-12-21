from tortoise.fields import *

from .base import AbstractBaseModel


class Category(AbstractBaseModel):
    name = CharField(max_length=30)
    description = CharField(max_length=100)


class Tag(AbstractBaseModel):
    category_id = ForeignKeyField(Category)
