from pydantic import BaseModel

class TransactionCreate(BaseModel):
    loan_id: int
    amount: float
    transaction_type: str  # disbursement, repayment

class TransactionOut(BaseModel):
    id: int
    loan_id: int
    amount: float
    transaction_type: str

    class Config:
        from_attributes = True
