from app.infrastructure.entry_point.dto.recurrent_expenses_dto import NewRecurrentExpenseInput, UpdateRecurrentExpenseInput
from app.domain.model.recurrent_expense import RecurrentExpense
from app.infrastructure.driven_adapter.persistence.entity.recurrent_expenses_entity import RecurrentExpensesEntity

class RecurrentExpensesMapper:

    @staticmethod
    def map_recurrent_expense_to_recurrent_expense_entity(recurrent_expense: RecurrentExpense) -> RecurrentExpensesEntity:
        return RecurrentExpensesEntity(
            description=recurrent_expense.description,
            category_id=recurrent_expense.category_id,
            priority_id=recurrent_expense.priority_id,
            user_id=recurrent_expense.user_id
        )
    
    @staticmethod
    def map_recurrent_expense_entity_to_recurrent_expense(recurrent_expense_entity: RecurrentExpensesEntity) -> RecurrentExpense:
        return RecurrentExpense(
            id=recurrent_expense_entity.id,
            description=recurrent_expense_entity.description,
            category_id=recurrent_expense_entity.category_id,
            priority_id=recurrent_expense_entity.priority_id,
            user_id=recurrent_expense_entity.user_id
        )
    
    @staticmethod
    def map_recurrent_expense_update_to_recurrent_expense_entity(recurrent_expense: RecurrentExpense, existing_recurrent_expense: RecurrentExpensesEntity) -> RecurrentExpensesEntity:
        existing_recurrent_expense.description = recurrent_expense.description
        existing_recurrent_expense.amount = recurrent_expense.amount
        return existing_recurrent_expense