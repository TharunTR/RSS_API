from fastapi import FastAPI, HTTPException, Query
from config import RSS_FEEDS
from rss_service import fetch_all_feeds

app = FastAPI(title="Multi-RSS Feed API", version="2.0")

@app.get("/feeds")
async def get_feeds(
    category: str = Query(None, description="Filter by news category"),
    source: str = Query(None, description="Filter by news source")
):
    """
    Fetch and aggregate articles from multiple RSS feeds.
    Optional query parameters:
    - category: filter feeds by category
    - source: filter feeds by source
    """
    # Apply filters if provided
    filtered_feeds = [
        feed for feed in RSS_FEEDS
        if (not category or feed["category"].lower() == category.lower())
        and (not source or feed["source"].lower() == source.lower())
    ]

    # Fetch articles asynchronously
    results = await fetch_all_feeds(filtered_feeds)
    articles = [article for feed in results for article in feed["articles"]]

    if not articles:
        raise HTTPException(status_code=502, detail="Failed to fetch any feeds.")

    return {
        "status": "ok",
        "count": len(articles),
        "articles": articles
    }
