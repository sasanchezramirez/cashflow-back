from pydantic import BaseModel

class NewExpenseInput(BaseModel):
    description: str
    category_id: int
    priority_id: int
    user_id: int
    expense_date: str
    amount: int

class UpdateExpenseInput(BaseModel):
    id: int
    description: str
    category_id: int
    priority_id: int
    user_id: int
    expense_date: str
    amount: int