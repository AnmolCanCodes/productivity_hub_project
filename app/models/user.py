from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.main import Base

class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=True)
    password_hash = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = value
