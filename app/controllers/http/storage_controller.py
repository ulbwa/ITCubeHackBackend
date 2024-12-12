from uuid import UUID

from aiohttp_s3_client import S3Client
from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get
from litestar.response import Response, Stream

from app import interfaces
from app.types import exceptions


class StorageController(Controller):
    path = "/storage"

    @get(path="/{ref_id:uuid}")
    @inject
    async def stream_media_handler(
        self,
        ref_id: UUID,
        *,
        media_repository: FromDishka[interfaces.MediaRepository],
        s3_client: FromDishka[S3Client],
    ) -> Response:
        media = await media_repository.get(ref_id)
        file = await s3_client.get(media.get_file_key())

        if not file.ok:
            # return Redirect(app_config.media_placeholder_path)
            raise exceptions.NotFoundException()

        return Stream(
            file.content.iter_chunked(2**14),
            media_type=file.content_type,
            headers={"Content-Length": str(file.content_length)},
        )


__all__ = ("StorageController",)
