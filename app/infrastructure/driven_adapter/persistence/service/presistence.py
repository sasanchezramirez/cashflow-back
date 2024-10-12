import logging

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.infrastructure.driven_adapter.persistence.entity.user_entity import User_entity
from app.infrastructure.driven_adapter.persistence.repository.user_repository import UserRepository
from app.infrastructure.driven_adapter.persistence.repository.categories_repository import CategoriesRepository
from app.infrastructure.driven_adapter.persistence.repository.budgets_repository import BudgetsRepository
from app.infrastructure.driven_adapter.persistence.repository.priorities_repository import PrioritiesRepository
from app.infrastructure.driven_adapter.persistence.repository.recurrent_expenses_repository import RecurrentExpensesRepository
from app.infrastructure.driven_adapter.persistence.repository.expenses_repository import ExpensesRepository
from app.infrastructure.driven_adapter.persistence.repository.saves_repository import SavesRepository
from app.domain.model.user import User
from app.domain.gateway.persistence_gateway import PersistenceGateway
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.domain.model.category import Category
from app.domain.model.budget import Budget
from app.domain.model.priority import Priority
from app.domain.model.expense import Expense
from app.domain.model.recurrent_expense import RecurrentExpense
from app.domain.model.saves import Saves
import app.infrastructure.driven_adapter.persistence.mapper.user_mapper as mapper
from app.infrastructure.driven_adapter.persistence.mapper.categories_mapper import CategoriesMapper
from app.infrastructure.driven_adapter.persistence.mapper.budgets_mapper import BudgetsMapper
from app.infrastructure.driven_adapter.persistence.mapper.priorities_mapper import PrioritiesMapper
from app.infrastructure.driven_adapter.persistence.mapper.recurrent_expenses_mapper import RecurrentExpensesMapper
from app.infrastructure.driven_adapter.persistence.mapper.expenses_mapper import ExpensesMapper
from app.infrastructure.driven_adapter.persistence.mapper.saves_mapper import SavesMapper
logger = logging.getLogger("Persistence")

class Persistence(PersistenceGateway):
    def __init__(self, session: Session):
        logger.info("Init persistence service")
        self.session = session
        self.user_repository = UserRepository(session)
        self.category_repository = CategoriesRepository(session)
        self.budget_repository = BudgetsRepository(session)
        self.priority_repository = PrioritiesRepository(session)
        self.recurrent_expense_repository = RecurrentExpensesRepository(session)
        self.expense_repository = ExpensesRepository(session)
        self.saves_repository = SavesRepository(session)

# Users
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

# Categories

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
            
            CategoriesMapper.map_category_update_to_category_entity(category, existing_category)
          
            self.session.commit()
            return CategoriesMapper.map_category_entity_to_category(existing_category)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating category: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)

# Budgets

    def create_budget(self, budget: Budget):
        try:
            budget_entity = BudgetsMapper.map_budget_to_budget_entity(budget)
            created_budget_entity = self.budget_repository.create_budget(budget_entity)
            return BudgetsMapper.map_budget_entity_to_budget(created_budget_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating budget: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)

    def get_budgets(self, user_id: int):
        try:
            budget_entities = self.budget_repository.get_budgets_by_user_id(user_id)
            return [BudgetsMapper.map_budget_entity_to_budget(budget) for budget in budget_entities]
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting budgets: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def update_budget(self, budget: Budget):
        try:
            existing_budget = self.budget_repository.get_budget_by_id(budget.id)
            if not existing_budget:
                raise CustomException(ResponseCodeEnum.KOU02)
            updated_budget_entity = BudgetsMapper.map_budget_update_to_budget_entity(budget, existing_budget)
            updated_budget_entity = self.budget_repository.update_budget(updated_budget_entity)
            self.session.commit()
            return BudgetsMapper.map_budget_entity_to_budget(updated_budget_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating budget: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_budget_by_category(self, category_id: int):
        try:
            budget_entity = self.budget_repository.get_budget_by_category(category_id)
            return BudgetsMapper.map_budget_entity_to_budget(budget_entity)
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting budget by category: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def get_budgets_by_user_id(self, user_id: int) -> List[Budget]:
        try:
            budget_entities = self.budget_repository.get_budgets_by_user_id(user_id)
            return [BudgetsMapper.map_budget_entity_to_budget(budget) for budget in budget_entities]
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting budgets: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)

