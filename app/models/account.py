from datetime import datetime, timezone
from typing import Optional

class Account:
    def __init__(self, owner_name: str, balance: float = 0.0, created_at: Optional[datetime] = None):
        self.owner_name = owner_name
        self.balance = balance
        self.created_at = created_at or datetime.now(timezone.utc) 