from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

expenses = []

class Expense(BaseModel):
    title: str
    value: float
    category: str


@app.post("/expenses")
def add_expense(expense: Expense):
    expenses.append(expense)
    return {"message": "Expense added successfully", "expense": expense}

@app.get("/expenses")
def get_expenses():
    return {"expenses": expenses}
