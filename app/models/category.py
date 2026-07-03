from sqlalchemy import Column, ForeignKey, Integer, String
from app.database import Base

class Category(Base):

    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)


