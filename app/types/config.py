from pydantic import AnyHttpUrl, Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="db_")

    url: PostgresDsn
    pool_size: int = 5
    max_overflow: int = 10


class LitestarConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="litestar_")

    host: str
    port: int
    workers: int = Field(alias="WEB_CONCURRENCY", default=1)
    reload: bool = False
    debug: bool = False


class S3Config(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="s3_")

    url: AnyHttpUrl
    access_key: str
    secret_key: str


class AppConfig(BaseSettings):
    log_level: str = "INFO"

    instructor_images_bucket: str
    program_documents_bucket: str
    direction_icons_bucket: str
    announcement_images_bucket: str
    news_gallery_bucket: str


__all__ = "DatabaseConfig", "LitestarConfig", "S3Config", "AppConfig"
