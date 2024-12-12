from dishka import AsyncContainer, make_async_container

from app import env, providers
from app.types import config


def create_container() -> AsyncContainer:
    return make_async_container(
        providers.DatabaseProvider(),
        providers.ConfigProvider(),
        providers.RepositoryProvider(),
        providers.S3Provider(),
        context={
            config.AppConfig: env.APP_CONFIG,
            config.DatabaseConfig: env.DATABASE_CONFIG,
            config.LitestarConfig: env.LITESTAR_CONFIG,
            config.S3Config: env.S3_CONFIG,
        },
    )


__all__ = ("create_container",)
