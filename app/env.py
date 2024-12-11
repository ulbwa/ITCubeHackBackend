from pathlib import Path

from app.types import config

APP_CONFIG = config.AppConfig()  # type: ignore
DATABASE_CONFIG = config.DatabaseConfig()  # type: ignore
LITESTAR_CONFIG = config.LitestarConfig()  # type: ignore
S3_CONFIG = config.S3Config()  # type: ignore

PROJECT_PATH = Path(__file__).resolve().parent.parent
__all__ = (
    "PROJECT_PATH",
    "APP_CONFIG",
    "DATABASE_CONFIG",
    "LITESTAR_CONFIG",
    "S3_CONFIG",
)
