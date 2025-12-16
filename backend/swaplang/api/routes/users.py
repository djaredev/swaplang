from fastapi import APIRouter, status

from swaplang.auth.user import AuthUserDep
from swaplang.database.database import SessionDep
from swaplang.models.user import UpdatePassword, UserPublic, UserUpdate
from swaplang.services import user_service


router = APIRouter(prefix="/users", tags=["users"])


@router.patch("/me/password", status_code=status.HTTP_204_NO_CONTENT)
async def update_password_me(
    user: AuthUserDep, session: SessionDep, passwords: UpdatePassword
):
    user_service.update_password(user, passwords, session)
