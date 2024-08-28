import pytest

from app.cves import schemas
from app.cves.router import get_one_by_id, get_all, create_cves, delete_one_by_id


@pytest.mark.asyncio
class TestCveRouter:

    @pytest.mark.order(1)
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

        result = await create_cves(db_session=session, cves=schemas.PostManyCves(**cves))
        print(result)
        assert result is not None

    @pytest.mark.order(2)
    async def test_get_many(self, session):
        await self.test_create_one(session)
        result = await get_all(db_session=session)
        print(result)
        assert result is not None

    @pytest.mark.order(3)
    async def test_router_get_cve_by_id(self, session):
        await self.test_create_one(session)
        test_id = 1
        result = await get_one_by_id(db_session=session, id_=test_id)
        print(result)
        assert result is not None
