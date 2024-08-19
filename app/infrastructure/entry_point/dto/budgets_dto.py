from pydantic import BaseModel

class NewBudgetInput(BaseModel):
    weekly_amount: int
    monthly_amount: int

class UpdateBudgetInput(BaseModel):
    id: int
    weekly_amount: int
    monthly_amount: int