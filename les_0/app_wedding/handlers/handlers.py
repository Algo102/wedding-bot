import os
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
# from les_0.app_wedding.database.db import db_quiz
from sqlalchemy.ext.asyncio import AsyncSession
from les_0.app_wedding.compilate.sql_pdf import create_jpg_html
from les_0.app_wedding.database.models import Quiz
from les_0.app_wedding.database.orm_query import orm_add_user
from les_0.app_wedding.filters.chat_types import ChatTypeFilter
from les_0.app_wedding.kbds.inline import MenuCallBack, EndMenuCallBack
from les_0.app_wedding.menu_processing import get_menu_content

router = Router()
router.message.filter(ChatTypeFilter(["private"]))


@router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    media, reply_markup = await get_menu_content(session,
                                                 level=0, menu_name="main")
    await message.answer_photo(media.media, caption=media.caption,
                               reply_markup=reply_markup)


async def add_user(callback: types.CallbackQuery, session: AsyncSession):
    user = callback.from_user
    await orm_add_user(
        session,
        user_id=user.id,
    )
    await callback.answer()


async def dell_user(callback: types.CallbackQuery, session: AsyncSession):
    user = callback.from_user
    from sqlalchemy import delete
    query = delete(Quiz).where(Quiz.user_id == user.id)
    await session.execute(query)
    await session.commit()
    await callback.answer()


async def add_values(callback: types.CallbackQuery, session: AsyncSession,
                     values: str):
    from sqlalchemy import update
    user = callback.from_user
    update_mapping = {
        'season': ['winter', 'spring', 'summer', 'autumn'],
        'amount': ['two', 'folks', 'upto100', 'morethan100'],
        'place': ['garden', 'restaurant', 'sea', 'unique'],
        'style': ['classic', 'eccentric', 'modern', 'romantic', 'travel',
                  'vintage'],
        'colors': ['dirtyRose', 'emeraldGreen', 'macchiato', 'quartzPink',
                   'vanillaCream', 'wine'],
        'fashion': ['trapezoidal', 'naiad', 'sheath', 'ballGown', 'overalls',
                    'retro'],
        'costume': ['classicCostume', 'tuxedo', 'casual', 'modernCostume']
    }
    for column, possible_values in update_mapping.items():
        if values in possible_values:
            stmt = (update(Quiz).where(user.id == Quiz.user_id).values
                    (**{column: values}))
            await session.execute(stmt)
            break
    await session.commit()
    await callback.answer()


@router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery,
                    callback_data: MenuCallBack,
                    session: AsyncSession):
    """ Все уровни квиза"""
    if callback_data.menu_name == "main":
        await dell_user(callback, session)
    await add_user(callback, session)
    if callback_data.menu_name == "amount":
        await add_values(callback, session,
                         values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "place":
        await add_values(callback, session,
                         values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "style":
        await add_values(callback, session,
                         values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "colors":
        await add_values(callback, session,
                         values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "fashion":
        await add_values(callback, session,
                         values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "costume":
        await add_values(callback, session,
                         values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "end":
        await add_values(callback, session,
                         values=str(callback_data.page).split('_')[1])
    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )
    await callback.message.edit_media(media=media,
                                      reply_markup=reply_markup)
    await callback.answer()


async def get_quiz_values(session: AsyncSession, user_id: int) -> dict:
    from sqlalchemy import select
    stmt = select(Quiz).where(Quiz.user_id == user_id)
    result = await session.execute(stmt)

    quiz_values = {}
    for row in result.scalars():
        # Преобразуем объект строки в словарь
        row_dict = vars(row)
        row_dict = {key: value for key,
        value in row_dict.items() if not key.startswith('_')}
        quiz_values.update(row_dict)
    return quiz_values


@router.callback_query(EndMenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery,
                    callback_data: EndMenuCallBack,
                    session: AsyncSession):
    """ Результирующий хендлер """
    if callback_data.menu_name == "end":
        create_jpg_html(
            result_data=await get_quiz_values(
                session, user_id=callback.from_user.id),
            user_id=callback.from_user.id)

        print(await get_quiz_values(
            session, user_id=callback.from_user.id))
        await callback.message.answer_document(
            document=FSInputFile(
                f"./app_wedding/compilate/{callback.from_user.id}.jpg"))
        os.remove(f"./app_wedding/compilate/{callback.from_user.id}.jpg")
        os.remove(f"./app_wedding/compilate/{callback.from_user.id}.html")
    await callback.answer()
