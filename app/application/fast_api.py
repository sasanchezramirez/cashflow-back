from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.application.container import Container
from app.application.handler import Handlers
from app.domain.usecase.budget_balance_usecase import BudgetBalanceUseCase

@asynccontextmanager
async def lifespan(app):
    container = Container()
    app.container = container
    scheduler_service = container.scheduler_service()
    
    try:
        yield
    finally:
        await scheduler_service.shutdown()

def create_app():
    fast_api = FastAPI(lifespan=lifespan)

    for handler in Handlers.iterator():
        fast_api.include_router(handler.router)
        
    return fast_api
