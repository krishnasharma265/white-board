from pydantic import BaseModel

class PrivateMessageEvent(BaseModel):
    type:str
    to:str
    content:str