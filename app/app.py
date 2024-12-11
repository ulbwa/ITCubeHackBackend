from dishka.integrations.litestar import setup_dishka
from litestar import Litestar
from litestar.contrib.pydantic import PydanticPlugin

from app import controllers, ioc


def create_app() -> Litestar:
    container = ioc.create_container()
    app = Litestar(
        route_handlers=[controllers.http.router],
        # exception_handlers=controllers.http.exception_handlers,
        plugins=[PydanticPlugin(prefer_alias=True)],
    )
    setup_dishka(container, app)
    return app


__all__ = ("create_app",)
