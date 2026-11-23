import json
import time 
from anthropic import AsyncAnthropic
from fastapi import FastAPI

app=FastAPI(title="Feature Service",version="1.0.0")
client=AsyncAnthropic()
FALLBACK=[ {"title": "Find a restaurant", "text": "Browse restaurants by cuisine and city."},
    {"title": "Book a table", "text": "Choose a date, time and party size."},
    {"title": "Manage bookings", "text": "See all your reservations in one place."},]
TTL = 60 * 60
_cache = {"at": 0.0, "data": FALLBACK}

PROMPT = (
    "Write 3 short feature highlights for a restaurant reservation web app "
    "landing page. Reply with only a JSON array of objects with a 'title' "
    "(max 4 words) and a 'text' (max 12 words)."
)
@app.get('/')
async def get_features():
    if time.time()- _cache["at"]<TTL:
        return _cache["data"]
    try:
        message = await client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=400,
            messages=[{"role": "user", "content": PROMPT}],
        )
        text = "".join(b.text for b in message.content if b.type == "text")
        _cache.update(at=time.time(), data=json.loads(text))
    except Exception:
        _cache.update(at=time.time(), data=FALLBACK)
    return _cache["data"]
@app.get('/health')
async def healthCheck():
    return{"status":"Feature service is running"}