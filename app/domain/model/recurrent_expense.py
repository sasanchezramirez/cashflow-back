from pydantic import BaseModel
from typing import Optional

class RecurrentExpense(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    priority_id: Optional[int] = None