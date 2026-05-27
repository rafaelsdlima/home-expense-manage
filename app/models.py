from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.database import Base



class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    value = Column(Float)
    category = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))

class User(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)