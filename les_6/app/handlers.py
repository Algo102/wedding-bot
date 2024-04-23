from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
<<<<<<< HEAD:les_6/app/handlers.py
import les_6.app.keyboards as kb  # Добавил свой модуль с клавами
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


# Создали класс - модель состояние пользователя при регистрации
class Reg(StatesGroup):
    name = State()
    number = State()
=======
import les_0.app.keyboards as kb

router = Router()
>>>>>>> origin/main:les_0/app/handlers.py


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! {message.from_user.username}',
                        reply_markup=kb.main)


<<<<<<< HEAD:les_6/app/handlers.py
=======
@router.callback_query(F.data == 'about')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали "О нас"')
    await callback.message.edit_text('О нас!', reply_markup=await kb.inline_about())


@router.callback_query(F.data == 'about_b')
async def catalog(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('О боте', reply_markup=await kb.inline_about_b())


# @router.callback_query(F.data == 'Назад')
# async def back_to_main_menu(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.edit_text('Назад', reply_markup=kb.main)


@router.callback_query(F.data.startswith('about_kb_b_Назад'))
async def back_to_main_menu_from_about_b(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Назад', reply_markup=kb.main)







>>>>>>> origin/main:les_0/app/handlers.py
# reply_markup=kb.main) - подключил созданную клавиатуру к start
# reply_markup=kb.settings - или эту инлайн клаву


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Чем тебе помочь?', reply_markup=await kb.inline_cars())


# reply_markup=await kb.inline_cars() - await т.к. функция ассинхронная и () т.к. ее вызываем


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('All good!')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@router.message(Command('get_photo1'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAMSZhx8OjFDNaLA8aZoZ803wObrYU8AAnbUMRuNIOlILublV6qT-FQBAAMCAAN4AAM0BA',
        caption='Прикольный бокал')


@router.message(Command('get_photo2'))
async def get_photo(message: Message):
    await message.answer_photo(
        photo='https://img.freepik.com/free-photo/the-adorable-illustration-of-kittens-playing-in-the-forest-generative-ai_260559-483.jpg?size=338&ext=jpg&ga=GA1.1.867424154.1713052800&semt=ais',
        caption='Котик с интернета')


# @router.callback_query(F.data == 'catalog')
# async def catalog(callback: CallbackQuery):
#     # await callback.answer()  # Чтоб телега увидела, что сообщение перехватили и кнопка перестала переливаться
#     # await callback.answer('Вы выбрали каталог')  # а можно отправить уведомление для пользователя
#     await callback.answer('Вы выбрали каталог', show_alert=True)  # Уведомление с подтверждением
#     await callback.message.answer('Привет от коллБэк')

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог')
    await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())
    # Чтоб меню подменялось edit_text, для подмены картинки edit_caption


# FSMContext нужен для управления состояниями
@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)  # Ввели пользователя в состояние регистрации
    await message.answer('Введите ваше имя')  # Пользователь пишет имя


@router.message(Reg.name)  # Ловим состояние регистрации
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # Словливаем и сохраняем имя, которое написал пользователь
    await state.set_state(Reg.number)  # Меняем состояние
    await message.answer('Введите свой номер телефона')
    # await message.answer('Введите свой номер телефона', reply_markup=клава для ввода контакта)

# @router.message(Reg.number, F.contact)  # валидация контакта
@router.message(Reg.number)
async def two_tree(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()  # get_data достает всю введеную инфу и сохраняет в дата
    await message.answer(f'Регистрация завершена.\nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()  # Очищаем состояние
