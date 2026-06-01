from pydantic import ValidationError

from app.websocket.exceptions.handler import (
    send_websocket_error
)


async def validate_event(

    websocket,

    schema,

    data
):

    try:

        return schema(**data)

    except ValidationError as e:

        await send_websocket_error(

            websocket,

            e.errors()
        )

        return None