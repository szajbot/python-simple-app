from pydantic import BaseModel


class DriverCreate(BaseModel):
    name: str
    surname: str


class DriverUpdate(BaseModel):
    name: str
    surname: str


class DriverRead(BaseModel):
    user_id: int
    id: int
    name: str
    surname: str
    account_balance: float


class DriverDelete(BaseModel):
    id: int
    name: str
    surname: str
    account_balance: float
