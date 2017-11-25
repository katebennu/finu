from database import Base
from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey
from sqlalchemy.types import DateTime


class Company(Base):
    __tablename__ = 'companies'
    ticker = Column(String(256), primary_key=True)
    name = Column(String(256))
    # industries =


class Entry(Base):
    __tablename__ = 'entries'
    company = Column(String, ForeignKey("company.ticker"), primary_key=True)
    year = Column(Integer, primary_key=True)
    name = Column(String(256), primary_key=True)
    value = Column(Float)
    reported = Column(Boolean)


class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String(256), primary_key=True)
    price = Column(Float)
    # date = Column(DateTime())