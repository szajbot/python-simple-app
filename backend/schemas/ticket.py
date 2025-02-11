from pydantic import BaseModel


class TicketCreate(BaseModel):
    car_id: int
    entrance_date: str


class TicketUpdate(BaseModel):
    car_id: int
    entrance_date: str
    exit_date: str
    amount: float
    payed: bool


class TicketRead(BaseModel):
    id: int
    car_id: int
    entrance_date: str
    exit_date: str
    amount: float
    payed: bool


class TicketDelete(BaseModel):
    id: int
