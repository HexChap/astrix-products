import asyncio
import aiogram

from aiogram import types

from app.core import keyboards
from app.core.config import dp, bot
from app.utils.logger import logger
from app.core.strings import TecnicalInfo


async def on_startup(dispatcher):
    print(TecnicalInfo.welcome_message)

    await asyncio.sleep(float("-inf"))  # Чтобы приветствие отображалось первым.

    logger.info(f"Bot waked up!")


@dp.callback_query_handler()
async def process_callback(callback: types.CallbackQuery):
    cb_data = callback.data[-1]

    if cb_data == "open_main_menu":
        await bot.send_message(
            callback.from_user.id, 
            "Меню", 
            reply_markup=keyboards.MainMenu
        )

        await bot.answer_callback_query(callback.id)

    elif cb_data == "deposit":
        await bot.send_message(
            callback.from_user.id, 
            "Меню", 
            reply_markup=keyboards.MainMenu
        )

        await bot.answer_callback_query(callback.id, "Пока что не реализовано.")

    elif cb_data == "buy_subscription":
        await bot.send_message(
            callback.from_user.id, 
            "Меню", 
            reply_markup=keyboards.MainMenu
        )

        await bot.answer_callback_query(callback.id, "Пока что не реализовано.")


if __name__ == "__main__":
    aiogram.executor.start_polling(dp, on_startup=on_startup)
