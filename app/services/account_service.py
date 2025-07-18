from app.repositories.account_repository import AccountRepository

class AccountService:
    def __init__(self, repository: AccountRepository):
        self.repository = repository

    async def create_account(self, nombre_titular: str):
        return await self.repository.create_account(nombre_titular) 