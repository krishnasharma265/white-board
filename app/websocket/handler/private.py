from app.websocket.redis.publisher import (
    publish_message
)



async def handle_private_message(
    data,
    room,
    username,
    
    manager
    
    
):
    receiver=data.to
    content=data.content

    payload = {

        "type": "private_message",

        "sender": username,

        "to": data.to,

        "content": data.content
    }
    await publish_message(

        f"private:{data.to}",

        payload
    )

    