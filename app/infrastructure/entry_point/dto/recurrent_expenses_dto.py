from pydantic import BaseModel

class NewRecurrentExpenseInput(BaseModel):
    description: str
    amount: int

class UpdateRecurrentExpenseInput(BaseModel):
    id: int
    description: str
    amount: int