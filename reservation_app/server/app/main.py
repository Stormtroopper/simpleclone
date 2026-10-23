from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_db
from app.api import restaurants, reservations, users
@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
app=FastAPI(title="Restaurant Reservation API", description="test",version="0.1.0",lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"])
app.include_router(reservations.router, prefix="/reservations", tags=["reservations"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/health")
async def health_check():
    return {"status": "ok","message": "API is healthy"}