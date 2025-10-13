from sqlmodel import Session, select
from swaplang.auth.password import verify_password
from swaplang.models import User


def login(session: Session, username: str, password: str) -> User | None:
    db_user = session.exec(select(User).where(User.username == username)).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        return None
    return db_user
