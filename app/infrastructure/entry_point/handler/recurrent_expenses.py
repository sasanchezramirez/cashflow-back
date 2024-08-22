import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.utils.api_response import ApiResponse
from app.domain.usecase.recurrent_expenses_usecase import RecurrentExpensesUseCase

# Dtos
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.dto.recurrent_expenses_dto import NewRecurrentExpenseInput, UpdateRecurrentExpenseInput

# Mappers
from app.infrastructure.entry_point.mapper.recurrent_expenses_mapper import RecurrentExpensesMapper

logger = logging.getLogger("Recurrent Expenses Handler")

router = APIRouter(
    prefix='/recurrent-expenses',
    tags=['recurrent-expenses']
)

@router.post('/new-recurrent-expense',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def new_recurrent_expense(
    new_recurrent_expense_dto: NewRecurrentExpenseInput,
    recurrent_expense_usecase: RecurrentExpensesUseCase = Depends(Provide[Container.recurrent_expense_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init new-recurrent-expense handler")
    try:
        new_recurrent_expense = RecurrentExpensesMapper.map_new_recurrent_expense_dto_to_recurrent_expense(new_recurrent_expense_dto)
        created_recurrent_expense = recurrent_expense_usecase.create_recurrent_expense(new_recurrent_expense)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, created_recurrent_expense)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/get_recurrent_expenses',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def get_recurrent_expenses(
    user_id: int,
    recurrent_expense_usecase: RecurrentExpensesUseCase = Depends(Provide[Container.recurrent_expense_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init get_recurrent_expenses handler")
    try:
        recurrent_expenses = recurrent_expense_usecase.get_recurrent_expenses(user_id)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, recurrent_expenses)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/update-recurrent-expense',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def update_recurrent_expense(
    update_recurrent_expense_dto: UpdateRecurrentExpenseInput,
    recurrent_expense_usecase: RecurrentExpensesUseCase = Depends(Provide[Container.recurrent_expense_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init update-recurrent-expense handler")
    try:
        updated_recurrent_expense = RecurrentExpensesMapper.map_update_recurrent_expense_dto_to_recurrent_expense(update_recurrent_expense_dto)
        updated_recurrent_expense = recurrent_expense_usecase.update_recurrent_expense(updated_recurrent_expense)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, updated_recurrent_expense)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)