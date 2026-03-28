# LLM Incident Review Console

> FastAPI incident console for reviewing AI failures with timeline evidence, replay previews, and mitigation planning.

## Why this project exists

Most AI demos stop at generation. Real systems need incident review after things go wrong:

- prompt injection attempts
- hallucinated SQL or tool calls
- policy bypass attempts
- grounding failures
- unsafe replay loops

This project models the review layer after the incident already happened. It gives teams a place to inspect evidence, understand the runtime timeline, and plan a safe replay.

## What it includes

- incident queue with severity, impact, and service ownership
- timeline events across retrieval, reasoning, policy, and response stages
- evidence records for prompt fragments, tool requests, and invalid SQL drafts
- replay preview modes for safe re-runs
- mitigation tasks with owner and priority
- static dashboard for portfolio and demo screenshots

## API

- `GET /health`
- `GET /teams`
- `GET /playbooks`
- `GET /incidents`
- `GET /incidents/{incident_id}`
- `GET /incidents/{incident_id}/timeline`
- `GET /incidents/{incident_id}/evidence`
- `GET /incidents/{incident_id}/mitigations`
- `GET /incidents/{incident_id}/replay-preview`

## Quick start

```bash
python -m pip install -e .
python -m uvicorn llm_incident_review_console.main:app --reload
```

Open:

- `http://127.0.0.1:8000/dashboard`
- `http://127.0.0.1:8000/incidents`

## Example incidents

- `inc_1001` prompt injection attempt in `agent-runtime-control-tower`
- `inc_1002` hallucinated SQL draft in `danex-rag-service`

## Positioning

This is not another chatbot demo. It is incident forensics for AI systems: the layer between "something went wrong" and "we understand why it went wrong and how to replay safely."
