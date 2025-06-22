from __future__ import annotations

from pydantic import BaseModel
from typing import List, Optional


class LoginResponse(BaseModel):
    token: str


class LoginUnsuccessfulResponse(BaseModel):
    error: str


class RegisterResponse(BaseModel):
    id: int
    token: str


class RegisterUnsuccessfulResponse(BaseModel):
    error: str