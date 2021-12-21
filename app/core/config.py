from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import JSONStorage
from app.utils.config_reader import load_config


DATA_DIR = r"data"
STATES_FILE = fr"{DATA_DIR}\states.json"
CONFIG_FILE = fr"{DATA_DIR}\config.ini"

config = load_config(CONFIG_FILE)

bot = Bot(token=config.bot.token)
storage = JSONStorage(STATES_FILE)
dp = Dispatcher(bot, storage=storage)
