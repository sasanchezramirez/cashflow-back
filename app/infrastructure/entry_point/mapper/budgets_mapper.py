from app.infrastructure.entry_point.dto.budgets_dto import NewBudgetInput, UpdateBudgetInput
from app.domain.model.budget import Budget
from app.infrastructure.driven_adapter.persistence.entity.budgets_entity import BudgetsEntity

class BudgetsMapper:
    @staticmethod
    def map_new_budget_dto_to_budget(new_budget_dto: NewBudgetInput) -> Budget:
        return Budget(
            weekly_budget=new_budget_dto.weekly_amount,
            monthly_budget=new_budget_dto.monthly_amount,
            user_id=new_budget_dto.user_id
        )
