from sqlalchemy.orm import Session
from models import Driver, Car
from schemas import CarCreate, CarUpdate, DriverCreate, DriverUpdate

def create_driver(db: Session, driver: DriverCreate):
    db_driver = Driver(name=driver.name)
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver

def create_car(db: Session, car: CarCreate):
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_drivers(db: Session):
    return db.query(Driver).all()

def get_driver(db: Session, driver_id: int):
    return db.query(Driver).filter(Driver.id == driver_id).first()

def get_cars(db: Session):
    return db.query(Car).all()

def get_car(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()

def update_driver(db: Session, driver_id: int, driver: DriverUpdate):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver:
        db_driver.name = driver.name
        db.commit()
        db.refresh(db_driver)
    return db_driver

def update_car(db: Session, car_id: int, car: CarUpdate):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car:
        db_car.brand = car.brand
        db_car.model = car.model
        db_car.driver_id = car.driver_id
        db_car.registration_number = car.registration_number
        db.commit()
        db.refresh(db_car)
    return db_car

def delete_car(db: Session, car_id: int):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car:
        db.delete(db_car)
        db.commit()
    return db_car

def delete_driver(db: Session, driver_id: int):
    db_driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if db_driver:
        db.delete(db_driver)
        db.commit()
    return db_driver
