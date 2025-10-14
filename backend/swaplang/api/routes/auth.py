from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from swaplang.auth.token import create_access_token
from swaplang.auth.user import AuthUserDep
from swaplang.database import SessionDep
from swaplang.models import UserPublic
from swaplang.services import auth_service as service

router = APIRouter()


@router.post("/login", response_model=UserPublic)
async def login(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    response: Response,
):
    user = service.login(
        session=session, username=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(user.id)
    response.set_cookie(
        key="swaplang_token",
        value=access_token,
        httponly=True,
        secure=False,
    )

    return user


@router.get("/whoami", response_model=UserPublic)
async def whoami(user: AuthUserDep):
    return user
