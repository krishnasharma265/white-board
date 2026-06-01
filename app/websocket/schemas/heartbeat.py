from typing import Literal

from pydantic import BaseModel


class PingEvent(BaseModel):

    type: Literal["ping"]

class PongEvent(BaseModel):

    type: Literal["pong"]