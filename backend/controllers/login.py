from typing import List

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

import backend.crud.user as user_crud
import backend.schemas.user as user_schema
from backend.database import get_db

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.post("/login")
def login(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    return user_crud.login_user(db, user)


@router.post("/register")
def register(user: user_schema.UserRegister, db: Session = Depends(get_db)):
    return user_crud.register_user(db, user)


@router.get("/", response_model=List[user_schema.UserRead])
def read_user(db: Session = Depends(get_db)):
    return user_crud.get_user(db=db)


@router.get("/{user_id}", response_model=user_schema.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user(db=db, user_id=user_id)


@router.post("/", response_model=user_schema.UserCreate)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db=db, user=user)
