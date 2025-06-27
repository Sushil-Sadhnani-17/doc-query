from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ask():
    response = client.post("/ask", json={"question": "What is The Metamorphosis about?"})
    assert response.status_code == 200
    assert "answer" in response.json()
