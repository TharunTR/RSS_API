from fastapi import FastAPI
from pydantic import BaseModel
import feedparser
import httpx
import asyncio

app = FastAPI()

class FeedInfo(BaseModel):
    url: str
    source: str
    category: str
    country: str

class FeedResponse(BaseModel):
    name: str
    articles: list

async def fetch_feed(feed_info: FeedInfo) -> FeedResponse:
    url = feed_info.url
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            response.raise_for_status()
            feed = feedparser.parse(response.text)
            articles = []
            for entry in feed.entries:
                articles.append({
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "publishedAt": entry.get("published", ""),
                    "summary": entry.get("summary", ""),
                    "source": feed_info.source,
                    "category": feed_info.category,
                    "country": feed_info.country
                })
            return {"name": feed_info.name, "articles": articles}
    except Exception:
        return {"name": feed_info.name, "articles": []}

async def fetch_all_feeds(feeds: list) -> list:
    tasks = [fetch_feed(feed) for feed in feeds]
    return await asyncio.gather(*tasks)

@app.post("/feeds/", response_model=FeedResponse)
async def get_feeds(feeds: list[FeedInfo]):
    results = await fetch_all_feeds(feeds)
    return {"feeds": results}