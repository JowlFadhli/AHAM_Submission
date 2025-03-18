import pytest
from FlaskApp import app

# Test Client Setup
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test Case 1: Get funds from funds.db
def test_get_funds(client):
    response = client.get('/funds')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Data should be a list
    assert all("fund_name" in fund for fund in data)

# Test Case 2: Get funds from investment_funds.db
def test_get_investment_funds(client):
    response = client.get('/investment-funds')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)  # Data should be a list
    assert all("fund_name" in fund for fund in data)

# Test Case 3: Add a new fund to funds.db
def test_add_fund(client):
    response = client.post('/funds/add', json={
        "fund_name": "Test Fund",
        "performance": 8.2
    })
    assert response.status_code == 201
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Fund 'Test Fund' added successfully."

# Test Case 4: Add duplicate fund to funds.db
def test_add_duplicate_fund(client):
    client.post('/funds/add', json={
        "fund_name": "Duplicate Fund",
        "performance": 7.5
    })
    response = client.post('/funds/add', json={
        "fund_name": "Duplicate Fund",
        "performance": 7.5
    })
    assert response.status_code == 409  # Conflict
    data = response.get_json()
    assert "error" in data

# Test Case 5: Delete a fund from funds.db
def test_delete_fund(client):
    response = client.delete('/funds/delete/1')  # Assuming fund ID 1 exists
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Fund with ID 1 deleted successfully."

# Test Case 6: Delete a non-existent fund from funds.db
def test_delete_nonexistent_fund(client):
    response = client.delete('/funds/delete/9999')  # Non-existent fund ID
    assert response.status_code == 404  # Not Found
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "Fund with ID 9999 not found"
