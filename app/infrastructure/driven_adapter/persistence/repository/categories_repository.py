from app.infrastructure.driven_adapter.persistence.entity.categories_entity import CategoryEntity
from sqlalchemy.orm import Session

class CategoriesRepository:
    def __init__(self, session: Session):
        self.session = session

    
    def create_category(self, category_entity: CategoryEntity):
        self.session.add(category_entity)
        self.session.commit()
        self.session.refresh(category_entity)
        return category_entity
    
    def get_category_by_id(self, id):
        category_entity = self.session.query(CategoryEntity).filter_by(id=id).first()
        self.session.refresh(category_entity)
        return category_entity
    
    def get_categories_by_user_id(self, user_id):
        category_entities = self.session.query(CategoryEntity).filter_by(user_id=user_id).all()
        self.session.refresh(category_entities)
        return category_entities
        
    
    def update_category(self, category):
        self.session.commit()
        self.session.refresh(category)
        return category