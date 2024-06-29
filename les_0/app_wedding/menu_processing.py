from aiogram.types import InputMediaPhoto
from sqlalchemy.ext.asyncio import AsyncSession

from les_0.app_wedding.database.orm_query import orm_get_banner
from les_0.app_wedding.kbds.inline import (
    get_user_main_btns, get_user_season_btns, get_user_amount_btns,
    get_user_place_btns, get_user_style_btns, get_user_colors_btns,
    get_user_costume_btns, get_user_fashion_btns, get_user_end_btns,
)


async def main_menu(session, level, menu_name):
    """ Стартовое меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_main_btns(level=level)

    return image, kbds


async def season(session, level, menu_name):
    """ Второй уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_season_btns(level=level)

    return image, kbds


async def amount(session, level, menu_name):
    """ Третий уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_amount_btns(level=level)

    return image, kbds


async def place(session, level, menu_name):
    """ Второй уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_place_btns(level=level)

    return image, kbds


async def style(session, level, menu_name):
    """ Третий уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_style_btns(level=level)

    return image, kbds


async def colors(session, level, menu_name):
    """ Второй уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_colors_btns(level=level)

    return image, kbds


async def fashion(session, level, menu_name):
    """ Третий уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_fashion_btns(level=level)

    return image, kbds


async def costume(session, level, menu_name):
    """ Третий уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_costume_btns(level=level)

    return image, kbds


async def end(session, level, menu_name):
    """ Третий уровень меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_end_btns(level=level)

    return image, kbds


async def get_menu_content(
        session: AsyncSession,
        menu_name: str,
        level: int,
        # page: str | None = None
):
    """ Контент на вывод по уровням (сессия для работы с бд из в,
    левел уровень подтягивания клавиатуры инлайн,
    название меню строковое значение"""
    if level == 0:
        return await main_menu(session, level, menu_name)
    elif level == 10:
        return await season(session, level, menu_name)
    elif level == 20:
        return await amount(session, level, menu_name)
    elif level == 30:
        return await place(session, level, menu_name)
    elif level == 40:
        return await style(session, level, menu_name)
    elif level == 50:
        return await colors(session, level, menu_name)
    elif level == 60:
        return await fashion(session, level, menu_name)
    elif level == 70:
        return await costume(session, level, menu_name)
    elif level == 80:
        return await end(session, level, menu_name)