# Priorities

    def create_priority(self, priority: Priority):
        try:
            priority_entity = PrioritiesMapper.map_priority_to_priority_entity(priority)
            created_priority_entity = self.priority_repository.create_priority(priority_entity)
            return PrioritiesMapper.map_priority_entity_to_priority(created_priority_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating priority: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)

    def get_priorities(self, user_id: int):
        try:
            priority_entities = self.priority_repository.get_priorities_by_user_id(user_id)
            return [PrioritiesMapper.map_priority_entity_to_priority(priority) for priority in priority_entities]
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting priorities: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def update_priority(self, priority: Priority):
        try:
            existing_priority = self.priority_repository.get_priority_by_id(priority.id)
            if not existing_priority:
                raise CustomException(ResponseCodeEnum.KOU02)
            updated_priority_entity = PrioritiesMapper.map_priority_update_to_priority_entity(priority, existing_priority)
            updated_priority_entity = self.priority_repository.update_priority(updated_priority_entity)
            self.session.commit()
            return PrioritiesMapper.map_priority_entity_to_priority(updated_priority_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating priority: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
# Recurrent Expenses

    def create_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        try:
            recurrent_expense_entity = RecurrentExpensesMapper.map_recurrent_expense_to_recurrent_expense_entity(recurrent_expense)
            created_recurrent_expense_entity = self.recurrent_expense_repository.create_recurrent_expense(recurrent_expense_entity)
            return RecurrentExpensesMapper.map_recurrent_expense_entity_to_recurrent_expense(created_recurrent_expense_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating recurrent expense: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)

    def get_recurrent_expenses(self, user_id: int):
        try:
            recurrent_expense_entities = self.recurrent_expense_repository.get_recurrent_expenses_by_user_id(user_id)
            return [RecurrentExpensesMapper.map_recurrent_expense_entity_to_recurrent_expense(recurrent_expense) for recurrent_expense in recurrent_expense_entities]
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting recurrent expenses: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def update_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        try:
            existing_recurrent_expense = self.recurrent_expense_repository.get_recurrent_expense_by_id(recurrent_expense.id)
            if not existing_recurrent_expense:
                raise CustomException(ResponseCodeEnum.KOU02)
            updated_recurrent_expense_entity = RecurrentExpensesMapper.map_recurrent_expense_update_to_recurrent_expense_entity(recurrent_expense, existing_recurrent_expense)
            updated_recurrent_expense_entity = self.recurrent_expense_repository.update_recurrent_expense(updated_recurrent_expense_entity)
            self.session.commit()
            return RecurrentExpensesMapper.map_recurrent_expense_entity_to_recurrent_expense(updated_recurrent_expense_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating recurrent expense: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
# Expenses

    def create_expense(self, expense: Expense):
        try:
            expense_entity = ExpensesMapper.map_expense_to_expense_entity(expense)
            created_expense_entity = self.expense_repository.create_expense(expense_entity)
            return ExpensesMapper.map_expense_entity_to_expense(created_expense_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating expense: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)

    def get_expenses(self, user_id: int):
        try:
            expense_entities = self.expense_repository.get_expenses_by_user_id(user_id)
            return [ExpensesMapper.map_expense_entity_to_expense(expense) for expense in expense_entities]
        except CustomException as e:
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error getting expenses: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    def update_expense(self, expense: Expense):
        try:
            existing_expense = self.expense_repository.get_expense_by_id(expense.id)
            if not existing_expense:
                raise CustomException(ResponseCodeEnum.KOU02)
            
            updated_expense_entity = ExpensesMapper.map_expense_update_to_expense_entity(expense, existing_expense)
            
            self.session.commit()
            return ExpensesMapper.map_expense_entity_to_expense(existing_expense)  # Mismas referencias
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error updating expense: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)
        
    # Saves
    def insert_new_save(self, saves: Saves):
        try:
            saves_entity = SavesMapper.map_saves_to_saves_entity(saves)
            created_saves_entity = self.saves_repository.create_save(saves_entity)
            return SavesMapper.map_saves_entity_to_saves(created_saves_entity)
        except CustomException as e:
            self.session.rollback()
            raise e
        except SQLAlchemyError as e:
            logger.error(f"Error creating save: {e}")
            self.session.rollback()
            raise CustomException(ResponseCodeEnum.KOG02)