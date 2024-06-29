from aiogram import F, Router
from aiogram.types import CallbackQuery
import les_0.app_wedding.handlers_old.keyboards as kb
from les_0.app_wedding.database.db import db_quiz

router_one = Router()

""" Первый под уровень квиза - блок сезонов """


@router_one.callback_query(F.data == 'spring')
async def season_spring(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Весна', reply_markup=kb.next_back_season)
    db_quiz['season'] = 'spring'


@router_one.callback_query(F.data == 'summer')
async def season_summer(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Лето', reply_markup=kb.next_back_season)
    db_quiz['season'] = 'summer'


@router_one.callback_query(F.data == 'autumn')
async def season_autumn(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Осень', reply_markup=kb.next_back_season)
    db_quiz['season'] = 'autumn'


@router_one.callback_query(F.data == 'winter')
async def season_winter(callback: CallbackQuery):
    await callback.answer('Вы выбрали "Выбор сезона"')
    await callback.message.edit_text(
        'Зима', reply_markup=kb.next_back_season)
    db_quiz['season'] = 'winter'


@router_one.callback_query(F.data == 'seasons')
async def back_season(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вернулись на выбор сезона', reply_markup=kb.seasons)


@router_one.callback_query(F.data == 'amount')
async def season_spring(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Какое кол-во гостей вы ожидаете?', reply_markup=kb.amount)
