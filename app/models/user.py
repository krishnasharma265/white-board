from app.database.database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import Mapped
class User(Base):
    __tablename__="users"
    __allow_unmapped__=True

    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    username=Column(String,unique=True,nullable=False,index=True)
    password=Column(String)

    