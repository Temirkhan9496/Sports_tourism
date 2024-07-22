from typing import Optional
from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    new = "new"
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class RequestBase(BaseModel):
    name: str
    phone: str
    email: str
    direction: str
    level: str
    start_date: str
    duration: int
    price: float

class RequestCreate(RequestBase):
    pass

class Request(RequestBase):
    id: int
    status: StatusEnum

    class Config:
        orm_mode = True