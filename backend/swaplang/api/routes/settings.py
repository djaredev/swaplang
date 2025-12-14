from fastapi import APIRouter, HTTPException, status

from swaplang.auth.user import AuthUserDep
from swaplang.database.database import SessionDep
from swaplang.services import settings_service


router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("/languages")
async def get_available_languages(user: AuthUserDep, session: SessionDep):
    return settings_service.get_available_languages(session)
