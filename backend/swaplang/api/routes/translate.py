from fastapi import APIRouter

from swaplang.auth.user import AuthUserDep
from swaplang.translator import translate

router = APIRouter()


@router.post("/translate")
async def swap_lang(
    user: AuthUserDep, text: str, source_language: str, target_language: str
):
    translation = translate(
        text=text, source_language=source_language, target_language=target_language
    )
    return {"translation": translation}
