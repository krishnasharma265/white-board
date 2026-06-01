from fastapi import FastAPI
from app.routes import routes ,auth
from app.websocket import routes as route
from app.database.connection import db_init
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from app.routes.routes import manager
from contextlib import asynccontextmanager
from app.websocket.redis.subscriber import redis_subscriber

db_init()

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    print("[startup] starting redis subscriber...")
    task = asyncio.create_task(redis_subscriber(manager))
    print("[startup] redis subscriber started")
    yield
    task.cancel()
app=FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # tighten this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router)
app.include_router(routes.router)
app.include_router(route.router)
