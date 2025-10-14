import logging
from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine, select
from swaplang.config import settings
from swaplang.models import User
from swaplang.services import user_service as service

logger = logging.getLogger("database")

engine = create_engine(settings.DATABASE_URL, echo=True)  # echo=True for debugging


def _get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(_get_db)]


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def init_db():
    logger.info("Initializing database...")
    create_db_and_tables()
    with Session(engine) as session:
        user = session.exec(select(User).limit(1)).first()
        if not user:
            logger.info("Creating superuser...")
            service.create_superuser(session)
            logger.info("Superuser created.")
        else:
            logger.info("Superuser already exists.")
    logger.info("Database initialized.")
