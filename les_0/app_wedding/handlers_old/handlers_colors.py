from aiogram import F, Router
from aiogram.types import CallbackQuery
import les_0.app_wedding.handlers_old.keyboards as kb
from les_0.app_wedding.database.db import db_quiz

router_three = Router()


@router_three.callback_query(F.data == 'emerald_green')
async def colors_emerald_green(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Изумрудно-зеленый', reply_markup=kb.next_back_colors)
    db_quiz['colors'] = 'emerald_green'


@router_three.callback_query(F.data == 'vanilla_cream')
async def colors_vanilla_cream(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Ванильный', reply_markup=kb.next_back_colors)
    db_quiz['colors'] = 'vanilla_cream'


@router_three.callback_query(F.data == 'macchiato')
async def colors_macchiato(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Капучино', reply_markup=kb.next_back_colors)
    db_quiz['colors'] = 'macchiato'


@router_three.callback_query(F.data == 'dusty_rose')
async def colors_dusty_rose(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Пыльная роза', reply_markup=kb.next_back_colors)
    db_quiz['colors'] = 'dusty_rose'


@router_three.callback_query(F.data == 'wine')
async def colors_wine(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Винный', reply_markup=kb.next_back_colors)
    db_quiz['colors'] = 'wine'


@router_three.callback_query(F.data == 'quartz_pink')
async def colors_quartz_pink(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Розовый кварц', reply_markup=kb.next_back_colors)
    db_quiz['colors'] = 'quartz_pink'


@router_three.callback_query(F.data == 'colors')
async def colors_colors(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Перевыберите цветовую палитру', reply_markup=kb.colors)


@router_three.callback_query(F.data == 'fashion_main')
async def next_fashion(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Выберите силуэт свадебного платья', reply_markup=kb.fashion)
