from fastapi import APIRouter, HTTPException, Body
from pydantic import HttpUrl
from models.url import URL
from pymongo import MongoClient
import shortuuid
from models.url import URL, UrlRequest
import os

router = APIRouter()

# MongoDB connection
db_url = os.getenv("DB_URL")
client = MongoClient(db_url)
db = client.url_shortener


@router.post("/shorten", response_model=URL)
async def shorten_url(url_request: UrlRequest = Body(...)):
    original_url = url_request.original_url

    # Check if the URL already exists in the database
    existing_url = db.urls.find_one({"original_url": str(original_url)})
    if existing_url:
        return URL(**existing_url)

    # Generate a new short URL
    short_url = shortuuid.uuid()[:6]
    url = URL(original_url=str(original_url), short_url=short_url)

    # Insert the new URL into the database
    db.urls.insert_one(url.model_dump())

    return url


@router.get("/{short_url}", response_model=URL)
async def redirect_url(short_url: str):
    url = db.urls.find_one({"short_url": short_url})
    if url:
        return URL(**url)
    else:
        raise HTTPException(status_code=404, detail="URL not found")
