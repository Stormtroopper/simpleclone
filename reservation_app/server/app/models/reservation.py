from typing import Optional,List
from datetime import datetime
from enum import Enum
from beanie import Document,Link
from pydantic import Field
from pymongo import IndexModel,ASCENDING
from app.models.table  import Table
from app.models.restaurant import Restaurant
from app.models.user import User
class ReservationStatus(str,Enum):
    PENDING="pending"
    CONFIRMED="confirmed"
    CANCELLED="cancelled"
    SUCCESS="success"
    NO_SHOW="no_show"
class Reservation(Document):
    user:Link[User]
    restaurant:Link[Restaurant]
    tables:List[Link[Table]]=[]
    reservation_time:datetime
    status:ReservationStatus=ReservationStatus.PENDING
    # for optimistic locking, to prevent race conditions when multiple users try to update the same reservation simultaneously
    version:int=1
    class Settings:
        name="reservations"
        indexes = [
            IndexModel([("restaurant", ASCENDING), ("reservation_time", ASCENDING)]),
            IndexModel([("user", ASCENDING)]),
            IndexModel([("status", ASCENDING)]),
        ]
