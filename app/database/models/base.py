from tortoise.fields import *
from tortoise import Model


class TimestampedMixin:
    created_at = DatetimeField(auto_now_add=True)
    updated_at = DatetimeField(auto_now=True)


class AbstractBaseModel(Model):
    id = IntField(pk=True)

    class Meta:
        abstract = True


class BaseUserModel(AbstractBaseModel, TimestampedMixin):
    name = CharField(max_length=50)
    city = CharField(max_length=30)
