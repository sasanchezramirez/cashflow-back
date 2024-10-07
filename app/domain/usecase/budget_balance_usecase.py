import logging

from dependency_injector.wiring import inject, Provide
from app.application.container import Container

logger = logging.getLogger(__name__)

@inject
def monthly_task(
    recurrent_expense_usecase = Provide[Container.recurrent_expense_usecase],
    budget_usecase = Provide[Container.budget_usecase],
):
    logger.info("Monthly tasks executed.")
