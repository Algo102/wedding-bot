# replay кнопки на месте клавиатуры, содержимое которых
# отправляется в чат
# inline кнопки находятся уже в чате, запрос-callback видит только
# сервер, пользователь видит уже результат

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# В клаве д.б. список в котором список в котором кнопки list[list[KeyboardButton]]
# Клавиатура с двумя строками, в первой одна кнопка, во второй две
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
],
    resize_keyboard=True,  # Оптимизировать размеры (уменьшить)
    input_field_placeholder='Выберете пункт меню',
    one_time_keyboard=True)  # Чтоб исчезала после нажатия

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
        keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
    return keyboard.adjust(2).as_markup()
# в инлайн ОБЯЗАТЕЛЬНО нужно вставлять не только текст, но и что-то из доступного: ссылки и колбэки ...
