from aiogram import F, Router
from aiogram.types import CallbackQuery
import les_0.app_wedding.keyboards as kb
from les_0.app_wedding.database.db import db_quiz

router_four = Router()


@router_four.callback_query(F.data == 'restaurant')
async def place_restaurant(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Банкетный зал', reply_markup=kb.next_back_place)
    db_quiz['place'] = 'restaurant'


@router_four.callback_query(F.data == 'unique')
async def place_unique(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Уникальное локация', reply_markup=kb.next_back_place)
    db_quiz['place'] = 'unique'


@router_four.callback_query(F.data == 'garden')
async def place_garden(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вечеринка в саду', reply_markup=kb.next_back_place)
    db_quiz['place'] = 'garden'


@router_four.callback_query(F.data == 'sea')
async def place_sea(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'У берега моря', reply_markup=kb.next_back_place)
    db_quiz['place'] = 'sea'


@router_four.callback_query(F.data == 'place')
async def back_place(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выберите место проведения еще раз', reply_markup=kb.place)


@router_four.callback_query(F.data == 'style')
async def next_style(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Добро пожаловать в выбор стиля', reply_markup=kb.style)
