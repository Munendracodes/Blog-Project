from datetime import datetime, timezone
from app.database.connection import Base
from sqlalchemy import String, Integer, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blog"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False, index=True)
    content = Column(String, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    owner = relationship("User", back_populates="blogs")