from sqlalchemy import Column, Integer, String
from app.infrastructure.driven_adapter.persistence.config.database import Base

class ExpensesEntity(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String, index=True)
    category_id = Column(Integer, index=True)
    priority_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    expense_date = Column(String, index=True)
    amount = Column(Integer, index=True)