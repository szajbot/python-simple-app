from typing import List

import uvicorn
from fastapi import Depends, HTTPException
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import crud
import models
import schemas

database = "backend"
host = "localhost"
user = "backenduser"
password = "password"
port = "5432"


def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )


engine = get_connection()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/cars", response_model=List[schemas.CarRead])
def read_cars(db: Session = Depends(get_db)):
    return crud.get_cars(db=db)


@app.get("/car/{car_id}", response_model=schemas.CarRead)
def read_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.get_car(db=db, car_id=car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@app.get("/drivers", response_model=List[schemas.DriverRead])
def read_drivers(db: Session = Depends(get_db)):
    return crud.get_drivers(db=db)


@app.get("/driver/{driver_id}", response_model=schemas.DriverRead)
def read_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.get_driver(db=db, driver_id=driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver


@app.post("/car", response_model=schemas.CarCreate)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db=db, car=car)


@app.put("/car/{car_id}", response_model=schemas.CarRead)
def update_car(car_id: int, car: schemas.CarUpdate, db: Session = Depends(get_db)):
    return crud.update_car(db=db, car_id=car_id, car=car)


@app.delete("/car/{car_id}", status_code=204)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = crud.delete_car(db=db, car_id=car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return


@app.post("/driver/", response_model=schemas.DriverCreate)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db=db, driver=driver)


@app.put("/driver/{driver_id}", response_model=schemas.DriverRead)
def update_driver(driver_id: int, driver: schemas.DriverUpdate, db: Session = Depends(get_db)):
    return crud.update_driver(db=db, driver_id=driver_id, driver=driver)


@app.delete("/driver/{driver_id}", status_code=204)
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    driver = crud.delete_driver(db=db, driver_id=driver_id)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
