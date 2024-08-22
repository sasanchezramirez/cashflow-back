import logging

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.utils.api_response import ApiResponse
from app.domain.usecase.priorities_usecase import PrioritiesUseCase

# Dtos
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.dto.priorities_dto import NewPriorityInput, UpdatePriorityInput

# Mappers
from app.infrastructure.entry_point.mapper.priorities_mapper import PrioritiesMapper

logger = logging.getLogger("Priorities Handler")

router = APIRouter(
    prefix='/priorities',
    tags=['priorities']
)

@router.post('/new-priority',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def new_priority(
    new_priority_dto: NewPriorityInput,
    priority_usecase: PrioritiesUseCase = Depends(Provide[Container.priority_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init new-priority handler")
    try:
        new_priority = PrioritiesMapper.map_new_priority_dto_to_priority(new_priority_dto)
        created_priority = priority_usecase.create_priority(new_priority)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, created_priority)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/get_priorities',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def get_priorities(
    user_id: int,
    priority_usecase: PrioritiesUseCase = Depends(Provide[Container.priority_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init get_priorities handler")
    try:
        priorities = priority_usecase.get_priorities(user_id)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, priorities)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)

@router.post('/update-priority',
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def update_priority(
    update_priority_dto: UpdatePriorityInput,
    priority_usecase: PrioritiesUseCase = Depends(Provide[Container.priority_usecase]),
    current_user: str = Depends(get_current_user)
):
    logger.info("Init update-priority handler")
    try:
        updated_priority = PrioritiesMapper.map_update_priority_dto_to_priority(update_priority_dto)
        updated_priority = priority_usecase.update_priority(updated_priority)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, updated_priority)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)