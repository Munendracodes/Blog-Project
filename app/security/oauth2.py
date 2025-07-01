from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.security.token import decode_access_token
from app.models.user_model import User
from sqlalchemy.orm import Session
from app.database.connection import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decode_access_token(token)
    if payload is None or "id" not in payload:
        raise credentials_exception

    user_id = payload["id"]

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise credentials_exception

    return user

