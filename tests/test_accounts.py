import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_account():
    response = client.post("/accounts", json={"owner_name": "Test User"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["message"] == "Account created successfully"
    global created_account_id
    created_account_id = data["id"]

def test_update_balance():
    response = client.post("/accounts", json={"owner_name": "Balance User"})
    account_id = response.json()["id"]
    response = client.patch(f"/accounts/{account_id}", json={"amount": 100.0})
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == account_id
    assert data["balance"] == 100.0

def test_list_accounts():
    response = client.get("/accounts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "owner_name" in data[0]
        assert "balance" in data[0]
        assert "created_at" in data[0] 