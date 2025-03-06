from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Driver(Base):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    account_balance = Column(Numeric, index=True)

    users = relationship("User", back_populates="drivers")
    cars = relationship("Car", back_populates="driver", cascade="all, delete-orphan")

class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True, index=True)
    driver_id = Column(Integer, ForeignKey("driver.id"), nullable=False)
    brand = Column(String, index=True)
    model = Column(String, index=True)
    registration = Column(String, unique=True, index=True)

    driver = relationship("Driver", back_populates="cars")
    tickets = relationship("Ticket", back_populates="car", cascade="all, delete-orphan")

class Ticket(Base):
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True, index=True)
    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)
    parking_id = Column(Integer, index=True)
    entrance_date = Column(String, index=True)
    exit_date = Column(String, index=True, nullable=True)
    amount = Column(Numeric, index=True, nullable=True)
    payed = Column(Boolean, index=True, nullable=True)

    car = relationship("Car", back_populates="tickets")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, index=True)
    password = Column(String, index=True)

    drivers = relationship("Driver", back_populates="users", cascade="all, delete-orphan")

class Parking(Base):
    __tablename__ = 'parking'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    free_spots = Column(Integer, index=True)
    occupied_spots = Column(Integer, index=True)