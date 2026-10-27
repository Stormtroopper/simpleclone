from typing import Optional
from datetime import datetime
from beanie import Document
from typing import Optional
from pydantic import EmailStr,Field
from pymongo import IndexModel,ASCENDING
class User(Document):
    email:EmailStr
    firstName:str
    lastName:str
    phone:Optional[str]=None
    is_active:bool=True
    created_at:datetime=Field(default_factory=datetime.utcnow()) 
    class Settings:
        name:"users"
        indexes=[IndexModel([("email", ASCENDING)],unique=True)]