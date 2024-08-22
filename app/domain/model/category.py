from pydantic import BaseModel
from typing import Optional, List

class Category(BaseModel):
    id: Optional[int] = None
    description: Optional[str] = None
    user_id: Optional[int] = None
    budget_id: Optional[int] = None

class Categories(BaseModel):
    categories: List[Category]