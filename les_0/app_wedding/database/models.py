from sqlalchemy import DateTime, String, func, Text, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(),
                                              onupdate=func.now())


class Quiz(Base):
    """ Наполнение результирующего словаря """
    __tablename__ = 'quiz'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Numeric, unique=True)
    season: Mapped[str] = mapped_column(String(25), nullable=True)
    amount: Mapped[str] = mapped_column(String(25), nullable=True)
    place: Mapped[str] = mapped_column(String(25), nullable=True)
    style: Mapped[str] = mapped_column(String(25), nullable=True)
    colors: Mapped[str] = mapped_column(String(25), nullable=True)
    fashion: Mapped[str] = mapped_column(String(25), nullable=True)
    costume: Mapped[str] = mapped_column(String(25), nullable=True)


class Banner(Base):
    __tablename__ = 'banner'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(15), unique=True)
    image: Mapped[str] = mapped_column(String(150), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
