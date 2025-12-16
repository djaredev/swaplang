from fastapi import APIRouter, HTTPException, status

from swaplang.auth.user import AuthUserDep
from swaplang.config import settings
from swaplang.database.database import SessionDep
from swaplang.models.language import LanguageUpdate
from swaplang.services import settings_service


router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("/languages")
async def get_available_languages(user: AuthUserDep, session: SessionDep):
    return settings_service.get_available_languages(session)


@router.put("/languages")
async def update_enabled_languages(
    user: AuthUserDep, session: SessionDep, languages: list[LanguageUpdate]
):
    if not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only superusers can update enabled languages",
        )
    settings_service.update_enabled_languages(session, languages)
    return {"status": "enabled languages updated"}


@router.get("/models")
async def get_available_models(user: AuthUserDep):
    # For now, we only have one model available
    return {"models": [settings.DEFAULT_MODEL]}


@router.get("/system_prompt")
async def get_system_prompt(user: AuthUserDep):
    return {"system_prompt": settings.DEFAULT_SYSTEM_PROMPT}
