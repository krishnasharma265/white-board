import json
import asyncio
from app.websocket.redis.client import redis_subscriber_client

async def redis_subscriber(manager):
    while True:
        try:
            pubsub = redis_subscriber_client.pubsub()
            await pubsub.psubscribe("*")
            print("[redis_subscriber] subscribed")

            async for message in pubsub.listen():
                if message["type"] != "pmessage":
                    continue
                try:
                    channel = message["channel"]
                    if isinstance(channel, bytes):
                        channel = channel.decode("utf-8")

                    data = json.loads(message["data"])
                    print(f"[redis_subscriber] got: channel={channel} type={data.get('type')}")

                    if channel.startswith("private:"):
                        username = channel.split(":")[1]
                        await manager.send_to_user(username, data)
                    else:
                        await manager.broadcast(channel, data)

                except Exception as e:
                    print(f"[redis_subscriber] message error: {e}")
                    continue

        except Exception as e:
            print(f"[redis_subscriber] crashed: {e} — restarting in 2s")
            await asyncio.sleep(2)