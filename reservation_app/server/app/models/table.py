from typing import Optional
from beanie import Document,Link
from pydantic import Field
from pymongo import IndexModel, ASCENDING
from app.models.restaurant import Resturant
class Table(Document):
    restaurant:Link[Resturant]
    table_number:int=Field(...,ge=1)
    capacity:int=Field(...,ge=1)
    is_available:bool=True
    class Settings:
        
        name:str="tables"
        indexes=[
            IndexModel([("restaurant", ASCENDING)]),
            IndexModel([("table_number", ASCENDING)]),
        ]