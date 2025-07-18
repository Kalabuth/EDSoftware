from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AccountCreate(BaseModel):
    owner_name: str = Field(..., example="Juan Perez")

class AccountResponse(BaseModel):
    id: str
    owner_name: str
    balance: float
    created_at: datetime

class UpdateBalance(BaseModel):
    amount: float 