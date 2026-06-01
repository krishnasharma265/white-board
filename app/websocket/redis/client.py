from redis.asyncio import Redis

from app.core.config import REDIS_URL


# redis_client = Redis.from_url(

#     REDIS_URL,

#     decode_responses=True
# )


# separate connections — Redis pub/sub requires dedicated connection for subscriber
redis_client = Redis.from_url(REDIS_URL, decode_responses=True)
redis_subscriber_client = Redis.from_url(REDIS_URL, decode_responses=True)