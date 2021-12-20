from aiogram import executor

from app.core.config import dp, config
from app.utils.logger import logger


async def on_startup(dispatcher):
    logger.info(f"Bot waked up! Bot's ID: {config.bot.bot_id}")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
