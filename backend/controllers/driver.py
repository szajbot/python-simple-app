from typing import List

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import backend.crud.driver as driver_crud
import backend.schemas.driver as driver_schema
from backend.database import get_db

router = APIRouter(
    prefix="/drivers",
    tags=["drivers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[driver_schema.DriverRead])
def read_drivers(db: Session = Depends(get_db)):
    return driver_crud.get_drivers(db=db)

@router.get("/details", response_model=List[driver_schema.DriverRead])
def get_drivers_with_details(db: Session = Depends(get_db)):
    return driver_crud.get_drivers_with_details(db=db)

@router.get("/{user_id}", response_model=driver_schema.DriverRead)
def read_driver(user_id: int, db: Session = Depends(get_db)):
    return driver_crud.get_driver(db=db, user_id=user_id)


@router.get("/{user_id}/balance", response_model=driver_schema.DriverRead)
def get_driver_balance(user_id: int, db: Session = Depends(get_db)):
    return driver_crud.get_driver_balance(db=db, user_id=user_id)


@router.post("/", response_model=driver_schema.DriverCreate)
def create_driver(driver: driver_schema.DriverCreate, db: Session = Depends(get_db)):
    return driver_crud.create_driver(db=db, driver=driver)


@router.post("/{user_id}/{balance}", response_model=driver_schema.DriverRead)
def update_driver_balance(user_id: int, balance: float, db: Session = Depends(get_db)):
    return driver_crud.update_driver_balance(db=db, user_id=user_id, balance=balance)


@router.put("/{driver_id}", response_model=driver_schema.DriverRead)
def update_driver(driver_id: int, driver: driver_schema.DriverUpdate, db: Session = Depends(get_db)):
    return driver_crud.update_driver(db=db, driver_id=driver_id, driver=driver)


@router.delete("/{driver_id}", status_code=204)
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    return driver_crud.delete_driver(db=db, driver_id=driver_id)
