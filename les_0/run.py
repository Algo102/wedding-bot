# pip install aiogram
# python.exe -m pip install --upgrade pip  # не обязательно
# pip list  # Смотрим установленные пакеты

import asyncio
import logging

from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from os import getenv
from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher

from les_0.app_wedding.middlewares.db import DataBaseSession
from les_0.app_wedding.database.engine import session_maker, create_db, drop_db
from les_0.app_wedding.handlers.handlers import router

load_dotenv(find_dotenv())

from les_0.app_wedding.user_group import user_group_router
from les_0.app_wedding.admin_private import admin_router

bot = Bot(token=getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []


async def on_startup():
    # await drop_db()

    await create_db()


async def main():
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    dp.include_router(router)
    dp.include_router(user_group_router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print('Я запустился')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
