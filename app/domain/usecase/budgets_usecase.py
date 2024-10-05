import logging

from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.budget import Budget
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("Budgets UseCase")

class BudgetsUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def create_budget(self, budget: Budget):
        logger.info("Init create budget usecase")
        try:
            created_budget = self.persistence_gateway.create_budget(budget)
            return created_budget
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def get_budgets(self, user_id: int):
        logger.info("Init get budgets usecase")
        try:
            budgets = self.persistence_gateway.get_budgets(user_id)
            return budgets
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def update_budget(self, budget: Budget):
        logger.info("Init update budget usecase")
        try:
            updated_budget = self.persistence_gateway.update_budget(budget)
            return updated_budget
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
    def update_budget_amount_by_category_id(self, category_id: int, amount: float):
        logger.info("Init update budget amount usecase")
        try:
            budget: Budget = self.persistence_gateway.get_budget_by_category(category_id)
            old_monthly_amount = budget.monthly_budget
            new_monthly_amount = old_monthly_amount + amount
            old_weekly_amount = budget.weekly_budget
            new_weekly_amount = old_weekly_amount - amount
            budget.monthly_budget = new_monthly_amount
            budget.weekly_budget = new_weekly_amount
            updated_budget = self.persistence_gateway.update_budget(budget)
            return updated_budget
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)


