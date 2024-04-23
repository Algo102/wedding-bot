from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import les_5.app.keyboards as kb  # Добавил свой модуль с клавами

router = Router()


# Для подключения диспетчера из главного файла, и заменили все dp на router
# И в основном файл передаем роутер в dp


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! {message.from_user.username}',
                        reply_markup=kb.main)


# reply_markup=kb.main) - подключил созданную клавиатуру к start
# reply_markup=kb.settings - или эту инлайн клаву


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Чем тебе помочь?', reply_markup=await kb.inline_cars())


# reply_markup=await kb.inline_cars() - await т.к. функция ассинхронная и () т.к. ее вызываем


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


# @router.callback_query(F.data == 'catalog')
# async def catalog(callback: CallbackQuery):
#     # await callback.answer()  # Чтоб телега увидела, что сообщение перехватили и кнопка перестала переливаться
#     # await callback.answer('Вы выбрали каталог')  # а можно отправить уведомление для пользователя
#     await callback.answer('Вы выбрали каталог', show_alert=True)  # Уведомление с подтверждением
#     await callback.message.answer('Привет от коллБэк')

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог')
    await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())
    # Чтоб меню подменялось edit_text, для подмены картинки edit_caption