from typing import Annotated, Sequence

from fastapi import APIRouter, Path, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.cves import crud, models
from app.cves import schemas
from app.deps import get_db

router = APIRouter(prefix="/cves")


@router.get("/{id}")
async def get_one_by_id(
        id_: int = Path(..., title="The ID of the CVE", gt=0, alias='id'),
        db_session: AsyncSession = Depends(get_db)
) -> schemas.ReadCve:
    print(id_)
    result = await crud.CveRepository.get_one_by_id(db_session, id_)
    return schemas.ReadCve.model_validate(result)


@router.get("/{id}")
async def delete_one_by_id(
        id_: int = Path(..., title="The ID of the CVE", gt=0, alias='id'),
        db_session: AsyncSession = Depends(get_db)
):
    print(id_)
    result = await crud.CveRepository.delete_one_by_id(db_session, id_)
    await db_session.commit()
    return {'result': result}


@router.get("/")
async def get_all(
        limit: Annotated[int, Query(gt=0, le=1_000)] = 100,
        offset: Annotated[int, Query(ge=0)] = 0,
        db_session: AsyncSession = Depends(get_db)
) -> list[schemas.ReadCve]:
    result = await crud.CveRepository.get_many(db_session, limit, offset)
    return [schemas.ReadCve.model_validate(i) for i in result]


@router.post("/")
async def create_cves(cves: schemas.PostManyCves, db_session: AsyncSession = Depends(get_db)) -> list[schemas.ReadCve]:
    cves_: list[dict] = [i.model_dump() for i in cves.cves]
    res: Sequence[models.CveModel] = await crud.CveRepository.create_many(db_session, cves_)

    return [await i.to_dict() for i in res]
