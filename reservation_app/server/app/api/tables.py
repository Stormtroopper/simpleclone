from typing import List
from fastapi import APIRouter, Depends, HTTPException
from beanie import PydanticObjectId
from app.models.table import Table
router = APIRouter(prefix="/tables", tags=["Tables"])
@router.post("/", response_model=Table)
async def enter_table(table: Table):
    
    await table.insert()
    return table
@router.get("/", response_model=List[Table])
async def list_tables(restaurant_id: PydanticObjectId | None = None, skip: int = 0, limit: int = 20):
    query = Table.find_all()
    if restaurant_id:
        query = query.find(Table.restaurant.ref.id == restaurant_id)
    return await query.skip(skip).limit(limit).to_list()