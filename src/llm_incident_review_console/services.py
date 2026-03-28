from __future__ import annotations

from dataclasses import asdict

from llm_incident_review_console.models import ReplayPreview
from llm_incident_review_console.repository import IncidentRepository


class IncidentReviewService:
    def __init__(self, repository: IncidentRepository) -> None:
        self.repository = repository

    def health_snapshot(self) -> dict[str, int | str]:
        return self.repository.health_snapshot()

    def list_teams(self) -> list[dict[str, str]]:
        return [asdict(item) for item in self.repository.list_teams()]

    def list_playbooks(self) -> list[dict[str, str]]:
        return [asdict(item) for item in self.repository.list_playbooks()]

    def list_incidents(self) -> list[dict[str, object]]:
        return [asdict(item) for item in self.repository.list_incidents()]

    def get_incident(self, incident_id: str) -> dict[str, object]:
        incident = self.repository.get_incident(incident_id)
        if not incident:
            raise ValueError("Incident not found.")
        return asdict(incident)

    def list_timeline(self, incident_id: str) -> list[dict[str, str]]:
        self.get_incident(incident_id)
        return [asdict(item) for item in self.repository.list_timeline(incident_id)]

    def list_evidence(self, incident_id: str) -> list[dict[str, str]]:
        self.get_incident(incident_id)
        return [asdict(item) for item in self.repository.list_evidence(incident_id)]

    def list_mitigations(self, incident_id: str) -> list[dict[str, str]]:
        self.get_incident(incident_id)
        return [asdict(item) for item in self.repository.list_mitigations(incident_id)]

    def replay_preview(self, incident_id: str) -> dict[str, object]:
        incident = self.get_incident(incident_id)
        mode = "safe-replay"
        expected_outcome = "Replay should remain blocked until mitigations are applied."
        notes = [
            "Use synthetic credentials and non-production tools only.",
            "Persist the exact retrieval set that triggered the incident.",
            "Mask customer content before any human review export.",
        ]
        if incident["category"] == "hallucinated-sql":
            mode = "schema-locked-replay"
            expected_outcome = "Replay should produce grounded SQL or fail closed before execution."
            notes = [
                "Freeze schema graph and deny unknown columns.",
                "Compare replay draft against validator output.",
                "Return analyst-facing explanation instead of partial SQL.",
            ]
        preview = ReplayPreview(
            incident_id=incident_id,
            mode=mode,
            expected_outcome=expected_outcome,
            safety_notes=notes,
        )
        return asdict(preview)
