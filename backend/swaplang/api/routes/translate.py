from fastapi import APIRouter, HTTPException, status

from swaplang.auth.user import AuthUserDep
from swaplang.database import SessionDep
from swaplang.models import Translated
from swaplang.translator import translate
from swaplang.services import language_service

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
    return Translated(lang=target_language, text=translation)
