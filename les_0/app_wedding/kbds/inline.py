from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallBack(CallbackData, prefix="main"):
    menu_name: str
    level: int | None = None
    page: str | None = None


class EndMenuCallBack(CallbackData, prefix="end"):
    menu_name: str
    level: int | None = None


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Старт квиза 🍕": "season",
        "О боте ℹ️": "about_b",
        "О нас 💰": "about",
    }
    for text, menu_name in btns.items():
        if menu_name == 'season':
            keyboard.add(
                InlineKeyboardButton(
                    text=text,
                    callback_data=MenuCallBack(level=10,
                                               menu_name='season',
                                               page='str_one').pack()))

        elif menu_name == 'result':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=1,
                                         menu_name=menu_name).pack()))
        else:
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=level,
                                         menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_season_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Зима": "winter",
        "Весна": "spring",
        "Лето": "summer",
        "Осень": "autumn",
        "Назад": "main",
    }
    for text, menu_name in btns.items():
        if menu_name == 'main':
            keyboard.add(
                InlineKeyboardButton(text='Назад',
                                     callback_data=MenuCallBack(
                                         level=0, menu_name='main',
                                         page='main_main').pack()))
        elif menu_name == 'winter':
            keyboard.add(
                InlineKeyboardButton(text="Зима",
                                     callback_data=MenuCallBack(
                                         level=20, menu_name='amount',
                                         page='season_winter').pack()))
        elif menu_name == 'spring':
            keyboard.add(
                InlineKeyboardButton(text="Весна",
                                     callback_data=MenuCallBack(
                                         level=20, menu_name='amount',
                                         page='season_spring').pack()))
        elif menu_name == 'summer':
            keyboard.add(
                InlineKeyboardButton(text="Лето",
                                     callback_data=MenuCallBack(
                                         level=20, menu_name='amount',
                                         page='season_summer').pack()))
        elif menu_name == 'autumn':
            keyboard.add(
                InlineKeyboardButton(text="Осень",
                                     callback_data=MenuCallBack(
                                         level=20, menu_name='amount',
                                         page='season_autumn').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_amount_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Только в 2м": "two",
        "Только близкие": "folks",
        "До ста": "upto100",
        "Больше 100": "morethan100",
        "Назад": "start2",
    }
    for text, menu_name in btns.items():
        if menu_name == "start2":
            keyboard.add(
                InlineKeyboardButton(text='Назад',
                                     callback_data=MenuCallBack(
                                         level=10, menu_name='season',
                                         page='amount_season').pack()))
        elif menu_name == 'two':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=30, menu_name='place',
                                         page='amount_two').pack()))
        elif menu_name == 'folks':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=30, menu_name='place',
                                         page='amount_folks').pack()))
        elif menu_name == 'upto100':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=30, menu_name='place',
                                         page='amount_upto100').pack()))
        elif menu_name == 'morethan100':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=30, menu_name='place',
                                         page='amount_morethan100').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_place_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "В саду": "garden",
        "Ресторан": "restaurant",
        "На берегу моря": "sea",
        "Уникальное место": "unique",
        "Назад": "start3",
    }
    for text, menu_name in btns.items():
        if menu_name == "start3":
            keyboard.add(
                InlineKeyboardButton(text='Назад',
                                     callback_data=MenuCallBack(
                                         level=20, menu_name='amount',
                                         page='place_amount').pack()))
        elif menu_name == 'garden':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=40, menu_name='style',
                                         page='place_garden').pack()))
        elif menu_name == 'restaurant':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=40, menu_name='style',
                                         page='place_restaurant').pack()))
        elif menu_name == 'sea':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=40, menu_name='style',
                                         page='place_sea').pack()))
        elif menu_name == 'unique':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=40, menu_name='style',
                                         page='place_unique').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_style_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Классическая": "classic",
        "Эксцентричная": "eccentric",
        "Модерн": "modern",
        "Романтическая": "romantic",
        "Путешествие": "travel",
        "Винтажная": "vintage",
        "Назад": "start4",
    }
    for text, menu_name in btns.items():
        if menu_name == "start4":
            keyboard.add(
                InlineKeyboardButton(text='Назад',
                                     callback_data=MenuCallBack(
                                         level=30, menu_name='place',
                                         page='style_place').pack()))
        elif menu_name == 'classic':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=50, menu_name='colors',
                                         page='style_classic').pack()))
        elif menu_name == 'eccentric':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=50, menu_name='colors',
                                         page='style_eccentric').pack()))
        elif menu_name == 'modern':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=50, menu_name='colors',
                                         page='style_modern').pack()))
        elif menu_name == 'romantic':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=50, menu_name='colors',
                                         page='style_romantic').pack()))
        elif menu_name == 'travel':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=50, menu_name='colors',
                                         page='style_travel').pack()))
        elif menu_name == 'vintage':
            keyboard.add(
                InlineKeyboardButton(text=text,
                                     callback_data=MenuCallBack(
                                         level=50, menu_name='colors',
                                         page='style_vintage').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_colors_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Пыльная роза": "dirtyRose",
        "Изумрудно-зеленый": "emeraldGreen",
        "Капучино": "macchiato",
        "Розовый кварц": "quartzPink",
        "Ванильный": "vanillaCream",
        "Винный": "wine",
        "Назад": "start5",
    }
    for text, menu_name in btns.items():
        if menu_name == "start5":
            keyboard.add(
                InlineKeyboardButton(
                    text='Назад', callback_data=MenuCallBack(
                        level=40, menu_name='style',
                        page='colors_style').pack()))
        elif menu_name == 'dirtyRose':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=60, menu_name='fashion',
                        page='colors_dirtyRose').pack()))
        elif menu_name == 'emeraldGreen':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=60, menu_name='fashion',
                        page='colors_emeraldGreen').pack()))
        elif menu_name == 'macchiato':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=60, menu_name='fashion',
                        page='colors_macchiato').pack()))
        elif menu_name == 'quartzPink':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=60, menu_name='fashion',
                        page='colors_quartzPink').pack()))
        elif menu_name == 'vanillaCream':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=60, menu_name='fashion',
                        page='colors_vanillaCream').pack()))
        elif menu_name == 'wine':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=60, menu_name='fashion',
                        page='colors_wine').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_fashion_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Трапециевидный силуэт": "trapezoidal",
        "Русалка": "naiad",
        "Футляр": "sheath",
        "Бальное платье": "ballGown",
        "Комбинезон": "overalls",
        "Ретро": "retro",
        "Назад": "start6",
    }
    for text, menu_name in btns.items():
        if menu_name == "start6":
            keyboard.add(
                InlineKeyboardButton(
                    text='Назад', callback_data=MenuCallBack(
                        level=50, menu_name='colors',
                        page='fashion_colors').pack()))
        elif menu_name == 'trapezoidal':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=70, menu_name="costume",
                        page='fashion_trapezoidal').pack()))
        elif menu_name == 'naiad':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=70, menu_name="costume",
                        page='fashion_naiad').pack()))
        elif menu_name == 'sheath':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=70, menu_name="costume",
                        page='fashion_sheath').pack()))
        elif menu_name == 'ballGown':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=70, menu_name="costume",
                        page='fashion_ballGown').pack()))
        elif menu_name == 'overalls':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=70, menu_name="costume",
                        page='fashion_overalls').pack()))
        elif menu_name == 'retro':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=70, menu_name="costume",
                        page='fashion_retro').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_costume_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Классика": "classicCostume",
        "Смокинг": "tuxedo",
        "Кэжуал": "casual",
        "Современный костюм": "modernCostume",
        "Назад": "start7",
    }
    for text, menu_name in btns.items():
        if menu_name == "start7":
            keyboard.add(
                InlineKeyboardButton(
                    text='Назад', callback_data=MenuCallBack(
                        level=60, menu_name='fashion',
                        page='costume_fashion').pack()))
        elif menu_name == 'classicCostume':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=80, menu_name='end',
                        page='costume_classicCostume').pack()))
        elif menu_name == 'tuxedo':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=80, menu_name='end',
                        page='costume_tuxedo').pack()))
        elif menu_name == 'casual':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=80, menu_name='end',
                        page='costume_casual').pack()))
        elif menu_name == 'modernCostume':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=80, menu_name='end',
                        page='costume_modernCostume').pack()))
    return keyboard.adjust(*sizes).as_markup()


def get_user_end_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Ваш результат": "result",
        "Пройти еще раз": "again",
    }
    for text, menu_name in btns.items():
        if menu_name == "result":
            keyboard.add(
                InlineKeyboardButton(
                    text='Ваш результат',
                    callback_data=EndMenuCallBack(
                        level=80,
                        menu_name='end').pack()))
        elif menu_name == 'again':
            keyboard.add(
                InlineKeyboardButton(
                    text=text, callback_data=MenuCallBack(
                        level=0, menu_name='main',
                        page='again_main').pack()))
    return keyboard.adjust(*sizes).as_markup()