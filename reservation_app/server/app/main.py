from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db
from app.api import restaurants, reservation, users
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
app=FastAPI(title="Restaurant Reservation API", description="test",version="0.1.0",lifespan=lifespan)
# allowed_origins = [
#     origin.strip()
#     for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
#     if origin.strip()
# ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(restaurants.router)
# app.include_router(tables.router)
app.include_router(reservation.router)

@app.get("/health")
async def health_check():
    return {"status": "ok","message": "API is healthy"}