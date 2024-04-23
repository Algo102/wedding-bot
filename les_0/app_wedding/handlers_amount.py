from aiogram import F, Router
from aiogram.types import CallbackQuery
import les_0.app_wedding.keyboards as kb
from les_0.app_wedding.database.db import db_quiz

router_six = Router()

""" Второй уровень квиза - Количество гостей """

@router_six.callback_query(F.data == 'together')
async def amount_together(callback: CallbackQuery):
    await callback.answer('Только вдвоем')
    await callback.message.edit_text(
        'Только вдвоем', reply_markup=kb.next_back_amount)
    db_quiz['amount'] = 'together'


@router_six.callback_query(F.data == 'folks')
async def amount_folks(callback: CallbackQuery):
    await callback.answer('Только близкие')
    await callback.message.edit_text(
        'Только близкие', reply_markup=kb.next_back_amount)
    db_quiz['amount'] = 'folks'


@router_six.callback_query(F.data == 'upto100')
async def amount_upto100(callback: CallbackQuery):
    await callback.answer('До 100')
    await callback.message.edit_text(
        'До 100', reply_markup=kb.next_back_amount)
    db_quiz['amount'] = 'upto100'


@router_six.callback_query(F.data == 'more100')
async def amount_more100(callback: CallbackQuery):
    await callback.answer('Более 100')
    await callback.message.edit_text(
        'Более 100', reply_markup=kb.next_back_amount)
    db_quiz['amount'] = 'more100'


@router_six.callback_query(F.data == 'amount')
async def back_amount(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вы передумали?', reply_markup=kb.amount)


@router_six.callback_query(F.data == 'place')
async def next_place(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выбор места проведения свадьбы', reply_markup=kb.place)
