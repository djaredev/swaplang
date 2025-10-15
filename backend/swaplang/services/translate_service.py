from typing import Sequence
from sqlmodel import Session, and_, col, or_, select

from swaplang.models import Translation, User, Direction, Cursor
from swaplang.utils.cursor import decode_cursor, encode_cursor


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


def get_translations(
    user: User,
    session: Session,
    encoded_cursor: str | None,
    limit: int,
    direction: Direction,
) -> tuple[Sequence[Translation], str | None]:
    statement = select(Translation).where(Translation.user_id == user.id)
    if encoded_cursor:
        cursor = decode_cursor(encoded_cursor)
        if direction == Direction.NEXT:
            statement = statement.where(
                or_(
                    Translation.created_at < cursor.created_at,
                    and_(
                        Translation.created_at == cursor.created_at,
                        Translation.id < cursor.id,
                    ),
                )
            ).order_by(col(Translation.created_at).desc(), col(Translation.id).desc())
        else:
            statement = statement.where(
                or_(
                    Translation.created_at > cursor.created_at,
                    and_(
                        Translation.created_at == cursor.created_at,
                        Translation.id > cursor.id,
                    ),
                )
            ).order_by(col(Translation.created_at).asc(), col(Translation.id).asc())
    else:
        statement = statement.order_by(
            col(Translation.created_at).desc(), col(Translation.id).desc()
        )
    translations = session.exec(statement.limit(limit)).all()
    if not translations:
        return [], None
    return translations, encode_cursor(
        Cursor(id=translations[-1].id, created_at=translations[-1].created_at)
    )
