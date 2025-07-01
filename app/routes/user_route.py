from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserBase, UserResponse
from app.database.connection import get_db
from app.models.user_model import User
from sqlalchemy.orm import Session
from app.security.hash import hash_password

router = APIRouter(tags=["Users"], prefix="/users")


@router.post("/", response_model=UserResponse)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    user_data = user.model_dump()
    user_data["password"] = hash_password(user.password)
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    