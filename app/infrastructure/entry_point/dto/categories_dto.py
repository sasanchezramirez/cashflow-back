from pydantic import BaseModel

class NewCategoryInput(BaseModel):
    description: str
    user_id: int
    budget_id: int