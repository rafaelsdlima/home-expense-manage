from sqlalchemy.orm import Session
from app.models import Expense, User
from app.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException


def create_expense(db: Session, expense, user):

    new_expense = Expense(title=expense.title, value=expense.value, category=expense.category, owner_id=user.id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


def get_expenses(db: Session):
    return db.query(Expense).filter(
    Expense.owner_id == user.id).all()


def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    if expense:
        db.delete(expense)
        db.commit()
        return {"message": "expense deleted"}

    return {
        "message": "expense not found"
    }


def update_expense(
    db: Session,
    expense_id: int,
    updated_expense
):

    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    if expense:

        expense.title = updated_expense.title
        expense.value = updated_expense.value
        expense.category = updated_expense.category
        db.commit()
        db.refresh(expense)
        return expense

    return {"message": "expense not found"}

def create_user(db, user):

    hashed = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db, user):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        return {"error": "Invalid email"}

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        return {"error": "Invalid password"}

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {"access_token": token, "token_type": "bearer"}