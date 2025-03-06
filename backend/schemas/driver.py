from pydantic import BaseModel


class DriverCreate(BaseModel):
    name: str
    surname: str

class DriverDetails(BaseModel):
    id: int
    name: str
    surname: str
    account_balance: float
    brand: str
    model: str
    registration: str

class DriverUpdate(BaseModel):
    name: str
    surname: str


class DriverRead(BaseModel):
    user_id: int
    id: int
    name: str
    surname: str
    account_balance: float

class DriverBalance(BaseModel):
    account_balance: float


class DriverDelete(BaseModel):
    id: int
    name: str
    surname: str
    account_balance: float
