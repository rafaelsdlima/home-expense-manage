from sqlalchemy.orm import Session

from app.models import Expense


def create_expense(db: Session, expense):

    new_expense = Expense(
        title=expense.title,
        value=expense.value,
        category=expense.category
    )

    db.add(new_expense)

    db.commit()

    db.refresh(new_expense)

    return new_expense


def get_expenses(db: Session):

    return db.query(Expense).all()


def delete_expense(db: Session, expense_id: int):

    expense = db.query(Expense).filter(
        Expense.id == expense_id
    ).first()

    if expense:

        db.delete(expense)

        db.commit()

        return {
            "message": "expense deleted"
        }

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

    return {
        "message": "expense not found"
    }