from enum import StrEnum


class AnnouncementSortOption(StrEnum):
    DEFAULT = "default"
    CREATED_AT = "created_at"


__all__ = ("AnnouncementSortOption",)
