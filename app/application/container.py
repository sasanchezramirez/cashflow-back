from app.application.handler import Handlers
from app.domain.usecase.user_usecase import UserUseCase
from app.domain.usecase.auth_usecase import AuthUseCase
from app.domain.usecase.categories_usecase import CategoriesUseCase
from app.domain.usecase.budgets_usecase import BudgetsUseCase
from app.domain.usecase.priorities_usecase import PrioritiesUseCase
from app.domain.usecase.recurrent_expenses_usecase import RecurrentExpensesUseCase
from app.domain.usecase.expenses_usecase import ExpensesUseCase
from app.infrastructure.driven_adapter.persistence.service.presistence import Persistence
from app.infrastructure.driven_adapter.persistence.config.database import SessionLocal
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules= Handlers.modules())

    session = providers.Singleton(SessionLocal)

    persistence_gateway = providers.Factory(Persistence, session=session)

    user_usecase = providers.Factory(UserUseCase, persistence_gateway=persistence_gateway)
    auth_usecase = providers.Factory(AuthUseCase, persistence_gateway=persistence_gateway)
    category_usecase = providers.Factory(CategoriesUseCase, persistence_gateway=persistence_gateway)
    budget_usecase = providers.Factory(BudgetsUseCase, persistence_gateway=persistence_gateway)
    priority_usecase = providers.Factory(PrioritiesUseCase, persistence_gateway=persistence_gateway)
    recurrent_expense_usecase = providers.Factory(RecurrentExpensesUseCase, persistence_gateway=persistence_gateway)
    expense_usecase = providers.Factory(ExpensesUseCase, persistence_gateway=persistence_gateway)

