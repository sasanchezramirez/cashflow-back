import logging

from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.expense import Expense
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("Expenses UseCase")

class ExpensesUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def create_expense(self, expense: Expense):
        logger.info("Init create expense usecase")
        try:
            created_expense = self.persistence_gateway.create_expense(expense)
            return created_expense
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def get_expenses(self, user_id: int):
        logger.info("Init get expenses usecase")
        try:
            expenses = self.persistence_gateway.get_expenses(user_id)
            return expenses
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def update_expense(self, expense: Expense):
        logger.info("Init update expense usecase")
        try:
            updated_expense = self.persistence_gateway.update_expense(expense)
            return updated_expense
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)