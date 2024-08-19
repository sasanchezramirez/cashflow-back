import logging

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
        except Exception as e:
            logger.error(f"Unhandled error: {e}")
            raise e
        
