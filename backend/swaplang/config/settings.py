from pydantic import EmailStr, Field, SecretStr, computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
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


settings = Settings()  # type: ignore
