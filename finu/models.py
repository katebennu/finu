from database import Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.types import DateTime


class Company(Base):
    __tablename__ = 'companies'
    ticker = Column(String(256), primary_key=True)
    # industries =


class StatementEntry(Base):
    __tablename__ = 'statements'
    company = Column(String, ForeignKey("company.ticker"), primary_key=True)
    year = Column(Integer, primary_key=True)
    name = Column(String(256), primary_key=True)
    value = Column(Float)


class Stock(Base):
    __tablename__ = 'prices'
    ticker = Column(String(256), primary_key=True)
    price = Column(Float)
    # date = Column(DateTime())