from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    value = Column(Float)
    category = Column(String)
    date = Column(Date)