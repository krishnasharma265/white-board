async def send_websocket_error(

    websocket,

    message: str
):

    await websocket.send_json({

        "type": "error",

        "message": message
    })