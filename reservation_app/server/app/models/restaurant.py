from typing import List, Optional
from datetime import time
# odm for mongo db built on top of pydantic
from beanie import Document
# Data validation and settings management library 
from pydantic import BaseModel, Field
# pymongo is the native python driver for mongodb
from pymongo import IndexModel, ASCENDING
class OpeningHours(BaseModel):
    day:int =Field(...,ge=0,le=6)
    open_time:time
    close_time:time
class Restaurant(Document):
    name:str
    description:Optional[str]=None
    cuisine:Optional[str]=None
    address:str
    city:str
    phone_number:Optional[str]=None
    opening_hours:List[OpeningHours]=[]
    is_active:bool=True
class Settings:
    
    name:str="restaurants"
    indexes=[
        IndexModel([("city", ASCENDING)]),
        IndexModel([("name",ASCENDING)]),
        IndexModel([("cuisine", ASCENDING)]),
    ]
