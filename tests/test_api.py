from __future__ import annotations

from pathlib import Path

from fastapi.testclient import TestClient

from llm_incident_review_console.main import create_app
from llm_incident_review_console.repository import SQLiteIncidentRepository


def make_client(tmp_path: Path) -> TestClient:
    repo = SQLiteIncidentRepository(tmp_path / "incidents.db")
    return TestClient(create_app(repo))


def test_health_endpoint(tmp_path: Path) -> None:
    client = make_client(tmp_path)

    response = client.get("/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["service"] == "llm-incident-review-console"
    assert payload["incidents"] == 2


def test_incident_detail_and_timeline(tmp_path: Path) -> None:
    client = make_client(tmp_path)

    incident_response = client.get("/incidents/inc_1001")
    timeline_response = client.get("/incidents/inc_1001/timeline")

    assert incident_response.status_code == 200
    assert incident_response.json()["category"] == "prompt-injection"
    assert timeline_response.status_code == 200
    assert len(timeline_response.json()) >= 3


def test_replay_preview_varies_by_category(tmp_path: Path) -> None:
    client = make_client(tmp_path)

    critical_response = client.get("/incidents/inc_1001/replay-preview")
    sql_response = client.get("/incidents/inc_1002/replay-preview")

    assert critical_response.status_code == 200
    assert critical_response.json()["mode"] == "safe-replay"
    assert sql_response.status_code == 200
    assert sql_response.json()["mode"] == "schema-locked-replay"


def test_missing_incident_returns_not_found(tmp_path: Path) -> None:
    client = make_client(tmp_path)

    response = client.get("/incidents/does-not-exist")

    assert response.status_code == 404
