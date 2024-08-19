import logging

from fastapi import APIRouter, Depends 
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from app.application.container import Container
from app.domain.model.util.custom_exceptions import CustomException
from app.domain.usecase.util.jwt import get_current_user
from app.domain.model.util.response_codes import ResponseCodeEnum
from app.infrastructure.entry_point.utils.api_response import ApiResponse
from app.domain.usecase.categories_usecase import CategoriesUseCase

#Dtos
from app.infrastructure.entry_point.dto.response_dto import ResponseDTO
from app.infrastructure.entry_point.dto.categories_dto import NewCategoryInput

#Mappers
from app.infrastructure.entry_point.mapper.categories_mapper import CategoriesMapper

logger = logging.getLogger("Categories Handler")

router = APIRouter(
    prefix='/categories',
    tags=['categories']
)

@router.post('/new-category', 
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def new_category(
    new_category_dto: NewCategoryInput,
    category_usecase: CategoriesUseCase = Depends(Provide[Container.category_usecase]),
    current_user: str = Depends(get_current_user)
): 
    """
    Creates a new category in the system.
    
    Args:
        new_category_dto (dict): The data transfer object containing the category's details.
        category_usecase (object): The Category UseCase.

    Returns:
        ResponseDTO: A response object containing the operation data.
    """
    logger.info("Init new-category handler")
    try:
        new_category = CategoriesMapper.map_new_category_dto_to_category(new_category_dto)
        created_category = category_usecase.create_category(new_category)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, created_category)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)
        return JSONResponse(status_code=500, content=response_code)
    
@router.post('/get_categories',  
    response_model=ResponseDTO,
    responses={
        200: {"description": "Operation successful", "model": ResponseDTO},
        400: {"description": "Validation Error", "model": ResponseDTO},
        500: {"description": "Internal Server Error", "model": ResponseDTO},
    }
)
@inject
async def get_categories(
    user_id: int,
    category_usecase: CategoriesUseCase = Depends(Provide[Container.category_usecase]),
    current_user: str = Depends(get_current_user)
):
    """
    Gets all categories for a user.
    
    Args:
        user_id (int): The user's id.
        category_usecase (object): The Category UseCase.

    Returns:
        ResponseDTO: A response object containing the operation data.
    """
    logger.info("Init get_categories handler")
    try:
        categories = category_usecase.get_categories(user_id)
        return ApiResponse.create_response(ResponseCodeEnum.KO000, categories)
    except CustomException as e:
        response_code = e.to_dict()
        return JSONResponse(status_code=e.http_status, content=response_code)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        response_code = ApiResponse.create_response(ResponseCodeEnum.KOG01)