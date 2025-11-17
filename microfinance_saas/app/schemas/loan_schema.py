from pydantic import BaseModel
from typing import Optional

class LoanCreate(BaseModel):
    user_id: int
    amount: float
    interest_rate: Optional[float] = 0.05
    term_months: int

class LoanOut(BaseModel):
    id: int
    user_id: int
    amount: float
    interest_rate: float
    term_months: int
    status: str

    class Config:
        from_attributes = True
