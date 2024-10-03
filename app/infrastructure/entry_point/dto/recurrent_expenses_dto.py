from pydantic import BaseModel

class NewRecurrentExpenseInput(BaseModel):
    user_id: int
    description: str
    category_id: int
    priority_id: int

class UpdateRecurrentExpenseInput(BaseModel):
    id: int
    description: str
    category_id: int
    priority_id: int
