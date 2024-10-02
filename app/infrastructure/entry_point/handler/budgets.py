import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.utils.api_response import ApiResponse
from app.domain.usecase.budgets_usecase import BudgetsUseCase

# Dtos
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.dto.budgets_dto import NewBudgetInput, UpdateBudgetInput

# Mappers
from app.infrastructure.entry_point.mapper.budgets_mapper import BudgetsMapper

logger = logging.getLogger("Budgets Handler")

router = APIRouter(
    prefix='/budgets',
    tags=['budgets']
)

@router.post('/new-budget',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def new_budget(
    new_budget_dto: NewBudgetInput,
    budget_usecase: BudgetsUseCase = Depends(Provide[Container.budget_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init new-budget handler")
    try:
        new_budget = BudgetsMapper.map_new_budget_dto_to_budget(new_budget_dto)
        created_budget = budget_usecase.create_budget(new_budget)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, created_budget)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/get-budgets',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def get_budgets(
    user_id: int,
    budget_usecase: BudgetsUseCase = Depends(Provide[Container.budget_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init get_budgets handler")
    try:
        budgets = budget_usecase.get_budgets(user_id)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, budgets)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/update-budget',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def update_budget(
    update_budget_dto: UpdateBudgetInput,
    budget_usecase: BudgetsUseCase = Depends(Provide[Container.budget_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init update-budget handler")
    try:
        updated_budget = BudgetsMapper.map_update_budget_dto_to_budget(update_budget_dto)
        updated_budget = budget_usecase.update_budget(updated_budget)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, updated_budget)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)