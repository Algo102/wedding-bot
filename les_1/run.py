# pip install aiogram
# python.exe -m pip install --upgrade pip  # не обязательно
# pip list  # Смотрим установленные пакеты

# Основа проекта

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN

# Эти переменные - объекты-экземпляры класса от бот и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()
# Диспетчер - основной роутер или в него передаются роутеры
# Его задача обрабатывать обновления: сообщения, колбеки и т.д.


# Пока хендлер пишим тут, отлавливаем команду старт
# Функция принимает объект Message, внутри этой функции с помощью
# класса message, обращаемся к методу answer, который отвечает этому же пользователю
# Декоратор - диспетчер, который ждет сообщение start
@dp.message(CommandStart())
async def cmf_start(message: Message):
    await message.answer('Привет!')


async def main():
    await dp.start_polling(bot)  # функция ожидает обнавления в боте


# Добавили исключение, чтоб не было ошибки при выходе с программы
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # Добавил логирование на время разработки, будут тормоза при более 150 пользователей
    try:
        asyncio.run(main())  # Запускает ассинхронно, только этот файл, приимпорте он не запустится
    except KeyboardInterrupt:
        print('Exit')