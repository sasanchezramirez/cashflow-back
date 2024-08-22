from app.infrastructure.driven_adapter.persistence.entity.recurrent_expenses_entity import RecurrentExpensesEntity
from sqlalchemy.orm import Session

class RecurrentExpensesRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_recurrent_expense(self, recurrent_expense_entity: RecurrentExpensesEntity):
        self.session.add(recurrent_expense_entity)
        self.session.commit()
        self.session.refresh(recurrent_expense_entity)
        return recurrent_expense_entity

    def get_recurrent_expense_by_id(self, id: int):
        recurrent_expense_entity = self.session.query(RecurrentExpensesEntity).filter_by(id=id).first()
        self.session.refresh(recurrent_expense_entity)
        return recurrent_expense_entity
    
    def get_recurrent_expenses_by_user_id(self, user_id: int):
        recurrent_expense_entities = self.session.query(RecurrentExpensesEntity).filter_by(user_id=user_id).all()
        for recurrent_expense_entity in recurrent_expense_entities:
            self.session.refresh(recurrent_expense_entity)
        return recurrent_expense_entities
    
    def update_recurrent_expense(self, recurrent_expense_entity: RecurrentExpensesEntity):
        self.session.commit()
        self.session.refresh(recurrent_expense_entity)
        return recurrent_expense_entity