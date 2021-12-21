from tortoise.fields import *

from .base import AbstractBaseModel


class City(AbstractBaseModel):
    name = CharField(max_length=30)
