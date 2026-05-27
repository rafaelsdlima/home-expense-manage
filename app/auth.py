from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from fastapi import Depends, HTTPException
from app.database import SessionLocal
from app.models import User
from sqlalchemy.orm import Session

SECRET_KEY = "secret"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        email = payload.get("sub")

        user = db.query(User).filter(
            User.email == email
        ).first()

        if user is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid authentication"
            )

        return user

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )