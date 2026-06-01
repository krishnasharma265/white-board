from app.services.message_service import (
    create_message
)
from app.websocket.redis.publisher import (
    publish_message
)

async def handle_message(

    data,
    room,
    username,
    db,
    manager
):

    content = data.content

    message = create_message(

        db=db,

        room=room,

        username=username,

        content=content
    )

    payload = {

        "type": "message",

        "username": username,

        "content": content
    }


    await publish_message(

        room,

        payload
    )