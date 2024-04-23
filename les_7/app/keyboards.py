from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from les_7.app.database.requests import get_categories, get_category_item

# Переделали главную клавиатуру под callback, которы будет обрабатывать Callbackquery в handlers
# можно отправлять без callback_data, т.к. текст хендлер сможет поймать
# main = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Каталог', callback_data='catalog'),
#      InlineKeyboardButton(text='Корзина', callback_data='basket')],
#     [InlineKeyboardButton(text='Контакты', callback_data='contacts')],
# ])

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


# one_time_keyboard=True)  # Чтоб исчезала после нажатия


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

#
# # Переделали главную клавиатуру под callback, которы будет обрабатывать Callbackquery в handlers
# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Футболки', callback_data='tee_shirt'),
#      InlineKeyboardButton(text='Кросовки', callback_data='sneackers')],
#     [InlineKeyboardButton(text='Кепки', callback_data='caps')],
# ])
#
# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
#                                                            request_contact=True)]],
#                                  resize_keyboard=True)
#
# # в инлайн ОБЯЗАТЕЛЬНО нужно вставлять не только текст, но и что-то из доступного: ссылки и колбэки ...
# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/watch?v=')]
# ])
#
# # KeyboardBuilder - используется, не для статичных клавиатур, к примеру
# # название кнопок одгружается из списка или БД, который периодически меняется
# cars = ['Tesla', 'Mersedes', 'BMW']
#
#
# async def reply_cars():
#     keyboard = ReplyKeyboardBuilder()
#     for car in cars:
#         keyboard.add(KeyboardButton(text=car))
#     return keyboard.adjust(2).as_markup()  # adjust пишем если хотим указать количество кнопок в строке
#
#
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         # keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
#         keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
#     return keyboard.adjust(2).as_markup()
# # в инлайн ОБЯЗАТЕЛЬНО нужно вставлять не только текст, но и что-то из доступного: ссылки и колбэки ...
