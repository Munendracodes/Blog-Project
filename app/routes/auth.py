from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user_model import User 
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.security.hash import verify_password
from app.security.token import create_access_token


router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("/", include_in_schema=False)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password if user is not None else ""):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"id": user.id})
    return {"access_token": token, "token_type": "bearer"}