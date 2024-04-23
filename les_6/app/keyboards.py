from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog'),
     InlineKeyboardButton(text='Корзина', callback_data='basket')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')],
])

<<<<<<< HEAD:les_6/app/keyboards.py
=======

about_kb = ['Назад', 'Контакт', ]


async def inline_about():
    keyboard = InlineKeyboardBuilder()
    for item in about_kb:
        keyboard.add(InlineKeyboardButton(text=item, callback_data=f'about_kb_{item}'))
    return keyboard.adjust(2).as_markup()


async def inline_about_b():
    keyboard = InlineKeyboardBuilder()
    for item in about_kb:
        keyboard.add(InlineKeyboardButton(text=item, callback_data=f'about_kb_b_{item}'))
    return keyboard.adjust(2).as_markup()








>>>>>>> origin/main:les_0/app/keyboards.py
# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Каталог')],
#     [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
# ],
#     resize_keyboard=True,  # Оптимизировать размеры (уменьшить)
#     input_field_placeholder='Выберете пункт меню',)
    # one_time_keyboard=True)  # Чтоб исчезала после нажатия

# в инлайн ОБЯЗАТЕЛЬНО нужно вставлять не только текст, но и что-то из доступного: ссылки и колбэки ...
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/watch?v=')]
])

# KeyboardBuilder - используется, не для статичных клавиатур, к примеру
# название кнопок одгружается из списка или БД, который периодически меняется
cars = ['Tesla', 'Mersedes', 'BMW']


async def reply_cars():
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup()  # adjust пишем если хотим указать количество кнопок в строке


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        # keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
        keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
    return keyboard.adjust(2).as_markup()
# в инлайн ОБЯЗАТЕЛЬНО нужно вставлять не только текст, но и что-то из доступного: ссылки и колбэки ...
