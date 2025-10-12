from sqlmodel import SQLModel, Session, create_engine, select
from swaplang.config import settings
from swaplang.models import User
from swaplang.auth import get_password_hash


engine = create_engine(settings.DATABASE_URL, echo=True)  # echo=True for debugging


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


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

