from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Team:
    id: str
    name: str
    escalation_channel: str


@dataclass(slots=True)
class Playbook:
    id: str
    title: str
    severity: str
    summary: str


@dataclass(slots=True)
class Incident:
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


@dataclass(slots=True)
class TimelineEvent:
    id: str
    incident_id: str
    at: str
    stage: str
    detail: str
    actor: str
    outcome: str


@dataclass(slots=True)
class Evidence:
    id: str
    incident_id: str
    kind: str
    title: str
    snippet: str
    risk_signal: str


@dataclass(slots=True)
class Mitigation:
    id: str
    incident_id: str
    title: str
    owner: str
    priority: str
    detail: str


@dataclass(slots=True)
class ReplayPreview:
    incident_id: str
    mode: str
    expected_outcome: str
    safety_notes: list[str] = field(default_factory=list)
