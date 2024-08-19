from app.infrastructure.entry_point.dto.budgets_dto import NewBudgetInput, UpdateBudgetInput
from app.domain.model.budget import Budget
from app.infrastructure.driven_adapter.persistence.entity.budgets_entity import BudgetsEntity

class BudgetsMapper:
    @staticmethod
    def map_new_budget_dto_to_budget(new_budget_dto: NewBudgetInput) -> Budget:
        return Budget(
            weekly_amount=new_budget_dto.weekly_amount,
            monthly_amount=new_budget_dto.monthly_amount
        )

    @staticmethod
    def map_budget_to_budget_entity(budget: Budget) -> BudgetsEntity:
        return BudgetsEntity(
            weekly_amount=budget.weekly_amount,
            monthly_amount=budget.monthly_amount
        )
    
    @staticmethod
    def map_budget_entity_to_budget(budget_entity: BudgetsEntity) -> Budget:
        return Budget(
            id=budget_entity.id,
            weekly_amount=budget_entity.weekly_amount,
            monthly_amount=budget_entity.monthly_amount
        )
    
    @staticmethod
    def map_budget_update_to_budget_entity(budget: Budget, existing_budget: BudgetsEntity) -> BudgetsEntity:
        existing_budget.weekly_amount = budget.weekly_amount
        existing_budget.monthly_amount = budget.monthly_amount
        return existing_budget