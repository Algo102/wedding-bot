from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import les_7.app.keyboards as kb  # Добавил свой модуль с клавами
import les_7.app.database.requests as rq
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from les_7.app.middlewares import TestMiddleware

router = Router()
# router.message.middleware(TestMiddleware())  # iner - работает после хендлера
router.message.outer_middleware(TestMiddleware())  # - внешний срабатывает всегда


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! {message.from_user.username}')
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в магазин кроссовок',
                         reply_markup=kb.main)


# reply_markup=kb.main) - подключил созданную клавиатуру к start
# reply_markup=kb.settings - или эту инлайн клаву


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    # await message.answer('Вы выбрали каталог', show_alert=True)  # Уведомление с подтверждением
    await message.answer('Выберите категорию ', reply_markup=await kb.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(
        f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$')

#
# # Создали класс - модель состояние пользователя при регистрации
#
#
# class Reg(StatesGroup):
#     name = State()
#     age = State()
#     number = State()
#
#
#
#
#
# @router.message(Command('help'))
# async def cmd_help(message: Message):
#     await message.answer('Чем тебе помочь?', reply_markup=await kb.inline_cars())
#
#
# # reply_markup=await kb.inline_cars() - await т.к. функция ассинхронная и () т.к. ее вызываем
#
#
# @router.message(F.text == 'Как дела?')
# async def how_are_you(message: Message):
#     await message.answer('All good!')
#
#
# @router.message(F.photo)
# async def get_photo(message: Message):
#     await message.answer(f'ID фото: {message.photo[-1].file_id}')
#
#
# @router.message(Command('get_photo1'))
# async def get_photo(message: Message):
#     await message.answer_photo(
#         photo='AgACAgIAAxkBAAMSZhx8OjFDNaLA8aZoZ803wObrYU8AAnbUMRuNIOlILublV6qT-FQBAAMCAAN4AAM0BA',
#         caption='Прикольный бокал')
#
#
# @router.message(Command('get_photo2'))
# async def get_photo(message: Message):
#     await message.answer_photo(
#         photo='https://img.freepik.com/free-photo/the-adorable-illustration-of-kittens-playing-in-the-forest-generative-ai_260559-483.jpg?size=338&ext=jpg&ga=GA1.1.867424154.1713052800&semt=ais',
#         caption='Котик с интернета')







# @router.callback_query(F.data == 'tee_shirt')
# async def tee_shirt(callback: CallbackQuery):
#     await callback.answer('Вы выбрали раздел футболки')
#     await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())
#
#
# # @router.callback_query(F.data == 'catalog')
# # async def catalog(callback: CallbackQuery):
# # await callback.answer()  # Чтоб телега увидела, что сообщение перехватили и кнопка перестала переливаться
# # await callback.answer('Вы выбрали каталог')  # а можно отправить уведомление для пользователя
# #     await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())
# # Чтоб меню подменялось edit_text, для подмены картинки edit_caption
#
#
# # FSMContext нужен для управления состояниями
#
#
# @router.message(Command('reg'))
# async def register(message: Message, state: FSMContext):
#     await state.set_state(Reg.name)  # Ввели пользователя в состояние регистрации
#     await message.answer('Введите ваше имя')  # Пользователь пишет имя
#
#
# @router.message(Reg.name)  # Ловим состояние регистрации
# async def reg_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)  # Словливаем и сохраняем имя, которое написал пользователь
#     await state.set_state(Reg.age)  # Меняем состояние
#     await message.answer('Введите свой возраст')
#
#
# @router.message(Reg.age)
# async def reg_age(message: Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     await state.set_state(Reg.number)
#     # await message.answer('Введите свой телефон')
#     await message.answer('Введите свой телефон', reply_markup=kb.get_number)
#
#
# # @router.message(Reg.number, F.contact)  # принимает номер телефона с кнопки, свой контакт
# @router.message(Reg.number)  # принимает номер телефона с клавиатуры
# async def reg_number(message: Message, state: FSMContext):
#     await state.update_data(number=message.text)
#     # await state.update_data(number=message.contact.phone_number)
#     data = await state.get_data()
#     await message.answer(
#         f'Регистрация завершена.\nИмя: {data["name"]}\nВозраст: {data["age"]}\nНомер: {data["number"]}')
#     await state.clear()  # Очищаем состояние
