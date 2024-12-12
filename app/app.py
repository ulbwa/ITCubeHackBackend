from dishka.integrations.litestar import setup_dishka
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.contrib.pydantic import PydanticPlugin

from app import controllers, ioc


def create_app() -> Litestar:
    container = ioc.create_container()
    cors_config = CORSConfig(allow_origins=["*"], allow_methods=["*"])
    app = Litestar(
        route_handlers=[controllers.http.router],
        exception_handlers=controllers.http.exception_handlers,
        plugins=[PydanticPlugin(prefer_alias=True)],
        cors_config=cors_config,
    )
    setup_dishka(container, app)
    return app


__all__ = ("create_app",)
