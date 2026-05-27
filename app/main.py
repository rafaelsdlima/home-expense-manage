from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, Expense , User
from app.schemas import UserCreate, ExpenseCreate, Expense, Login
from app.crud import create_user, create_expense, get_expenses, delete_expense, update_expense, login_user
from app.security import get_current_user
from app.auth import get_current_user

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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_expense(db, expense, current_user)

@app.get("/expenses")
def list_expenses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_expenses(db, current_user)


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

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.post("/login")
def login(user: Login, db: Session = Depends(get_db)):
    return login_user(db, user)