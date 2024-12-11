from typing import AsyncIterable

import orjson
from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)

from app.types import config


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_engine(
        self, app_config: config.AppConfig, db_config: config.DatabaseConfig
    ) -> AsyncEngine:
        return create_async_engine(
            url=str(db_config.url),
            echo=app_config.log_level.casefold() == "debug",
            json_deserializer=orjson.loads,
            json_serializer=orjson.dumps,
            pool_size=db_config.pool_size,
            max_overflow=db_config.max_overflow,
        )

    @provide(scope=Scope.REQUEST)
    async def get_connection(
        self, engine: AsyncEngine
    ) -> AsyncIterable[AsyncConnection]:
        async with engine.connect() as connection:
            yield connection

    @provide(scope=Scope.REQUEST)
    async def get_session(self, engine: AsyncEngine) -> AsyncIterable[AsyncSession]:
        session = AsyncSession(bind=engine)
        yield session
        await session.close()


__all__ = ("DatabaseProvider",)
