from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

""" Клавиатура для возврата назад пере используется """
back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='Назад')]])

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Старт квиза', callback_data='quiz'),
     InlineKeyboardButton(text='Результат', callback_data='result')],
    [InlineKeyboardButton(text='О боте', callback_data='about_b'),
     InlineKeyboardButton(text='О нас', callback_data='about')],
])

""" Выбор сезона свадьбы """

seasons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💐         Весна         💐', callback_data='spring'),
     InlineKeyboardButton(text='💐         Лето          💐', callback_data='summer')],
    [InlineKeyboardButton(text='💐         Осень         💐', callback_data='autumn'),
     InlineKeyboardButton(text='💐         Зима          💐', callback_data='winter')],
    [InlineKeyboardButton(text='Назад', callback_data='Назад')],
])

next_back_season = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='seasons'),
     InlineKeyboardButton(text='Далее', callback_data='amount')]])

""" Выбор количества участников свадьбы """
amount = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Только вдвоем', callback_data='together'),
     InlineKeyboardButton(text='Только близкие', callback_data='folks')],
    [InlineKeyboardButton(text='До 100', callback_data='upto100'),
     InlineKeyboardButton(text='Более 100', callback_data='more100')],
    [InlineKeyboardButton(text='Назад', callback_data='seasons')],
])

next_back_amount = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='amount'),
     InlineKeyboardButton(text='Далее', callback_data='place')]])

""" Выбор места проведения свадьбы """

place = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Банкетный зал', callback_data='restaurant'),
     InlineKeyboardButton(text='Уникальная локация', callback_data='unique')],
    [InlineKeyboardButton(text='Вечеринка в саду', callback_data='garden'),
     InlineKeyboardButton(text='У берега моря', callback_data='sea')],
    [InlineKeyboardButton(text='Назад', callback_data='amount')],
])

next_back_place = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='place'),
     InlineKeyboardButton(text='Далее', callback_data='style')]])

""" Выбор стиля свадьбы """

style = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Романтическая свадьба', callback_data='romantic'),
     InlineKeyboardButton(text='Винтажная свадьба', callback_data='vintage')],
    [InlineKeyboardButton(text='Эксцентричная свадьба', callback_data='eccentric'),
     InlineKeyboardButton(text='Современная свадьба', callback_data='modern')],
    [InlineKeyboardButton(text='Классическая свадьба', callback_data='classic'),
     InlineKeyboardButton(text='Свадьба в стиле travel', callback_data='travel')],
    [InlineKeyboardButton(text='Назад', callback_data='place')],
])

next_back_style = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='style'),
     InlineKeyboardButton(text='Далее', callback_data='colors')]])

""" Выбор цветовой палитры """

colors = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изумрудно-зеленый', callback_data='emerald_green'),
     InlineKeyboardButton(text='Ванильный', callback_data='vanilla_cream')],
    [InlineKeyboardButton(text='Капучино', callback_data='macchiato'),
     InlineKeyboardButton(text='Пыльная роза', callback_data='dusty_rose')],
    [InlineKeyboardButton(text='Винный', callback_data='wine'),
     InlineKeyboardButton(text='Розовый кварц', callback_data='quartz_pink')],
    [InlineKeyboardButton(text='Назад', callback_data='style')],
])

next_back_colors = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='colors'),
     InlineKeyboardButton(text='Далее', callback_data='fashion_main')]])

""" Выбор фасона платья """

fashion = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Трапециевидный силуэт', callback_data='trapezoidal'),
     InlineKeyboardButton(text='Русалка', callback_data='naiad')],
    [InlineKeyboardButton(text='Футляр', callback_data='sheath'),
     InlineKeyboardButton(text='Бальное платье', callback_data='ball_gown')],
    [InlineKeyboardButton(text='Комбинезон', callback_data='overalls'),
     InlineKeyboardButton(text='Ретро', callback_data='retro')],
    [InlineKeyboardButton(text='Назад', callback_data='colors')],
])

next_back_fashion = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='fashion'),
     InlineKeyboardButton(text='Далее', callback_data='costume')]])

""" Выбор костюма жениха """

costume = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Классика', callback_data='classic_costume'),
     InlineKeyboardButton(text='Смокинг', callback_data='tuxedo')],
    [InlineKeyboardButton(text='Кэжуал', callback_data='casual'),
     InlineKeyboardButton(text='Современный костюм', callback_data='modern_costume')],
    [InlineKeyboardButton(text='Назад', callback_data='fashion')],
])

next_back_costume = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='costume'),
     InlineKeyboardButton(text='Далее', callback_data='result_data')]
])

""" Итог квиза """

result_data = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='costume'),
     InlineKeyboardButton(text='Меню', callback_data='menu')]
])

