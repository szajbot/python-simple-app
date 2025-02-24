from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.models import User, Driver
from backend.schemas.user import UserCreate, UserLogin, UserRegister


def login_user(db: Session, user: UserLogin):
    db_user = db.query(User).filter(User.login == user.login).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User or login invalid")
    return db_user


def register_user(db: Session, user: UserRegister):
    existing_user = db.query(User).filter(User.login == user.login).first()

    if existing_user:
        raise HTTPException(status_code=403, detail="Email already registered")
    else:
        new_user = User(login=user.login, password=user.password)  # Store password as plain text
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        added_user = db.query(User).filter(User.login == user.login).first()
        new_driver = Driver(name=user.name, surname=user.surname, account_balance=0, user_id=added_user.id)
        db.add(new_driver)
        db.commit()
        db.refresh(new_user)
        return new_user


def create_user(db: Session, user: UserCreate):
    existing_user = db.query(User).filter(User.login == user.login).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="User is already registered")
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, ticket_id: int):
    db_ticket = db.query(User).filter(User.id == ticket_id).first()
    if db_ticket:
        db.delete(db_ticket)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="User not found")
    return db_ticket
