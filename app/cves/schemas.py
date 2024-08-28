from datetime import datetime, tzinfo, timedelta, UTC

from pydantic import BaseModel, field_serializer
from pydantic_core._pydantic_core import TzInfo


class PostCve(BaseModel):
    raw_info: dict
    cve_id: str
    description: str | None = None
    title: str | None = None
    problem_types: str | None = None
    published_date: datetime
    last_modified_date: datetime

    class Config:
        from_attributes = True

    @field_serializer('published_date')
    def serialize_published_date(self, value: datetime) -> datetime:
        return value.replace(tzinfo=None)

    @field_serializer('last_modified_date')
    def serialize_last_modified_date(self, value: datetime) -> datetime:
        return value.replace(tzinfo=None)


class ReadCve(PostCve):
    id: int
    description: str
    title: str
    problem_types: str


class PostManyCves(BaseModel):
    cves: list[PostCve]
