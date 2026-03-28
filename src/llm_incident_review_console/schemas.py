from __future__ import annotations

from pydantic import BaseModel


class TeamOut(BaseModel):
    id: str
    name: str
    escalation_channel: str


class PlaybookOut(BaseModel):
    id: str
    title: str
    severity: str
    summary: str


class IncidentOut(BaseModel):
    id: str
    team_id: str
    playbook_id: str
    title: str
    status: str
    severity: str
    category: str
    service: str
    environment: str
    started_at: str
    detection_source: str
    model: str
    cost_usd: float
    latency_ms: int
    summary: str
    prompt_excerpt: str
    response_excerpt: str
    policy_verdict: str
    replay_risk: str
    impact: str


class TimelineEventOut(BaseModel):
    id: str
    incident_id: str
    at: str
    stage: str
    detail: str
    actor: str
    outcome: str


class EvidenceOut(BaseModel):
    id: str
    incident_id: str
    kind: str
    title: str
    snippet: str
    risk_signal: str


class MitigationOut(BaseModel):
    id: str
    incident_id: str
    title: str
    owner: str
    priority: str
    detail: str


class ReplayPreviewOut(BaseModel):
    incident_id: str
    mode: str
    expected_outcome: str
    safety_notes: list[str]


class HealthOut(BaseModel):
    service: str
    incidents: int
    open_incidents: int
    critical_incidents: int
    teams: int
    playbooks: int
    database_backend: str
