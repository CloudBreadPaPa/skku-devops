import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200  # True가 나와야 함
    assert response.json() == {"Hello": "World"}
