from aiogram import F, Router
from aiogram.types import CallbackQuery

import les_0.app_wedding.keyboards as kb
from les_0.app_wedding.database.db import db_quiz
from les_0.app_wedding.database.engine import session_maker
from les_0.app_wedding.database.models import Quiz

router_eight = Router()


async def add_data(session):
    data = Quiz(tg_id=db_quiz['user_id'],
                season=db_quiz['season'],
                amount=db_quiz['amount'],
                place=db_quiz['place'],
                style=db_quiz['style'],
                colors=db_quiz['colors'],
                fashion=db_quiz['fashion'],
                costume=db_quiz['costume'])
    session.add(data)
    await session.commit()


@router_eight.callback_query(F.data == 'costume')
async def back_fashion(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вернулись в выбор костюмов', reply_markup=kb.costume)


@router_eight.callback_query(F.data == 'menu')
async def next_costume(callback: CallbackQuery):
    async with session_maker() as session:
        await add_data(session)
    await callback.answer()
    await callback.message.edit_text(
        'Меню', reply_markup=kb.main)
