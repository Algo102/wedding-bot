from sqlalchemy import DateTime, String, BigInteger, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Quiz(Base):
    __tablename__ = 'quiz'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)
    season: Mapped[str] = mapped_column(String(25))
    amount: Mapped[str] = mapped_column(String(25))
    place: Mapped[str] = mapped_column(String(25))
    style: Mapped[str] = mapped_column(String(25))
    colors: Mapped[str] = mapped_column(String(25))
    fashion: Mapped[str] = mapped_column(String(25))
    costume: Mapped[str] = mapped_column(String(25))
