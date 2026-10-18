from pydantic import BaseModel
from fastapi_users import schemas
import uuid
from datetime import datetime

class PostCreate (BaseModel):
    caption :str | None = None
    url : str
    file_type :str
    file_name : str
    title: str
    content: str


class PostResponse(BaseModel):
    id : uuid.UUID
    user_id : uuid.UUID
    url : str
    caption : str | None = None
    file_type : str
    file_name : str
    created_at : datetime
    title: str
    content :str

    class Config :
        from_attributes = True


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class UserUpdate(schemas.BaseUserUpdate):
    pass