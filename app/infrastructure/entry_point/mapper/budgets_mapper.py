from app.infrastructure.entry_point.dto.budgets_dto import NewBudgetInput, UpdateBudgetInput
from app.domain.model.budget import Budget
from app.infrastructure.driven_adapter.persistence.entity.budgets_entity import BudgetsEntity

class BudgetsMapper:
    @staticmethod
    def map_new_budget_dto_to_budget(new_budget_dto: NewBudgetInput) -> Budget:
        return Budget(
            weekly_budget=new_budget_dto.weekly_amount,
            monthly_budget=new_budget_dto.monthly_amount,
            user_id=new_budget_dto.user_id,
            category_id=new_budget_dto.category_id
        )
    
    @staticmethod
    def map_update_budget_dto_to_budget(update_budget_dto: UpdateBudgetInput) -> Budget:
        return Budget(
            id=update_budget_dto.id,
            weekly_budget=update_budget_dto.weekly_amount,
            monthly_budget=update_budget_dto.monthly_amount,
            user_id=update_budget_dto.user_id,
            category_id=update_budget_dto.category_id
        )
