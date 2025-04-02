from fastapi import HTTPException

from sqlalchemy.orm import Session
from backend.models import Parking


def get_parkings(db: Session):
    return db.query(Parking).order_by(Parking.id).all()


def occupy_spot(db: Session, parking_id: int):
    parking = db.query(Parking).filter(Parking.id == parking_id).first()
    if not parking:
        raise HTTPException(status_code=404, detail="Parking not found")
    parking.occupied_spots += 1
    parking.free_spots -= 1
    db.add(parking)
    db.commit()
    return parking


def free_spot(db: Session, parking_id: int):
    parking = db.query(Parking).filter(Parking.id == parking_id).first()
    if not parking:
        raise HTTPException(status_code=404, detail="Parking not found")
    parking.occupied_spots -= 1
    parking.free_spots += 1
    db.add(parking)
    db.commit()
    return parking
