from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapped_column

Base = declarative_base()

class Driver(Base):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    surname = Column(String, unique=True, index=True)
    account_balance = Column(Numeric, unique=True, index=True)

class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True, index=True)
    driver_id = mapped_column(ForeignKey("driver.id"))
    brand = Column(String, index=True)
    model = Column(String, index=True)
    registration_number = Column(String, unique=True, index=True)

    fk_driver = relationship("Driver", back_populates="cars")
