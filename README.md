# Multi-RSS Feed Aggregator API

A FastAPI-based RSS aggregator that fetches and serves agriculture news from multiple Indian sources. Supports async fetching, filtering by category or source, and returns structured JSON for easy integration with apps and dashboards. Easily extendable and production-ready.

## Features

- Aggregates news from multiple RSS feeds
- Asynchronous fetching for high performance
- Filter articles by category or source
- Clean, structured JSON output
- Easily extendable feed configuration

## Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the API server**
   ```sh
   uvicorn main:app --reload
   ```

## Usage

- Access the API at: `http://localhost:8000/feeds`
- Filter by category or source:
  - `http://localhost:8000/feeds?category=Agriculture`
  - `http://localhost:8000/feeds?source=Google News`
- View interactive docs at: `http://localhost:8000/docs`

## Configuration

- Add or edit RSS feeds in `config.py`:
  ```python
  RSS_FEEDS = [
      {
          "name": "Google News Agriculture India",
          "url": "https://news.google.com/rss/search?q=agriculture+india&hl=en-IN&gl=IN&ceid=IN:en",
          "category": "Agriculture",
          "country": "India",
          "source": "Google News"
      },
      # Add more feeds as needed
  ]
  ```

## Project Structure

```
rss_api/
├── main.py
├── config.py
├── rss_service.py
├── requirements.txt
└── README.md
```

## License

MIT License

##
