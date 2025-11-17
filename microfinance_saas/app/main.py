from fastapi import FastAPI
from app.api.v1 import users, loans, transactions

app = FastAPI(title="Multi-Wallet")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(loans.router, prefix="/loans", tags=["Loans"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])

@app.get("/")
def root():
    return {"message": "Multi-Wallet is here!"}
