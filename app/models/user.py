from datetime import datetime
from sqlmodel import Field,SQLModel


class UserBase(SQLModel):
    username:str
    email:str=Field(unique=True)
    deleted:bool=Field(default=False)


class User(UserBase,table=True):
    __tablename__="users"
    user_id:int|None=Field(default=None,primary_key=True)
    join_date:datetime=Field(default_factory=datetime.now)

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    user_id:int

class UserUpdate(UserBase):
    name:str|None=None
    email:str|None=None
    deleted:bool|None=None

__all__=[
    "User",
    "UserCreate",
    "UserRead",
    "UserUpdate"
]

