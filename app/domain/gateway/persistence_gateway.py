from abc import ABC, abstractmethod
from app.domain.model.user import User
from app.domain.model.category import Category
from app.domain.model.budget import Budget
from app.domain.model.priority import Priority
from app.domain.model.expense import Expense
from app.domain.model.recurrent_expense import RecurrentExpense
from app.domain.model.saves import Saves
from typing import List

class PersistenceGateway(ABC):

    #Users

    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_user_by_id(self, id: int):
        pass

    @abstractmethod
    def get_user_by_email(self, id: int):
        pass

    @abstractmethod
    def update_user(self, user: User):
        pass

    @abstractmethod
    def get_users_id(self) -> List[int]:
        pass

    #Categories

    @abstractmethod
    def create_category(self, category: Category):
        pass

    @abstractmethod
    def get_categories_by_user_id(self, user_id: int):
       pass

    @abstractmethod
    def update_category(self, category: Category):
        pass
    
     # Budgets

    @abstractmethod
    def create_budget(self, budget: Budget):
        pass

    @abstractmethod
    def get_budgets(self, user_id: int):
        pass

    @abstractmethod
    def update_budget(self, budget: Budget):
        pass

    @abstractmethod
    def get_budget_by_category(self, category_id: int):
        pass

    @abstractmethod
    def get_budgets_by_user_id(self, user_id: int) -> List[Budget]:
        pass
    # Priorities

    @abstractmethod
    def create_priority(self, priority: Priority):
        pass

    @abstractmethod
    def get_priorities(self, user_id: int):
        pass

    @abstractmethod
    def update_priority(self, priority: Priority):
        pass

    # Recurrent Expenses

    @abstractmethod
    def create_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        pass

    @abstractmethod
    def get_recurrent_expenses(self, user_id: int):
        pass

    @abstractmethod
    def update_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        pass

    # Expenses

    @abstractmethod
    def create_expense(self, expense: Expense):
        pass

    @abstractmethod
    def get_expenses(self, user_id: int):
        pass

    @abstractmethod
    def update_expense(self, expense: Expense):
        pass

    # Saves

    @abstractmethod
    def insert_new_save(self, saves: Saves):
        pass
    