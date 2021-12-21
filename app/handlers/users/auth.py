from app.core.config import dp


@dp.message_handler(commands=["ping"])
async def test(msg):
    await msg.reply("Pong")
