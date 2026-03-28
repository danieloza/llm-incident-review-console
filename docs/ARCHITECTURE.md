# Architecture

## Purpose

`llm-incident-review-console` models the post-incident workflow for AI systems.

It focuses on five artifacts:

1. Incident metadata
2. Timeline events
3. Evidence records
4. Replay previews
5. Mitigation tasks

## Layers

- `main.py`
  FastAPI interface and route definitions.
- `services.py`
  Review logic, replay mode selection, and error handling.
- `repository.py`
  SQLite-backed persistence with seeded demo data.
- `dashboard.html`
  Portfolio-facing dashboard for screenshots and demos.

## Incident model

Each incident captures:

- the owning team
- the playbook
- the affected service and environment
- model, cost, and latency
- prompt and response excerpts
- policy verdict
- replay risk
- impact statement

## Replay preview

Replay preview intentionally does not execute anything.

It exists to answer:

- should we replay this at all
- under what constraints
- what safe outcome are we trying to prove

That separation is deliberate. Incident review should not be coupled directly to live remediation.
