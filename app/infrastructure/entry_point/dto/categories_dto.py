from pydantic import BaseModel
from typing import List

class NewCategoryInput(BaseModel):
    description: str
    user_id: int
    budget_id: int

class CategoryOutputDto(BaseModel):
    id: int
    description: str
    user_id: int
    budget_id: int

class CategoryListOutputDto(BaseModel):
    categories = List[CategoryOutputDto]