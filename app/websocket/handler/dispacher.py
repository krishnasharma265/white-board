from app.websocket.handler.message import (
    handle_message
)

from app.websocket.handler.typing import (
    handle_typing,
    handle_stop_typing,
    handle_private_typing,
    handle_private_stop_typing
)

from app.websocket.handler.private import (
    handle_private_message
)

from app.websocket.schemas.message import MessageEvent
from app.websocket.schemas.typing import TypingEvent,PrivateTypingEvent,PrivateStopTypingEvent,StopTypingEvent
from app.websocket.schemas.private import PrivateMessageEvent
from pydantic import ValidationError
from app.websocket.exceptions.handler import send_websocket_error
from app.websocket.exceptions.validator import validate_event

from app.websocket.limiter import (
    RateLimiter
)
from app.websocket.handler.drawing import handle_draw
from app.websocket.schemas.heartbeat import (
    PingEvent
)

from app.websocket.handler.heartbeat import (
    handle_ping
)
from app.websocket.schemas.drawing import DrawEvent



limiter = RateLimiter()

LIMITS = {

    "message": (5, 10),

    "typing": (20, 10),

    "stop_typing": (20, 10),

    "private_message": (3, 10),

    "private_typing": (20, 10),

    "private_stop_typing": (20, 10),
    "ping": (30, 60),
    "draw": (200, 10),

}

async def dispatch_event(
    websocket,
    event_type,
    data,
    room,
    username,
    db,
    manager
):

    limit, seconds = LIMITS.get(

        event_type,

        (5, 10)
    )

    allowed = limiter.is_allowed(

        username=username,

        event_type=event_type,

        limit=limit,

        seconds=seconds
    )

    if not allowed:

        await send_websocket_error(

            websocket,

            "Too many requests"
        )

        return



    if event_type == "message":
        validated_data = await validate_event(

            websocket,

            MessageEvent,

            data
        )

        if not validated_data:
            return
        
        await handle_message(
            validated_data,
            room,
            username,
            db,
            manager
        )

    elif event_type == "typing":
        validated_data = await validate_event(

            websocket,

            TypingEvent,

            data
        )

        if not validated_data:
            return
        
        await handle_typing(
            room,
            username,
            manager
        )

    elif event_type == "stop_typing":
        validated_data = await validate_event(

            websocket,

            StopTypingEvent,

            data
        )

        if not validated_data:
            return
        
        await handle_stop_typing(
            room,
            username,
            manager
        )

    elif event_type == "private_typing":
        validated_data = await validate_event(

            websocket,

            PrivateTypingEvent,

            data
        )

        if not validated_data:
            return
        
        await handle_private_typing(
            validated_data,
            room,
            username,
            manager
        )

    elif event_type == "private_stop_typing":
        validated_data = await validate_event(

            websocket,

            PrivateStopTypingEvent,

            data
        )

        if not validated_data:
            return
        
        await handle_private_stop_typing(
            validated_data,
            room,
            username,
            manager
        )

    elif event_type == "private_message":
        validated_data = await validate_event(

            websocket,

            PrivateMessageEvent,

            data
        )

        if not validated_data:
            return
        
        await handle_private_message(
            validated_data,
            room,
            username,
            manager
        )

    elif event_type == "ping":

        validated_data = await validate_event(

            websocket,

            PingEvent,

            data
        )

        if not validated_data:
            return

        await handle_ping(websocket)

    elif event_type=="draw":
        validated_data=await validate_event(
            websocket,
            DrawEvent,
            data
            )
        
        if not validated_data :
            return

        await handle_draw(
            db=db,
            room_id=room,
            user_id=username,
            data=validated_data.model_dump(),
            manager=manager

        )

    else:

        await send_websocket_error(

            websocket,

            f"Unknown event: {event_type}"
        )