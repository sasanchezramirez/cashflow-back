from app.infrastructure.driven_adapter.persistence.entity.expenses_entity import ExpensesEntity
from sqlalchemy.orm import Session

class ExpensesRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_expense(self, expense_entity: ExpensesEntity):
        self.session.add(expense_entity)
        self.session.commit()
        self.session.refresh(expense_entity)
        return expense_entity

    def get_expense_by_id(self, id: int):
        expense_entity = self.session.query(ExpensesEntity).filter_by(id=id).first()
        self.session.refresh(expense_entity)
        return expense_entity
    
    def get_expenses_by_user_id(self, user_id: int):
        expense_entities = self.session.query(ExpensesEntity).filter_by(user_id=user_id).all()
        for expense_entity in expense_entities:
            self.session.refresh(expense_entity)
        return expense_entities
    
    def update_expense(self, expense_entity: ExpensesEntity):
        self.session.commit()
        self.session.refresh(expense_entity)
        return expense_entity