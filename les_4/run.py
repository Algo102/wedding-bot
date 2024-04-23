# pip install aiogram
# python.exe -m pip install --upgrade pip  # не обязательно
# pip list  # Смотрим установленные пакеты

import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from les_4.app.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)  # Подключили к диспетчеру роутер из хендлерс
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
