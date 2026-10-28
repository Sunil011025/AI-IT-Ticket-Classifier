
import pytest

import app as app_module
from database import init_db


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a temporary database so tests don't change your real tickets.
    monkeypatch.setattr(
        "database.DATABASE_PATH",
        tmp_path / "test_tickets.db",
    )

    init_db()

    app_module.app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
    )

    with app_module.app.test_client() as test_client:
        yield test_client


def test_homepage_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"AI IT Ticket Classifier" in response.data


def test_empty_ticket_is_rejected(client):
    response = client.post(
        "/",
        data={"description": "   "},
    )

    assert response.status_code == 200
    assert b"Please enter a ticket description." in response.data


def test_ticket_is_classified_and_saved(client, monkeypatch):
    def fake_classifier(description):
        return {
            "category": "Network",
            "priority": "High",
            "sentiment": "Urgent",
            "suggested_response": "Please check your Wi-Fi.",
        }

    monkeypatch.setattr(
        app_module,
        "classify_ticket",
        fake_classifier,
    )

    response = client.post(
        "/",
        data={"description": "Office Wi-Fi is not working."},
    )

    assert response.status_code == 200
    assert b"Classification Result" in response.data
    assert b"Network" in response.data
    assert b"Ticket ID:" in response.data

    history = client.get("/tickets")

    assert history.status_code == 200
    assert b"Office Wi-Fi is not working." in history.data


def test_ai_failure_shows_friendly_message(client, monkeypatch):
    def failing_classifier(description):
        raise RuntimeError("Simulated AI service failure")

    monkeypatch.setattr(
        app_module,
        "classify_ticket",
        failing_classifier,
    )

    response = client.post(
        "/",
        data={"description": "My laptop is not working."},
    )

    assert response.status_code == 200
    assert b"Unable to classify this ticket right now." in response.data
