from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TicketCreate(BaseModel):
    car_id: int
    entrance_date: datetime


class TicketUpdate(BaseModel):
    exit_date: Optional[datetime]
    amount: Optional[float]
    payed: Optional[bool]


class TicketRead(BaseModel):
    id: int
    car_id: int
    entrance_date: datetime
    exit_date: Optional[datetime]
    amount: Optional[float]
    payed: Optional[bool]

class ActiveTicketRead(BaseModel):
    id: int
    car_id: int
    registration: str
    entrance_date: datetime
    exit_date: Optional[datetime]
    entrance_date: datetime
    exit_date: Optional[datetime]
    amount: Optional[float]
    payed: Optional[bool]

class DeactivateTicketWithDetails(BaseModel):
    id: int
    car_id: int
    entrance_date: datetime
    exit_date: datetime
    amount: float
    payed: bool

    registration: str
    model: str
    brand: str



class TicketDelete(BaseModel):
    id: int
