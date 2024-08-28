Create .env by example.env
Change credentials

~~~bash
alembic upgrade heads
poetry install --no-root
uvicorn app.main:app
~~~