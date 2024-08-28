import datetime

import pytest

from app.cves import crud, schemas


@pytest.mark.asyncio
class TestCveRepo:
    async def test_get_many(self, session):
        async with session as s:
            cves = await crud.CveRepository.get_many(s, limit=1)
            print(cves)
            assert cves is not None

    async def test_get_one_by_id(self, session):
        test_id = 202170
        async with session as s:
            cve = await crud.CveRepository.get_one_by_id(s, test_id)
            print(cve)
            assert cve is not None

    async def test_create(self, session):
        cve = schemas.PostCve(raw_info={'test': 'Test'}, cve_id='test',
                description='test',
                title='test',
                problem_types='CWE-78', published_date=datetime.datetime(2017, 11, 2, 16, 0),
                last_modified_date=datetime.datetime(2024, 8, 5, 18, 28, 16, 743000))
        async with session as s:
            db_res = await crud.CveRepository.create_many(s, cve.model_dump())
            print(db_res)
