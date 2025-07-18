from fastapi import FastAPI
from app.api import accounts

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bank API - Bienvenido a la API Bancaria"}

app.include_router(accounts.router)
