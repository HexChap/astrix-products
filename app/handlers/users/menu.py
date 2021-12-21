from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from app.core.config import dp


@dp.message_handler()
async def on_message(msg: types.Message):
    content = msg.text
    author = msg.from_user

    user_type = "user"

    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("<- Назад", callback_data="open_main_menu"))

    if content == "Лента товаров":
        await msg.reply("Пока что не реализовано. Ждите еще полгода...")

    # # TODO: Сделать это все
    elif content == "Личный кабинет":
        if user_type == "partner":
            pass

            # kb.add(
            #     InlineKeyboardButton("Пополнить баланс", callback_data="deposit"),
            #     InlineKeyboardButton("Оплатить подписку", callback_data="buy_subscription")
            # )

            # text = (
            #     "**Ваш профиль:**\n"
            #     f"Имя: `{author.full_name}` ({author.mention})\n"
            #     f"ID: `{author.id}`"
            #     f"Статус: `{db_user.status}`"
            #     f"Баланс: `{db_user.cash}`"
            #     f"Рейтинг: `{db_user.rating}`"
            #     f"Кол-во оценок: `{db_user.assessments_count}`"
            #     f"Действующие подписки: `{db_user.subcsriptions}`"
            # )

        else:
            text = (
                "**Ваш профиль:**\n"
                f"Имя: `{author.full_name}` ({author.mention})\n"
                f"ID: `{author.id}`"
                # f"Статус: `{db_user.status}`"
                # f"Баланс: `{db_user.cash}`"
                # f"Рейтинг: `{db_user.rating}`"
                # f"Кол-во предложений: `{db_user.offers_count}`"
            )

        await msg.reply(text, reply_markup=kb)

    elif content == "Выставить на продажу":
        await msg.reply("Пока что не реализовано.")

    elif content == "Витрина":
        await msg.reply("Пока что не реализовано.")

    elif content == "Правила":
        await msg.reply("Пока что не реализовано.")

    elif content == "Информация":
        await msg.reply("Пока что не реализовано.")

    elif content == "Поддержка":
        await msg.reply("Пока что не реализовано.")

    elif content == "Стать партнёром":
        await msg.reply("Пока что не реализовано.")

    elif content == "Партнёры/рейтинги":
        await msg.reply("Пока что не реализовано.")

    elif content == "Проекты Astrix":
        await msg.reply("Пока что не реализовано.")
