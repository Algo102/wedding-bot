from aiogram import F, Router
from aiogram.types import CallbackQuery
import les_0.app_wedding.handlers_old.keyboards as kb
from les_0.app_wedding.database.db import db_quiz

router_seven = Router()


@router_seven.callback_query(F.data == 'classic_costume')
async def costume_classic(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Классика', reply_markup=kb.next_back_costume)
    db_quiz['costume'] = 'classic_costume'


@router_seven.callback_query(F.data == 'tuxedo')
async def costume_tuxedo(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Смокинг', reply_markup=kb.next_back_costume)
    db_quiz['costume'] = 'tuxedo'


@router_seven.callback_query(F.data == 'casual')
async def costume_casual(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Кэжуал', reply_markup=kb.next_back_costume)
    db_quiz['costume'] = 'casual'


@router_seven.callback_query(F.data == 'modern_costume')
async def costume_something(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Современный костюм', reply_markup=kb.next_back_costume)
    db_quiz['costume'] = 'modern_costume'


@router_seven.callback_query(F.data == 'costume')
async def back_fashion(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вернулись в выбор фасона платьев', reply_markup=kb.costume)


@router_seven.callback_query(F.data == 'result_data')
async def next_result_data(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        str(db_quiz), reply_markup=kb.result_data)
