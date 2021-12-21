from aiogram.dispatcher.filters.state import State, StatesGroup


class BaseUser(StatesGroup):
    city = State()
    name = State()
