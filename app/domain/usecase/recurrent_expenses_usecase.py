import logging

from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.recurrent_expense import RecurrentExpense
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("Recurrent Expenses UseCase")

class RecurrentExpensesUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def create_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        logger.info("Init create recurrent expense usecase")
        try:
            created_recurrent_expense = self.persistence_gateway.create_recurrent_expense(recurrent_expense)
            return created_recurrent_expense
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def get_recurrent_expenses(self, user_id: int):
        logger.info("Init get recurrent expenses usecase")
        try:
            recurrent_expenses = self.persistence_gateway.get_recurrent_expenses(user_id)
            return recurrent_expenses
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def update_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        logger.info("Init update recurrent expense usecase")
        try:
            updated_recurrent_expense = self.persistence_gateway.update_recurrent_expense(recurrent_expense)
            return updated_recurrent_expense
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)