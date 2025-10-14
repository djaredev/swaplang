from sqlmodel import Session, select

from swaplang.models import Language


def get_lang(session: Session, id: str) -> Language | None:
    return session.exec(select(Language).where(Language.id == id)).first()


def create_default_langs(session: Session):
    session.add(Language(id="en", name="English"))
    session.add(Language(id="es", name="Spanish"))
    session.add(Language(id="fr", name="French"))
    session.add(Language(id="de", name="German"))
    session.add(Language(id="it", name="Italian"))
    session.add(Language(id="pt", name="Portuguese"))
    session.add(Language(id="ru", name="Russian"))
    session.add(Language(id="zh", name="Chinese"))
    session.add(Language(id="ja", name="Japanese"))
    session.add(Language(id="ko", name="Korean"))
    session.add(Language(id="ar", name="Arab"))
    session.add(Language(id="hi", name="Hindi"))
    session.commit()
