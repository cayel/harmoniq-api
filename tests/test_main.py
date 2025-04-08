import pytest
from fastapi.testclient import TestClient
from pathlib import Path
import sys
import os
import json
from unittest.mock import patch, MagicMock

# Ajouter le chemin du projet à PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

# Créer un client de test
client = TestClient(app)

# Données de test
TEST_RANKING_ID = "test-ranking-id"
TEST_RANKING_DATA = {
    "id": TEST_RANKING_ID,
    "title": "Test Ranking",
    "media": "Test Media",
    "description": "Test description",
    "created_at": "2025-04-08T19:49:38+00:00",
    "updated_at": "2025-04-08T19:49:38+00:00"
}

@pytest.fixture(autouse=True)
def mock_rankings_data():
    test_data = [{"id": "test-id", "title": "Test Ranking", "media": "Test Media"}]
    
    with patch('main.rankings_data', test_data):
        yield

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}

def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_get_rankings():
    response = client.get("/rankings")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

# ... le reste des tests ...