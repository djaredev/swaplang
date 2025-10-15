from sqlmodel import Session, and_, col, or_, select

from swaplang.models import Translation, User, Direction, Cursor


def create_translate(
    session: Session,
    user: User,
    source_lang: str,
    source_text: str,
    target_lang: str,
    target_text: str,
):
    session.add(
        Translation(
            user_id=user.id,
            source_lang=source_lang,
            source_text=source_text,
            target_lang=target_lang,
            target_text=target_text,
        )
    )
    session.commit()
