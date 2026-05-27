from pydantic import BaseModel

class Expense(BaseModel):
    title: str
    value: float
    category: str

class ExpenseCreate(BaseModel):
    title: str
    value: float
    category: str