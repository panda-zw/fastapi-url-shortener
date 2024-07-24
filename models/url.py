from pydantic import BaseModel, HttpUrl
from datetime import datetime


class URL(BaseModel):
    original_url: str
    short_url: str
    created_at: datetime


class UrlRequest(BaseModel):
    original_url: HttpUrl


