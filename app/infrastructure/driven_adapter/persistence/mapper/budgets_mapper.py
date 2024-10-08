from app.infrastructure.entry_point.dto.budgets_dto import NewBudgetInput, UpdateBudgetInput
from app.domain.model.budget import Budget
from app.infrastructure.driven_adapter.persistence.entity.budgets_entity import BudgetsEntity

class BudgetsMapper:

    @staticmethod
    def map_budget_to_budget_entity(budget: Budget) -> BudgetsEntity:
        return BudgetsEntity(
            weekly_amount=budget.weekly_budget,
            monthly_amount=budget.monthly_budget,
            user_id=budget.user_id,
            category_id=budget.category_id,
            weekly_balance=budget.weekly_balance,
            monthly_balance=budget.monthly_balance
        )
    
    @staticmethod
    def map_budget_entity_to_budget(budget_entity: BudgetsEntity) -> Budget:
        return Budget(
            id=budget_entity.id,
            weekly_budget=budget_entity.weekly_amount,
            monthly_budget=budget_entity.monthly_amount,
            user_id=budget_entity.user_id,
            category_id=budget_entity.category_id,
            weekly_balance=budget_entity.weekly_balance,
            monthly_balance=budget_entity.monthly_balance
        )
    
    @staticmethod
    def map_budget_update_to_budget_entity(budget: Budget, existing_budget: BudgetsEntity) -> BudgetsEntity:
        existing_budget.weekly_amount = budget.weekly_budget
        existing_budget.monthly_amount = budget.monthly_budget
        existing_budget.user_id = budget.user_id
        existing_budget.category_id = budget.category_id
        existing_budget.weekly_balance = budget.weekly_balance
        existing_budget.monthly_balance = budget.monthly_balance
        return existing_budget