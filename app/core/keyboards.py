from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


MainMenu = ReplyKeyboardMarkup()

MainMenu.add(
    KeyboardButton("Лента товаров"),
    KeyboardButton("Личный кабинет"),
    KeyboardButton("Выставить на продажу"),
    KeyboardButton("Витрина"),
    KeyboardButton("Правила"),
    KeyboardButton("Информация"),
    KeyboardButton("Поддержка"),
    KeyboardButton("Стать партнёром"),
    KeyboardButton("Партнёры/рейтинги"),
    KeyboardButton("Проекты Astrix")
)

