import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.sse import sse_router
from app.consumers import run_consumer
app=FastAPI()
app.include_router(sse_router)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start Kafka consumer in the background
    task = asyncio.create_task(run_consumer())
    yield
    task.cancel()

app = FastAPI(title="Notification Service", version="1.0.0", lifespan=lifespan)
app.include_router(sse_router)
@app.get("/health")
async def health_check():
    return {"status": "Notification Service is running"}