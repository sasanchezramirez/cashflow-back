from sqlalchemy import Column, Integer, String
from app.infrastructure.driven_adapter.persistence.config.database import Base

class PrioritiesEntity(Base):
    __tablename__ = "priorities"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String, index=True)
    user_id = Column(Integer, index=True)
