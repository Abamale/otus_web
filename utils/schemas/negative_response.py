from __future__ import annotations

from pydantic import BaseModel


class NegativeResponse(BaseModel):
    error: str
    how_to_get_one: str