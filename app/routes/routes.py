from fastapi import APIRouter,WebSocket,WebSocketDisconnect,status
from sqlalchemy.orm import Session
from jose import JWTError,jwt
from app.websocket.manager import ConnectionManager
from app.database.connection import SessionLocal
from app.services.message_service import get_room_messages
from app.core.config import SECRET_KEY,ALGORITHM
from app.websocket.handler.dispacher import dispatch_event

router = APIRouter()

manager = ConnectionManager()

SECRET_KEY = SECRET_KEY
ALGORITHM = ALGORITHM


@router.websocket("/ws/{room}")
async def websocket_endpoint(
    websocket: WebSocket,
    room: str
):

    db: Session = SessionLocal()

    token = websocket.query_params.get("token")

    if not token:

        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )

        return

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

    except JWTError:

        await websocket.close(
            code=status.WS_1008_POLICY_VIOLATION
        )

        return

    await manager.connect(room,username,websocket)

    old_messages = get_room_messages(db, room)

    for msg in old_messages:

        await websocket.send_json({

            "type": "message",

            "username": msg.username,

            "content": msg.content
        })


    

    
    await manager.broadcast(room, {
        "type": "online_users",
        "users": manager.get_online_users(room)
    })
    try:
        while True:
            data = await websocket.receive_json()
            event_type = data.get("type")
            await dispatch_event(
                websocket=websocket,
                event_type=event_type,
                data=data,
                room=room,
                username=username,
                db=db,
                manager=manager
            )

    except WebSocketDisconnect:

        manager.disconnect(room,username)
        
        if room in manager.active_connections:

            online_users = (
                manager.get_online_users(room)
            )

            await manager.broadcast(

                room,

                {
                    "type": "online_users",

                    "users": online_users
                }
            )

    finally:

        db.close()