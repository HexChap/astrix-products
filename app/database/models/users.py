from tortoise import Model
from tortoise.fields import *

from .base import BaseUserModel
from .validators import PhoneNumberValidator


class BuyerModelORM(BaseUserModel):
    categories = CharField(max_length=300)
    org_address = CharField(max_length=150)
    phone_numbers = CharField(validators=[PhoneNumberValidator()])
