from sqlalchemy import select, update, delete, BigInteger
from sqlalchemy.ext.asyncio import AsyncSession

from les_0.app_wedding.database.models import Banner, Quiz


async def orm_add_banner_description(session: AsyncSession, data: dict):
    """ Работа с баннерами (информационными страницами) через админку """
    query = select(Banner)
    result = await session.execute(query)
    if result.first():
        return
    session.add_all([Banner(name=name, description=description)
                     for name, description in data.items()])
    await session.commit()


async def orm_change_banner_image(
        session: AsyncSession, name: str, image: str):
    query = update(Banner).where(Banner.name == name).values(image=image)
    await session.execute(query)
    await session.commit()


async def orm_get_banner(session: AsyncSession, page: str):
    query = select(Banner).where(Banner.name == page)
    result = await session.execute(query)
    return result.scalar()


async def orm_get_info_pages(session: AsyncSession):
    query = select(Banner)
    result = await session.execute(query)
    return result.scalars().all()


async def orm_add_user(
        session: AsyncSession,
        user_id: int
):
    """ Добавляем юзера в БД """
    # query = select(User).where(User.user_id == user_id)
    query = select(Quiz).where(user_id == Quiz.user_id)
    result = await session.execute(query)
    if result.first() is None:
        session.add(
            Quiz(user_id=user_id)
        )
        await session.commit()


async def orm_dell_user(
        session: AsyncSession,
        user_id: int
):
    """ Добавляем юзера в БД """
    query = select(Quiz).where(Quiz.user_id == user_id)
    result = await session.execute(query)
    if result.first() is None:
        await session.delete(
            Quiz(user_id=user_id)
        )
        await session.commit()
