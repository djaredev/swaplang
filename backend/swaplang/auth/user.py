import uuid
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyCookie
from jwt import InvalidTokenError
from sqlmodel import select
from swaplang.auth.token import decode_token
from swaplang.database import SessionDep
from swaplang.models import User

cookie_scheme = APIKeyCookie(name="swaplang_token")


def _get_auth_user(token: Annotated[str, Depends(cookie_scheme)], session: SessionDep):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_token(token)
    except InvalidTokenError:
        raise credentials_exception
    user_id: str = payload.get("sub")
    if not user_id:
        raise credentials_exception
    user = session.exec(select(User).where(User.id == uuid.UUID(user_id))).first()
    if user is None:
        raise credentials_exception
    return user


AuthUserDep = Annotated[User, Depends(_get_auth_user)]
