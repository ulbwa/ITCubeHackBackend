from app.repositories.announcement_repository import AnnouncementRepository
from app.repositories.instructor_repository import InstructorRepository
from app.repositories.media_repository import MediaRepository
from app.repositories.news_repository import NewsRepository
from app.repositories.study_repository import StudyRepository

__all__ = (
    "AnnouncementRepository",
    "StudyRepository",
    "MediaRepository",
    "NewsRepository",
    "InstructorRepository",
)
