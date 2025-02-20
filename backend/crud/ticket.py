from sqlalchemy.orm import Session
from backend.models import Ticket, Driver, Car
from backend.schemas.ticket import TicketCreate, TicketUpdate


def create_ticket(db: Session, ticket: TicketCreate):
    db_ticket = Ticket(**ticket.model_dump())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


def get_tickets(db: Session):
    return db.query(Ticket).all()


def get_tickets_for_car(db: Session, car_id: int):
    return db.query(Ticket).all().filter(Ticket.car_id == car_id).sort().all()


def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    return db_ticket


def update_ticket(db: Session, ticket_id: int, ticket: TicketUpdate):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db_ticket.exit_date = ticket.exit_date
        db_ticket.amount = ticket.amount
        db_ticket.payed = ticket.payed
        db.commit()
        db.refresh(db_ticket)
    return db_ticket


def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def get_all_tickets_for_user(db: Session, user_id: int):
    db_driver = db.query(Driver).filter(Driver.user_id == user_id).first()
    if not db_driver:
        print("Driver not found")
        return []
    db_car = db.query(Car).filter(Car.driver_id == db_driver.id).first()
    if not db_car:
        print("Car not found")
        return []
    return db.query(Ticket).filter(Ticket.car_id == db_car.id)


def get_tickets_for_user_filtered_by_exit(db: Session, user_id: int, have_exit_time: bool):
    tickets = get_all_tickets_for_user(db, user_id)
    if not tickets:
        print("Tickets not found")
        return tickets

    if have_exit_time:
        return tickets.filter(Ticket.exit_date != None)
    elif not have_exit_time:
        return tickets.filter(Ticket.exit_date == None)

    if not tickets:
        print("Tickets not found")
        return []
    return tickets


def get_tickets_for_user(db: Session, user_id: int):
    tickets = get_all_tickets_for_user(db, user_id)
    if not tickets:
        print("Tickets not found")
        return []
    return tickets


def get_active_tickets_for_user(db: Session, user_id: int):
    return get_tickets_for_user_filtered_by_exit(db, user_id, have_exit_time=False)


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
        print("Driver account balance exceeds ticket amount")
    elif ticket.payed is True:
        print("Ticket payed")
    else:
        driver.account_balance -= ticket.amount
        ticket.payed = True
        db.commit()
        db.refresh(driver)
        db.refresh(ticket)
        return ticket
