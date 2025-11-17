from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.loan_schema import LoanCreate, LoanOut
from app.services.loan_service import create_loan, get_loans
from app.core.database import get_db

router = APIRouter(prefix="/loans", tags=["Loans"])


@router.post(
    "/",
    response_model=LoanOut,
    status_code=status.HTTP_201_CREATED
)
async def add_loan(
    payload: LoanCreate,
    db: Session = Depends(get_db)
) -> LoanOut:
    """
    Create a new loan.
    """
    loan = create_loan(
        db=db,
        user_id=payload.user_id,
        amount=payload.amount,
        interest_rate=payload.interest_rate,
        term_months=payload.term_months,
    )

    if not loan:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Loan could not be created"
        )

    return loan


@router.get(
    "/",
    response_model=List[LoanOut],
    status_code=status.HTTP_200_OK
)
async def list_loans(
    db: Session = Depends(get_db)
) -> List[LoanOut]:
    """
    Retrieve all loans.
    """
    loans = get_loans(db)

    if loans is None:
        return []  # Enforces consistent return type

    return loans

