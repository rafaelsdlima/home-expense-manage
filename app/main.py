from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session

from app.database import SessionLocal, engine

from app.models import Base, Expense as ExpenseModel

from app.schemas import ExpenseCreate, Expense

from app.crud import (
    create_expense,
    get_expenses,
    delete_expense,
    update_expense
)

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def read_root():

    return {
        "message": "API is working!"
    }


@app.post("/expenses")
def add_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db)
):

    return create_expense(db, expense)


@app.get("/expenses")
def list_expenses(
    db: Session = Depends(get_db)
):

    return get_expenses(db)


@app.delete("/expenses/{expense_id}")
def remove_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    return delete_expense(db, expense_id)


@app.put("/expenses/{expense_id}")
def edit_expense(
    expense_id: int,
    expense: Expense,
    db: Session = Depends(get_db)
):

    return update_expense(db, expense_id, expense)