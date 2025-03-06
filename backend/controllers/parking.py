from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

import backend.crud.parking as parking_crud
import backend.schemas.parking as parking_schema
from backend.database import get_db

router = APIRouter(
    prefix="/parkings",
    tags=["parkings"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[parking_schema.ParkingRead])
def get_parkings(db: Session = Depends(get_db)):
    return parking_crud.get_parkings(db=db)

@router.post("/{parking_id}/free", response_model=parking_schema.ParkingRead)
def free_spot_for_parking(parking_id: int, db: Session = Depends(get_db)):
    return parking_crud.free_spot(db=db, parking_id=parking_id)

@router.post("/{parking_id}/occupy", response_model=parking_schema.ParkingRead)
def occupy_spot_for_parking(parking_id: int, db: Session = Depends(get_db)):
    return parking_crud.occupy_spot(db=db, parking_id=parking_id)