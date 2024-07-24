from typing import Optional

from pydantic import BaseModel, HttpUrl
from datetime import datetime


class URL(BaseModel):
    original_url: str
    short_url: str
    created_at: Optional[datetime] = None


class UrlRequest(BaseModel):
    original_url: HttpUrl


