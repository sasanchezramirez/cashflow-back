from app.infrastructure.driven_adapter.persistence.entity.priorities_entity import PrioritiesEntity
from sqlalchemy.orm import Session

class PrioritiesRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_priority(self, priority_entity: PrioritiesEntity):
        self.session.add(priority_entity)
        self.session.commit()
        self.session.refresh(priority_entity)
        return priority_entity

    def get_priority_by_id(self, id: int):
        priority_entity = self.session.query(PrioritiesEntity).filter_by(id=id).first()
        self.session.refresh(priority_entity)
        return priority_entity
    
    def get_priorities_by_user_id(self, user_id: int):
        priority_entities = self.session.query(PrioritiesEntity).filter_by(user_id=user_id).all()
        for priority_entity in priority_entities:
            self.session.refresh(priority_entity)
        return priority_entities
    
    def update_priority(self, priority_entity: PrioritiesEntity):
        self.session.commit()
        self.session.refresh(priority_entity)
        return priority_entity