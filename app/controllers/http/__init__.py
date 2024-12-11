from litestar import Router

from app.controllers.http.announcement_controller import AnnouncementController

router = Router(
    path="",
    route_handlers=[AnnouncementController],
)
# sexception_handlers = get_exception_handlers()

__all__ = ("router",)  # "exception_handlers"
