from app.websocket.redis.publisher import publish_message

async def handle_typing(

    room,
    username,
    manager
):

    payload = {

        "type": "typing",

        "username": username
    }


    await publish_message(

        room,

        payload
    )
async def handle_stop_typing(

    room,
    username,
    manager
):
    payload = {

        "type": "stop_typing",

        "username": username
    }


    await publish_message(

        room,

        payload
    )
    
async def handle_private_typing(
    data,
    room,
    username,
    manager
):
    receiver=data.to

    payload = {

        "type": "private_typing",

        "username": username,

        "to": data.to
    }


    await publish_message(

        f"private:{data.to}",

        payload
    )
    

        
    
async def handle_private_stop_typing(
    data,
    room,
    username,
    manager
):
    
    payload = {

        "type": "private_stop_typing",

        "username": username,

        "to": data.to
    }


    await publish_message(

        f"private:{data.to}",


        payload
    )
    