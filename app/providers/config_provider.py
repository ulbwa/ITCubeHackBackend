from dishka import Provider, Scope, from_context

from app.types import config


class ConfigProvider(Provider):
    scope = Scope.APP

    database_config = from_context(config.DatabaseConfig)
    litestar_config = from_context(config.LitestarConfig)
    s3_config = from_context(config.S3Config)
    app_config = from_context(config.AppConfig)


__all__ = ("ConfigProvider",)
