from app.infrastructure.entry_point.dto.recurrent_expenses_dto import NewRecurrentExpenseInput, UpdateRecurrentExpenseInput
from app.domain.model.recurrent_expense import RecurrentExpense
from app.infrastructure.driven_adapter.persistence.entity.recurrent_expenses_entity import RecurrentExpensesEntity

class RecurrentExpensesMapper:
    @staticmethod
    def map_new_recurrent_expense_dto_to_recurrent_expense(new_recurrent_expense_dto: NewRecurrentExpenseInput) -> RecurrentExpense:
        return RecurrentExpense(
            description=new_recurrent_expense_dto.description,
            amount=new_recurrent_expense_dto.amount
        )

    @staticmethod
    def map_recurrent_expense_to_recurrent_expense_entity(recurrent_expense: RecurrentExpense) -> RecurrentExpensesEntity:
        return RecurrentExpensesEntity(
            description=recurrent_expense.description,
            amount=recurrent_expense.amount
        )
    
    @staticmethod
    def map_recurrent_expense_entity_to_recurrent_expense(recurrent_expense_entity: RecurrentExpensesEntity) -> RecurrentExpense:
        return RecurrentExpense(
            id=recurrent_expense_entity.id,
            description=recurrent_expense_entity.description,
            amount=recurrent_expense_entity.amount
        )
    
    @staticmethod
    def map_recurrent_expense_update_to_recurrent_expense_entity(recurrent_expense: RecurrentExpense, existing_recurrent_expense: RecurrentExpensesEntity) -> RecurrentExpensesEntity:
        existing_recurrent_expense.description = recurrent_expense.description
        existing_recurrent_expense.amount = recurrent_expense.amount
        return existing_recurrent_expense