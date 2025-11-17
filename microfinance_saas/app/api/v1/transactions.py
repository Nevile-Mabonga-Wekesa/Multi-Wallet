from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.transaction_schema import TransactionCreate, TransactionOut
from app.services.transaction_service import create_transaction, get_transactions
from app.core.database import get_db
from typing import List
router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionOut)
def add_transaction(txn: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, txn.loan_id, txn.amount, txn.transaction_type)

@router.get("/", response_model=List[TransactionOut])
def list_transactions(db: Session = Depends(get_db)):
    return get_transactions(db)
