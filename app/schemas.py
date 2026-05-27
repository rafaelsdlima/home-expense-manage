from pydantic import BaseModel

class Expense(BaseModel):
    title: str
    value: float
    category: str

class ExpenseCreate(BaseModel):
    title: str
    value: float
    category: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str