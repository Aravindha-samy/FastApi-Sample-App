from datetime import datetime
from sqlmodel import Field,SQLModel

class PostBase(SQLModel):
    content: str
    user_id: int = Field(foreign_key="user.user_id")
    deleted: bool = Field(default=False)
    title: str

class Post(PostBase,table=True):
    __tablename__="posts"
    post_id:int|None=Field(default=None,primary_key=True)
    post_date:datetime=Field(default_factory=datetime.now)
    

class PostCreate(PostBase):
    pass

class PostRead(PostBase):
    post_id:int
    post_date:datetime

class PostUpdate(PostBase):
    content:str|None=None
    

