from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.models import Car, Driver
from backend.schemas.car import CarCreate, CarUpdate


def create_car(db: Session, car: CarCreate):
    db_car = Car(**car.model_dump())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def get_cars(db: Session):
    return db.query(Car).all()


def get_cars_expanded(db: Session):
    return (db.query(Car.id, Driver.name, Driver.surname, Car.driver_id, Car.brand, Car.model, Car.registration)
     .join(Driver, Car.driver_id == Driver.id)
     .all())


def get_car(db: Session, car_id: int):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car


def delete_car(db: Session, car_id: int):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car:
        db.delete(db_car)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car


def update_car(db: Session, car_id: int, car: CarUpdate):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car:
        db_car.brand = car.brand
        db_car.model = car.model
        db_car.driver_id = car.driver_id
        db_car.registration_number = car.registration_number
        db.commit()
        db.refresh(db_car)
    else:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car


def get_car_for_driver(db: Session, driver_id: int):
    db_car = db.query(Car).filter(Car.driver_id == driver_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
