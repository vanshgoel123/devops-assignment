from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
def test_health_check():
    res= client.get("/api/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_message():
    res = client.get("/api/message")
    assert res.status_code == 200
    assert "You've successfully integrated the backend!" in res.json()["message"]