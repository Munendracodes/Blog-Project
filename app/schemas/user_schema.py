from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    created_at: datetime
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)