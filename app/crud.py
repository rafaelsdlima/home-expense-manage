from fastapi import FastAPI
from pydantic import BaseModel
from app.models import Expense
from app.database import Base
from sqlalchemy.orm import Session

app = FastAPI()

expenses = []

def create_expense(db, expense):
    new_expense = Expense(        
        title=expense.title,
        value=expense.value,
        category=expense.category
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    expenses.append(new_expense)
    return new_expense



def get_expenses():
    return expenses

def delete_expense(expense_id, update_expense):
    for expense in expenses:
        if expense["id"] == expense_id:
            expense["title"] = update_expense.title
            expense["value"] = update_expense.value
            expense["category"] = update_expense.category

            return {
                "messege": "Expense atualizado com sucesso",
                "data": expense
            }
    return {"message": "Expense não encontrado"}
