import aiogram as telegram

from app.core.config import config


class TecnicalInfo:
    welcome_message = (
        "Бот онлайн!\n" 
        f"Никнейм бота: @{config.bot.username}\n"
        f"ID бота: {config.bot.id}\n" 
        f"Развернут на фреймворке: {telegram.__name__} " 
        f"v{telegram.__version__}\n"
    )
