from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Test syncing tariffs from Wildberries API and updating Google Sheets
def test_sync_tariffs():
    response = client.post("/sync-tariffs/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tariffs synced successfully!"}


# Test retrieving tariffs from the database
def test_read_tariffs():
    response = client.get("/tariffs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
