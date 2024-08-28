import datetime

import pytest

from app.cves import crud, schemas


@pytest.mark.asyncio
class TestCveRepo:

    @pytest.mark.order(1)
    async def test_create(self, session):
        cve = schemas.PostCve(raw_info={'test': 'Test'}, cve_id='test',
                              description='test',
                              title='test',
                              problem_types='CWE-78', published_date=datetime.datetime(2017, 11, 2, 16, 0),
                              last_modified_date=datetime.datetime(2024, 8, 5, 18, 28, 16, 743000))
        db_res = await crud.CveRepository.create_many(session, cve.model_dump())
        print(db_res)
        assert len(db_res) > 0

    @pytest.mark.order(2)
    async def test_get_many(self, session):
        await self.test_create(session)
        cves = await crud.CveRepository.get_many(session, limit=1)
        print(cves)
        assert cves != []

    @pytest.mark.order(3)
    async def test_get_one_by_cve_id(self, session):
        await self.test_create(session)
        test_id = 'test'
        cve = await crud.CveRepository.get_one_by_cve_id(session, test_id)
        print(cve)
        assert cve is not None

    @pytest.mark.order(4)
    async def test_get_one_by_id(self, session):
        await self.test_create(session)
        test_id = 1
        cve = await crud.CveRepository.get_one_by_id(session, test_id)
        print(cve)
        assert cve is not None

    @pytest.mark.order(5)
    async def test_delete_one_by_id(self, session):
        await self.test_create(session)
        test_id = 1
        cve = await crud.CveRepository.delete_one_by_id(session, test_id)
        print(cve)
        assert cve is not None
