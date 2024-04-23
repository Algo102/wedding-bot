from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from les_0.app_wedding.database.db import db_quiz

from aiogram.utils.formatting import Bold

import les_0.app_wedding.keyboards as kb

router = Router()


#  Отлавливаем команду /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет! {message.from_user.username}',
                         reply_markup=kb.main)


""" Первый уровень квиза - выбор сезона """


@router.callback_query(F.data == 'quiz')
async def season_quiz(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        Bold('Выбор сезона').as_html(), reply_markup=kb.seasons)
    db_quiz.clear()
    db_quiz['user_id'] = callback.message.from_user.id


# @router.message(F.photo)
# async def get_photo(message: Message):
#     await message.answer(f'ID фото: {message.photo[-1].file_id}')


""" 0й Уровень """


@router.callback_query(F.data == 'about')
async def main_about(callback: CallbackQuery):
    await callback.answer('Вы выбрали "О нас"')
    await callback.message.edit_text(
        'Супер команда специалистов из ГБ', reply_markup=kb.back)


@router.callback_query(F.data == 'about_b')
async def main_about_b(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Бот помогает устроить вашу свадьбу', reply_markup=kb.back)


@router.callback_query(F.data.startswith('Назад'))
async def back_main(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'И снова привет', reply_markup=kb.main)
