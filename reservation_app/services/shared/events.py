from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventType(str, Enum):
    USER_REGISTERED = "user.registered"
    USER_LOGGED_IN = "user.logged_in"
    USER_LOGGED_OUT = "user.logged_out"
    PASSWORD_CHANGED = "password.changed"
    RESERVATION_MADE = "reservation.made"
    RESERVATION_CANCELLED = "reservation.cancelled"
class BaseEvent(BaseModel):
    event_type: EventType
    timestamp: datetime
    user_id: Optional[str] = None
    data: Optional[dict] = None