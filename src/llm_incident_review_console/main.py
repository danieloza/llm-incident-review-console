from __future__ import annotations

from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse

from llm_incident_review_console.config import database_path
from llm_incident_review_console.repository import IncidentRepository, SQLiteIncidentRepository
from llm_incident_review_console.schemas import (
    EvidenceOut,
    HealthOut,
    IncidentOut,
    MitigationOut,
    PlaybookOut,
    ReplayPreviewOut,
    TeamOut,
    TimelineEventOut,
)
from llm_incident_review_console.services import IncidentReviewService


repository = SQLiteIncidentRepository(database_path())


def get_repository() -> IncidentRepository:
    return repository


def get_service(repo: IncidentRepository = Depends(get_repository)) -> IncidentReviewService:
    return IncidentReviewService(repo)


def create_app(repo: IncidentRepository | None = None) -> FastAPI:
    app = FastAPI(title="LLM Incident Review Console", version="0.1.0")
    if repo is not None:
        app.dependency_overrides[get_repository] = lambda: repo

    dashboard_path = Path(__file__).with_name("dashboard.html")

    @app.get("/", include_in_schema=False)
    def root() -> FileResponse:
        return FileResponse(dashboard_path)

    @app.get("/dashboard", include_in_schema=False)
    def dashboard() -> FileResponse:
        return FileResponse(dashboard_path)

    @app.get("/health", response_model=HealthOut)
    def health(service: IncidentReviewService = Depends(get_service)) -> HealthOut:
        return HealthOut(**service.health_snapshot())

    @app.get("/teams", response_model=list[TeamOut])
    def teams(service: IncidentReviewService = Depends(get_service)) -> list[TeamOut]:
        return [TeamOut(**item) for item in service.list_teams()]

    @app.get("/playbooks", response_model=list[PlaybookOut])
    def playbooks(service: IncidentReviewService = Depends(get_service)) -> list[PlaybookOut]:
        return [PlaybookOut(**item) for item in service.list_playbooks()]

    @app.get("/incidents", response_model=list[IncidentOut])
    def incidents(service: IncidentReviewService = Depends(get_service)) -> list[IncidentOut]:
        return [IncidentOut(**item) for item in service.list_incidents()]

    @app.get("/incidents/{incident_id}", response_model=IncidentOut)
    def incident(incident_id: str, service: IncidentReviewService = Depends(get_service)) -> IncidentOut:
        try:
            payload = service.get_incident(incident_id)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return IncidentOut(**payload)

    @app.get("/incidents/{incident_id}/timeline", response_model=list[TimelineEventOut])
    def incident_timeline(incident_id: str, service: IncidentReviewService = Depends(get_service)) -> list[TimelineEventOut]:
        try:
            payload = service.list_timeline(incident_id)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return [TimelineEventOut(**item) for item in payload]

    @app.get("/incidents/{incident_id}/evidence", response_model=list[EvidenceOut])
    def incident_evidence(incident_id: str, service: IncidentReviewService = Depends(get_service)) -> list[EvidenceOut]:
        try:
            payload = service.list_evidence(incident_id)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return [EvidenceOut(**item) for item in payload]

    @app.get("/incidents/{incident_id}/mitigations", response_model=list[MitigationOut])
    def incident_mitigations(incident_id: str, service: IncidentReviewService = Depends(get_service)) -> list[MitigationOut]:
        try:
            payload = service.list_mitigations(incident_id)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return [MitigationOut(**item) for item in payload]

    @app.get("/incidents/{incident_id}/replay-preview", response_model=ReplayPreviewOut)
    def replay_preview(incident_id: str, service: IncidentReviewService = Depends(get_service)) -> ReplayPreviewOut:
        try:
            payload = service.replay_preview(incident_id)
        except ValueError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return ReplayPreviewOut(**payload)

    return app


app = create_app()
