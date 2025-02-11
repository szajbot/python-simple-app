from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Driver(Base):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    account_balance = Column(Numeric, index=True)

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
    entrance_date = Column(String, index=True)
    exit_date = Column(String, index=True)
    amount = Column(Numeric, index=True)
    payed = Column(Boolean, index=True)

    car = relationship("Car", back_populates="tickets")
