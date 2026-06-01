async def handle_ping(

    websocket
):

    await websocket.send_json({

        "type": "pong"
    })