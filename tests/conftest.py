import asyncio
import contextlib

import pytest

from app import db


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
@contextlib.asynccontextmanager
async def session():
    async with db.make_session() as session:
        yield session
