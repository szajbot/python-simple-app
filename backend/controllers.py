from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
import database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/drivers/", response_model=schemas.DriverCreate)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db=db, driver=driver)

@router.post("/cars/", response_model=schemas.CarCreate)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db=db, car=car)

@router.get("/drivers/", response_model=List[schemas.DriverRead])
def read_drivers(db: Session = Depends(get_db)):
    return crud.get_drivers(db=db)

@router.get("/drivers/{driver_id}", response_model=schemas.DriverRead)
def read_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.get_driver(db=db, driver_id=driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.get("/cars/", response_model=List[schemas.CarRead])
def read_cars(db: Session = Depends(get_db)):
    return crud.get_cars(db=db)

@router.get("/cars/{car_id}", response_model=schemas.CarRead)
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.get_car(db=db, car_id=car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.put("/cars/{car_id}", response_model=schemas.CarRead)
def update_car(car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)):
    return crud.update_car(db=db, car_id=car_id, car=car)

@router.delete("/cars/{car_id}", status_code=204)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.delete_car(db=db, car_id=car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return

@router.delete("/drivers/{driver_id}", status_code=204)
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.delete_driver(db=db, driver_id=driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return
