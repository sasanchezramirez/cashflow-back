from app.domain.model.category import Category
from app.infrastructure.entry_point.dto.categories_dto import NewCategoryInput, UpdateCategoryInput


class CategoriesMapper:
    @staticmethod
    def map_new_category_dto_to_category(new_category_dto: NewCategoryInput):
        category = Category(
            description=new_category_dto.description,
            user_id=new_category_dto.user_id,
            budget_id=new_category_dto.budget_id
        )
        return category
    
    @staticmethod
    def map_update_category_dto_to_category(update_category_dto: UpdateCategoryInput):
        category = Category(
            id=update_category_dto.id,
            description=update_category_dto.description,
            budget_id=update_category_dto.budget_id
        )
        return category