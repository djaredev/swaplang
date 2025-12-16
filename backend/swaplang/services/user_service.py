from fastapi import HTTPException
from sqlmodel import Session, select
from swaplang.auth.password import get_password_hash, verify_password
from swaplang.config import settings
from swaplang.models import User, UpdatePassword


def create_superuser(session: Session):
    superuser = User(
        username=settings.SUPERUSER_USERNAME,
        email=settings.SUPERUSER_EMAIL,
        hashed_password=get_password_hash(
            settings.SUPERUSER_PASSWORD.get_secret_value()
        ),
        is_superuser=True,
    )
    session.add(superuser)
    session.commit()
    session.refresh(superuser)
    return superuser


def get_user_by_username(username: str, session: Session) -> User | None:
    db_user = session.exec(select(User).where(User.username == username)).first()
    return db_user


def get_user_by_email(email: str, session: Session) -> User | None:
    db_user = session.exec(select(User).where(User.email == email)).first()
    return db_user


def update_password(user: User, passwords: UpdatePassword, session: Session):
    if not verify_password(passwords.current_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    if passwords.current_password == passwords.new_password:
        raise HTTPException(
            status_code=400,
            detail="New password must be different from the current one.",
        )
    user.hashed_password = get_password_hash(passwords.new_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
