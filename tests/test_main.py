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
# Données de test
TEST_RANKINGS_DATA = [
    {
        "media": "Radio X",
        "title": "The 25 best indie albums of 1992",
        "year": 1992,
        "url": "https://www.radiox.co.uk/features/x-lists/best-albums-1992/",
        "id": "7a2f25f4-470e-4abc-a8a3-133e838f6e93",
        "country": "UK"
    },
    {
        "media": "Paste",
        "title": "The 25 Best Albums of 1992",
        "year": 1992,
        "url": "https://www.pastemagazine.com/music/best-albums/best-albums-of-1992/",
        "id": "86ab493c-af21-4778-a6cb-337205b22e6f",
        "country": "US"
    }
]
@pytest.fixture(autouse=True)
def mock_rankings_data():
    with patch("main.rankings_data", TEST_RANKINGS_DATA):
        yield

def test_get_all_rankings():
    response = client.get("/rankings")
    assert response.status_code == 200
    # Vérifie que la clé 'rankings' contient les données attendues
    assert response.json() == {"rankings": TEST_RANKINGS_DATA}

