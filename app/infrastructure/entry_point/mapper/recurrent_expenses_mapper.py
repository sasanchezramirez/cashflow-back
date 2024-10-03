from app.infrastructure.entry_point.dto.recurrent_expenses_dto import NewRecurrentExpenseInput, UpdateRecurrentExpenseInput
from app.domain.model.recurrent_expense import RecurrentExpense
from app.infrastructure.driven_adapter.persistence.entity.recurrent_expenses_entity import RecurrentExpensesEntity

class RecurrentExpensesMapper:
    @staticmethod
    def map_new_recurrent_expense_dto_to_recurrent_expense(new_recurrent_expense_dto: NewRecurrentExpenseInput) -> RecurrentExpense:
        return RecurrentExpense(
            description=new_recurrent_expense_dto.description,
            category_id=new_recurrent_expense_dto.category_id,
            priority_id=new_recurrent_expense_dto.priority_id,
            user_id=new_recurrent_expense_dto.user_id
        )
