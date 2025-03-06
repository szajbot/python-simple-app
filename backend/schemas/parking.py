from pydantic import BaseModel


class ParkingRead(BaseModel):
    id: int
    name: str
    address: str
    free_spots: int
    occupied_spots: int
