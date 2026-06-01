from sqlalchemy import Column,Integer,String,JSON,DateTime
from datetime import datetime

from app.database.database import Base


class BoardEvent(Base):

    __tablename__ = "board_events"

    id = Column(Integer, primary_key=True)

    room_id = Column(String, nullable=False)

    user_id = Column(String, nullable=False)

    event_type = Column(String, nullable=False)

    event_data = Column(JSON, nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )