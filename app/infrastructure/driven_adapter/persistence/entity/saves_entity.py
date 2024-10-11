from sqlalchemy import Column, Integer, String
from app.infrastructure.driven_adapter.persistence.config.database import Base

class SavesEntity(Base):
    __tablename__ = "saves"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    month = Column(String, index=True)
    saves = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
