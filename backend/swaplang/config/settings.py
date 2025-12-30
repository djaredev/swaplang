import logging
import secrets
from pathlib import Path
from importlib.resources import files
from typing import Annotated
from pydantic import (
    AfterValidator,
    BeforeValidator,
    DirectoryPath,
    EmailStr,
    Field,
    FilePath,
    SecretStr,
    computed_field,
    model_validator,
)
from pydantic_settings import BaseSettings

from swaplang.config.logger_config import setup_logger


def _mkdir(value: str | DirectoryPath) -> DirectoryPath:
    path = Path(value)
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created directory at: {path.resolve()}")
    return path


def _resolve_path(value: DirectoryPath) -> DirectoryPath:
    return value.resolve()


class DataDir(BaseSettings):
    DATA_DIR: Annotated[
        DirectoryPath, BeforeValidator(_mkdir), AfterValidator(_resolve_path)
    ] = Path("data/")
    LOG_LEVEL: str = "INFO"

    @computed_field
    @property
    def LOG_PATH(self) -> DirectoryPath:
        return _mkdir(f"{self.DATA_DIR}/logs/") / "swaplang.log"


_data_dir = DataDir()  # type: ignore

setup_logger(log_level=_data_dir.LOG_LEVEL, log_path=_data_dir.LOG_PATH)
logger = logging.getLogger("app")


class Settings(DataDir):
    ENVIRONMENT: str = "dev"
    API: str = "/api"
    API_NAME: str = "Swaplang API"
    ALLOWED_ORIGINS: str = "http://localhost:5173"

    @computed_field
    @property
    def PORT(self) -> int:
        if self.ENVIRONMENT == "dev":
            return 8000
        return 1717

    @computed_field
    @property
    def OPENAPI_URL(self) -> str | None:
        if self.ENVIRONMENT != "dev":
            return None
        return f"{self.API}/openapi.json"

    DB_DIALECT: str = "sqlite"
    DB_DRIVER: str = ""
    SUPERUSER_USERNAME: str = Field(min_length=2, max_length=255)
    SUPERUSER_EMAIL: EmailStr = Field(max_length=255)
    SUPERUSER_PASSWORD: SecretStr = Field(min_length=8, max_length=40)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DB_DIALECT}{self.DB_DRIVER}:////{self.DATA_DIR}/swaplang.db"

    HF_HUB_REPO_ID: str = "ggml-org/gemma-3-1b-it-GGUF"
    DEFAULT_MODEL: str = "gemma-3-1b-it-Q8_0.gguf"
    DEFAULT_SYSTEM_PROMPT: str = ""

    @computed_field
    @property
    def MODELS_DIR(self) -> DirectoryPath:
        print(
            f"==== Ensuring models directory exists at: {Path(self.DATA_DIR) / 'models'}"
        )
        return _mkdir(Path(self.DATA_DIR) / "models")

    @computed_field
    @property
    def MODEL_PATH(self) -> Path:
        return self.MODELS_DIR / self.DEFAULT_MODEL

    SECRET_KEY: SecretStr = SecretStr("")

    @computed_field
    @property
    def SECRET_KEY_FILE_PATH(self) -> FilePath:
        secret_key_file_path = self.DATA_DIR / "secretkey.txt"
        secret_key_file_path.touch(exist_ok=True)
        return secret_key_file_path

    @model_validator(mode="after")
    def _create_secret_key(self):
        if self.SECRET_KEY.get_secret_value():
            logger.info("Secret key already exists.")
            return self
        try:
            self.SECRET_KEY = SecretStr(self.SECRET_KEY_FILE_PATH.read_text("utf-8"))
            logger.info("Reading secret key from file...")
            if not self.SECRET_KEY.get_secret_value().strip():
                logger.info("Secret key not found, generating new one...")
                self.SECRET_KEY = SecretStr(secrets.token_hex(32))
                self.SECRET_KEY_FILE_PATH.write_text(
                    self.SECRET_KEY.get_secret_value(), "utf-8"
                )
                logger.info("New secret key generated and saved to file.")
        except Exception:
            pass
            logger.exception("Error handling secret key from file.")
        return self

    FRONTEND_DIR: Annotated[
        DirectoryPath, BeforeValidator(_mkdir), AfterValidator(_resolve_path)
    ] = files("swaplang") / "frontend"  # type: ignore

    @computed_field
    @property
    def FRONTEND_INDEX_PATH(self) -> str:
        return f"{self.FRONTEND_DIR}/index.html"

    @computed_field
    @property
    def FRONTEND_STATIC_PATH(self) -> DirectoryPath:
        return _mkdir(f"{self.FRONTEND_DIR}/static")


settings = Settings()  # type: ignore
