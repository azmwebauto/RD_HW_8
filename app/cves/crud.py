import logging
from typing import Mapping, Sequence

from sqlalchemy import insert, select, delete, Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.cves import models


class CveRepository:
    @staticmethod
    async def delete_one_by_id(session: AsyncSession, id_: int):
        statement = delete(models.CveModel).where(models.CveModel.id == id_)
        try:
            cursor_result = await session.execute(statement)
            await session.commit()
            return cursor_result
        except Exception as e:
            logging.error(e)
            await session.rollback()

    @staticmethod
    async def get_one_by_id(session: AsyncSession, id_: int) -> models.CveModel | None:
        statement = select(models.CveModel).where(models.CveModel.id == id_)
        cve_instance = await session.execute(statement)
        return cve_instance.scalar_one_or_none()

    @staticmethod
    async def create_many(session: AsyncSession, cves: Sequence[Mapping]) -> Sequence[models.CveModel]:
        stmt = insert(models.CveModel).returning(models.CveModel).values(cves)
        try:
            result = await session.execute(stmt)
            await session.commit()
            return result.scalars().all()
        except Exception as e:
            logging.error(e)
            await session.rollback()

    @staticmethod
    async def get_many(session: AsyncSession, limit: int = 100, offset: int = 0) -> Sequence[models.CveModel]:
        statement = select(models.CveModel).limit(limit).offset(offset)
        res = await session.execute(statement)
        return res.scalars().all()
