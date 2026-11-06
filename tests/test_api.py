from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_chat_success():

    response = client.post(
        "/chat",
        json={
            "question": "What is Python?"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert len(data["answer"]) > 0


def test_empty_question():

    response = client.post(
        "/chat",
        json={
            "question": ""
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "error"


def test_missing_question():

    response = client.post(
        "/chat",
        json={}
    )

    assert response.status_code == 422


def test_invalid_question_type():

    response = client.post(
        "/chat",
        json={
            "question": 123
        }
    )

    assert response.status_code == 422


def test_not_found():

    response = client.get("/unknown")

    assert response.status_code == 404


def test_whitespace_question():

    response = client.post(
        "/chat",
        json={
            "question": "   "
        }
    )

    assert response.status_code == 200
    assert response.json()["status"] == "error"