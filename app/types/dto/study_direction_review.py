from uuid import UUID

from pydantic import BaseModel, alias_generators


class StudyDirectionReview(
    BaseModel, populate_by_name=True, alias_generator=alias_generators.to_camel
):
    ref_id: UUID
    author: str
    title: str
    description: str
    rating: int
    program_title: str


__all__ = ("StudyDirectionReview",)
