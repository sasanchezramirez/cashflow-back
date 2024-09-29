import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.utils.api_response import ApiResponse
from app.domain.usecase.expenses_usecase import ExpensesUseCase

# Dtos
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.dto.expenses_dto import NewExpenseInput, UpdateExpenseInput

# Mappers
from app.infrastructure.entry_point.mapper.expenses_mapper import ExpensesMapper

logger = logging.getLogger("Expenses Handler")

router = APIRouter(
    prefix='/expenses',
    tags=['expenses']
)

@router.post('/new-expense',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def new_expense(
    new_expense_dto: NewExpenseInput,
    expense_usecase: ExpensesUseCase = Depends(Provide[Container.expense_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init new-expense handler")
    try:
        new_expense = ExpensesMapper.map_new_expense_dto_to_expense(new_expense_dto)
        created_expense = expense_usecase.create_expense(new_expense)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, created_expense)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/get-expenses',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def get_expenses(
    user_id: int,
    expense_usecase: ExpensesUseCase = Depends(Provide[Container.expense_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init get-expenses handler")
    try:
        expenses = expense_usecase.get_expenses(user_id)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, expenses)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/update-expense',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def update_expense(
    update_expense_dto: UpdateExpenseInput,
    expense_usecase: ExpensesUseCase = Depends(Provide[Container.expense_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init update-expense handler")
    try:
        updated_expense = ExpensesMapper.map_update_expense_dto_to_expense(update_expense_dto)
        updated_expense = expense_usecase.update_expense(updated_expense)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, updated_expense)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)