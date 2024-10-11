import logging



from app.domain.gateway.persistence_gateway import PersistenceGateway

logger = logging.getLogger(__name__)

class BudgetBalanceUseCase:
    def __init__(self, persistence_gateway: PersistenceGateway):
        self.persistence_gateway = persistence_gateway

    def monthly_task():
        logger.info("Monthly tasks executed.")
