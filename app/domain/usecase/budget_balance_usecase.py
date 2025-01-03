import logging
from datetime import datetime

from app.domain.model.saves import Saves

from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger(__name__)

class BudgetBalanceUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def monthly_task(self):
        user_id_list = self.persistence_gateway.get_users_id()
        for user_id in user_id_list:
            budgets = self.persistence_gateway.get_budgets_by_user_id(user_id)
            total_budget = 0
            for budget in budgets:
                total_budget += budget.monthly_balance
            new_save = self.create_save(user_id, total_budget)
            try:
                self.persistence_gateway.insert_new_save(new_save)
                for budget in budgets:
                    budget.monthly_balance = budget.monthly_budget
                    self.persistence_gateway.update_budget(budget)
            except Exception as e:
                logger.error(f"Error creating save: {e}")
                raise e
            logger.info(f"Save created: {new_save}")

    def create_save(self, user_id: int, saves: int) -> Saves:
        save = Saves(
            month=datetime.now().strftime("%B"),
            saves=saves, 
            user_id=user_id)
        return save
    
    def weekly_task(self):
        user_id_list = self.persistence_gateway.get_users_id()
        for user_id in user_id_list:
            try:
                budgets = self.persistence_gateway.get_budgets_by_user_id(user_id)
                for budget in budgets:
                    budget.weekly_balance = budget.weekly_budget
                    self.persistence_gateway.update_budget(budget)
            except Exception as e:
                logger.error(f"Error creating save: {e}")
                raise e
            logger.info(f"Budget updated: {budget}")