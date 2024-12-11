from typing import Annotated, AsyncIterable

from aiohttp import ClientSession
from aiohttp_s3_client import S3Client
from dishka import FromComponent, Provider, Scope, provide

from app.types import config


class S3Provider(Provider):
    scope = Scope.REQUEST

    @provide
    async def get_session(
        self,
    ) -> AsyncIterable[Annotated[ClientSession, FromComponent("s3")]]:
        session = ClientSession()
        yield session
        await session.close()

    @provide
    async def get_client(
        self,
        session: Annotated[ClientSession, FromComponent("s3")],
        config: config.S3Config,
    ) -> S3Client:
        return S3Client(
            session=session,
            url=str(config.url),
            access_key_id=config.access_key,
            secret_access_key=config.secret_key,
        )


__all__ = ("S3Provider",)
