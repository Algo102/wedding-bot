from os import getenv
from dotenv import find_dotenv, load_dotenv

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from les_0.app_wedding.common.text_for_db import description_for_info_pages
from les_0.app_wedding.database.models import Base
from les_0.app_wedding.database.orm_query import orm_add_banner_description

load_dotenv(find_dotenv())
engine = create_async_engine(getenv("DB_URL"), echo=True)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with session_maker() as session:
        await orm_add_banner_description(session, description_for_info_pages)


async def drop_db():
    """ Если потребуется удаление """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
