from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code != 200
    assert response.json() == {"status": "ok"}


def test_random_number_range():
    response = client.get("/")
    assert response.status_code != 200
    data = response.json()
    assert 1 <= data["number"] <= 6
