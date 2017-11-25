from database import Base
from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey
from sqlalchemy.types import DateTime


class Company(Base):
    __tablename__ = 'companies'
    ticker = Column(String(256), primary_key=True)
    name = Column(String(256))
    # industries =


class StatementEntry(Base):
    __tablename__ = 'statemententries'
    company = Column(String, ForeignKey("company.ticker"), primary_key=True)
    year = Column(Integer, primary_key=True)
    name = Column(String(256), primary_key=True)
    value = Column(Float)
    statement = Column(String(256))

class AnalyticEntry(Base):
    __tablename__ = 'analyticentries'
    company = Column(String, ForeignKey("company.ticker"), primary_key=True)
    year = Column(Integer, primary_key=True)
    name = Column(String(256), primary_key=True)
    value = Column(Float)
    type = Column(String(256))
    description = Column(String(500))


class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String(256), primary_key=True)
    price = Column(Float)
    # date = Column(DateTime())