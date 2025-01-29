from pydantic import BaseModel

class CarCreate(BaseModel):
    brand: str
    model: str
    driver_id: int
    registration_number: str

class CarUpdate(BaseModel):
    brand: str
    model: str
    driver_id: int
    registration_number: str

class CarRead(BaseModel):
    id: int
    brand: str
    model: str
    driver_id: int
    registration_number: str

class DriverCreate(BaseModel):
    name: str

class DriverUpdate(BaseModel):
    name: str

class DriverRead(BaseModel):
    id: int
    name: str
