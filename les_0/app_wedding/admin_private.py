from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from sqlalchemy.ext.asyncio import AsyncSession

from les_0.app_wedding.database.orm_query import orm_change_banner_image, orm_get_info_pages
from les_0.app_wedding.filters.chat_types import ChatTypeFilter, IsAdmin
from les_0.app_wedding.kbds.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())

ADMIN_KB = get_keyboard(
    "Добавить/Изменить баннер",
    placeholder="Выберите действие",
    sizes=(1,),
)


@admin_router.message(Command("admin"))
async def admin_features(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=ADMIN_KB)


class AddBanner(StatesGroup):
    """ Микро FSM для загрузки/изменения баннеров """
    image = State()


@admin_router.message(StateFilter(None), F.text == 'Добавить/Изменить баннер')
async def add_image2(message: types.Message, state: FSMContext, session: AsyncSession):
    """ Отправляем перечень информационных страниц бота и становимся в состояние отправки photo """
    pages_names = [page.name for page in await orm_get_info_pages(session)]
    await message.answer(f"Отправьте фото баннера.\nВ описании укажите для какой страницы:\
                         \n{', '.join(pages_names)}")
    await state.set_state(AddBanner.image)


@admin_router.message(AddBanner.image, F.photo)
async def add_banner(message: types.Message, state: FSMContext, session: AsyncSession):
    """ Добавляем/изменяем изображение в таблице (там уже есть записанные страницы по именам:
    main, season, amount, place, style, colors, fashion, costume, end """
    image_id = message.photo[-1].file_id
    for_page = message.caption.strip()
    pages_names = [page.name for page in await orm_get_info_pages(session)]
    if for_page not in pages_names:
        await message.answer(f"Введите нормальное название страницы, например:\
                         \n{', '.join(pages_names)}")
        return
    await orm_change_banner_image(session, for_page, image_id, )
    await message.answer("Баннер добавлен/изменен.")
    await state.clear()


@admin_router.message(AddBanner.image)
async def add_banner2(message: types.Message, state: FSMContext):
    """ Ловим некорректный ввод """
    await message.answer("Отправьте фото баннера или отмена")
