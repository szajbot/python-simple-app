from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import backend.crud.car as car_crud
import backend.schemas.car as car_schema
from backend.database import get_db

router = APIRouter(
    prefix="/cars",
    tags=["cars"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[car_schema.CarRead])
def read_cars(db: Session = Depends(get_db)):
    return car_crud.get_cars(db=db)


@router.get("/{car_id}", response_model=car_schema.CarRead)
def read_car(car_id: int, db: Session = Depends(get_db)):
    return car_crud.get_car(db=db, car_id=car_id)


@router.get("/driver/{driver_id}", response_model=car_schema.CarRead)
def read_car_for_driver(driver_id: int, db: Session = Depends(get_db)):
    return car_crud.get_car_for_driver(db=db, driver_id=driver_id)


@router.post("", response_model=car_schema.CarCreate)
def create_car(car: car_schema.CarCreate, db: Session = Depends(get_db)):
    return car_crud.create_car(db=db, car=car)


@router.put("/{car_id}", response_model=car_schema.CarRead)
def update_car(car_id: int, car: car_schema.CarUpdate, db: Session = Depends(get_db)):
    return car_crud.update_car(db=db, car_id=car_id, car=car)


@router.delete("/{car_id}", status_code=204)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    return car_crud.delete_car(db=db, car_id=car_id)
