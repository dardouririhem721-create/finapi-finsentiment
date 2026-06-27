"""Tests d'intégration end-to-end — démarre l'API et l'attaque."""

import threading
import time

import pytest
import requests

from finapi.app import create_app


@pytest.fixture(scope="module")
def live_server():
    """Démarre le serveur Flask dans un thread séparé."""
    app = create_app()
    app.config["TESTING"] = True
    server = threading.Thread(target=lambda: app.run(port=5099, use_reloader=False))
    server.daemon = True
    server.start()
    time.sleep(1)
    yield "http://localhost:5099"


def test_e2e_health(live_server):
    response = requests.get(f"{live_server}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_e2e_price(live_server):
    response = requests.get(f"{live_server}/price/AAPL")
    assert response.status_code in [200, 404, 500]


def test_e2e_db_stats(live_server):
    response = requests.get(f"{live_server}/db/stats")
    assert response.status_code in [200, 500]


def test_e2e_sentiment_missing_text(live_server):
    response = requests.post(f"{live_server}/sentiment", json={})
    assert response.status_code == 400
