import json

from app.websocket.redis.client import (
    redis_client
)


async def publish_message(

    room: str,

    message: dict
):

    await redis_client.publish(

        room,

        json.dumps(message)
    )