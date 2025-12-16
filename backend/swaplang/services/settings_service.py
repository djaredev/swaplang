from sqlmodel import Session, select

from swaplang.models.language import Language, LanguageUpdate


def get_available_languages(session: Session, only_enabled):
    if only_enabled:
        return session.exec(
            select(Language).where(Language.enabled == only_enabled)
        ).all()
    return session.exec(select(Language)).all()


def update_enabled_languages(session: Session, languages: list[LanguageUpdate]):
    for lang in languages:
        db_lang = session.get(Language, lang.id)
        if db_lang:
            db_lang.enabled = lang.enabled
            session.add(db_lang)
    session.commit()
