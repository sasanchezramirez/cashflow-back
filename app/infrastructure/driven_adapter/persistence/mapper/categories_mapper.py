from app.domain.model.category import Category
from app.infrastructure.driven_adapter.persistence.entity.categories_entity import CategoryEntity

class CategoriesMapper:
    @staticmethod
    def map_category_entity_to_category(category_entity: CategoryEntity):
        category = Category(
            id=category_entity.id,
            description=category_entity.description,
            budget_id=category_entity.budget_id,
            user_id=category_entity.user_id
        )
        return category
    
    @staticmethod
    def map_category_to_category_entity(category: Category):
        category_entity = CategoryEntity(
            description=category.description,
            budget_id=category.budget_id,
            user_id=category.user_id
        )
        return category_entity
    
    @staticmethod
    def map_category_update_to_category_entity(category: Category, existing_category: CategoryEntity):
        existing_category.description = category.description
        existing_category.budget_id = category.budget_id
        return existing_category