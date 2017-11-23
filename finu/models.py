from database import Base
from sqlalchemy import Column, Float, String
from sqlalchemy.types import DateTime

class Price(Base):
    """
    Example Signups table
    """
    __tablename__ = 'prices'
    ticker = Column(String(256), primary_key=True)
    price = Column(Float)
    date = Column(DateTime())
