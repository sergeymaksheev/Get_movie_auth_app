import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    username = str
    birthdate: Optional[datetime.date]
    role_id = int
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
 

class UserCreate(schemas.BaseUserCreate):
    username: str
    birthdate: Optional[datetime.date]
    role_id: int
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class UserUpdate(schemas.BaseUserUpdate):
    pass