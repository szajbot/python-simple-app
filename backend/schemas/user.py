from pydantic import BaseModel


class UserCreate(BaseModel):
    password: str
    login: str


class UserLogin(BaseModel):
    password: str
    login: str

class UserRegister(BaseModel):
    password: str
    login: str

class UserRead(BaseModel):
    id: int
    password: str
    login: str


class UserDelete(BaseModel):
    id: int
    name: str
    surname: str
