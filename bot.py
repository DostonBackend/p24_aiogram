import os
from asyncio import run

from aiogram.filters import Command
# from distutils import Command

from aiogram.types import BotCommand, Message
from dotenv import load_dotenv

from functions import start, stop, start_menu, info, help, vacancy, finish, register_idora_nomi, \
    register_texnalogiya, register_phone, \
    register_hudud, register_masul_shaxs_user_name, register_murojat_vaqti, register_ish_vaqti
from states import SignUp

load_dotenv()

from aiogram import Bot, Dispatcher

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


async def main(dp) -> None:
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Bot ni ishga tushirish"),
            BotCommand(command="/help", description="Yordam"),
            BotCommand(command="/info", description="Ma`lumotingiz"),
            BotCommand(command="/vacancy", description="Ishga e`lon berish")
        ]
    )
    dp.startup.register(start)
    dp.message.register(start_menu, Command("start"))
    dp.message.register(info, Command("info"))
    dp.message.register(help, Command("help"))
    dp.message.register(vacancy, Command("vacancy"))
    dp.message.register(register_idora_nomi, SignUp.idora_nomi)
    dp.message.register(register_texnalogiya, SignUp.texnalogiya)
    dp.message.register(register_phone, SignUp.phone)
    dp.message.register(register_hudud, SignUp.hudud)
    dp.message.register(register_masul_shaxs_user_name, SignUp.masul_shaxs_user_name)
    dp.message.register(register_murojat_vaqti, SignUp.murojat_vaqti)
    dp.message.register(register_ish_vaqti, SignUp.ish_vaqti)
    dp.message.register(finish, SignUp.maosh)

    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))
