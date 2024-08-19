import logging

from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.category import Category
from app.domain.gateway.persistence_gateway import PersistenceGateway
logger = logging.getLogger("Categories UseCase")

class CategoriesUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def create_category(self, category: Category):
        logger.info("Init create category usecase")
        try:
            created_category = self.persistence_gateway.create_category(category)
            return created_category
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
    
    def get_categories(self, user_id: int):
        logger.info("Init get categories usecase")
        try:
            categories = self.persistence_gateway.get_categories_by_user_id(user_id)
            return categories
        except CustomException as e:
            logger.error(f"Custom exception: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise CustomException(ResponseCodeEnum.KOG01)
        
        
