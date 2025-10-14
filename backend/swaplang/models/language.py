from sqlmodel import Field, SQLModel


class LanguageBase(SQLModel):
    id: str = Field(max_length=2, primary_key=True)
    name: str = Field(min_length=1, max_length=20)


class LanguagePublic(LanguageBase): ...


class Language(LanguageBase, table=True): ...
