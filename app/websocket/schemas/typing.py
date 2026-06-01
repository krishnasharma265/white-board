from pydantic import BaseModel
from typing import Literal

class TypingEvent(BaseModel):
    type:Literal["typing"]
    

class PrivateTypingEvent(BaseModel):

    type: Literal["private_typing"]

    to: str

class PrivateStopTypingEvent(BaseModel):

    type: Literal["private_stop_typing"]

    to: str
class StopTypingEvent(BaseModel):

    type: Literal["stop_typing"]

    