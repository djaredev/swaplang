from sqlmodel import Session, select

from swaplang.models import Language


def get_lang(session: Session, id: str) -> Language | None:
    return session.exec(select(Language).where(Language.id == id)).first()
