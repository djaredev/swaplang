from pathlib import Path
from pydantic import DirectoryPath, EmailStr, Field, SecretStr, computed_field
from pydantic_settings import BaseSettings


def _mkdir(value: str | DirectoryPath) -> DirectoryPath:
    path = Path(value)
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created directory at: {path.resolve()}")
    return path


class Settings(BaseSettings):
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

    DB_DIALECT: str = "sqlite"
    DB_DRIVER: str = ""
    SUPERUSER_USERNAME: str = Field(min_length=2, max_length=255)
    SUPERUSER_EMAIL: EmailStr = Field(max_length=255)
    SUPERUSER_PASSWORD: SecretStr = Field(min_length=8, max_length=40)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: SecretStr

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return f"{self.DB_DIALECT}{self.DB_DRIVER}:///swaplang.db"

    DATA_DIR: str = "data/"
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


settings = Settings()  # type: ignore
