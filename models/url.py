from pydantic import BaseModel, HttpUrl


class URL(BaseModel):
    original_url: str
    short_url: str


class UrlRequest(BaseModel):
    original_url: HttpUrl


