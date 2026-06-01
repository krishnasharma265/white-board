from sqlalchemy.orm import Session

from app.models.message import Message


def create_message(
    db: Session,
    room: str,
    username: str,
    content: str
):

    message = Message(

        room=room,
        username=username,
        content=content
    )

    db.add(message)

    db.commit()

    db.refresh(message)

    return message

def get_room_messages(
    db: Session,
    room: str
):

    return (
        db.query(Message)
        .filter(Message.room == room)
        .order_by(Message.created_at.asc()).limit(50)
        .all()
    )