from sqlalchemy.orm import Session
from app.models.transaction import Transaction

def create_transaction(db: Session, loan_id: int, amount: float, transaction_type: str):
    txn = Transaction(loan_id=loan_id, amount=amount, transaction_type=transaction_type)
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn

def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    from app.models.transaction import Transaction
    return db.query(Transaction).offset(skip).limit(limit).all()
