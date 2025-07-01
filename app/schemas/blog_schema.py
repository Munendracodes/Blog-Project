from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.user_schema import UserResponse

class BlogBase(BaseModel):
    title: str
    content: str

class BlogResponse(BlogBase):
    id: int
    created_at: datetime
    owner: UserResponse
    
    model_config = ConfigDict(from_attributes=True)