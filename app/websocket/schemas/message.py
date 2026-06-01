from pydantic import BaseModel,Field
from typing import Literal
class MessageEvent(BaseModel):
    type:Literal["message"]
    content:str=Field(min_length=1,max_length=500)
