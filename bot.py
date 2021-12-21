import asyncio

import aiogram

from app.core.config import dp
from app.utils.logger import logger
from app.core.strings import TecnicalInfo


async def on_startup(dispatcher):
    print(TecnicalInfo.welcome_message)

    await asyncio.sleep(float("-inf"))  # Чтобы приветствие отображалось первым.

    logger.info(f"Bot waked up!")


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, on_startup=on_startup)
