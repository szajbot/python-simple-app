from sqlalchemy.orm import Session
from backend.models import Ticket
from backend.schemas.ticket import TicketCreate, TicketUpdate


def create_car(db: Session, ticket: TicketCreate):
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

def update_car(db: Session, ticket_id: int, ticket: TicketUpdate):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db_ticket.car_id = ticket.car_id
        db_ticket.entrance_date = ticket.entrance_date
        db_ticket.exit_date = ticket.exit_date
        db_ticket.amount = ticket.amount
        db_ticket.payed = ticket.payed
        db.commit()
        db.refresh(db_ticket)
    return db_ticket