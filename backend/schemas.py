from pydantic import BaseModel


class DriverCreate(BaseModel):
    name: str
    surname: str


class DriverUpdate(BaseModel):
    name: str
    surname: str
    account_balance: float


class DriverRead(BaseModel):
    id: int
    name: str
    surname: str
    account_balance: float


class CarCreate(BaseModel):
    driver_id: int
    brand: str
    model: str
    driver_id: int
    registration_number: str


class CarUpdate(BaseModel):
    driver_id: int
    brand: str
    model: str
    driver_id: int
    registration_number: str


class CarRead(BaseModel):
    id: int
    driver_id: int
    brand: str
    model: str
    registration_number: str


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
