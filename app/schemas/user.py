from typing import List, Optional
from pydantic import BaseModel


class UserVO(BaseModel):
    class Config:
        orm_mode = True


class UserDTO(UserVO):
    user_id: Optional[str]
    user_email: Optional[str]
    password: Optional[str]
    user_name: Optional[str]
    phone: Optional[str]
    birth: Optional[str]
    address: Optional[str]
    job: Optional[str]
    user_interests: Optional[str]
    token: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]


class UserList(UserVO):
    user_id: Optional[str]
    user_email: Optional[str]
    password: Optional[str]
    user_name: Optional[str]
    phone: Optional[str]
    birth: Optional[str]
    address: Optional[str]
    job: Optional[str]
    user_interests: Optional[str]
    token: Optional[str]


class UserUpdate(BaseModel):
    user_id: Optional[str]
    phone: Optional[str]
    job: Optional[str]
    user_interests: Optional[str]
    updated_at: Optional[str]
    token: Optional[str]

    class Config:
        orm_mode = True
