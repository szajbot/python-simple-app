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
    print("debug")
    db_user = user_crud.login_user(db, user)

    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {"message": "Login successful"}

@router.post("/register")
def register(user: user_schema.UserRegister, db: Session = Depends(get_db)):
    print("debug")
    db_user = user_crud.register_user(db, user)

    return {"message": "Login successful", "user": {"id": db_user.id}}

@router.get("/", response_model=List[user_schema.UserRead])
def read_user(db: Session = Depends(get_db)):
    return user_crud.get_user(db=db)


@router.get("/{user_id}", response_model=user_schema.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=user_schema.UserCreate)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db=db, user=user)