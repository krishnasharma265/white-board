from pydantic import BaseModel,Field

class CreateUser(BaseModel):
    username:str=Field(min_length=1)
    password:str


class LoginUser(BaseModel):
    username:str
    password:str