from app.database.connection import Base
from sqlalchemy import String, Integer, Column, DateTime
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    
    blogs = relationship("Blog", back_populates="owner")
    