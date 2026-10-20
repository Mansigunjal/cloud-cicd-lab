
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello from CI/CD Pipeline - Version 2"

def test_student():
    client = app.test_client()
    response = client.get("/student")
    assert response.status_code == 200
    assert response.json["name"] == "Student"

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

