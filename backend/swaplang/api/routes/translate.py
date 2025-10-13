from fastapi import APIRouter

from swaplang.translator import translate

router = APIRouter()


@router.post("/api/translate")
async def swap_lang(text: str, source_language: str, target_language: str):
    translation = translate(
        text=text, source_language=source_language, target_language=target_language
    )
    return {"translation": translation}
