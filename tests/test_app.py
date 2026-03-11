from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_api_time():
    response = client.get("/api/time")
    assert response.status_code == 200
    data = response.json()
    assert "utc_time" in data


def test_api_time_fail_header():
    response = client.get("/api/time", headers={"X-Debug": "fail"})
    assert response.status_code == 500
