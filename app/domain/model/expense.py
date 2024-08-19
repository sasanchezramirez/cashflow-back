from pydantic import BaseModel
from typing import Optional

class Expense(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    description: Optional[str] = None
    category_id: Optional[int] = None
    amount: Optional[float] = None
    expense_date: Optional[str] = None
    priority_id: Optional[int] = None
