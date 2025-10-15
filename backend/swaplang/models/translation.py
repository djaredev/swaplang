from datetime import datetime
from typing import Sequence
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel


class TranslationBase(SQLModel):
    source_text: str = Field(min_length=1)
    target_text: str = Field(min_length=1)
    source_lang: str = Field(max_length=2, foreign_key="language.id")
    target_lang: str = Field(min_length=2, foreign_key="language.id")


class TranslationUpdate(SQLModel):
    source_text: str | None = Field(default=None, min_length=1)
    target_text: str | None = Field(default=None, min_length=1)
    source_lang: str | None = Field(default=None)
    target_lang: str | None = Field(default=None)


class Translated(SQLModel):
    lang: str
    text: str


class TranslationPublic(TranslationBase):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())


class TranslationCreate(TranslationBase): ...


class Translation(TranslationPublic, table=True):
    user_id: UUID = Field(foreign_key="user.id")


class TranslationsPublic(SQLModel):
    translations: Sequence[Translation]
    next_cursor: str | None
