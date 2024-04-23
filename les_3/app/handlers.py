from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()
# Для подключения диспетчера из главного файла, и заменили все dp на router
# И в основном файл передаем роутер в dp


@router.message(CommandStart())
async def cmf_start(message: Message):
    await message.reply(f'Привет! {message.from_user.username}')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Чем тебе помочь?')


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('All good!')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo1'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMSZhx8OjFDNaLA8aZoZ803wObrYU8AAnbUMRuNIOlILublV6qT-FQBAAMCAAN4AAM0BA',
        caption='Прикольный бокал')


@router.message(Command('get_photo2'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://img.freepik.com/free-photo/the-adorable-illustration-of-kittens-playing-in-the-forest-generative-ai_260559-483.jpg?size=338&ext=jpg&ga=GA1.1.867424154.1713052800&semt=ais',
        caption='Котик с интернета')
