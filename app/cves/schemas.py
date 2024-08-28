from dataclasses import Field
from datetime import datetime

from pydantic import BaseModel, field_serializer, Field, field_validator, validator


class PostCve(BaseModel):
    raw_info: dict
    cve_id: str = Field(min_length=1)
    description: str | None = None
    title: str | None = None
    problem_types: str | None = None
    published_date: datetime
    last_modified_date: datetime

    class Config:
        from_attributes = True

    @field_validator('cve_id')
    def cve_is_valid(cls, v):
        assert 'CVE' in v
        return v

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
    cves: list[PostCve] = Field(max_items=1000)


class DeleteResult(BaseModel):
    result: int
