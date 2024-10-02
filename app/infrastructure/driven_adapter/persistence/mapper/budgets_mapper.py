from app.infrastructure.entry_point.dto.budgets_dto import NewBudgetInput, UpdateBudgetInput
from app.domain.model.budget import Budget
from app.infrastructure.driven_adapter.persistence.entity.budgets_entity import BudgetsEntity

class BudgetsMapper:

    @staticmethod
    def map_budget_to_budget_entity(budget: Budget) -> BudgetsEntity:
        return BudgetsEntity(
            weekly_amount=budget.weekly_budget,
            monthly_amount=budget.monthly_budget,
            user_id=budget.user_id
        )
    
    @staticmethod
    def map_budget_entity_to_budget(budget_entity: BudgetsEntity) -> Budget:
        return Budget(
            id=budget_entity.id,
            weekly_budget=budget_entity.weekly_amount,
            monthly_budget=budget_entity.monthly_amount,
            user_id=budget_entity.user_id
        )
    
    @staticmethod
    def map_budget_update_to_budget_entity(budget: Budget, existing_budget: BudgetsEntity) -> BudgetsEntity:
        existing_budget.weekly_amount = budget.weekly_budget
        existing_budget.monthly_amount = budget.monthly_budget
        existing_budget.user_id = budget.user_id
        return existing_budget