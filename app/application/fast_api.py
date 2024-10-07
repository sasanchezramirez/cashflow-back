from fastapi import FastAPI
from app.application.container import Container
from app.application.handler import Handlers
from app.domain.usecase.budget_balance_usecase import monthly_task



def create_app():
    container = Container()
    fast_api = FastAPI()
    fast_api.container = container 
    scheduler_service = container.scheduler_service()
    scheduler_service.schedule_monthly_task(func=monthly_task)

    @fast_api.on_event("shutdown")
    def shutdown_event():
        scheduler_service.shutdown()
    for handler in Handlers.iterator():
        fast_api.include_router(handler.router)
    return fast_api