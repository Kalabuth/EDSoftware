from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.account import Account
from typing import Optional
from datetime import datetime, timezone
from bson import ObjectId

class AccountRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.collection = db["accounts"]

    async def create_account(self, owner_name: str) -> dict:
        account = {
            "owner_name": owner_name,
            "balance": 0.0,
            "created_at": datetime.now(timezone.utc),
        }
        result = await self.collection.insert_one(account)
        account["_id"] = str(result.inserted_id)
        return account

    async def update_balance(self, account_id: str, amount: float) -> dict:
        account = await self.collection.find_one({"_id": ObjectId(account_id)})
        if not account:
            return None
        new_balance = account["balance"] + amount
        await self.collection.update_one({"_id": ObjectId(account_id)}, {"$set": {"balance": new_balance}})
        account["balance"] = new_balance
        return account

    async def list_accounts(self) -> list:
        accounts = []
        async for acc in self.collection.find():
            accounts.append({
                "id": str(acc["_id"]),
                "owner_name": acc["owner_name"],
                "balance": acc["balance"],
                "created_at": acc["created_at"]
            })
        return accounts 