from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from app.database import Base

class Task(Base):

    __tablename__ = "tasks"

    task_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, nullable=False, default=False)
    priority = Column(String(50), nullable=True)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


