from fastapi import HTTPException

from sqlalchemy.orm import Session
from backend.models import Ticket, Driver, Car, Parking
from backend.schemas.ticket import TicketCreate, TicketUpdate
from backend.crud import parking as parking_crud


def create_ticket(db: Session, ticket: TicketCreate):
    car = db.query(Car).filter(Car.id == ticket.car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    parking_crud.occupy_spot(db, ticket.parking_id)

    db_ticket = Ticket(**ticket.model_dump())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_tickets(db: Session):
    return (db.query(Ticket.id, Ticket.car_id, Parking.name, Parking.address, Ticket.entrance_date, Ticket.exit_date,
                     Ticket.amount, Ticket.payed)
            .join(Parking, Ticket.parking_id == Parking.id)
            .all())


def get_tickets_for_car(db: Session, car_id: int):
    return db.query(Ticket).filter(Ticket.car_id == car_id).all().sort()


def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return db_ticket


def update_ticket(db: Session, ticket_id: int, ticket: TicketUpdate):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db_ticket.exit_date = ticket.exit_date
        db_ticket.amount = ticket.amount
        db_ticket.payed = ticket.payed
        db.commit()
        db.refresh(db_ticket)
    else:
        raise HTTPException(status_code=404, detail="Ticket not found")

    parking_crud.free_spot(db, db_ticket.parking_id)

    db_ticket = (
        db.query(Ticket.id, Ticket.car_id, Parking.name, Parking.address, Ticket.entrance_date, Ticket.exit_date,
                 Ticket.amount, Ticket.payed)
        .join(Parking, Ticket.parking_id == Parking.id)
        .filter(Ticket.id == ticket_id)
        .first())

    return db_ticket


def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def get_all_tickets_for_user(db: Session, user_id: int):
    db_driver = db.query(Driver).filter(Driver.user_id == user_id).first()
    if not db_driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    db_car = db.query(Car).filter(Car.driver_id == db_driver.id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")

    return (
        db.query(Ticket.id, Ticket.car_id, Parking.name, Parking.address, Ticket.entrance_date, Ticket.exit_date,
                 Ticket.amount, Ticket.payed)
        .join(Parking, Ticket.parking_id == Parking.id)
        .filter(Ticket.car_id == db_car.id))


def get_tickets_for_user_filtered_by_exit(db: Session, user_id: int, have_exit_time: bool):
    tickets = get_all_tickets_for_user(db, user_id)

    if have_exit_time and tickets:
        return tickets.filter(Ticket.exit_date != None)
    elif not have_exit_time and tickets:
        return tickets.filter(Ticket.exit_date == None)

    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")

    return tickets


def get_tickets_for_user(db: Session, user_id: int):
    tickets = get_all_tickets_for_user(db, user_id)
    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    return tickets


def get_active_tickets_for_user(db: Session, user_id: int):
    return (
        db.query(Ticket.id, Ticket.car_id, Parking.name, Parking.address, Car.registration, Ticket.entrance_date,
                 Ticket.exit_date,
                 Ticket.amount, Ticket.payed)
        .join(Car, Ticket.car_id == Car.id)
        .join(Parking, Ticket.parking_id == Parking.id)
        .filter(Car.driver_id == user_id, Ticket.exit_date.is_(None))
        .all()
    )


def get_not_active_tickets_for_user(db: Session, user_id: int):
    return (
        db.query(Ticket.id, Ticket.car_id, Ticket.entrance_date, Ticket.exit_date,
                 Ticket.amount, Ticket.payed, Car.registration, Car.model, Car.brand)
        .join(Car, Ticket.car_id == Car.id)
        .filter(Car.driver_id == user_id, Ticket.exit_date.isnot(None))
        .all()
    )


def pay_for_ticket(db: Session, ticket_id: int, user_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    driver = db.query(Driver).filter(Driver.user_id == user_id).first()
    if driver.account_balance < ticket.amount:
        raise HTTPException(status_code=403, detail="Driver balance too low")
    elif ticket.payed is True:
        raise HTTPException(status_code=403, detail="Ticket payed")
    else:
        driver.account_balance -= ticket.amount
        ticket.payed = True
        db.commit()
        db.refresh(driver)
        db.refresh(ticket)

    return (
        db.query(Ticket.id, Ticket.car_id, Parking.name, Parking.address, Ticket.entrance_date, Ticket.exit_date,
                 Ticket.amount, Ticket.payed)
        .join(Parking, Ticket.parking_id == Parking.id)
        .filter(Ticket.id == ticket_id)
        .first())
