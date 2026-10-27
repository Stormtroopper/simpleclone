from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models.reservation import Reservation
from app.models.restaurant import Restaurant
from app.models.table import Table
from app.models.user import User
async def init_db():
    client=AsyncIOMotorClient(settings.mongodb_url)
    await init_beanie(database=client[settings.database_name],document_models=[Reservation,Restaurant,Table,User])
    print(f"Database connected successfully: {settings.database_name}")