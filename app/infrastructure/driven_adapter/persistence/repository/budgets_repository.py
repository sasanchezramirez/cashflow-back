from app.infrastructure.driven_adapter.persistence.entity.budgets_entity import BudgetsEntity
from sqlalchemy.orm import Session

class BudgetsRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_budget(self, budget_entity: BudgetsEntity):
        self.session.add(budget_entity)
        self.session.commit()
        return budget_entity

    def get_budget_by_id(self, id: int):
        budget_entity = self.session.query(BudgetsEntity).filter_by(id=id).first()
        self.session.refresh(budget_entity)
        return budget_entity
    
    def get_budgets_by_user_id(self, user_id: int):
        budget_entities = self.session.query(BudgetsEntity).filter_by(user_id=user_id).all()
        for budget_entity in budget_entities:
            self.session.refresh(budget_entity)
        return budget_entities
    
    def update_budget(self, budget_entity: BudgetsEntity):
        self.session.commit()
        self.session.refresh(budget_entity)
        return budget_entity
    
    def get_budget_by_category(self, category_id: int):
        budget_entity = self.session.query(BudgetsEntity).filter_by(category_id=category_id).first()
        self.session.refresh(budget_entity)
        return budget_entity