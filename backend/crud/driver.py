from sqlalchemy.orm import Session

from backend.models import Driver
from backend.schemas import DriverCreate, DriverUpdate


def create_driver(db: Session, driver: DriverCreate):
    db_driver = Driver(**driver.model_dump())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def get_drivers(db: Session):
    return db.query(Driver).all()


def get_driver(db: Session, driver_id: int):
    return db.query(Driver).filter(Driver.id == driver_id).first()


def update_driver(db: Session, driver_id: int, driver: DriverUpdate):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver:
        db_driver.name = driver.name
        db.commit()
        db.refresh(db_driver)
    return db_driver


def delete_driver(db: Session, driver_id: int):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver:
        db.delete(db_driver)
        db.commit()
    return db_driver
