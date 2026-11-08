from fastapi import FastAPI
from app.sse import sse_router
app=FastAPI()
app.include_router(sse_router)
@app.get("/health")
async def health_check():
    return {"status": "Notification Service is running"}