from app.websocket.schemas.drawing import DrawEvent
#from websocket.manager import ConnectionManager as manager
from app.models.drawing import BoardEvent
from sqlalchemy.orm import Session
async def handle_draw(
        db:Session,
        
        room_id: str,
        user_id:str,
        data: dict,
        manager
        ):

    validated_data = DrawEvent(**data)

    await manager.broadcast(
        
        room=room_id,
        message=validated_data.model_dump()
    )


    event = BoardEvent(
        room_id=room_id,
        user_id=user_id,
        event_type="draw",
        event_data=data
    )

    db.add(event)

    db.commit()