from pydantic import BaseModel
from typing import Optional

class saves(BaseModel):
    id: Optional[int] = None
    month: Optional[str] = None
    saves: Optional[int] = None
    user_id: Optional[int] = None