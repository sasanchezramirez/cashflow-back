from sqlalchemy import Column, Integer
from app.infrastructure.driven_adapter.persistence.config.database import Base

class BudgetsEntity(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    weekly_amount = Column(Integer, index=True)
    monthly_amount = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    category_id = Column(Integer, index=True)
    weekly_balance = Column(Integer, index=True)
    monthly_balance = Column(Integer, index=True)
