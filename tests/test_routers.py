import pytest

from app.cves import schemas
from app.cves.router import get_one_by_id, get_all, create_cves, delete_one_by_id


@pytest.mark.asyncio
class TestCveRouter:

    async def test_router_get_cve_by_id(self, session):
        test_id = 202170
        async with session as s:
            result = await get_one_by_id(db_session=s, id_=test_id)
        print(result)
        assert result is not None

    async def test_get_many(self, session):
        async with session as s:
            result = await get_all(db_session=s)
        print(result)
        assert result is not None

    async def test_create_one(self, session):
        cves = {
            "cves": [
                {
                    "raw_info": {},
                    "cve_id": "test",
                    "description": "test",
                    "title": "test",
                    "problem_types": "test",
                    "published_date": "2024-08-27T13:54:36.007Z",
                    "last_modified_date": "2024-08-27T13:54:36.007Z"
                }
            ]
        }

        async with session as s:
            result = await create_cves(db_session=s, cves=schemas.PostManyCves(**cves))
            print(result)
            assert result is not None
