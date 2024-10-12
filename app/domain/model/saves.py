from pydantic import BaseModel
from typing import Optional

class Saves(BaseModel):
    id: Optional[int] = None
    month: Optional[str] = None
    saves: Optional[int] = None
    user_id: Optional[int] = None