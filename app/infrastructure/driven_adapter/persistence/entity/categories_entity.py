from sqlalchemy import Column, Integer, String
from app.infrastructure.driven_adapter.persistence.config.database import Base

class CategoryEntity(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    budget_id = Column(Integer, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, index=True)
