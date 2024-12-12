from dataclasses import dataclass
from datetime import datetime, timedelta
from uuid import UUID

from app import utils
from app.types.domain.media import Media


@dataclass(kw_only=True, slots=True)
class Instructor:
    ref_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    description: str | None
    seniority: timedelta
    created_at: datetime
    updated_at: datetime | None
    media: Media

    def get_display_name(self) -> str:
        return (
            f"{self.last_name.title()} {self.first_name.title()}"
            if self.middle_name is None
            else f"{self.last_name.title()} {self.first_name.title()} {self.middle_name.title()}"  # noqa: E501
        )

    def get_display_short_name(self) -> str:
        return (
            f"{self.last_name.title()} {self.first_name.title()[0]}."
            if self.middle_name is None
            else f"{self.last_name.title()} {self.first_name.title()[0]}. {self.middle_name.title()[0]}."  # noqa: E501
        )

    def get_display_seniority(self) -> str:
        if self.seniority.days > 365:
            years = self.seniority.days // 365
            if years > 5:
                return "более 5-ти лет"
            return f'{years} {utils.plural(years, ("год", "года", "лет"))}'
        elif self.seniority.days > 30:
            months = self.seniority.days // 30
            return f'{months} {utils.plural(months, ("месяц", "месяца", "месяцев"))}'
        else:
            return f'{self.seniority.days} {utils.plural(self.seniority.days, ("день", "дня", "дней"))}'  # noqa: E501


__all__ = ("Instructor",)
