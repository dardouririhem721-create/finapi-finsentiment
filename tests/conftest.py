"""Fixtures partagees entre tests."""

import pytest

from finapi.app import create_app


@pytest.fixture
def client():
    """Client Flask de test (pas de vrai serveur)."""
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()
