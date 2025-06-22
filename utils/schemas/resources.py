from __future__ import annotations

from typing import List
from pydantic import BaseModel


class Resource(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class SupportResource(BaseModel):
    url: str
    text: str


class ResourceListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Resource]
    support: SupportResource


class SingleResourceResponse(BaseModel):
    data: Resource
    support: SupportResource