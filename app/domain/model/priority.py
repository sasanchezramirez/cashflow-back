from pydantic import BaseModel
from typing import Optional

class Priority(BaseModel):
    id: Optional[int] = None
    description: Optional[str] = None