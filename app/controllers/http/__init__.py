from litestar import Router

from app.controllers.http.announcement_controller import AnnouncementController
from app.controllers.http.exception_handlers import get_exception_handlers
from app.controllers.http.news_controller import NewsController
from app.controllers.http.storage_controller import StorageController
from app.controllers.http.study_controller import StudyController

router = Router(
    path="",
    route_handlers=[
        AnnouncementController,
        StudyController,
        StorageController,
        NewsController,
    ],
)
exception_handlers = get_exception_handlers()

__all__ = "router", "exception_handlers", "StudyController"
