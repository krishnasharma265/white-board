from fastapi import WebSocket
import json

class ConnectionManager:

    def __init__(self):

        self.active_connections: dict[
            str,
            dict[str, WebSocket]
        ] = {}

        self.user_connections: dict[
            str,
            WebSocket
        ] = {}

    async def connect(
        self,
        room: str,
        username: str,
        websocket: WebSocket
    ):

        await websocket.accept()

        if room not in self.active_connections:

            self.active_connections[room] = {}

        self.active_connections[room][username] = websocket
        self.user_connections[username] = websocket
        print(f"{username} joined {room}")


    def disconnect(
        self,
        room: str,
        username: str
    ):

        del self.active_connections[room][username]

        if len(self.active_connections[room]) == 0:

            del self.active_connections[room]

        if username in self.user_connections:

            del self.user_connections[username]

        print(f"{username} left {room}")


    async def broadcast(
        self,
        room: str,
        message: dict
    ):
        if room not in self.active_connections:
            return
        disconnected_users = []

        for username, connection in (
            self.active_connections[room].items()
        ):

            try:

                await connection.send_json(message)

            except Exception:

                disconnected_users.append(username)

        for username in disconnected_users:

            self.disconnect(room, username)

    def get_online_users(
        self,
        room: str
    ):

        if room not in self.active_connections:

            return []

        return list(
            self.active_connections[room].keys()
        )

    async def send_private_message(
        self,
        room: str,
        sender: str,
        receiver: str,
        message: str
    ):

        target_connection = (
            self.active_connections[room]
            .get(receiver)
        )

        if target_connection:

            await target_connection.send_json(message)

    async def send_json(
        self,
        websocket: WebSocket,
        data: dict
    ):

        await websocket.send_json(data)

    

    async def send_to_user(

        self,

        username: str,

        message: dict
    ):

        websocket = self.user_connections.get(
            username
        )

        if websocket:

            await websocket.send_json(
                message
            )