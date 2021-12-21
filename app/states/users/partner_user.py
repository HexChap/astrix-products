from aiogram.dispatcher.filters.state import State

from .base_user import BaseUser


class PartnerRegistration(BaseUser):
    categories = State()
    address = State()
    phone_number = State()

