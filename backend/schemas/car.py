from pydantic import BaseModel


class CarCreate(BaseModel):
    driver_id: int
    brand: str
    model: str
    registration: str


class CarUpdate(BaseModel):
    brand: str
    model: str
    driver_id: int
    registration: str


class CarRead(BaseModel):
    id: int
    driver_id: int
    brand: str
    model: str
    registration: str

class CarReadExpanded(BaseModel):
    id: int
    driver_id: int
    name: str
    surname: str
    brand: str
    model: str
    registration: str

class CarDelete(BaseModel):
    id: int
