from app.infrastructure.entry_point.dto.expenses_dto import NewExpenseInput, UpdateExpenseInput
from app.domain.model.expense import Expense

class ExpensesMapper:
    @staticmethod
    def map_new_expense_dto_to_expense(new_expense_dto: NewExpenseInput) -> Expense:
        return Expense(
            description=new_expense_dto.description,
            category_id=new_expense_dto.category_id,
            priority_id=new_expense_dto.priority_id,
            user_id=new_expense_dto.user_id,
            expense_date=new_expense_dto.expense_date,
            amount=new_expense_dto.amount
        )

    @staticmethod
    def map_update_expense_dto_to_expense(update_expense_dto: UpdateExpenseInput) -> Expense:
        return Expense(
            id=update_expense_dto.id,
            description=update_expense_dto.description,
            category_id=update_expense_dto.category_id,
            priority_id=update_expense_dto.priority_id,
            user_id=update_expense_dto.user_id,
            expense_date=update_expense_dto.expense_date,
            amount=update_expense_dto.amount
        )