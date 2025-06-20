from __future__ import annotations

from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SupportUser(BaseModel):
    url: str
    text: str


class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
    support: SupportUser

class SingleUserResponse(BaseModel):
    data: User
    support: SupportUser


class UserCreateResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


class UserUpdateResponse(BaseModel):
    name: str
    job: str
    updatedAt: str