import logging

from app.core.config import config

# from .loguru import loguru


async def on_startup_notify(dp):
    for admin_id in config.admin_ids:
        try:
            await dp.bot.send_message(admin_id, "Бот проснулся!")

        except Exception as err:
            logging.exception(err)
