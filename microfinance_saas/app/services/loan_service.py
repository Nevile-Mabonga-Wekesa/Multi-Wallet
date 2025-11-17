from sqlalchemy.orm import Session
from app.models.loan import Loan

def create_loan(db: Session, user_id: int, amount: float, interest_rate: float, term_months: int):
    loan = Loan(user_id=user_id, amount=amount, interest_rate=interest_rate, term_months=term_months)
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan

def get_loans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Loan).offset(skip).limit(limit).all()
