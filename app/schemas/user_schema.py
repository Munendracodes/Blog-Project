from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    created_at: datetime
    email: EmailStr
    class Config:
        orm_mode = True