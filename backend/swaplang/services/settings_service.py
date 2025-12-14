from sqlmodel import Session, select

from swaplang.models.language import Language


def get_available_languages(session: Session):
    return session.exec(select(Language)).all()


