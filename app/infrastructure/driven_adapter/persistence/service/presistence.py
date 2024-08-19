import logging

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.infrastructure.driven_adapter.persistence.entity.user_entity import User_entity
from app.infrastructure.driven_adapter.persistence.repository.user_repository import UserRepository
from app.infrastructure.driven_adapter.persistence.repository.categories_repository import CategoriesRepository
from app.domain.model.user import User
from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.category import Category
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper
from app.infrastructure.driven_adapter.persistence.mapper.categories_mapper import CategoriesMapper
logger = logging.getLogger("Persistence")

class Persistence(PersistenceGateway):
    def __init__(self, session: Session):
        logger.info("Init persistence service")
        self.session = session
        self.user_repository = UserRepository(session)
        self.category_repository = CategoriesRepository(session)

    def create_user(self, user: User):
        try:
            user_entity = User_entity(user)
            created_user_entity = self.user_repository.create_user(user_entity)
            self.session.commit()
            return mapper.map_user_entity_to_user(created_user_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_user_by_id(self, id: int):
        try:
            user_entity = self.user_repository.get_user_by_id(id)
            return mapper.map_user_entity_to_user(user_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_user_by_email(self, email: str):
        try:
            user_entity = self.user_repository.get_user_by_email(email)
            return mapper.map_user_entity_to_user(user_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
    
    def update_user(self, user: User):
        try:
            existing_user = self.user_repository.get_user_by_id(user.id)
            if not existing_user:
                raise CustomException(ResponseCodeEnum.KOU02)
            user_entity = mapper.map_user_update_to_user_entity(user, existing_user)
            updated_user_entity = self.user_repository.update_user(user_entity)
            self.session.commit()
            return mapper.map_user_entity_to_user(updated_user_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating user: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def create_category(self, category: Category):
        try:
            category_entity = CategoriesMapper.map_category_to_category_entity(category)
            created_category_entity = self.category_repository.create_category(category_entity)
            self.session.commit()
            return CategoriesMapper.map_category_entity_to_category(created_category_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating category: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_category_by_id(self, id: int):
        try:
            category_entity = self.category_repository.get_category_by_id(id)
            return CategoriesMapper.map_category_entity_to_category(category_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting category: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
            
    
    def get_categories_by_user_id(self, user_id: int):
        try:
            categories = []
            category_entities = self.category_repository.get_categories_by_user_id(user_id)
            for category_entity in category_entities:
                categories.append(CategoriesMapper.map_category_entity_to_category(category_entity))
            return categories
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting categories: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def update_category(self, category: Category):
        try:
            existing_category = self.category_repository.get_category_by_id(category.id)
            if not existing_category:
                raise CustomException(ResponseCodeEnum.KOU02)
            category_entity = CategoriesMapper.map_category_update_to_category_entity(category, existing_category)
            updated_category_entity = self.category_repository.update_category(category_entity)
            self.session.commit()
            return CategoriesMapper.map_category_entity_to_category(updated_category_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating category: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
