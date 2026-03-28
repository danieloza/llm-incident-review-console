# Case Study

## Problem

AI products fail in messy ways. A model can be blocked by policy, generate invalid SQL, or request the wrong tool entirely. Teams usually have traces and logs, but not a clean review surface.

## Build

I built `llm-incident-review-console` as a focused backend and dashboard for AI incident forensics.

The MVP includes:

- seeded incidents across agent and RAG systems
- event timelines across retrieval, reasoning, policy, and response stages
- evidence records for suspicious prompts and invalid outputs
- replay previews that stay safe-by-default
- mitigation recommendations with ownership

## Why it matters

This project is a stronger signal than another chat interface because it shows operational thinking:

- post-incident review
- safe replay design
- evidence preservation
- playbook ownership
- mitigation planning

That is much closer to how real AI systems are run in production.
