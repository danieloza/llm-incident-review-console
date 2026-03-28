from __future__ import annotations

import os
from pathlib import Path


def database_path() -> Path:
    configured = os.getenv("LLM_INCIDENT_DB_PATH")
    if configured:
        return Path(configured)
    return Path(__file__).resolve().parents[2] / "data" / "incidents.db"
