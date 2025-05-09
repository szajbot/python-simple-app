from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED

import backend.crud.ticket as ticket_crud
import backend.schemas.ticket as ticket_schema
from backend.database import get_db

router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[ticket_schema.TicketRead])
def get_tickets(db: Session = Depends(get_db)):
    return ticket_crud.get_tickets(db=db)


@router.get("/user/{user_id}/active", response_model=List[ticket_schema.ActiveTicketRead])
def get_active_tickets_for_user(user_id: int, db: Session = Depends(get_db)):
    return ticket_crud.get_active_tickets_for_user(db=db, user_id=user_id)


@router.get("/user/{user_id}/deactivate", response_model=List[ticket_schema.DeactivateTicketWithDetails])
def get_not_active_tickets_for_user(user_id: int, db: Session = Depends(get_db)):
    return ticket_crud.get_not_active_tickets_for_user(db=db, user_id=user_id)


@router.post("/pay/{user_id}/{ticket_id}", response_model=ticket_schema.TicketRead)
def pay_for_ticket(user_id: int, ticket_id: int, db: Session = Depends(get_db)):
    return ticket_crud.pay_for_ticket(db=db, user_id=user_id, ticket_id=ticket_id)


@router.get("/{ticket_id}", response_model=ticket_schema.TicketRead)
def get_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    return ticket_crud.get_ticket_by_id(db=db, ticket_id=ticket_id)


@router.get("/user/{user_id}", response_model=List[ticket_schema.TicketRead])
def get_tickets_for_user(user_id: int, db: Session = Depends(get_db)):
    return ticket_crud.get_tickets_for_user(db=db, user_id=user_id)


@router.post("", status_code=HTTP_201_CREATED)
def create_ticket(ticket: ticket_schema.TicketCreate, db: Session = Depends(get_db)):
    return ticket_crud.create_ticket(db=db, ticket=ticket)


@router.put("/{ticket_id}", response_model=ticket_schema.TicketUpdate)
def update_ticket(ticket_id: int, ticket: ticket_schema.TicketUpdate, db: Session = Depends(get_db)):
    return ticket_crud.update_ticket(db=db, ticket_id=ticket_id, ticket=ticket)
