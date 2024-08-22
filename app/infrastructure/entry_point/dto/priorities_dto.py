from pydantic import BaseModel

class NewPriorityInput(BaseModel):
    description: str

class UpdatePriorityInput(BaseModel):
    id: int
    description: str