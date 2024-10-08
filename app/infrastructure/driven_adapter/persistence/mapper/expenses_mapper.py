from app.domain.model.expense import Expense
from app.infrastructure.driven_adapter.persistence.entity.expenses_entity import ExpensesEntity

class ExpensesMapper:
    @staticmethod
    def map_expense_to_expense_entity(expense: Expense) -> ExpensesEntity:
        return ExpensesEntity(
            id=expense.id,
            description=expense.description,
            category_id=expense.category_id,
            priority_id=expense.priority_id,
            user_id=expense.user_id,
            expense_date=expense.expense_date,
            amount=expense.amount
        )
    
    @staticmethod
    def map_expense_entity_to_expense(expense_entity: ExpensesEntity) -> Expense:
        return Expense(
            id=expense_entity.id,
            description=expense_entity.description,
            category_id=expense_entity.category_id,
            priority_id=expense_entity.priority_id,
            user_id=expense_entity.user_id,
            expense_date=expense_entity.expense_date,
            amount=expense_entity.amount
        )
    
    @staticmethod
    def map_expense_update_to_expense_entity(expense: Expense, existing_expense: ExpensesEntity) -> ExpensesEntity:
        existing_expense.description = expense.description
        existing_expense.category_id = expense.category_id
        existing_expense.priority_id = expense.priority_id
        existing_expense.user_id = expense.user_id
        existing_expense.expense_date = expense.expense_date
        existing_expense.amount = expense.amount
        return existing_expense