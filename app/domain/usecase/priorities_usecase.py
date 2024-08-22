import logging

from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.priority import Priority
from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger("Priorities UseCase")

class PrioritiesUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def create_priority(self, priority: Priority):
        logger.info("Init create priority usecase")
        try:
            created_priority = self.persistence_gateway.create_priority(priority)
            return created_priority
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def get_priorities(self, user_id: int):
        logger.info("Init get priorities usecase")
        try:
            priorities = self.persistence_gateway.get_priorities(user_id)
            return priorities
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)

    def update_priority(self, priority: Priority):
        logger.info("Init update priority usecase")
        try:
            updated_priority = self.persistence_gateway.update_priority(priority)
            return updated_priority
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)