from uuid import UUID
from fastapi import APIRouter, HTTPException, status

from swaplang.auth.user import AuthUserDep
from swaplang.database import SessionDep
from swaplang.models import (
    Translated,
    Direction,
    TranslationsPublic,
    TranslationPublic,
    TranslationUpdate,
)
from swaplang.translator import translate
from swaplang.services import language_service
from swaplang.services import translate_service

router = APIRouter()


@router.post("/translate", response_model=Translated)
async def swap_lang(
    user: AuthUserDep,
    session: SessionDep,
    text: str,
    source_language: str,
    target_language: str,
):
    sl = language_service.get_lang(session, source_language)
    tl = language_service.get_lang(session, target_language)
    if not sl:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Language '{source_language}' not available",
        )
    if not tl:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Language '{target_language}' not available",
        )
    translation = translate(text=text, source_language=sl.name, target_language=tl.name)
    if not translation:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error while translating",
        )
    translate_service.create_translate(
        session=session,
        user=user,
        source_lang=source_language,
        source_text=text,
        target_lang=target_language,
        target_text=translation,
    )
    return Translated(lang=target_language, text=translation)


@router.get("/translation", response_model=TranslationsPublic)
async def get_translations(
    user: AuthUserDep,
    session: SessionDep,
    cursor: str | None = None,
    direction: Direction = Direction.NEXT,
    limit: int = 10,
):
    translations, next_cursor = translate_service.get_translations(
        user=user,
        session=session,
        encoded_cursor=cursor,
        direction=direction,
        limit=limit,
    )
    return TranslationsPublic(translations=translations, next_cursor=next_cursor)


@router.patch("/translation/{id}", response_model=TranslationPublic)
async def update_translation(
    user: AuthUserDep,
    session: SessionDep,
    id: UUID,
    translation_update: TranslationUpdate,
):
    updated_translation = translate_service.update_translation(
        user=user, session=session, id=id, translation_update=translation_update
    )
    if not updated_translation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return updated_translation
