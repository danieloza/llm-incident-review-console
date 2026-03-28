# LinkedIn Showcase

## Hook

I built an incident review console for AI systems: timeline evidence, replay previews, mitigation planning, and post-mortem visibility for prompt injection, hallucinated SQL, and policy failures.

## Post

Most AI demos end at generation.
Real systems need a way to understand failures after they happen.

So I built `LLM Incident Review Console`:

- FastAPI backend for reviewing AI incidents
- timeline evidence across retrieval, reasoning, policy, and response stages
- replay previews that stay safe-by-default
- mitigation tasks with owner and priority
- grounded examples from prompt injection and hallucinated SQL failures
- screenshot-ready dashboard for ops and review flows

What I wanted to show with this project was not another chat interface, but the post-mortem layer around AI systems:

- what exactly happened
- where the bad signal entered the system
- what policy blocked or missed
- how to replay safely
- which team owns the mitigation

The demo includes two seeded incidents:

1. prompt injection attempt against `agent-runtime-control-tower`
2. hallucinated SQL draft in `danex-rag-service`

Repo:
https://github.com/danieloza/llm-incident-review-console

If you work on AI platform engineering, I’d be curious what you’d add next: diffable replays, eval regression packs, or incident-to-playbook automation?

## Short Version

I built an incident review console for AI systems with FastAPI, timeline evidence, replay previews, and mitigation planning.

The point was simple: not another AI demo, but the layer that explains what went wrong after a prompt injection, hallucinated SQL draft, or policy failure.

Repo:
https://github.com/danieloza/llm-incident-review-console

## Featured Blurb

FastAPI incident console for AI systems with timeline evidence, replay previews, mitigation planning, and post-mortem workflows.
