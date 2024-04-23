# pip install aiogram
# python.exe -m pip install --upgrade pip  # не обязательно
# pip list  # Смотрим установленные пакеты
# pip install sqlalchemy - устаовка БД
# pip install aiosqlite - для асинхронной работы фреймворков

import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from les_7.app.handlers import router
from les_7.app.database.models import async_main


async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)  # Подключили к диспетчеру роутер из хендлерс
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
