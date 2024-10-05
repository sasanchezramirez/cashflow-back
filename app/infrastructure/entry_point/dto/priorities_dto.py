from pydantic import BaseModel

class NewPriorityInput(BaseModel):
    description: str
    user_id: int

class UpdatePriorityInput(BaseModel):
    id: int
    description: str
    user_id: int