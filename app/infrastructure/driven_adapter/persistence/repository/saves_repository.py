from sqlalchemy.orm import Session
from app.infrastructure.driven_adapter.persistence.entity.saves_entity import SavesEntity

class SavesRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_save(self, saves_entity: SavesEntity):
        self.session.add(saves_entity)
        self.session.commit()
        return saves_entity