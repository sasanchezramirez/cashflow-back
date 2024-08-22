from abc import ABC, abstractmethod
from app.domain.model.user import User
from app.domain.model.category import Category
from app.domain.model.budget import Budget
from app.domain.model.priority import Priority
from app.domain.model.expense import Expense
from app.domain.model.recurrent_expense import RecurrentExpense

class PersistenceGateway(ABC):

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
    def create_category(self, category: Category):
        pass

    @abstractmethod
    def get_categories_by_user_id(self, user_id: int):
       pass

    @abstractmethod
    def update_category(self, category: Category):
        pass

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
    def create_priority(self, priority: Priority):
        pass

    @abstractmethod
    def get_priorities(self, user_id: int):
        pass

    @abstractmethod
    def update_priority(self, priority: Priority):
        pass

    @abstractmethod
    def create_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        pass

    @abstractmethod
    def get_recurrent_expenses(self, user_id: int):
        pass

    @abstractmethod
    def update_recurrent_expense(self, recurrent_expense: RecurrentExpense):
        pass

    @abstractmethod
    def create_expense(self, expense: Expense):
        pass

    @abstractmethod
    def get_expenses(self, user_id: int):
        pass

    @abstractmethod
    def update_expense(self, expense: Expense):
        pass