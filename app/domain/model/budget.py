from pydantic import BaseModel
from typing import Optional

class Budget(BaseModel):
    id: Optional[int] = None
    weekly_budget: Optional[float] = None
    monthly_budget: Optional[float] = None