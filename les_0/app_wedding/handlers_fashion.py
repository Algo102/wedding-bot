from aiogram import F, Router
from aiogram.types import CallbackQuery
import les_0.app_wedding.keyboards as kb
from les_0.app_wedding.database.db import db_quiz

router_five = Router()


@router_five.callback_query(F.data == 'trapezoidal')
async def fashion_trapezoidal(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Трапециевидный силуэт', reply_markup=kb.next_back_fashion)
    db_quiz['fashion'] = 'trapezoidal'


@router_five.callback_query(F.data == 'naiad')
async def fashion_naiad(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Русалка', reply_markup=kb.next_back_fashion)
    db_quiz['fashion'] = 'naiad'


@router_five.callback_query(F.data == 'sheath')
async def fashion_sheath(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Футляр', reply_markup=kb.next_back_fashion)
    db_quiz['fashion'] = 'sheath'


@router_five.callback_query(F.data == 'ball_gown')
async def fashion_ball_gown(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Бальное платье', reply_markup=kb.next_back_fashion)
    db_quiz['fashion'] = 'ball_gown'


@router_five.callback_query(F.data == 'overalls')
async def fashion_overalls(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Комбинезон', reply_markup=kb.next_back_fashion)
    db_quiz['fashion'] = 'overalls'


@router_five.callback_query(F.data == 'retro')
async def fashion_retro(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Ретро', reply_markup=kb.next_back_fashion)
    db_quiz['fashion'] = 'retro'


@router_five.callback_query(F.data == 'fashion')
async def back_fashion(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вернулись в выбор фасона платьев', reply_markup=kb.fashion)


@router_five.callback_query(F.data == 'costume')
async def next_costume(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выберите костюм жениха', reply_markup=kb.costume)
