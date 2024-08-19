from abc import ABC, abstractmethod
from app.domain.model.user import User
from app.domain.model.category import Category

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