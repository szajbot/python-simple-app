import decimal

from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.models import Driver, Car
from backend.schemas.driver import DriverCreate, DriverUpdate


def create_driver(db: Session, driver: DriverCreate):
    db_driver = Driver(
        surname=driver.surname,
        name=driver.name,
        account_balance=0
    )
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def get_drivers(db: Session):
    return db.query(Driver).all()


def get_driver(db: Session, user_id: int):
    db_user = db.query(Driver).filter(Driver.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Driver not found")
    return db_user


def update_driver(db: Session, driver_id: int, driver: DriverUpdate):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver:
        db_driver.name = driver.name
        db.commit()
        db.refresh(db_driver)
    else:
        raise HTTPException(status_code=404, detail="Driver not found")
    return db_driver


def delete_driver(db: Session, driver_id: int):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver:
        db.delete(db_driver)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Driver not found")
    return db_driver


def update_driver_balance(db: Session, user_id: int, balance: float):
    db_driver = db.query(Driver).filter(Driver.user_id == user_id).first()
    db_driver.account_balance = db_driver.account_balance + decimal.Decimal(balance)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def get_driver_balance(db: Session, user_id: int):
    return db.query(Driver).filter(Driver.user_id == user_id).first()


def get_drivers_with_details(db: Session):
    return (db.query(Driver.id, Driver.name, Driver.surname, Driver.account_balance, Car.brand, Car.model, Car.registration)
            .join(Car, Driver.id == Car.driver_id)
            .all())