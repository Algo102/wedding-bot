# pip install aiogram
# python.exe -m pip install --upgrade pip  # не обязательно
# pip list  # Смотрим установленные пакеты

# Основа проекта

import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
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
    # await message.answer('Привет!')
    await message.reply(f'Привет! {message.from_user.username}')  # ответ на собщение
    await message.answer(f'Твой id - {message.from_user.id}')
    # также есть фамилия, премиум, вступление в группу, телефон и т.д.


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Чем тебе помочь?')


# F мейджик фильтр, обрабатывает текст, картинки, фидео, стикеры, локации
@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('All good!')


# Словили фото и отправили пользователю его id
@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


# По команде get_photo1, будет отправляться фото сразу с сервера телеграмма
@dp.message(Command('get_photo1'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMSZhx8OjFDNaLA8aZoZ803wObrYU8AAnbUMRuNIOlILublV6qT-FQBAAMCAAN4AAM0BA',
        caption='Прикольный бокал')


# По команде get_photo2, будет отправляться фото по ссылке
@dp.message(Command('get_photo2'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://img.freepik.com/free-photo/the-adorable-illustration-of-kittens-playing-in-the-forest-generative-ai_260559-483.jpg?size=338&ext=jpg&ga=GA1.1.867424154.1713052800&semt=ais',
        caption='Котик с интернета')


async def main():
    await dp.start_polling(bot)  # функция ожидает обнавления в боте


# Добавили исключение, чтоб не было ошибки при выходе с программы
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # Добавил логирование на время разработки, будут тормоза при более 150 пользователей
    try:
        asyncio.run(main())  # Запускает ассинхронно, только этот файл, приимпорте он не запустится
    except KeyboardInterrupt:
        print('Exit')