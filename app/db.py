from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.orm import DeclarativeBase

from app import config


def create_engine() -> AsyncEngine:
    return create_async_engine(
        config.DB_URI,
        # echo=True,
    )


ENGINE = create_engine()


@asynccontextmanager
async def make_session() -> AsyncGenerator[AsyncSession, None]:
    session_factory = async_sessionmaker(ENGINE)
    async with session_factory() as session:
        yield session


class Base(AsyncAttrs, DeclarativeBase):
    pass
