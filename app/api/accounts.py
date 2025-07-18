from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas.account import AccountCreate, UpdateBalance
from app.repositories.account_repository import AccountRepository
from motor.motor_asyncio import AsyncIOMotorClient
import os

router = APIRouter()

async def get_db():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
    db = client["bank_db"]
    try:
        yield db
    finally:
        client.close()

@router.post("/accounts", status_code=status.HTTP_201_CREATED)
async def create_account(account: AccountCreate, db=Depends(get_db)):
    repo = AccountRepository(db)
    created = await repo.create_account(account.owner_name)
    return {"id": str(created["_id"]), "message": "Account created successfully"}

@router.patch("/accounts/{account_id}")
async def update_balance(account_id: str, data: UpdateBalance, db=Depends(get_db)):
    repo = AccountRepository(db)
    updated = await repo.update_balance(account_id, data.amount)
    if not updated:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"id": str(updated["_id"]), "balance": updated["balance"]}

@router.get("/accounts")
async def list_accounts(db=Depends(get_db)):
    repo = AccountRepository(db)
    accounts = await repo.list_accounts()
    return accounts 