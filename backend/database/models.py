from sqlalchemy import Column, Integer, String, Float, Date
from .db import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    amount = Column(Float)
    category = Column(String)
    payment_mode = Column(String)
    date = Column(Date)
